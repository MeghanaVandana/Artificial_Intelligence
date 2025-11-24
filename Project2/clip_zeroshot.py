# clip_zeroshot.py
"""
Zero-shot image classification using Hugging Face CLIP.
Usage: python clip_zeroshot.py path/to/image.jpg
"""

import sys
import torch
import numpy as np
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

# --- Config ---
MODEL_NAME = "openai/clip-vit-base-patch32"  # change to any available CLIP model
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# --- Helpers ---
def load_model():
    model = CLIPModel.from_pretrained(MODEL_NAME).to(DEVICE)
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)
    return model, processor

def image_to_embedding(model, processor, image: Image.Image):
    inputs = processor(images=image, return_tensors="pt").to(DEVICE)
    with torch.no_grad():
        image_emb = model.get_image_features(**inputs)
    image_emb = image_emb / image_emb.norm(p=2, dim=-1, keepdim=True)
    return image_emb.cpu().numpy()

def texts_to_embeddings(model, processor, texts):
    inputs = processor(text=texts, return_tensors="pt", padding=True).to(DEVICE)
    with torch.no_grad():
        text_emb = model.get_text_features(**inputs)
    text_emb = text_emb / text_emb.norm(p=2, dim=-1, keepdim=True)
    return text_emb.cpu().numpy()

def score_image_vs_texts(image_emb, text_embs):
    # cosine similarities since embeddings are normalized
    sims = (text_embs @ image_emb.T).squeeze()  # shape: (n_texts,)
    return sims

# --- Main ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clip_zeroshot.py path/to/image.jpg")
        sys.exit(1)

    image_path = sys.argv[1]
    image = Image.open(image_path).convert("RGB")

    model, processor = load_model()
    img_emb = image_to_embedding(model, processor, image)
    # Example labels (you can modify / expand)
    labels = [
        "a photo of a dog",
        "a photo of a cat",
        "a photo of a car",
        "an aerial photo of a city",
        "a picture of food"
    ]
    text_embs = texts_to_embeddings(model, processor, labels)
    sims = score_image_vs_texts(img_emb, text_embs)

    # print sorted scores
    ranking = sorted(zip(labels, sims), key=lambda x: x[1], reverse=True)
    print("Zero-shot ranking (label, similarity):")
    for label, score in ranking:
        print(f"{label:30s} {float(score):.4f}")

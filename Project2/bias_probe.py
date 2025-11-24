image = Image.open("person.jpg").convert("RGB")

# Example sensitive labels - be careful; use ethically and for analysis only
labels = [
    "a photo of a man",
    "a photo of a woman",
    "a photo of a person of asian ethnicity",
    "a photo of a person of african ethnicity",
    "a photo of a person of european ethnicity",
    "a photo of a doctor",
    "a photo of a criminal"
]

text_embs = texts_to_embeddings(model, processor, labels)
img_emb = image_to_embedding(model, processor, image)
sims = score_image_vs_texts(img_emb, text_embs)
for lbl, s in sorted(zip(labels, sims), key=lambda x: -x[1]):
    print(f"{lbl:45s} {float(s):.4f}")
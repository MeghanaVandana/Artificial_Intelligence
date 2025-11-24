import os
from PIL import Image
from glob import glob
from tqdm import tqdm

def evaluate_folder(model, processor, root_dir, classes, transform=None):
    """
    root_dir/
        classA/
            img1.jpg
        classB/
    classes: list of class names (base labels)
    transform: optional Pillow transform function applied to image
    """
    total = 0
    correct = 0
    expanded_labels, mapping = expand_labels(classes)
    text_embs = texts_to_embeddings(model, processor, expanded_labels)

    for cls in classes:
        files = glob(os.path.join(root_dir, cls, "*"))
        for f in files:
            img = Image.open(f).convert("RGB")
            if transform:
                img = transform(img)
            img_emb = image_to_embedding(model, processor, img)
            sims = score_image_vs_texts(img_emb, text_embs)
            # aggregate and pick best
            from collections import defaultdict
            agg = defaultdict(list)
            for m, s in zip(mapping, sims):
                agg[m].append(float(s))
            agg_mean = {k: np.mean(v) for k, v in agg.items()}
            pred = max(agg_mean.items(), key=lambda x: x[1])[0]
            total += 1
            if pred == cls:
                correct += 1
    return correct / total if total > 0 else 0.0

# Example transform to simulate distribution shift (brightness change)
from PIL import ImageEnhance
def brightness_transform(factor):
    def _t(img):
        return ImageEnhance.Brightness(img).enhance(factor)
    return _t


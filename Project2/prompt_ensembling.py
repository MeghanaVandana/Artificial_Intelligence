# prompt_ensembling.py (snippet to integrate into clip_zeroshot.py)
PROMPT_TEMPLATES = [
    "a photo of {}.",
    "an image of {}.",
    "a cropped photo of {}.",
    "a drawing of {}.",
    "a close-up of {}."
]

def expand_labels(base_labels):
    expanded = []
    mapping = []
    for lbl in base_labels:
        for t in PROMPT_TEMPLATES:
            expanded.append(t.format(lbl))
            mapping.append(lbl)
    return expanded, mapping

# Example usage inside main:
# base_labels = ["dog", "cat", "car"]
# expanded, mapping = expand_labels(base_labels)
# text_embs = texts_to_embeddings(model, processor, expanded)
# sims = score_image_vs_texts(img_emb, text_embs)  # dimension: len(expanded)
# # aggregate by base label
# from collections import defaultdict
# agg = defaultdict(list)
# for base, sim in zip(mapping, sims):
#     agg[base].append(float(sim))
# agg_mean = {k: float(np.mean(v)) for k, v in agg.items()}
# ranking = sorted(agg_mean.items(), key=lambda x: x[1], reverse=True)

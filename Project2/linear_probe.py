import torch.nn as nn, torch.optim as optim

# Suppose train_embs (N x D) and train_labels (N) precomputed using model.get_image_features(...)
D = train_embs.shape[1]
num_classes = len(classes)
classifier = nn.Linear(D, num_classes).to(DEVICE)
opt = optim.Adam(classifier.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

for epoch in range(10):
    classifier.train()
    logits = classifier(torch.tensor(train_embs).to(DEVICE))
    loss = loss_fn(logits, torch.tensor(train_labels).to(DEVICE))
    loss.backward(); opt.step(); opt.zero_grad()

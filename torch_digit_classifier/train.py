import torch
import torch.nn as nn
from torch.utils import data

from sklearn.model_selection import train_test_split

import numpy as np
import matplotlib.pyplot as plt

from mnist_set import MnistSet
from model_def import MyModel

"Tune the hyperparameters here"
num_epochs = 2
learning_rate = 1e-5
decay = 1e-5
batch_size = 64

# Loading data
print("Loading data...")
raw_data = np.loadtxt('./data/train.csv', dtype=int, delimiter=',', skiprows = 1, max_rows = 100000)
# without_labels = raw_data[:,1:]
# labels = raw_data[:,0]

# Train-test split
train_set, test_set = train_test_split(raw_data, test_size=0.25, stratify=raw_data[:,0])
train_loader = data.DataLoader(MnistSet(train_set), batch_size=batch_size)
val_loader = data.DataLoader(MnistSet(test_set), batch_size=batch_size)


# Train
model = MyModel()
# Loss and optimizer
criterion =  nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, weight_decay=decay)

print('Beginning training..')
total_step = len(train_loader)
tr_loss_list = []
tr_steps = []
val_loss_list = []
for epoch in range(num_epochs):
    try:
        # Training
        print('Epoch {}'.format(epoch+1))
        for i, local_data in enumerate(train_loader):
            # local_batch, local_labels = local_batch[:,1:].float().view(batch_size,1,28,28), local_batch[:,0]
            # Forward pass
            local_batch, local_labels = local_data
            outputs = model.forward(local_batch)
            loss = criterion(outputs, local_labels)

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (i+1) % 10 == 0:
                tr_loss_list.append(loss.item())
                tr_steps.append(i+1+(epoch*total_step))
                print ('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'
                       .format(epoch+1, num_epochs, i+1, total_step, loss.item()))

        # Validation
        with torch.no_grad():
            valset_loss_lst = []
            for local_batch, local_labels in val_loader:
                # local_batch, local_labels = local_batch[:,1:].float(), local_batch[:,0]

                outputs = model.forward(local_batch)
                loss = criterion(outputs, local_labels)
                valset_loss_lst.append(loss.item())
            val_loss = np.sum(valset_loss_lst) / len(valset_loss_lst)
            print("Validation loss: {}".format(val_loss))
            val_loss_list.append(val_loss)
    except KeyboardInterrupt:
        break

fig_name = "loss_curve.png"
num_steps = np.array(range(1,1+len(val_loss_list))) * total_step
plt.figure()
plt.plot(tr_steps, tr_loss_list, label='Training Loss')
plt.plot([tr_steps[0]] + list(num_steps), [tr_loss_list[0]] + val_loss_list,label='Validation Loss')
plt.xlabel("Iterations")
plt.ylabel("Cross-entropy Loss")
plt.legend()
plt.savefig(fig_name,dpi=150)

# Testing...
print('Beginning Validation...')
with torch.no_grad():
    correct = 0
    total = 0
    predicted_list = []
    groundtruth_list = []
    for (local_batch,local_labels) in val_loader:

        outputs = model.forward(local_batch)
        _, predicted = torch.max(outputs.data, 1)
        total += local_labels.size(0)
        predicted_list.extend(predicted)
        groundtruth_list.extend(local_labels)
        correct += (predicted == local_labels).sum().item()

    print('Accuracy of the network on the {} test images: {} %'.format(total, 100 * correct / total))

torch.save(model.state_dict(), './model.pt')
print("Model state dict saved to disk as './model.pt'")

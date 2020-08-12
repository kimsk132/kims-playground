import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils import data

import sklearn.metrics as metrics
from sklearn.model_selection import StratifiedKFold, train_test_split

import time
import numpy as np
import matplotlib.pyplot as plt


# Simple Alex net
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        # define some common layers: 
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=5, kernel_size=3, stride=1)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=1)

        self.conv2 = nn.Conv2d(in_channels=5, out_channels=5, kernel_size=3, stride=1)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=1)

        self.conv3 = nn.Conv2d(in_channels=5, out_channels=3, kernel_size=3, stride=1)
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=1)

        self.fc4 = nn.Linear(1083, 100)
        self.fc5 = nn.Linear(100, 10)

    def forward(self, x):
        # now you can use the layers you defined, to write the forward pass, i.e.,
        # network architecture for your model
        # Output size = 1 + (input_size - kernel_size) / stride
        # Input x size 1 * 28 * 28
        x = self.pool1(F.relu(self.conv1(x)))
        # x after conv 5 * 26 * 26
        # x after pool 5 * 25 * 25
        x = self.pool2(F.relu(self.conv2(x)))
        # x after conv 5 * 23 * 23
        # x after pool 5 * 22 * 22
        x = self.pool3(F.relu(self.conv3(x)))
        # x after conv 3 * 20 * 20
        # x after pool 3 * 19 * 19

        x = x.view(-1, 1083)
        x = F.relu(self.fc4(x))
        x = self.fc5(x)
        return x

"Tune the hyperparameters here"
num_epoch = 100
learning_rate = 1e-3
decay = 1e-5
batch_size = 10

# Loading data
raw_data = np.loadtxt('./data/train.csv', dtype=int, delimiter=',', skiprows = 1, max_rows = 100)
print("Raw data loaded")
# without_labels = raw_data[:,1:]
# labels = raw_data[:,0]

# Train-test split
train_set, test_set = train_test_split(raw_data, test_size=0.25)
train_loader = data.DataLoader(train_set, batch_size=batch_size)
val_loader = data.DataLoader(test_set, batch_size=batch_size)


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
for epoch in range(num_epoch):
    try:
        # Training
        print('epoch {}'.format(epoch))
        for i, local_batch in enumerate(train_loader):
            local_batch, local_labels = local_batch[:,1:].float().view(batch_size,1,28,28), local_batch[:,0]
            # Forward pass
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
            for local_batch in val_loader:
                local_batch, local_labels = local_batch[:,1:].float(), local_batch[:,0]

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

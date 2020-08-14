import torch.nn as nn
import torch.nn.functional as F

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        # define some common layers: 
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=100, kernel_size=3, stride=1)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.conv2 = nn.Conv2d(in_channels=100, out_channels=50, kernel_size=3, stride=1)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.conv3 = nn.Conv2d(in_channels=50, out_channels=10, kernel_size=3, stride=1)
        # self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.fc1 = nn.Linear(90, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        # now you can use the layers you defined, to write the forward pass, i.e.,
        # network architecture for your model
        # Output size = 1 + (input_size - kernel_size) // stride
        # Input x size 1 * 28 * 28
        x = F.relu(self.conv1(x))
        x = self.pool1(x)
        # x after conv 100 * 26 * 26
        # x after pool 100 * 13 * 13
        x = F.relu(self.conv2(x))
        x = self.pool2(x)
        # x after conv 50 * 11 * 11
        # x after pool 50 * 5 * 5
        x = F.relu(self.conv3(x))
        # x = self.pool3(x)
        # x after conv 50 * 3 * 3

        x = x.view(-1, 90)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

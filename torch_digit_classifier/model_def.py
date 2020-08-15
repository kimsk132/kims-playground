import torch.nn as nn
import torch.nn.functional as F

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        # define some common layers: 
        self.norm0 = nn.BatchNorm2d(1)

        self.conv1 = nn.Conv2d(in_channels=1, out_channels=128, kernel_size=3, stride=1, padding=1)
        self.norm1 = nn.BatchNorm2d(128)
        self.drop1 = nn.Dropout2d(0.25)

        self.conv2 = nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, stride=1, padding=1)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.norm2 = nn.BatchNorm2d(128)
        self.drop2 = nn.Dropout2d(0.25)

        self.conv3 = nn.Conv2d(in_channels=128, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.fc1 = nn.Linear(3136, 1000)
        self.dropfc1 = nn.Dropout(0.25)
        self.fc2 = nn.Linear(1000, 128)
        self.dropfc2 = nn.Dropout(0.25)
        self.fc3 = nn.Linear(128, 10)

    def forward(self, x):
        # now you can use the layers you defined, to write the forward pass, i.e.,
        # network architecture for your model
        # Output size = 1 + (input_size - kernel_size) // stride
        # Input x size 1 * 28 * 28
        x = self.norm0(x)
        x = F.relu(self.conv1(x))
        x = self.norm1(x)
        x = self.drop1(x)
        # x size 128 * 28 * 28

        x = F.relu(self.conv2(x))
        x = self.pool2(x)
        x = self.norm2(x)
        x = self.drop2(x)
        # x size 128 * 14 * 14

        x = F.relu(self.conv3(x))
        x = self.pool3(x)
        # x size 128 * 7 * 7

        x = x.view(-1, 3136)
        x = F.relu(self.fc1(x))
        x = self.dropfc1(x)
        x = F.relu(self.fc2(x))
        x = self.dropfc2(x)
        x = self.fc3(x)
        return x

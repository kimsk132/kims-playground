import torch.nn as nn
import torch.nn.functional as F

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        # define some common layers: 
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, stride=1)

        self.conv2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.drop2 = nn.Dropout2d(0.25)

        self.conv3 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1)
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.drop3 = nn.Dropout2d(0.25)

        self.conv4 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1)
        self.pool4 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.fc1 = nn.Linear(64, 10)

    def forward(self, x):
        # now you can use the layers you defined, to write the forward pass, i.e.,
        # network architecture for your model
        # Output size = 1 + (input_size - kernel_size) // stride
        # Input x size 1 * 28 * 28
        x = F.relu(self.conv1(x))

        x = F.relu(self.conv2(x))
        x = self.pool2(x)
        x = self.drop2(x)

        x = F.relu(self.conv3(x))
        x = self.pool3(x)
        x = self.drop3(x)

        x = F.relu(self.conv4(x))
        x = self.pool4(x)

        x = x.view(-1, 64)
        # x = F.relu(self.fc1(x))
        x = self.fc1(x)
        return x

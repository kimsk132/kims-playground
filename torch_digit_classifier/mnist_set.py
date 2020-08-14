import numpy as np
import torch
from torch.utils import data

class MnistSet(data.Dataset):
    'Characterizes a dataset for PyTorch'
    def __init__(self, data):
        'Initialization'
        self.data = torch.from_numpy(data)

    def __len__(self):
        'Denotes the total number of samples'
        return len(self.data)

    def __getitem__(self,idx):
        'Generates one sample of data'
        sample = self.data[idx, 1:].view((1, 28, 28)).float() / 255
        label = self.data[idx, 0]
        return sample, label.long()

class MnistTest(MnistSet):
    def __getitem__(self,idx):
        'Generates one sample of data'
        return self.data[idx].view((1, 28, 28)).float() / 255

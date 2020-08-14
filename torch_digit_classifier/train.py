# Citation: Adapted from UC Berkeley CS 189 Spring 2019 homework 6
import torch
import torch.nn as nn
from torch.utils import data

from sklearn.model_selection import train_test_split

import numpy as np

from utils import *
from model_def import MyModel

"Tune the hyperparameters here"
num_epochs = 100
learning_rate = 1e-3
decay = 1e-5
batch_size = 64

"Use these commands in interactive mode"
def train(num_epochs=num_epochs):
    train_and_savefig(model, optimizer, criterion, lr_scheduler, num_epochs, train_loader, val_loader)

def test():
    test_and_savefig(model, val_loader)

def save_model(path='./model_state.pt'):
    torch.save(model.state_dict(), path)
    print("Model state dict saved to disk as '{}'".format(path))

def save_checkpoint(path='./checkpoint.pth'):
    # Citation: https://discuss.pytorch.org/t/saving-model-and-optimiser-and-scheduler/52030/7
    checkpoint = { 
        'model': model,
        'optimizer': optimizer,
        'lr_scheduler': lr_scheduler
        }
    torch.save(checkpoint, path)
    print("Checkpoint saved to disk as '{}'".format(path))

def load_checkpoint(path='./checkpoint.pth'):
    global model, optimizer, lr_scheduler, criterion
    checkpoint = torch.load(path)
    model = checkpoint['model']
    optimizer = checkpoint['optimizer']
    lr_scheduler = checkpoint['lr_scheduler']
    criterion =  nn.CrossEntropyLoss()

def load_train_data():
    global raw_data, train_set, test_set, train_loader, val_loader
    # Loading data
    print("Loading training data...")
    raw_data = np.loadtxt('./data/train.csv', dtype=int, delimiter=',', skiprows = 1, max_rows = 100000)

    # Train-test split
    train_set, test_set = train_test_split(raw_data, test_size=0.25, stratify=raw_data[:,0])
    train_loader = data.DataLoader(MnistSet(train_set), batch_size=batch_size)
    val_loader = data.DataLoader(MnistSet(test_set), batch_size=batch_size)
    print("Training data loaded successfully.")

def run():
    option = input("Please enter checkpoint path (enter nothing to start over)\n")
    if option:
        load_checkpoint(option)
        print("Checkpoint loaded.")
    load_train_data()
    train()
    test()
    save_model()
    save_checkpoint()

# Model, loss and optimizer
model = MyModel()
criterion =  nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, weight_decay=decay)
lr_scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.95)

run()

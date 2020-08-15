import torch
import torch.nn as nn
from torch.utils import data

import numpy as np

from utils import MnistTest
from model_def import MyModel

# Loading data
print("Loading competition data...")
raw_data = np.loadtxt('./data/test.csv', dtype=int, delimiter=',', skiprows = 1)

batch_size = 128
test_loader = data.DataLoader(MnistTest(raw_data), batch_size=batch_size)

print("Running classifier...")
model = MyModel()
model.load_state_dict(torch.load('./model_state.pt'))
model.eval()


with torch.no_grad():
    predicted_list = []
    for data_point in test_loader:

        outputs = model.forward(data_point)
        _, predicted = torch.max(outputs.data, 1)
        predicted_list.extend(predicted)
    # Finally write to a file
    with open('./data/my_submission.csv', 'w') as f:
        f.write("ImageId,Label\n")
        for i, label in enumerate(predicted_list):
            f.write(f"{i+1},{label}\n")
print("csv saved.")

import numpy as np
import torch
from torch.utils import data
import matplotlib.pyplot as plt
import sklearn.metrics as metrics

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
        sample = self.data[idx, 1:].view((1, 28, 28)).float()
        label = self.data[idx, 0]
        return sample, label.long()

class MnistTest(MnistSet):
    def __getitem__(self,idx):
        'Generates one sample of data'
        return self.data[idx].view((1, 28, 28)).float()

def train_and_savefig(model, optimizer, criterion, lr_scheduler, num_epochs, train_loader, val_loader):
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
                    print ('Epoch [{}/{}], Step [{}/{}], Loss: {}'
                           .format(epoch+1, num_epochs, i+1, total_step, loss.item()))
            # Update learning rate
            lr_scheduler.step()

            # Validation
            with torch.no_grad():
                valset_loss_lst = []
                for local_batch, local_labels in val_loader:

                    outputs = model.forward(local_batch)
                    loss = criterion(outputs, local_labels)
                    valset_loss_lst.append(loss.item())
                val_loss = np.sum(valset_loss_lst) / len(valset_loss_lst)
                print("Validation loss: {}".format(val_loss))
                val_loss_list.append(val_loss)

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt received. Stopped training.")
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

def test_and_savefig(model, val_loader):
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

        print('Accuracy of the network on the {} test images: {:.3f} %'.format(total, 100 * correct / total))

    pl = [p.numpy().tolist() for p in predicted_list]
    gt = [p.numpy().tolist() for p in groundtruth_list]

    fig_name = "confusion_mat.png"
    confusion_mat = metrics.confusion_matrix(gt, pl)
    plt.figure()
    plt.matshow(confusion_mat)
    plt.colorbar()
    plt.xlabel("Predictions")
    plt.ylabel("Ground truth")
    plt.xticks(range(10))
    plt.yticks(range(10))
    plt.savefig(fig_name, dpi=150)

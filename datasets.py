import torch
from torch.autograd import Variable
import torchvision
from torchvision import transforms


CIFAR_CLASSES = (
    'plane', 'car', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
)

TRN_TRANSFORM = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor()
])
TST_TRANSFORM = transforms.Compose([
    transforms.ToTensor()
])

class LearnedTransform():
    def __init__(self, model):
        self.model = model

    def __call__(self, x):
        x = Variable(x)
        return self.model.transform(x)


def get_cifar_dataset(trn_size=50000, tst_size=10000,
                      trn_transform=TRN_TRANSFORM, tst_transform=TST_TRANSFORM):

    trainset = torchvision.datasets.CIFAR10(
        root='data/', train=True, download=True, transform=trn_transform)
    trainset.train_data = trainset.train_data[:trn_size]
    trainset.train_labels = trainset.train_labels[:trn_size]

    testset = torchvision.datasets.CIFAR10(
        root='data/', train=False, download=True, transform=tst_transform)
    testset.test_data = testset.test_data[:tst_size]
    testset.test_labels = testset.test_labels[:tst_size]

    return trainset, testset


def get_cifar_loader(trainset, testset, batch_size=64):
    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=batch_size, shuffle=True, num_workers=2)
    testloader = torch.utils.data.DataLoader(
        testset, batch_size=batch_size, shuffle=False, num_workers=2)

    return trainloader, testloader

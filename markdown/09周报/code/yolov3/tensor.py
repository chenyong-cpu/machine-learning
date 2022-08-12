import torch


if __name__ == '__main__':
    x = torch.tensor([1, 2, 3])
    y = torch.tensor([1, 2, 3])
    print(torch.dot(x, y))

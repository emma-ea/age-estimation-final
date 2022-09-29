import torch
import torch.nn as nn
import pretrainedmodels
import pretrainedmodels.utils

# from torchsummary import summary

import ssl

model_name_ = "se_resnext101_32x4d"

ssl._create_default_https_context = ssl._create_unverified_context


class ResCusNet(nn.Module):

    def __init__(self):
        super(ResCusNet, self).__init__()

        self.conv1 = nn.Conv2d(3, 128, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
        self.relu1 = nn.ReLU()
        self.maxPool1 = nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2), padding=0, dilation=3)

        self.conv2 = nn.Conv2d(128, 64, kernel_size=(5, 5))
        self.relu2 = nn.ReLU()
        self.maxPool2 = nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2))

        self.bn1 = nn.BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.relu3 = nn.ReLU()

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.maxPool1(x)

        x = self.conv2(x)
        x = self.relu2(x)
        x = self.maxPool2(x)

        x = self.bn1(x)
        x = self.relu3(x)
        return x


def get_model(model_name, num_classes=101, pretrained="imagenet"):
    model = pretrainedmodels.__dict__[model_name](pretrained=pretrained)

    for param in model.parameters():
        param.requires_grad = False

    # model.layer0 = ResCusNet()
    model.last_linear = nn.Linear(model.last_linear.in_features, num_classes)
    model.avg_pool = nn.AdaptiveAvgPool2d(1)

    return model


def main():
    model = get_model(model_name_)
    # print(summary(model, (244, 244, 3)))
    print(model)


if __name__ == '__main__':
    main()

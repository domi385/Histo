"""Module contains functions for obtaining PyTorch models."""
import torch.nn as nn
import torchvision.models as models


def get_alexnet(num_outputs, pretrained=True, fixed_weights=False):
    """Function obtains alexnet with given parameters.

    Parameters
    ----------
    num_outputs : int
        number of model outputs
    pretrained : bool
        if true model weights are downloaded from pretrained model on imagenet
    fixed_weigths : bool
        if true, all but last fully connected layer will be fixed

    Returns
    -------
    model : nn.Module
        PyTorch alexnet model
    """
    alexnet = models.alexnet(pretrained=pretrained)
    if fixed_weights:
        for param in alexnet.features.parameters():
            param.requires_grad = False
    num_features = alexnet.classifier[-1].in_features
    alexnet.classifier[-1] = nn.Linear(in_features=num_features, out_features=num_outputs)
    alexnet.classifier[-1].requires_grad = True
    return alexnet


def get_resnet(num_outputs, pretrained=True, fixed_weights=False):
    """Function obtains resnet with given parameters.

    Parameters
    ----------
    num_outputs : int
        number of model outputs
    pretrained : bool
        if true model weights are downloaded from pretrained model on imagenet
    fixed_weigths : bool
        if true, all but last fully connected layer will be fixed

    Returns
    -------
    model : nn.Module
        PyTorch resnet model
    """
    resnet = models.resnet18(pretrained=pretrained)
    if fixed_weights:
        for param in resnet.parameters():
            param.requires_grad = False
    num_features = resnet.fc.in_features
    resnet.fc = nn.Linear(in_features=num_features, out_features=num_outputs)
    return resnet


def get_inception(num_outputs, pretrained=True, fixed_weights=False):
    """Function obtains inception v3 with given parameters.

    Parameters
    ----------
    num_outputs : int
        number of model outputs
    pretrained : bool
        if true model weights are downloaded from pretrained model on imagenet
    fixed_weigths : bool
        if true, all but last fully connected layer will be fixed

    Returns
    -------
    model : nn.Module
        PyTorch inception v3 model
    """
    inception = models.inception_v3(pretrained=pretrained)
    if fixed_weights:
        for param in inception.parameters():
            param.requires_grad = False
    num_features_main = inception.fc.in_features
    inception.fc = nn.Linear(in_features=num_features_main, out_features=num_outputs)
    num_features_aux = inception.AuxLogits.fc.in_features
    inception.AuxLogits.fc = nn.Linear(in_features=num_features_aux,
                                       out_features=num_outputs)
    return inception


def get_densenet(num_outputs, pretrained=True, fixed_weights=False):
    """Function obtains densenet with given parameters.

    Parameters
    ----------
    num_outputs : int
        number of model outputs
    pretrained : bool
        if true model weights are downloaded from pretrained model on imagenet
    fixed_weigths : bool
        if true, all but last fully connected layer will be fixed

    Returns
    -------
    model : nn.Module
        PyTorch densenet model
    """
    dense = models.densenet121(pretrained=pretrained)
    if fixed_weights:
        for param in dense.parameters():
            param.requires_grad = False
    num_features = dense.classifier.in_features
    dense.classifier = nn.Linear(in_features=num_features, out_features=num_outputs)
    return dense

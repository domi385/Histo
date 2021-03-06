"""Module contains DenseNet experiment definitions."""
import functools
import torchvision.transforms as transforms
import histo.models as models
from histo.experiments.base_experiment import (NUM_CLASSES,
                                               base_experiment_initialization)
import histo.dataset as dataset


def base_densenet_experiment(experiment_name, learn_rate, batch_size,
                             validation_batch_size, num_epochs, weight_decay, pretrained,
                             fixed_weights, data_dict, device):
    """Base densenet experiment setup.

    Parameters
    ----------
    experiment_name : str
        current experiment name
    learn_rate : float
        learning rate
    batch_size : int
        training batch size
    validation_batch_size : int
        validation batch size
    num_epochs : int
        total number of epochs used in training
    weight_decay : float
        L2 weight decay constant
    pretrained : bool
        if true pretrained model will be used
    fixed_weights : bool
        if true all but last fully connected layers will be freezed while training
    data_dict : dict(str, torch.utils.data.DataLoader)
        dictionary with training, validation and test dataloaders
    device : torch.device
        device on which to perform operations

    Returns
    -------
    experiment : Experiment
        experiment instance
    """
    model = functools.partial(models.get_densenet, num_outputs=NUM_CLASSES,
                              pretrained=pretrained, fixed_weights=fixed_weights)
    return base_experiment_initialization(
        model_method=model, experiment_name=experiment_name, learn_rate=learn_rate,
        batch_size=batch_size, validation_batch_size=validation_batch_size,
        num_epochs=num_epochs, weight_decay=weight_decay, data_dict=data_dict,
        device=device)


def transformations_densenet_experiment_base(
        train_transformations, experiment_name, learn_rate, batch_size,
        validation_batch_size, num_epochs, weight_decay, pretrained, fixed_weights,
        device):
    """Function uses base_densenet_experiment with additional transformations for train
    set.

    Parameters
    ----------
    train_transformations : torchvision.transforms
        transforms object

    Returns
    -------
    experiment : Experiment
        experiment instance
    """
    valid_transform = transforms.Compose([
        transforms.ToTensor()])
    test_transform = transforms.Compose([
        transforms.ToTensor()
    ])

    data_transform = {
        'train': train_transformations,
        'valid': valid_transform,
        'test': test_transform
    }
    pcam_dataset = dataset.PCamDatasets(data_transforms=data_transform)
    train_set = pcam_dataset.train
    valid_set = pcam_dataset.valid
    test_set = pcam_dataset.test
    data_dict = {dataset.TRAIN: train_set, dataset.VALID: valid_set,
                 dataset.TEST: test_set}
    return base_densenet_experiment(
        experiment_name=experiment_name, learn_rate=learn_rate, batch_size=batch_size,
        validation_batch_size=validation_batch_size, num_epochs=num_epochs,
        weight_decay=weight_decay, pretrained=pretrained, fixed_weights=fixed_weights,
        data_dict=data_dict, device=device)


def get_experiment_densenet_1(data_dict, device):
    """See base_densenet_experiment"""
    return base_densenet_experiment(
        experiment_name="densenet_1", learn_rate=1e-5, batch_size=32,
        validation_batch_size=1024, num_epochs=10, weight_decay=0, pretrained=True,
        fixed_weights=False, data_dict=data_dict, device=device)


def get_experiment_densenet_2(data_dict, device):
    """See base_densenet_experiment"""
    return base_densenet_experiment(
        experiment_name="densenet_2", learn_rate=1e-3, batch_size=32,
        validation_batch_size=1024, num_epochs=10, weight_decay=0, pretrained=True,
        fixed_weights=False, data_dict=data_dict, device=device)


def get_experiment_densenet_3(data_dict, device):
    """See base_densenet_experiment"""
    return base_densenet_experiment(
        experiment_name="densenet_3", learn_rate=1e-4, batch_size=32,
        validation_batch_size=1024, num_epochs=10, weight_decay=0, pretrained=True,
        fixed_weights=False, data_dict=data_dict, device=device)


def get_experiment_densenet_4(data_dict, device):
    """See base_densenet_experiment"""
    return base_densenet_experiment(
        experiment_name="densenet_4", learn_rate=1e-5, batch_size=32,
        validation_batch_size=1024, num_epochs=10, weight_decay=0, pretrained=True,
        fixed_weights=True, data_dict=data_dict, device=device)


def get_experiment_densenet_5(data_dict, device):
    """See base_densenet_experiment"""
    return base_densenet_experiment(
        experiment_name="densenet_5", learn_rate=1e-3, batch_size=32,
        validation_batch_size=1024, num_epochs=10, weight_decay=0, pretrained=True,
        fixed_weights=True, data_dict=data_dict, device=device)


def get_experiment_densenet_6(data_dict, device):
    """See base_densenet_experiment"""
    return base_densenet_experiment(
        experiment_name="densenet_6", learn_rate=1e-4, batch_size=32,
        validation_batch_size=1024, num_epochs=10, weight_decay=0, pretrained=True,
        fixed_weights=True, data_dict=data_dict, device=device)


def get_experiment_densenet_7(data_dict, device):
    """See base_densenet_experiment"""
    return base_densenet_experiment(
        experiment_name="densenet_7", learn_rate=1e-6, batch_size=32,
        validation_batch_size=1024, num_epochs=8, weight_decay=0, pretrained=True,
        fixed_weights=False, data_dict=data_dict, device=device)


def get_experiment_densenet_8(data_dict, device):
    """See base_densenet_experiment"""
    return base_densenet_experiment(
        experiment_name="densenet_8", learn_rate=1e-6, batch_size=32,
        validation_batch_size=1024, num_epochs=8, weight_decay=0, pretrained=True,
        fixed_weights=True, data_dict=data_dict, device=device)


def get_experiment_densenet_9(data_dict, device):
    """See base_densenet_experiment"""
    return base_densenet_experiment(
        experiment_name="densenet_9", learn_rate=1e-3, batch_size=32,
        validation_batch_size=1024, num_epochs=20, weight_decay=0, pretrained=False,
        fixed_weights=False, data_dict=data_dict, device=device)


def get_experiment_densenet_10(data_dict, device):
    """See base_densenet_experiment"""
    return base_densenet_experiment(
        experiment_name="densenet_10", learn_rate=1e-4, batch_size=32,
        validation_batch_size=1024, num_epochs=20, weight_decay=0, pretrained=False,
        fixed_weights=False, data_dict=data_dict, device=device)


def get_experiment_densenet_11(data_dict, device):
    """See base_densenet_experiment"""
    return base_densenet_experiment(
        experiment_name="densenet_11", learn_rate=1e-5, batch_size=32,
        validation_batch_size=1024, num_epochs=20, weight_decay=0, pretrained=False,
        fixed_weights=False, data_dict=data_dict, device=device)


def get_experiment_densenet_12(data_dict, device):
    """See base_densenet_experiment"""
    return base_densenet_experiment(
        experiment_name="densenet_12", learn_rate=1e-6, batch_size=32,
        validation_batch_size=1024, num_epochs=20, weight_decay=0, pretrained=False,
        fixed_weights=False, data_dict=data_dict, device=device)


def get_experiment_densenet_rotation(device):
    """See transformations_densenet_experiment_base"""
    train_transform = transforms.Compose([
        transforms.RandomRotation(degrees=180),
        transforms.ToTensor(),
    ])

    return transformations_densenet_experiment_base(
        train_transformations=train_transform, experiment_name="densenet_rotation",
        learn_rate=1e-4, batch_size=32, validation_batch_size=1024, num_epochs=20,
        weight_decay=0, pretrained=True, fixed_weights=False, device=device)


def get_experiment_densenet_horizontalflip(device):
    """See transformations_densenet_experiment_base"""
    train_transform = transforms.Compose([
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.ToTensor(),
    ])
    return transformations_densenet_experiment_base(
        train_transformations=train_transform, experiment_name="horizontal_flip",
        learn_rate=1e-4, batch_size=32, validation_batch_size=1024, num_epochs=20,
        weight_decay=0, pretrained=True, fixed_weights=False, device=device)


def get_experiment_densenet_verticalflip(device):
    """See transformations_densenet_experiment_base"""
    train_transform = transforms.Compose([
        transforms.RandomVerticalFlip(p=0.5),
        transforms.ToTensor(),
    ])
    return transformations_densenet_experiment_base(
        train_transformations=train_transform, experiment_name="verticalflip",
        learn_rate=1e-4, batch_size=32, validation_batch_size=1024, num_epochs=20,
        weight_decay=0, pretrained=True, fixed_weights=False, device=device)


def get_experiment_densenet_brightness(device):
    """See transformations_densenet_experiment_base"""
    train_transform = transforms.Compose([
        transforms.ColorJitter(brightness=0.05),
        transforms.ToTensor(),
    ])
    return transformations_densenet_experiment_base(
        train_transformations=train_transform, experiment_name="densenet_brightness",
        learn_rate=1e-4, batch_size=32, validation_batch_size=1024, num_epochs=20,
        weight_decay=0, pretrained=True, fixed_weights=False, device=device)


def get_experiment_densenet_contrast(device):
    """See transformations_densenet_experiment_base"""
    train_transform = transforms.Compose([
        transforms.ColorJitter(contrast=0.05),
        transforms.ToTensor(),
    ])
    return transformations_densenet_experiment_base(
        train_transformations=train_transform, experiment_name="densenet_contrast",
        learn_rate=1e-4, batch_size=32, validation_batch_size=1024, num_epochs=20,
        weight_decay=0, pretrained=True, fixed_weights=False, device=device)


def get_experiment_densenet_hue(device):
    """See transformations_densenet_experiment_base"""
    train_transform = transforms.Compose([
        transforms.ColorJitter(hue=0.025),
        transforms.ToTensor(),
    ])
    return transformations_densenet_experiment_base(
        train_transformations=train_transform, experiment_name="densenet_hue",
        learn_rate=1e-4, batch_size=32, validation_batch_size=1024, num_epochs=20,
        weight_decay=0, pretrained=True, fixed_weights=False, device=device)


def get_experiment_densenet_saturation(device):
    """See transformations_densenet_experiment_base"""
    train_transform = transforms.Compose([
        transforms.ColorJitter(saturation=0.05),
        transforms.ToTensor(),
    ])
    return transformations_densenet_experiment_base(
        train_transformations=train_transform, experiment_name="densenet_saturation",
        learn_rate=1e-4, batch_size=32, validation_batch_size=1024, num_epochs=20,
        weight_decay=0, pretrained=True, fixed_weights=False, device=device)


def get_experiment_densenet_small_rotation(device):
    """See transformations_densenet_experiment_base"""
    train_transform = transforms.Compose([
        transforms.RandomRotation(degrees=5),
        transforms.ToTensor(),
    ])
    return transformations_densenet_experiment_base(
        train_transformations=train_transform, experiment_name="densenet_smallrotation",
        learn_rate=1e-4, batch_size=32, validation_batch_size=1024, num_epochs=20,
        weight_decay=0, pretrained=True, fixed_weights=False, device=device)


def get_experiment_densenet_transformation_composition(device):
    """See transformations_densenet_experiment_base"""
    train_transform = transforms.Compose(
        transforms=[
            transforms.RandomApply(
                [transforms.RandomOrder(transforms=[
                    transforms.RandomHorizontalFlip(p=0.5),
                    transforms.RandomVerticalFlip(p=0.5),
                    transforms.ColorJitter(brightness=0.05),
                    transforms.ColorJitter(contrast=0.05),
                    transforms.ColorJitter(hue=0.025),
                    transforms.RandomRotation(degrees=5)])], p=0.5),
            transforms.ToTensor()])
    return transformations_densenet_experiment_base(
        train_transformations=train_transform,
        experiment_name="densenet_transformation_composition", learn_rate=1e-4,
        batch_size=32, validation_batch_size=1024, num_epochs=20, weight_decay=0,
        pretrained=True, fixed_weights=False, device=device)

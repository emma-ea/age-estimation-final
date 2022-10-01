# Age estimation project - final year project

model training was done in google colab, the notebook file is stored in the colab_notebook directory.

# Dataset

To download dataset to main directory. Run bash script in data directory or simply click this hyperlink to download dataset.

Extract dataset and to a directory.

[appa-real](http://158.109.8.102/AppaRealAge/appa-real-release.zip)

# Creating a virtual environment

To run this project, its recommended you create a virtual environment and download all needed dependencies or modules from the
requirements.txt file using this command.

1. Create virtual environment

`python -m pip install venv`

`python -m venv my-environment`

`source env/bin/activate`

2. Install modules into virtual environment

`pip install -r requirement.txt`


# Running code

## model.py

Run this script if you want to explore the model parameters. Running this script for the first time will download and cache
the se_resnext101 model used in our project.

## defaults.py

this script contains hyperparameter configuration used in the project which include learning rate, epochs, optimizer, batch size, etc.

## dataset.py

Run this script by passing in the dataset directory to explore the dataset. 

for help: `python dataset.py -h`

eg: `python dataset.py --data_dir data/appa-real-database/`

## train.py

Run this script if you want to train the model.

for help: `python train.py -h`

eg: `python train.py --data_dir data/appa-real-database/ --tensorboard ./tf_log/`


## test.py

Run this script after training if you want to test a saved model.

for help: `python test.py -h`

eg: `python test.py --data_dir data/appa-real-database/ --resume checkpoint/path-to-saved-model-weights`

## demo.py

Run this file if you want to test model using a live webcam or photo

for help: `python demo.py -h`

eg using an image: `python demo.py --resume checkpoint/path-to-saved-model-weights --img_dir path-to-input-image --output_dir path-to-output-directory`

eg using webcam: `python demo.py --resume checkpoint/path-to-saved-model-weights`



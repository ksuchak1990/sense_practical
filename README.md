# sense_practical

This repository contains materials for the SENSE practical on agent-based
modelling as part of the training week on Machine Learning and AI.
The materials for the practical are separated into 4 subdirectories.

The `./data/` subdirectory contains the data required for the practical, as well
providing a location in which to place any data outputs that may be produced.

The `./notebooks/` subdirectory contains the jupyter notebooks that will be run
for the practical.
The practical consists of 4 notebooks.
The first of these notebooks (`./notebooks/0_introduction.ipynb`) provides an
introduction to the practical, giving an overview of agent-based models, the
pedestrian agent-based model used in this practical and how it will be used in
the practical.
The second notebook (`./notebooks/1_running_models.ipynb`) briefly outlines how
we go about running an instance of the agent-based model with user-specified
values for parameters.
The third notebook (`./notebooks/2_speed_calibration.ipynb`) provides some
activities in which we analyse some of the data provided with the goal of
identifying appropriate values for various speed parameters in the model.
The fourth notebook (`./notebooks/3_birth_rate_calibration.ipynb`) contains the
main activities of the practical in which we use the speed parameter values
found in the previous notebook to run the model with the aim of calibrating
other agent parameters in the model (specifically, the agent birth-rate).

## Getting started

* Cloning down the repository
* Setting up the environment
* Accessing data
* Using `jupyter-notebooks`/`jupyter-lab`

### Cloning down this repository

The first step in getting started with this practical is to get hold of this
repository.
We can do this by using git to clone the repository onto our own machines.
This is achieved by opening the terminal/command prompt and running the
following command:
```
git clone https://github.com/ksuchak1990/sense_practical
```
This will download a copy of the repository onto our machines.
We then wish to move into the folder that we have just downloaded, which we can
do by running the following command:
```
cd sense_practical
```

### Setting up the environment

This repository contains an `environment.yml` file, which documents the python
packages that are required to run this practical.
The easiest way to install this list of packages is to open your terminal or
anaconda prompt and run the following command:
```
conda env create -f environment.yml
```
This will create a conda environment named `sense-abm` which will contain all of
the required packages.
The environment can then be activated by running the following command:
```
conda activate sense-abm
```
Be aware that we should ensure that this environment is activated before running
any of the notebooks for the practicals.

## Practical Outline

* Getting hold of data
* Reformatting data
* Getting hold of video if necessary

## More Info

* Look at [DUST repository](https://github.com/urban-analytics/dust)
* Contact me: k.suchak@leeds.ac.uk


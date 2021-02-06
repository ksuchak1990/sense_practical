# sense_practical

## Introduction

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

The `./src/` subdirectory contains any source code used for the practical.
This is divided into two purposes:

* Code used for preprocessing data
* Code used for the agent-based model

The `./docs/` subdirectory contains any documentation relevant to the practical.

## Getting started

This section of the `README` will outline how to get started with the practical.
The process of getting started involves the following steps:

* Getting hold of the practical materials
* Installing the necessary python packages
* Getting access to the practical data
* Starting up `jupyter-notebook`/`jupyter-lab`

This practical can be approached via two avenues:

* GitHub
* Minerva

The requirements for obtaining the practical from GitHub are:

* `git`
* `make`
* `python 3.x` (preferably Anaconda Python)

The requirements for obtaining the practical from Minerva are that you have
access to the SENSE CDT Minerva organisation.
The advantage of obtaining the materials via Minerva is ease of access - you
will be able to download a zipped folder, unzip it and get started.
The advantage of obtaining the materials via GitHub is that you will be able to
pull any changes that I make to the practical in close to real-time.

*(The remainder of this section will assume that you are using Anaconda Python)*

### Getting started from GitHub

The process of getting started from GitHub consists of the following steps:

* Cloning down the repository with `git`
* Setting up a python environment with `conda`
* Setting up the data with `python 3`, `make` and `tar`

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

After getting hold of the repository, we wish to set up an environment.
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

After having installed all of the required packages under an environment and
having activated the environment, we wish to set up the data.
At present the input data exists in `./data/inputs` as a tar zip
(`frames.tar.gz`).
If you have `make` and `tar` installed on your computer then the process of
setting up the data can be automated by running:

```
make frames
```

Once we reach this stage, we are ready to get going with the notebooks in
`./notebooks/`!

### Getting Started from Minerva

If obtaining this practical from Minerva, you don't need to worry about any of
the data processing issues mentioned above - you can just download the zipped
folder, set up a Python environment and you're ready to go!

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

## More Info

* Look at [DUST repository](https://github.com/urban-analytics/dust)
* Contact me: k.suchak@leeds.ac.uk


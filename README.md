# PHSX815_Project2

## The Code

### Nested_Categorical.py

Provides 2 output files for the 2 tested hypotheses

-h shows possible inputs

Can change number of experiments, number of rolls, sides for simple hypothesis, and the categorical distribution used for complex hypothesis

Simple hypothesis (all 6 sided dice) outputs to a file called "alld6.txt"

Complex hypothesis (categorical distribution of dice) outputs to a file called "categorical.txt"

### Analysis.py

-h shows inputs

Can change number of the initial categorical distribution for the complex hypothesis (determines the x axis of its histogram)

Defaults to 20 to match the amount in the paper

Saves histograms using the two output files from Nested_Categorical.py as inputs

alld6.pdf is the histogram for the simple hypothesis

categorical.pdf is the histogram for the complex hypothesis

Also prints the probabilities for the bins that correspond to the dataset of the customer for each hypothesis

## Paper

File PHSX815_Proj.pdf

Uses the histograms  alld6.pdf and categorical.pdf in this repository

Replicate using default settings of Nested_Categorical.py and Analysis.py

Can also be found at https://www.overleaf.com/read/ndpmfctcchqd



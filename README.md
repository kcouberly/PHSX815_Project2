# PHSX815_Project2

## For Peer Review Input

Random.py has been modified to include random.categorical function to produce categorical distributions (sourced from Random.py in Prof Rogan's github)

### Nested_Categorical.py

Provides 2 outputs for the 2 potential hypotheses

-h for possible inputs

Runs a categorical distribution to determine which dice are rolled (default 1-20, can modify with settings)

Complex hypothesis is a categorical within a categorical -- initial dice roll determines the number of sides of the following dice roll

Simple hypothesis rolls only 6 sided die

Then dice are rolled n number of times and results averaged

alld6.txt output for simple, categorical.txt output for complex

For some reason the code creates empty output files the first time I run it, then fills the outputs correctly if I run it a second time, not too big a deal but I'm not sure why this is

Is anything confusing or hard to follow in the Nested_Categorical.py code?

Ideas for analysis -- which hypothesis is has higher likelyhood for a given roll average, plot the results of output files in a histogram

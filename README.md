# d-separation
CS676/hw1

This is a python implementation of
> Koller and Friedman (2009), "Probabilistic Graphical Models: Principles and Techniques" (page 75)

Usage
==========
```
python d-separation.py -f your_input_file -n1 node1 -n2 node2 -ob given_observations
```
given_observations should be in the format of 'X1,X2,...'(no space).

Simple Test
==========
Here I use a test case as in
> Koller and Friedman (2009), "Probabilistic Graphical Models: Principles and Techniques" (page 76)

The graph looks like below and is described in [example.py](https://github.com/qchenclaire/d-separation/blob/master/example.py)
![Alt text](https://github.com/qchenclaire/d-separation/blob/master/example.JPG=250x250)

For example,
```
python d-separation.py -f example.txt -n1 1 -n2 4 -ob 3
```
returns
```
False
```
means - <img src="https://latex.codecogs.com/gif.latex?1 \not \indep_d 4 | 3" />
```
python d-separation.py -f example.txt -n1 1 -n2 4 -ob 2,3
```
returns
```
True
```
means - <img src="https://latex.codecogs.com/gif.latex?1\indep_d 4 | 2, 3" /> 

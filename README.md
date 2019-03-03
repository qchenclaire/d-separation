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
means 1 and 4 are not d-separated given 3
```
python d-separation.py -f example.txt -n1 1 -n2 4 -ob 2,3
```
returns
```
True
```
means 1 and 4 not d-separated given 2, 3

Running Homework Example
==========
<!-- ```
python d-separation.py -f dag.txt -n1 61 -n2 68 -ob 4,19,90
```
returns
```
False
```


```
python d-separation.py -f dag.txt -n1 55 -n2 27 -ob 4,8,9,12,29,32,40,44,45,48,50,52
```
returns
```
True
``` -->
```
sh run.sh
```
returns
```
False
True
```

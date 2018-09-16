# Linear-Regression-using-SGD
Batch Gradient Descent(BGD) is an approach to find the least squared error which is defined by a Cost Function.
In this method, we have to come across only one training example at a time. Convergence occur not in smoother way.
The squared error will never reach to the minima instead it keeps oscillating around the minima. So the minima value
will not be exact. This is where this approach fails when we have to deal with high degree of precision. 

It does not make sum or average of examples in the training set and it is advised to take random training set.
This approach seems much faster than BGD when it comes to large data set. Its rapidness to convergence makes it
worth to be used ahead of BGD. 
 

Basic Definitions:

1. Epochs represent the no. of times we visit the data set.

2. Rate represents the size of step we take to reach minima (confidence) also called alpha.

3. Cost Function defines the relation for the Least Squared Error.

4. Bias term refers to the intercept term in the hypothesis equation.


Limitation of using this approach:

We don't get to know the precised value of the point of convergence of the cost function. 


Note:
Instead of taking one training example at a time, we can consider several mini batches inside the training set. 


import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:

    def __init__(self):
        self.q0=0.0
        self.q1=0.0
        self.rate=0.001
        self.epoch=4000


    def train_by_converge(self,x,y):       #training the model
        hox=[0]*x.size
        for i in range(self.epoch):
            for j in range(x.size):
                yp=(self.q1*x[j]+self.q0)
                hox[j]=yp
                min_cost_bias=-(1*(y[j]-yp))
                min_cost_slope=-(x[j]*(y[j]-yp))
                self.q0=self.q0-(self.rate*min_cost_bias)
                self.q1=self.q1-(self.rate*min_cost_slope)
            
            
        hox=np.array(hox)
        return self.q0,self.q1,hox

    def test(self,test_x):                #testing with best fit
        predicted_y=(test_x*self.q1)+self.q0
        return predicted_y

x=np.array([4,2,6,3,7,9,5,7,8,4])
y=np.array([4,3,7,2,9,8,5,7,2,0])
lr=LinearRegression()            #object creation
b,m,hox=lr.train_by_converge(x,y)
print m,b
yp=lr.test(x)
print yp
plt.scatter(x,y)
plt.plot(x,yp,"r")
plt.show()

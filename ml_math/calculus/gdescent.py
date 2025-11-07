import math


alpha=0.005
x=0.05
eps=1e-8
max_iter=1000

def function(x):
    return math.exp( x)-math.log(x)
def fPrime(x): 
    return math.exp(x)-(1/x)
def update(x,alpha):
    return x-alpha*fPrime(x)

pre_val=function(x)
for i in range(max_iter):
    x=update(x,alpha)
    curr_val=function(x)

    if(abs(curr_val-pre_val)<eps):
        print(f"Converged at iteration : {i} ")
        break
    # if curr_val> pre_val:
    #     x=update(x,-alpha)
    #     curr_val=function(x)
    #     break
    pre_val=curr_val
print(f"Minimum value  is: {x:.10f}")
print(f"futncion  with minimum value is: {function(x):.10f}")

import math 
m,b=0,0
alpha=0.05
max_iter=1000
eps=1e-8
def f(m,b):
    return 14*m*m+3*b*b+38+12*m*b-42*m-20*b

def grad(m,b):
    dfx=28*m+12*b-42
    dfy=6*b+12*m-20
    return dfx,dfy
def update(m,b,alpha):
    grad_x,grad_y=grad(m,b)
    m=m-alpha*grad_x
    b=b-alpha*grad_y
    return m,b
pre_val=f(m,b)
for i in range(max_iter):
    m,b=update(m,b,alpha)
    curr_val=f(m,b)

    if(abs(curr_val-pre_val)<eps):
        print(f"maximum iteration is : {i}")
        break
    pre_val=curr_val
print(f"Minimum value is :m={m:.6f},b={b:.6f}")
print(f"Function with minimum value is {f(m,b):.10f}")
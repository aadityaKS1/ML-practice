import numpy as np
import matplotlib.pyplot as plt
import utils

def birthday_prob(n):
    if n>365:
        return 1
    days=365
    i=np.arange(n)
    prob_unique=np.prod((days-i)/days)
    return 1-prob_unique

group_sizes=np.arange(1,61)
probabilites=[birthday_prob(n) for n in group_sizes]

plt.plot(group_sizes,probabilites)
plt.title("Birthday Problem")
plt.xlabel("People in Room")
plt.ylabel("Probabiltiy")
plt.show()
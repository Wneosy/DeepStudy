import numpy as np
t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)
ans = mean_squared_error(np.array(y), np.array(t))
print(ans)
y = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]
ans = mean_squared_error(np.array(y), np.array(t))
print(ans)

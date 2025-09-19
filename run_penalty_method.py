import math
import matplotlib.pyplot as plt
import numpy as np # optional - uncomment and use if you wish

# ==============================
# run_gradient_descent function:
# ==============================

def norm2(A):
    f = 0

    for j in range(0, len(A)):
       f = f + abs(A[j])**2

    return math.sqrt(f)


# To do: Write this function (uncomment the line below).
def run_gradient_descent(x_start, mu, eta, gradient_tolerance):
  x_j_1 = x_start
  gradient_vec = compute_gradient(x_j_1,mu) # compute the gradient vector each iteration

  while(norm2(gradient_vec) >= gradient_tolerance):
        gradient_vec = compute_gradient(x_j_1,mu)
        x_j_1 = [x_j_1[0] - eta * gradient_vec[0], x_j_1[1] - eta * gradient_vec[1]]  
  
  return x_j_1

# ==============================
# compute_gradient function:
# ==============================

# To do: Write this function (uncomment the line below).
def compute_gradient(x, mu):
   x_1 = x[0]
   x_2 = x[1]
   #gradient_f_of_p = [2*(x_1-1) + 4*mu*x_1(x_1**2 + x_2**2 - 1), 4*(x_2-2) + 4*x_2*mu(x_1**2 + x_2**2 - 1), (x_1**2 + x_2**2-1)**2] # should be a vector of two elements?
   gradient_f_of_p = [2*(x_1-1) + 4*mu*x_1*(x_1**2 + x_2**2 - 1), 4*(x_2-2) + 4*x_2*mu*(x_1**2 + x_2**2 - 1)]

   return gradient_f_of_p
# ==============================
# Main program:
# ==============================

mu_values = [1, 10, 100, 100]
eta = 0.0001;
x_start = [1,3]; #add a two-component vector here, with the chosen starting point
gradient_tolerance = 0.0000001

x_print = []
for mu in mu_values:
  x = run_gradient_descent(x_start, mu, eta, gradient_tolerance)
  x_print.append(x)
  output = f"x = ({x[0]:.4f}, {x[1]:.4f}), mu = {mu:.1f}"
  print(output)

x_1 = []
for i in range(len(x_print)):
   x_1.append((x_print[i])[0])
   

x_2 = []
for i in range(len(x_print)):
   x_2.append((x_print[i])[1])
  

y = x_2
x = mu_values
# plot our list in X,Y coordinates
plt.scatter(x, y)
plt.plot(x, y, marker = '.', markersize = 10)
plt.show()

# Test of norm2
#test_vec = [1,2,7]
#print(norm2(test_vec))
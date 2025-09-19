import math
import matplotlib.pyplot as plt
# ToDo: Uncomment the line below ("import ...") once you have implemented plot_iterations.
# You may need to install Matplotlib first: pip install matplotlib

# ============================================
# get_polynomial_value:
# ============================================

# ToDo: Write the get_polynomial_value function


def get_polynomial_value(x, polynomial_coefficients):
    poly_nr_coeff = len(polynomial_coefficients)  
    a = polynomial_coefficients.copy() # a is a list of coefficients [a_0,a_1,a_2.....a_n]
    x_list = []
    for i in range(poly_nr_coeff):
        x_list.append(pow(x,i))
    total = 0
    results = []
    for i in range(poly_nr_coeff):
        results.append(a[i] * x_list[i])
    for n in range(len(results)):
        total += results[n]
    
    return total

# ============================================
# differentiate_polynomial:
# ============================================

# ToDo: Write the differentiate_polynomial function

def differentiate_polynomial(polynomial_coefficients, derivative_order):
    for n in range(derivative_order):
        new_coeffs = []
        for i in range(1, len(polynomial_coefficients)):   # skip constant term (i=0)
            new_coeffs.append(i * polynomial_coefficients[i])
        
        polynomial_coefficients = new_coeffs # case where n = 1 skips for loop and sets poly coeffs to empty set

        if not polynomial_coefficients:   # polynomial became zero
            return []
    
    return polynomial_coefficients

# ============================================
# step_newton_raphson:
# ============================================

def step_newton_raphson(x, f_prime, f_double_prime):
    x_j_plus_1 =  x - (f_prime / f_double_prime)

    return x_j_plus_1
# ============================================
# run_newton-raphson:
# ============================================
     
def run_newton_raphson(polynomial_coefficients, starting_point, tolerance, maximum_number_of_iterations):
    X = []
    F = []
    if(len(polynomial_coefficients) < 2):
        print("the degree of the polynomial must be 2 or larger")
        return []

    f_prime = differentiate_polynomial(polynomial_coefficients, 1)
    f_biss = differentiate_polynomial(polynomial_coefficients, 2)
    f_prime_at_x_0 = get_polynomial_value(starting_point,f_prime)
    f_biss_at_x_0 = get_polynomial_value(starting_point,f_biss) #- if f_biss is 0 then dont
    if (f_biss_at_x_0 == 0):
        print("Second derivative of f(x0) was 0")
        return [] 
    else:
        x_j_plus_1 = step_newton_raphson(starting_point, f_prime_at_x_0, f_biss_at_x_0) # Otherwise start the algorithm with x0, f'(x0) and f''(x0)
        if(abs(x_j_plus_1 - starting_point) >= tolerance ): 
            X.append(starting_point) # X[0] = starting point
            F.append(get_polynomial_value(starting_point,polynomial_coefficients)) #f(x0)
        else:
            return [X,F]
        for n in range(1,maximum_number_of_iterations): # then we can execute our main iteration loop
            f_prime_at_x = get_polynomial_value(x_j_plus_1,f_prime)
            f_biss_at_x = get_polynomial_value(x_j_plus_1,f_biss) #- if f_biss is 0 then dont
            if (f_biss_at_x == 0):
                print("Second derivative of f was 0")
                return [] 
            else:
                X.append(x_j_plus_1)
                func_val_at_j_plus_1 = get_polynomial_value(x_j_plus_1,polynomial_coefficients)
                F.append(func_val_at_j_plus_1)
                x_j = x_j_plus_1 # Set the old xj plus 1 to xj
                x_j_plus_1 = step_newton_raphson(x_j, f_prime_at_x, f_biss_at_x) # New x j plus 1
                if(abs(x_j_plus_1 - x_j) < tolerance ):  # Check tolerance 
                    return [X,F]



# ============================================
# plot_iterations:
# ============================================

# ToDo: Write the plot_iterations function
#
# Here, you should use matplotlib. 
# Note: You must uncomment the second "import ..." statement above
# Then uncomment the line below and implement the function:
def plot_iterations(polynomial_coefficients,iterations):
    if(len(iterations) == 0):
        print("“the degree of the polynomial must be 2 or larger")
        return
    x_values = []
    y_values = []
    # Initialize the starting, stopping, and stepping values
    start = min(iterations[0])- 0.1
    stop = max(iterations[0]) + 0.1
    step = 0.00001
    #iterate until 'start' reaches or exceeds 'stop'
    while start < stop:
        start += step
        x_values.append(start)
        y_values.append(get_polynomial_value(start,polynomial_coefficients))
    print(x_values)
    print(y_values)
    plt.scatter(iterations[0],iterations[1])
    plt.plot(x_values, y_values)
    #plt.axis([0,2, 7,12])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
    return
    

# ============================================
# Main loop
# ============================================
tolerance = 0.00001

maximum_number_of_iterations = 10

polynomial_coefficients = [10,-2,-1,1]

starting_point = 2
# ToDo: Uncomment the two lines below, once you have implemented the functions above

iterations = run_newton_raphson(polynomial_coefficients, starting_point,

tolerance, maximum_number_of_iterations)

plot_iterations(polynomial_coefficients, iterations)
"""
HW1 Part 2 Big Data 1/28/2024
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


###########################################
#	    	Main Driver Function       	  #
###########################################


if __name__ == '__main__':

    # =============part c: Plot data and the optimal linear fit=================
    # NOTE: to finish this part, you need to finish the part(a) of this part
    # 		first

    # load the four data points of tihs problem
    X = np.array([0, 2, 3, 4])
    y = np.array([1, 3, 6, 8])

    # plot four data points on the plot
    plt.style.use('ggplot')
    plt.plot(X, y, 'ro')

    # replace the m_opt and b_opt with the solution you obtained from
    # 		part (a), note that y = mx + b
    "*** YOUR CODE HERE ***"
    m_opt = 62. / 35  # your solution from part a
    b_opt = 18. / 35  # your solution from part a
    "*** END YOUR CODE HERE ***"

    # generate 100 points along the line of optimal linear fit.

    # HINT:
    #	1) Use np.linspace to get the x-coordinate of 100 points
    #	2) Calculate the y-coordinate of those 100 points with the m_opt and
    #	   b_opt, remember y = mx+b.
    #	3) Use a.reshape(-1,1), where a is a np.array, to reshape the array
    #	   to appropraite shape for generating plot

    "*** YOUR CODE HERE ***"
    X_space = np.linspace(-1, 5, num=100).reshape(-1, 1)
    y_space = (m_opt * X_space + b_opt).reshape(-1, 1)
    "*** END YOUR CODE HERE ***"

    # plot the optimal learn fit you obtained and save it to your current
    # folder
    plt.plot(X_space, y_space)
    plt.savefig('hw1pr2c.png', format='png')
    plt.close()

    # =============part d: Optimal linear fit with random data points=================

    # variables to start with
    mu, sigma, sampleSize = 0, 1, 100

    # Generate white Gaussian noise
    # HINT: Use np.random.normal to generate noise

    "*** YOUR CODE HERE ***"
    noise = np.random.normal(mu, sigma, sampleSize).reshape(-1, 1)
    "*** END YOUR CODE HERE ***"

    # generate y-coordinate of the 100 points with noise

    # HINT:
    #	1) Use X_space created in the part (c) above as the x-coordinates
    #	2) In this case, y = mx + b + noise
    "*** YOUR CODE HERE ***"
    y_space_rand = m_opt * X_space + b_opt + noise
    "*** END YOUR CODE HERE ***"

    # calculate the new parameters for optimal linear fit using the
    #		100 new points generated above

    # HINT:
    #	1) Use np.ones_like to create a column of 1
    #	2) Use np.hstack to stack column of ones on X_space to create
    #	   X_space_stacked
    #	3) Use np.linalg.solve to solve W_opt following the normal equation:
    #	   X.T * X * W_opt = X.T * y

    "*** YOUR CODE HERE ***"
    X_space_stacked = np.hstack((np.ones_like(y_space), X_space))
    W_opt = np.linalg.solve(X_space_stacked.T @ X_space_stacked,
                            X_space_stacked.T @ y_space_rand)
    "*** END YOUR CODE HERE ***"

    # get the new m, and new b from W_opt obtained above
    b_rand_opt, m_rand_opt = W_opt.item(0), W_opt.item(1)

    # Generate the y-coordinate of 100 points with the new parameters
    #		obtained

    # HINT:
    #	1) Use X_space for x-coordinates (same)
    #	2) y = mx + b
    #	3) Make sure the array is in appropraite shape using a.reshape(-1,1)

    "*** YOUR CODE HERE ***"
    y_pred_rand = np.array(
        [m_rand_opt * x + b_rand_opt for x in X_space]).reshape(-1, 1)
    "*** END YOUR CODE HERE ***"

    # generate plot
    # plot original data points and line
    plt.plot(X, y, 'ro')
    orig_plot, = plt.plot(X_space, y_space, 'r')

    # plot the generated 100 points with white gaussian noise and the new line
    plt.plot(X_space, y_space_rand, 'bo')
    rand_plot, = plt.plot(X_space, y_pred_rand, 'b')

    # set up legend and save the plot to the current folder
    plt.legend((orig_plot, rand_plot),
               ('original fit', 'fit with noise'), loc='best')
    plt.savefig('hw1pr2d.png', format='png')
    plt.close()

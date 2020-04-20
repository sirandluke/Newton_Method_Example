import math
import sys

### Author Luke Sirand


# Algorithm for Newton Method 
# @ param x -> int storing x cor
# @ param y -> int storing y cor
# @ param n -> maximum allowed iterations
# @ param m -> steps of m
# @ return -> void/ print out values at each step
def Newton_Method(x,y,n,m):

    for i in range(0,m):
        x = x + 0.1
        for j in range(0,n):
            g_of_xy = polyFunc(x,y)
            temp = g_of_xy / dy_polyFunc(y)
            y = y - temp
        x = round(x,6)
        send_to_file = (str(i) + space + str(x) + space + str(y) + space + str(g_of_xy))
        print(send_to_file)




# G(x,y) = 3x^7 + 2y^5 - x^3 + y^3 -3
def polyFunc(x,y):
    return (3*(x**7) + 2*(y**5) - (x**3) + (y**3) - 3)

# dG(x,y)/dy = 10y^4 + 3y^2
def dy_polyFunc(y):
    return (10*(y**4) + 3*(y**2))


# for formatting
space = "                "

# Let x = 0 & y = 1 for start of iteration
x = 0
y = 1

# define number of iterations n
n = 4

# define the number of steps m for x variable
m = 10

# perform Newton Method
send_to_file = ("i" + space + "x" + space + "y" + space + "        G(x,y)")

# send all output to txt file
sys.stdout = open('output.txt', 'w')
print (send_to_file)
print ('\n')
Newton_Method(x,y,n,m)

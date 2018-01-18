# Simpson_Rule-Array-Operations_Initial_Integration_Differentiation-
Mathematical acrobatics with CO2 data

Simpson Rule
Write a program to that integrates sin(x)e^(-x)dx from 0 to pi
using the both the Trapezoidal and Simpson
Rules. Make the program write out a delimited file where the first column is the number of bins, the
second the Trapezoidal rule value, and the third the Simpson’s rule value. Write out the data file for
the number of bins ranging from 1 to 20.

Array Operation with CO2 Data
Using the ”co2 mm mlo.txt” data, write a script that uses the Numpy where() function and the min()
and max() functions to find and print the largest and smallest CO2 fractions using the interpolated
column for the month of December only!
Note: the where() function creates a more complicated datatype than one might assume. It is called
a tuple. To ensure a useable array of indices, run the results of np.where() through np.squeeze()
which reduces the dimensionality. When in doubt, use the type() function manually to see what kind
of variable you are dealing with.

Initial Differentiation
Using the CO2 data, use the central difference method to calculate the derivative of the ”seasonally
adjusted trend” data. You can skip the derivative of the first and last points for now (but note you
would use forward and backwards formulas for those two points). Have the script make and save a
plot of the derivative. 

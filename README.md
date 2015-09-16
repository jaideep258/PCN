# PCN
PCN assignments

assgn1.py contains implementation of followng three questions:

1. A biased coin is tossed successively until heads comes up twice in a row or tails comes up twice in a
row. The probability of the coin landing heads is q. Let X be the number of tosses until two heads
or two tails appear in a row. Find an expression for the probability mass function of X. Find the
expected value for X as a function of q.

2. Consider the generation of uniformly distributed pseudorandom numbers using the multiplicative con-
gruential method.
sn+1 = (k · sn)mod(m), n = 0, 1, . . .
rn = sn/m, n = 0, 1, . . .
s0 is referred to as the seed which may be any integer between 1 and 2147483646, and rn is the sequence
of uniformly distributed numbers in the interval (0,1). Let k = 16807 and m = 2147483647. Write a
program to implement the above method, and test the program by calculating the mean and variance
for 10000 generated numbers. Use a starting seed value of s0 = 1111. Also, count the number of
outcomes in each of the intervals [ j−1 10 , j 10 ], j = 1, . . . , 10. The output of your program should show the
calculated mean and variance, as well as the number of outcomes in each interval. It should NOT print
out each of the 10000 generated numbers. Submit hard copies of your source code and the output of
your program. Note that you may need to use double precision floating point variables for the seeds
and the random numbers.

3. An exponentially distributed pseudorandom number may be generated using the following approach:
y = −1/Lambda*ln r
y is the random number which is exponentially distributed with parameter lambda, and r is random number
uniformly distributed between 0 and 1. Generate a sequence of 10000 exponentially distributed random
numbers with  = 2, and calculate the mean and variance in your main program. Use the program
in the previous problem to generate the r values. Do NOT use any system supplied random number
generators. Compare these values to the theoretical values of mean and variance for the exponential
distribution. 

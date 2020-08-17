#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) there is 1 while loop in this which will increase as more items are iterated


b) O(n log n) There is a nested loop the outer loop will run O(n) times but the inner loop 
   runs O(log n) the value of j is doubling each time


c) O(n) regardless of how many times it runs or what number you put in bunnies will always be 
   O(n) it does 1 operation on bunnyEars regardless of what is passed

## Exercise II

# For this exercise I will pretend we have 20 floors and floor 6 (f) is the breaking floor
# We can take a similar approch as binary search.

# Spread the floors out into 2 different arrays using the midppoint labeled lower and upper.  This will put the left hand side
# as the lower floors (lower floors 1 - 10) and the right hand side as the higher floors (higher floors 11 - 20).

# We will then take the midpoint of of lower(5) and check to see if the egg breaks. 
#   if No, we then use the right-side of lower and drop and egg until it breaks (in this case it would break at 6, f)
#   if Yes, then we use the left-side of lower and drop the egg until it does not break and we know index + 1 is the breaking floor

# Worst case scenario:
# If we only had 7 floors we would have to search the entire array of lower and half the array of higher to find the breaking floor

# Big O: O(n log(n))

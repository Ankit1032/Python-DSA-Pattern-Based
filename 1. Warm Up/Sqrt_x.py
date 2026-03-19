'''
Approach
We first check if x is 0 or 1. If it is, we know that the square root of 0 and 1 is 0 and 1 respectively, so we directly return x.

For any other value of x, we set up a search range between 1 and x. We initialize two variables start and end to represent the range.

Now comes the clever part: We use a while loop to repeatedly divide the search range in half (Binary Search) to find the square root.

In each iteration of the loop, we calculate the middle value mid using the formula start + (end - start) / 2. This formula ensures that we don't encounter any integer overflow when dealing with large values of x.

Next, we calculate the square of mid and compare it with x.

If the square of mid is greater than x, we know the square root lies in the lower half of the search range. So, we move the end pointer to the left to narrow down the search range.

If the square of mid is equal to x, we have found the square root! So, we return mid as the answer.

If the square of mid is less than x, we know the square root lies in the upper half of the search range. So, we move the start pointer to the right to continue the search.

We repeat steps 4 to 8 until the start pointer becomes greater than the end pointer. At this point, we have found the floor value of the square root, and end holds that value.

To ensure that we return the correct floor value of the square root, we round down the value of end to the nearest integer using the Math.round() method.
'''
import math
class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2: # the sqrt of 0 is 0 and sqrt of 1 is 1
            return x
        
        start = 1
        end = x

        while (start <= end):
            mid = (start + end)//2

            sq = mid*mid

            if sq == x:
                return mid

            if sq > x:
                end = mid-1
            else:
                start = mid+1

        return end

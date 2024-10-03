# Find the missing number

## Explanation

Given an array **arr[]** of size **N-1** with integers in the range if **[1, N]**, find the missing number from the first **N** integers.

## Examples ##

    Input: arr[] = {1, 2, 4, 6, 3, 7, 8} , N = 8
    Output: 5
    Explanation: Here the size of the array is 8, so the range will be [1, 8]. The missing number between 1 to 8 is 5

    Input: arr[] = {1, 2, 3, 5}, N = 5
    Output: 4
    Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4


## First approach (Using Hashing)

The very basic idea is to use an array to store the frequency of each element in the given array.
The number with a frequency of 0 is the missing number.

## Using Sum of N terms Formula – O(n) time and O(1) auxiliary space

### An efficient approach is to use summation formula. As we know that the sum of the first N natural numbers is given by the formula **N * (N + 1) / 2**. Compute this sum and subtract the sum of all elements in the array from it to get the missing number.


*   ### Compute the sum of the first N natural numbers as expected sum using the formula.
        array = {1, 2, 4, 6, 3, 7, 8} ; N = 8
        sum = sum(array) => 31
*   ### Calculate the sum of the given array elements.
        expected_sum = 8 * (8 + 1) / 2 => 36

*   ### Subtract the sum of the array elements from the expected sum to find the missing number.
        expected_sum - sum = 36 - 31 = 5 
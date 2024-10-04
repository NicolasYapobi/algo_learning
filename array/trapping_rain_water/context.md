# Trapping Rain Water

## Explanation

<img src="img/Trapping-Rain-Water-Problem.png"
    alt="maximum_1"
    style="float: left; margin-right: 10px;" 
/>

Trapping Rainwater Problem states that given an array of ***n non-negative integers arr[]*** representing an elevation map where the width of each bar is 1, compute how much water it can trap after rain.

## Examples ##

    Input: arr[] = {3, 0, 1, 0, 4, 0, 2}
    Output: 10
    Explanation: The expected rainwater to be trapped is shown in the above image.

    Input: arr[]   = {3, 0, 2, 0, 4}
    Output: 7
    Explanation: We trap 0 + 3 + 1 + 3 + 0 = 7 units.

    Input: arr[] = {1, 2, 3, 4}
    Output: 0
    Explanation : We cannot trap water as there is no height bound on both sides

    Input: arr[] = {10, 9, 0, 5}
    Output: 5
    Explanation : We trap 0 + 0 + 5 + 0 = 5

# First approach

* An element of the array can store water if there are higher bars on the left and the right. 
* The amount of water to be stored in every position can be found by finding the heights of the higher bars on the left and right sides. 
* The total amount of water stored is the summation of the water stored in each index.
* No water can be filled if there is no boundary on both sides.

Traverse every array element and find the highest bars on the left and right sides. Take the smaller of two heights. The difference between the smaller height and the height of the current element is the amount of water that can be stored in this array element.

# Using Two Pointers - O(n) Time and O(1) Space

The approach is mainly based on the following facts:

* If we consider a subarray arr[left…right], we can decide the amount of water either for arr[left] or arr[right] if we know the left max (max element in arr[0…left-1]) and right max (max element in arr[right+1…n-1].

* If left max is less than the right max, then we can decide for arr[left]. Else we can decide for arr[right]

* If we decide for arr[left], then the amount of water would be left max – arr[left]

### How does this work? # 
Let us consider the case when left max is less than the right max. For **arr[left]**, we know left max for it and we also know that the right max for it would not be less than left max because we already have a greater value in **arr[right..n-1]**. Any other value from left + 1 to right – 1 would anyways be more than left max.

## ExAMPLES

Consider:

    arr[] = {3, 0, 5, 0, 4}
Initial values:

    left = 1, right = 3, lMax = arr[0] = 3, rMax = arr[4] = 4
    res = 0 (stores total water trapped)
then:

    left = 1, right = 3::  Since lMax < rMax, we fill water in arr[left] as 3- 0 = 3, 
    left = 2, right = 3:   lMax < rMax, but arr[left] > lMax, we don't fill water, we update lMax  = 5
    left = 3, right = 3:   Since lMax >= rMax, we fill water in arr[right] as 4-0

Total water trapped = 3 + 0 + 4 = 7
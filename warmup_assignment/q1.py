"""
Q1. Given an array of N integers. Your task is to print the sum of all of the integers.

Example 1:
Input:
4
1 2 3 4
Output:
10

Example 2:
Input:
6
5 8 3 10 22 45
Output:
93
"""

class Solution:
    def sum_of_all_integers(self, arr, n):
        """
        method to return sum of all integers in given array
        TC: O(n)
        SC: O(1)
        """
        summation_of_integers = 0
        for i in range(n):
            summation_of_integers += arr[i]
        return summation_of_integers



solution = Solution()
length_of_array = int(input())
input_array = list(map(int, input().split()))
print(solution.sum_of_all_integers(input_array, length_of_array))
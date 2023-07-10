"""
Q2. Given an array A[] of N integers and an index Key. Your task is to print the element present at
index key in the array.

Example 1:
Input:
5 2
10 20 30 40 50
Output:
30

Example 2:
Input:
7 4
10 20 30 40 50 60 70
Output:
50
"""
class Solution:
    def fetch_element_using_index(self, arr, N, key):
        """
        method to return element at requested_index if present, otherwise return None
        TC: O(1)
        SC: O(1)
        """
        if N <= key:
            return None
        return arr[key]


solution = Solution()
length_of_array, index_of_element = map(int, input().split())
input_array = list(map(int, input().split()))
print(solution.fetch_element_using_index(input_array, length_of_array, index_of_element))
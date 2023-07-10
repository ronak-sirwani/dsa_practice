"""
Q3. Given an sorted array A of size N. Find number of elements which are less than or equal to given
element X.

Example 1:
Input:
N = 6
A[] = {1, 2, 4, 5, 8, 10}
X = 9
Output:
5

Example 2:
Input:
N = 7
A[] = {1, 2, 2, 2, 5, 7, 9}
X = 2
Output:
4
"""

class Solution:
    def fetch_elements_less_than_given_element(self, arr, N, X):
        """
        method to return no. of elements less than or equal to X if present, 
        otherwise return None
        TC: O(logn)
        SC: O(1)
        """
        left_limit, right_limit = 0, N-1

        while left_limit <= right_limit:
            middle = (left_limit+right_limit)//2

            if arr[middle] <= X:
                left_limit = middle + 1
            else:
                right_limit = middle - 1
        
        return left_limit


solution = Solution()
length_of_array = int(input())
input_array = list(map(int, input().split()))
upper_limit = int(input())
print(solution.fetch_elements_less_than_given_element(input_array, length_of_array, upper_limit))
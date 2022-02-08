"""
169. Majority Element

Given an array [nums] of size [n], return the majority element.
The majority element is the element that appears more than [n/2] times.
You may assume that the majority element always exists in the array.
"""

"""
E.g.
Input: nums = [3, 2, 3]
Output: 3

Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2

Constraints:
-  n == nums.length
-  1 <= n <= 5 * 10^4
-  -2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def get_majority(self, nums):
        """
        :param nums: list[int]
        :return: int
        """
        count = 0
        major = 0
        for num in nums:
            if count == 0:
                major = num
                count = 1
            else:
                if major == num:
                    count += 1
                else:
                    count -= 1
        return major


if __name__ == '__main__':
    test_solution = Solution()
    my_ans = test_solution.get_majority([1,2,2,2,5])
    print(my_ans)




'''
Given an integer array nums, move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
'''

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    len_array = len(nums)
    for item in range(len(nums) - 1, -1, -1):
        if (nums[item] == 0):
            nums.pop(item)
    
    while len(nums) < len_array:
        nums.append(0)
    
moveZeroes([0,1,0,3,12])
#moveZeroes([0])
#moveZeroes([0,0,1])
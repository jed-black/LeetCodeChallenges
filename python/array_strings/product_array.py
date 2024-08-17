'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

# TODO: REFACTOR TO BE O(N)
def productExceptSelf( nums):
    product_array = []
    for index, value in enumerate(nums):
        product_value = 1
        nums_list = nums[:index] + nums[index + 1:]

        for num in nums_list:
            product_value *= num
        product_array.append(product_value)
    return product_array
        

#productExceptSelf([1,2,3,4])
productExceptSelf([-1,1,0,-3,3])
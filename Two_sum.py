########## 1. Two sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def two_sum(nums,target):
    num_to_index = {}
    for i, num in enumerate(nums):
    # check if the complement of the current number is in the dictionary
        complement = target - num
        if complement in num_to_index:
            # if it is, return the indices of the current number and the complement
            return [num_to_index[complement], i]
        else:
            # if it's not, add the current number and its index to the dictionary
            num_to_index[num] = i
    return num_to_index

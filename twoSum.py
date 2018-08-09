# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


#high level idea:
#make a run through the array, store the compliment of the value at that index, with the index
#if we ever see the value of a current character in the dictionary, we know that it's compliment has
#already been saved. So this is our matching pair.

def twoSum(nums, sum):
    dict = {}
    #   where i is the index, and val is the value at that index
    for i, val in enumerate(nums):

        if val in dict:
            return (i, dict[val])
        else:
            compliment = sum - val
            dict.update({compliment: i})

#driver code
nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))

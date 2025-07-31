########################################################################
#https://leetcode.com/problems/two-sum/description/
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
############################################################################
from typing import List, Dict, Tuple

def twoSum(nums: List[int], target: int) -> List[int]:
    arr_dict = {}
    for i in range(len(nums)):
        other = target -nums[i]
        if other in arr_dict:
            return [arr_dict[other],i]
        arr_dict[nums[i]] = i  #this insert happens after the check to avoid using the same element twice
    return []

if __name__ == "__main__":
    arr = [1,2,4]
    target = 3
    print(twoSum(arr, target))
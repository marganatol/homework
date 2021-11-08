# -*- coding: utf-8 -*-
nums = list(map(int,input('Введите цифры через пробел :').split()))
 
def is_monotonic(nums):
    count = 1
    for i in range (0, len(nums) - 1):
        if (nums[i] <= nums[i + 1]):
            count += 1
    if (count == len(nums)):
        return True
    count = 1
    for i in range (0, len(nums) - 1):
        if (nums[i] >= nums[i + 1]):
            count += 1
    if (count == len(nums)):
        return True
    return False
    
if (is_monotonic(nums)):
    print("True")
else:
    print("False")

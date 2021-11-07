# -*- coding: utf-8 -*-

from random import randint

temp = int(input('Загаданное кол-во символов: '))
nums = []
for i in range(temp + 1): 
    nums.append(randint(1, temp))
def find_missing_nums(nums):
    normal_array = []
    for i in range(1, temp + 1):
        normal_array.append(i)
    array_with_absent_nums = []
    
    for i in range(len(normal_array)):
        if normal_array[i] not in nums:
            array_with_absent_nums.append(normal_array[i])
    return(array_with_absent_nums)

print(find_missing_nums(nums))
def two_sum(nums, target):
    nums_map = {}
    for i in range (0, len(nums)):
        nums_map[nums[i]] = i
    # print(nums_map)
    for i in range (0, len(nums)):
        match = target - nums[i]
        if(match in nums_map):
            if(i != nums_map[match]):
                return [i, nums_map[match]]
    return nums_map

nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))


nums = [3,2,4]
target = 6
print(two_sum(nums, target))

nums = [3,3]
target = 6
print(two_sum(nums, target))
                  

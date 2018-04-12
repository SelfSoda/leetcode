def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    for n in nums:
        if target - n in nums:
            j = 0
            for n2 in nums:
                if n2 == target - n and i != j:
                    return [i, j]
                j += 1
        i += 1

print(twoSum([2, 7, 11, 15], 26))
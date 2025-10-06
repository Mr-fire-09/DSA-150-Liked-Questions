# Day 3: Pair with Given Sum – Two Sum Problem
# Top 150 Notout DSA Series | Author: Neeraj Singh

def twoSum(nums,target):
    hashmap = {}
    for i , n in enumerate(nums):
        diff = target -n
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[n] = i
    return []


nums = list(map(int,input("Enter the elements of the array: ").split()))
target = int(input("Enter the target sum: "))
result = twoSum(nums,target)
print("Indices of the two numbers such that they add up to target are:", result)
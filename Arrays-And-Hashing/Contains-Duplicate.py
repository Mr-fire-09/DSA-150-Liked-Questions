# 🏏 Top 150 NotOut - Contains Duplicate
# Author: Neeraj Singh

def hasDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Taking user input
n = int(input("Enter the value : "))
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Displaying result
if hasDuplicate(nums):
    print("✅ Yes, the array contains duplicates.")
else:
    print("🎯 No, all elements are unique.")

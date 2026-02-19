from typing import List

def search(nums: List[int], target: int) -> int:
    # Your code here
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right)//2
        
        if nums[mid] == target:
            return nums.index(target)

        if nums[mid] < target:
            left = mid + 1

        if nums[mid] > target:
            right = mid - 1

        
    return -1
        

# Read input
nums = list(map(int, input().split()))
target = int(input())
print(search(nums, target))
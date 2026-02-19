from typing import List

def countInversions(arr: List[int]) -> int:
    # Your code here
    count = 0
    for ch1 in arr:
        for ch2 in arr:
            if ch1 < ch2 and arr.index(ch1) > arr.index(ch2):
                count = count + 1

    return count
    

# Read input
arr = list(map(int, input().split()))
print(countInversions(arr))
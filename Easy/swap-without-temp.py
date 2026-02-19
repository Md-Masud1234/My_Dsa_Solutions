def swap(a: int, b: int) -> str:
    # Your code here - don't use a temp variable
    a,b = b,a
    return f"{a} {b}"
# Read input
a, b = map(int, input().split())
print(swap(a, b))
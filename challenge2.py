def two_positive(a, b, c):
    # Counting the number of positive numbers
    positive_count = 0
    
    # Checking each number and updating the count
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    # Returning True if exactly two numbers are positive, otherwise returning False
    return positive_count == 2

# Examples
print(two_positive(2, 4, -3))   # Expected output: True
print(two_positive(-4, 6, 8))   # Expected output: True
print(two_positive(4, -6, 9))   # Expected output: True
print(two_positive(-4, 6, 0))   # Expected output: False
print(two_positive(4, 6, 10))   # Expected output: False
print(two_positive(-14, -3, -4)) # Expected output: False

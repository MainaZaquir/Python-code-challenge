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
print(two_positive(1, 4, -7))   # Expected output: True
print(two_positive(-9, 1, 9))   # Expected output: True
print(two_positive(2, -10, 9))   # Expected output: True
print(two_positive(-3, 5, 0))   # Expected output: False
print(two_positive(8, 21, 10))   # Expected output: False
print(two_positive(-21, -14, -7)) # Expected output: False

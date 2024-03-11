TOTAL_DIGITS = 100

non_bouncy = 0

count = [0] + [1]*9  # List to track how many numbers end with each digit
total_count = [0] + [1]*9

# Increasing
for num_digits in range(TOTAL_DIGITS-1):
    newcount = [0] * 10
    for digit in range(10):
        for i in range(digit, 10):
            newcount[i] += count[digit]
            total_count[i] += count[digit]
    count = [x for x in newcount]

print("\n#===================================================#\n")

non_bouncy += sum(total_count)

count = [0] + [1]*9  # List to track how many numbers end with each digit
total_count = [0] + [1]*9

# Decreasing
for num_digits in range(TOTAL_DIGITS-1):
    newcount = [0] * 10
    for digit in range(10):
        for i in range(digit+1):
            newcount[i] += count[digit]
            total_count[i] += count[digit]
    count = [x for x in newcount]
    
non_bouncy += sum(total_count)

print(non_bouncy - 9 * TOTAL_DIGITS)



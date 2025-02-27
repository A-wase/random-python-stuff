# Write a Python code to iterate the first 10 numbers, and in each iteration,
# print the sum of the current and previous number.
previous_num = -1

for num in range(10):
    sum = previous_num + num
    print(f"The current number is {num} and its sum with {previous_num} is: {sum}")
    previous_num += 1



nums = [3, 5, 7, 8]
target = 12

for i, num1 in enumerate(nums):
    for j, num2 in enumerate(nums):
        if i != j and num1 + num2 == target:
            print(num1, num2)

import random

list_input = input("Enter numbers separated by spaces: ")
list_input = list(map(float, list_input.split()))
target = int(input("Enter the target: "))

found_pair = False

while not found_pair:
    a = random.choice(list_input)
    b = random.choice(list_input)

    index_a = list_input.index(a)
    index_b = list_input.index(b)

    if a + b == target and index_a != index_b:
        print(index_a, index_b)
        found_pair = True

if not found_pair:
    print("No pair found that sums up to the target.")

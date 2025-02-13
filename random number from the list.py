import random
target = 3
list_input = input()

while True:
    a = int(random.choice(list_input))
    b = int(random.choice(list_input))

    index_a = list_input.index(a)
    index_b = list_input.index(b)

    if a + b == target:
        if index_a != index_b:
            print(index_a, index_b)
            break
    
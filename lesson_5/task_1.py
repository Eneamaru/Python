def nums_gen(n):
    for num in range(1, n + 1, 2):
        yield num


odd_to_11 = nums_gen(11)

print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))
print(next(odd_to_11))


def sum_all(*args):
    print(*args)
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,5,7,9))
print(sum_all(34,53,64))


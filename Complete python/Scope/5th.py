x = 34
def coder(num):
    def actual(x):
        return x ** num
    return actual
f = coder(2)
g = coder(3)

print(f(3))
print(g(5))
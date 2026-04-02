def solve(r, n):
    if n == 0:
        return r
    if n%2 == 1:
        return solve("1"+r, n//2)
    else:
        return solve("0"+r, n//2)
print(solve("", int(input())))

# n = int(input())
# k = bin(n)
# print(k.replace("0b",""))
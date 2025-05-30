def factorial(num):
    # Your code goes here.

    ans = 1
    while num:
        ans = ans * num
        num = num -1
    print(ans)
    return ans


factorial(5)
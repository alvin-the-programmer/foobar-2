def solution(n):
    n = int(n)
    num_steps = 0

    while n > 1:
        if n % 2 == 0:
            n = n >> 1 
        elif (n == 3) or (n % 4 == 1):
            n = n - 1
        else:
            n = n + 1
        num_steps += 1

    return num_steps

print(solution('15'))   # 5
print(solution('4'))    # 2
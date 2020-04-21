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


# def solution(n):
#     n = int(n)
#     steps = 0

#     while n > 1:
#         # if n is even, divide by 2 using bit manipulation
#         if n & 1 == 0:
#             n = n >> 1
#         else:
#         # Use bit manipulation to create as many 0 from LSB as possible
#             if (n == 3) or (n % 4 == 1):
#                 n = n - 1
#             else:
#                 n = n + 1
#             #   n = (n - 1) if (n == 3 or n % 4 == 1) else (n + 1)

#         steps += 1
#     return steps

print(solution('15'))   # 5
print(solution('4'))    # 2
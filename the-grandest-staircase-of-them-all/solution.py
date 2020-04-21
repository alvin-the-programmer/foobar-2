def solution(n):
    memo = {}

    def unique_staircases(num_bricks, stairs, previous_height = None):
        key = (num_bricks, previous_height)

        if key in memo:
            return memo[key]

        if num_bricks < 0:
            return 0

        if num_bricks == 0 and len(stairs) >= 2:
            return 1

        max_height = num_bricks + 1 if previous_height is None else previous_height

        total_staircases = 0
        for step_height in range(1, max_height):
            staircase = stairs + [ step_height ]
            total_staircases += unique_staircases(num_bricks - step_height, staircase, step_height)

        memo[key] = total_staircases
        return memo[key]

    return unique_staircases(num_bricks=n, stairs=[])


print(solution(0)) # 0
print(solution(1)) # 0
print(solution(3)) # 1
print(solution(4)) # 1
print(solution(5)) # 2
print(solution(200)) # 487067745
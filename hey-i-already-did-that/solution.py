def solution(n, base):
    visited = []

    def _solution(n, base):
        if n in visited:
            return len(visited) - visited.index(n)
        visited.append(n)
        k = len(n)
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))
        z_in_decimal = int(x, base) - int(y, base)
        z = number_to_base(z_in_decimal, base).rjust(k, '0')
        return _solution(z, base)
    return _solution(n, base)


def number_to_base(n, base):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return ''.join(str(digit) for digit in digits[::-1])

print(solution('1211', 10)) # 1
print(solution('210022', 3)) # 3
print(solution('0', 3)) # 1


# print(number_to_base(0, 3))

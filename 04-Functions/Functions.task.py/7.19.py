def f(number):
    s = str(number)
    total = 0
    for digit in s:
        if s.count(digit) > 1:
            total += int(digit)
    return total

if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))

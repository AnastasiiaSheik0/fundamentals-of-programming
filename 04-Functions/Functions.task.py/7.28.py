def f(dice):
    max_streak = 0
    current_streak = 1
    max_digit = dice[0]
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_streak += 1
        else:
            current_streak = 1
        if current_streak > max_streak:
            max_streak = current_streak
            max_digit = dice[i]
    return int(max_digit)

if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))

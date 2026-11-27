def f(detector):
    people = 0
    for sign in detector:
        if sign == "+":
            people += 1
        elif sign == "-":
            people -= 1
        if people >= 3:
            return True
    return False

if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))

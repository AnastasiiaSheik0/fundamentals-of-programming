def f(binary_number):
    for char in binary_number:
        if char != '0' and char != '1':
            return False
    return len(binary_number) > 0

if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))

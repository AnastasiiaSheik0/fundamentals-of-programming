num = int(input("Enter decimal number: "))
og_num = num
binary = ''

while not num == 0:
    binary += str(num % 2)
    num = num // 2

binary = binary[::-1]
print(f"{og_num}(10) = {binary}(2)")

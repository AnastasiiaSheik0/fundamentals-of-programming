import time

countdown = int(input("enter the nmber of seconds to count down : "))

while countdown > 0:
    if countdown == 5:
        print("five")
    elif countdown == 4:
        print("four")
    elif countdown == 3:
        print("three")
    elif countdown == 2:
        print("two")
    elif countdown == 1:
        print("one")
    else:
        print(countdown)
    countdown -= 1

    time.sleep(1) #wait or 1 sec 

print("Time's up!")
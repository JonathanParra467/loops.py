count = 100
while count >= 1:
    print(count, "bottles of beer on the wall")
    print(count, "bottles of beer")
    print("take one down, pass it around")
    count -= 1
    if count >= 2:
        print(count, "bottles of beer in the walls!")
        print("")
    elif count == 1:
        print(count, "bottle of beer in the wall!")
        print("")
    else:
        print("no bottles of beer on the wall!")
        print("")

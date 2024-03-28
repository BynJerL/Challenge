zPoint = 20

while True:
    print("Shop Item List:")
    # print("1\tComic Fantasy Book | 15z")
    # print("2\tPhilosophy Book | 45z")
    print("1\tYun's Special Noodle | 15z")
    print("2\tYummy Vegetable Soup | 5z")
    print("3\tCheeseburger | 7z")
    print("4\tFried Chicken with Tomayo Sauce | 5z")
    print("e\tExit\n")
    print(f"Your current z: {zPoint}z")
    code = str(input("Your Choice: "))

    if code == '1':
        if zPoint >= 15:
            zPoint -= 15
            print("You've bought a Yun's Special Noodle for 15z.")
        else:
            print("Not enough money.")
    elif code == '2':
        if zPoint >= 5:
            zPoint -= 5
            print("You've bought a Yummy Vegetable Soup for 5z.")
        else:
            print("Not enough money.")
    elif code == '3':
        if zPoint >= 7:
            zPoint -= 7
            print("You've bought a Chessburger for 7z.")
        else:
            print("Not enough money.")
    elif code == '4':
        if zPoint >= 5:
            zPoint -= 5
            print("You've bought a Fried Chicken with Tomayo Sauce for 5z.")
        else:
            print("Not enough money.")
    elif code == 'e':
        break
    else:
        print("Oops... wrong code")

    print()
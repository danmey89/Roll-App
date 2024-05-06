from functions import roll, get_data

data = get_data()

while True:
    uval = input("Please enter modifier: ")
    if uval in data[0].keys():
        for player in data:
            print(roll(uval, player))
    elif uval == "end":
        break
    else:
        print("Unknown input , please try again!")

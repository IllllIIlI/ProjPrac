import returnAddress


def Find():
    print("Please enter your current location.")
    cur_loc = input()
    return returnAddress.GetLoc(cur_loc)

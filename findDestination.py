import returnAddress


def Find():
    print("Please enter your destination.")
    dst_loc = input()
    return returnAddress.GetLoc(dst_loc)

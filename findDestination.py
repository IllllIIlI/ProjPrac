import returnAddress

def find():
    print("목적지를 입력하세요")
    dstloc = input()
    return returnAddress.getloc(dstloc)

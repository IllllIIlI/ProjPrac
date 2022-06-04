def guide():
    print("Before selecting the desired charger, press Y to learn the difference between a fast charger and a slow charger")
    answer = input()
    if answer == "Y":
        print("The charge cost of a slow charger is lower than that of a fast charger\n"
              "In the case of slow - about six hours until the full discharge in full charge\n"
              "fast charging by filling 80 percent of total discharge takes 15 to 30 minutes\n")

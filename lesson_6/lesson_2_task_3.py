month_nomber = int(input("Write the month number from 1 to 12: "))

dict_seasons = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer", 9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}


for key, value in dict_seasons:
    if month_nomber in dict_seasons.keys():
        print(value)

    else:
        print("The month number is wrong")




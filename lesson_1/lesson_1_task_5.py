earnings = float(input("Enter your annual earnings in euro ")) #NB!!! float()
spendings = float(input("Enter your annual spendings in euro ")) #float
personal = int(input("How many employees work in the company? "))
profit_comp = earnings - spendings
#print(profit)

if profit_comp > 0:
    print("Your venture is profitable! The profit is " + str(profit_comp))
    comp_profitableness = profit_comp / earnings  # print(f"The Profitableness of the venture is [profit / personal:.3f]")
    print("The profitableness of the venture is " + str(comp_profitableness)
    #personal_related_profit = profit / personal
    #print("The profit in relation to number of employees is " + str(personal_related_profit) #print(f"Personal related profit is [profit / personal:.3f]")

elif profit_comp < 0:
    print("Your company works with lost")

else :
    print("Your company works with nor profit not lost") #print(f"YOur company works with a lost [lost]")

days = 1
first_result = float(input("The distance on the first day - "))
goal_distance = float(input("The distance on the last day - "))

if first_result <= 0 or goal_distance <= 0:
    print("Please, enter positive numbers!")
else:
    while first_result < goal_distance:
        first_result = 1.1 * first_result
        days += 1
    print(f"The jogger will achieve the end result on {days} days") #Непонятно, где задается last_result как цель дстичжения. Предполагаю, строка 10... Решение через рекурсию оставила "на потом", но предполагаю, о чем речь


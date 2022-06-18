my_number = int(input("Enter a positive integer "))
#my_string = str(my_number)
maximum = my_number % 10
number = my_number

while number > 0:
    number_tail = number % 10
    if number_tail > maximum:
        maximum = number_tail

    if number_tail == 9:
        break
        maximum == 9

    number = number // 10
    print(number)

print(f"The greatest number in your integer {my_number} is {maximum}")



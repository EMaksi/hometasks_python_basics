string_sen = input("Enter any sentence of a few words ")
new_string = string_sen.split()
print(new_string)

       #"el" = [:10]
for i, el in enumerate(new_string):
    print(f"{i+1, el[:10]}\n")



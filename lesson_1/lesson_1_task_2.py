time_in_seconds = int(input("Enter time in seconds "))
hours = time_in_seconds // 3600
# my solution minutes = (time_in_seconds % 3600) // 60
minutes = (time_in_seconds// 60)-(hours * 60) #the tutors solution
#seconds = time_in_seconds - hours * 3600 - minutes * 60
seconds = time_in_seconds % 60

print(hours)
print(minutes)
print(seconds)

# how to format

print(f"{hours:04}:{minutes:04}:{seconds:04}")
#что, если часов получается больше 99?


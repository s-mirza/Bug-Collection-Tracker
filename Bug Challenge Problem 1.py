num_days = int(input("Enter the number of days you want to enter date for:"))

total_bugs = 0

for day in range(1, num_days + 1):
    bugs_collected = int(input(f"How many bugs did you observe on day {day}: "))
    total_bugs += bugs_collected

if num_days > 0:
    average_bugs = total_bugs / num_days
else:
    average_bugs = 0

print(f"The total bugs you studied is {total_bugs}")
print(f"The average number of bugs you studied on a daily basis is {average_bugs}")




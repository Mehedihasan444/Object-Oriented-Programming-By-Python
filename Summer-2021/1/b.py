
def add_missing_days(week_list):
    week_list.insert(2,"Monday")
    week_list.insert(4,"Wednesday")
def check_day(day):
    if day=="Friday":
        print("Today is holiday")
    else:
        print("working day")

week_list=["Saturday", "Sunday", "Tuesday", "Thursday", "Friday"]
add_missing_days(week_list)

for day in week_list:
    print(f"on {day}: ",end=" ")
    check_day(day)

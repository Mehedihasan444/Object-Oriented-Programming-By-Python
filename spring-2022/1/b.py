semester_fee=int(input("Enter Your Semester Fee: "))
result=float(input("Enter Your Result: "))
waiver=0
if result>3.5:
    waiver=semester_fee-(semester_fee*.2)
elif result>=3.00 and result<=3.5:
    waiver=semester_fee-(semester_fee*.1)
elif result<3.00:
    waiver=semester_fee-(semester_fee*.05)
print(waiver)

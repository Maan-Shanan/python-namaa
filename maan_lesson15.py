
stu = {"ismail":21,"sedra":13,"maan":25,"jaber":12,"manaf":17,"abd alfattah":21
       ,"hussam":2,"obai":13,"hith":11,"bhaa":9,"lama":1,"ahmad": 1}
while True:
    stu_name = input("Enter student name (or 'exit'):")
    if stu_name.lower() == 'exit':
        break
    stu_mark = int(input("Enter student mark:"))

    if stu_name in stu:
        stu[stu_name] += stu_mark
        print(stu)
    else:
        print("Error in name")


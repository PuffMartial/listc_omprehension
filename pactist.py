students = [100,90,80,70,60,50,40,30,20,10,0]

passed_student = [i if i >= 50 else "FAILED" for i in students]

print(passed_student)
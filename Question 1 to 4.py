

#Question Number 1
students = []
for i in range(5):
  students.append(input("Enter Student Name: "))
print("Student Names Are : ")
set_students = set(students)
print(set_students)




#Question Number 2
student_records = []
for i in range(3):
  std = []
  std.append(input("Enter Name: "))
  std.append(int(input("Enter Age: ")))
  std.append(int(input("Enter Marks: ")))
  student_records.append(std)

print("Before Updating")
print(student_records)

student_records[2][1] = 29
student_records[2][2] = 25
student_records[1][0] = "Akansha_DBDA"
student_records[1][2] = 87

print("After Updating")
print(student_records)




#Question Number 3
latest_tech=[]
for i in range(5):
  latest_tech.append(input("Enter Technology : "))
latest_tech_updated = latest_tech.copy()
print("Before Updating")
print("latest tech = ",end="")
print(latest_tech)
print("latest tech updated= ",end="")
print(latest_tech_updated)
latest_tech_updated[2] = "ESD"
print("After Updating")
print("latest tech = ",end="")
print(latest_tech)
print("latest tech updated= ",end="")
print(latest_tech_updated)





#Question Number 4
class Logical_coding:
  def __init__(self):
    pass
  
  def division(self):
    try:
      num1 = int(input("Enter Number 1 "))
      num2 = int(input("Enter Number 2 "))
      if num2 == 0:
        raise Exception("Division By Zero Exception Enter Non Zero Divisor")
      else:
        res = num1/num2
        print(f"{num1} / {num2} = {res}")
    except Exception as e:
      print(e)

obj = Logical_coding()
obj.division()
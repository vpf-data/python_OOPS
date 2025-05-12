
class Student:
    ...

def main():

    wizard=get_student()
    print(f"{wizard.name} is in {wizard.house}")

def get_student():
    student=Student()

    student.name = input("Enter name: ").lower()
    student.house= input("Enter house: ").lower()
    return student
if __name__ =="__main__":
    main()


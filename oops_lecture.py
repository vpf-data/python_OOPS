
class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house

def main():

    wizard=get_student()
    print(f"{wizard.name} is in {wizard.house}")

def get_student():
    name = input("Enter name: ").lower()
    house= input("Enter house: ").lower()
    student=Student(name,house)
    return student
if __name__ =="__main__":
    main()



class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in["gryffindor","hufflepuff","ravenclaw","slytherin"]:
            raise ValueError("Invalid House")
        self.name=name
        self.house=house

def main():

    wizard=get_student()
    print(f"{wizard.name} is in {wizard.house}")

def get_student():
    name = input("Enter name: ").lower()
    house= input("Enter house: ").lower()
    return Student(name,house)

if __name__ =="__main__":
    main()


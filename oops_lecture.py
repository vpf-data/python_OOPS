
class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in["gryffindor","hufflepuff","ravenclaw","slytherin"]:
            raise ValueError("Invalid House")
        self.name=name
        self.house=house

    def __str__(self):
        return f"{self.name} is from {self.house}"

def main():

    wizard=get_student()
    print(wizard)

def get_student():
    name = input("Enter name: ").lower()
    house= input("Enter house: ").lower()
    return Student(name,house)

if __name__ =="__main__":
    main()


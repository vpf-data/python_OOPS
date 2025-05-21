
class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house

    def __str__(self):
        return f"{self.name} is from {self.house}"

    #getter
    @property
    def house(self):
        return self._house
    #setter
    @house.setter
    def house(self,house):
        if house not in ["gryffindor","hufflepuff","ravenClaw","slytherin"]:
            raise ValueError("Invalid House")
        self._house =house

def main():
    wizard=get_student()
    print(wizard)

def get_student():
    name = input("Enter name: ").lower()
    house= input("Enter house: ").lower()
    return Student(name,house)

if __name__ =="__main__":
    main()


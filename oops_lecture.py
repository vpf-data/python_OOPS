def main():

    student=get_student()
    print(f"{student['name']} is in {student['house']}")

def get_student():
    student={}
    student["name"] = input("Enter name: ").lower()
    student["house"] = input("Enter house: ").lower()
    return student
if __name__ =="__main__":
    main()


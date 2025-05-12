def main():

    student=get_student()
    if student[0]=="padma":
        student[1]="ravenclaw"
    print(f"{student[0]} is in {student[1]}")

def get_student():
    name = input("Enter name: ").lower()
    house = input("Enter house: ").lower()
    return [name,house]
if __name__ =="__main__":
    main()


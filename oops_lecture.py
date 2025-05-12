def main():

    student=get_student()
    if student["name"]=="padma":
        student["house"]="ravenclaw"
    print(f"{student['name']} is in {student['house']}")

def get_student():
    name = input("Enter name: ").lower()
    house= input("Enter house: ").lower()
    return {"name":name,"house":house}
if __name__ =="__main__":
    main()


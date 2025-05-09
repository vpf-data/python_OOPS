def main():

    name = get_name()
    house = get_house()
    print(f"{name} is in {house}")

def get_name():
    return input("Enter name :")

def get_house():
    return input("Enter house :")

if __name__ =="__main__":
    main()


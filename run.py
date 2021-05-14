from cowin.co_win import main
def run():
    pincode = input("Enter pincode : ")
    age = input("Enter age : ")

    if pincode.isnumeric():
        if age is None:
            main(int(pincode))
        else:
            main(int(pincode), age)
    else:
        print("invalid pincode")

if __name__ == '__main__':
    run()
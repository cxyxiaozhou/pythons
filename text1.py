while True:

    try:
        firstname=input("pelase input firstname:")
        print(int(firstname))   
    except ValueError:
        print("you's value in error not str")
    else:
        print(firstname)
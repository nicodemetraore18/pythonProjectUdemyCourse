login={"Neamat":1234, "nico":0000, "Abel":111}
Username=input("Enter your name:")
password=int(input("Enter your password:"))
attempt=0
max_attempts=5
while attempt<max_attempts:
    if Username in login:
        if password==login[Username]:
            print("login Succesfull")
            break
        else:
            print("password is incorrect.Please try again.")
    else:
        print("Username is incorrect.Please try again.")
    attempt+=1
    if attempt<max_attempts:
        Username = input("Enter your name:")
        password = int(input("Enter your password:"))
    else:
        print("failed  ! Too many attempts")

    

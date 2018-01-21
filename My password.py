#creating a program where the user creates a user names and password
#the program lets the user his/her username then password
#it then prompts the user to verify what the chose, giving the user 3 chances to retype their correct username/password

print('Create a user name')
user_name = input()
print()
print('Create a password')
password = input()

print()
#verify your user/password
x = 0
y = 0
print('Verify your user name')
answer = input()
while x < 3:
    if answer == user_name:
        print('Correct!')
        print ('Verify your password')
        password_answer = input()
        while y < 3:
            if password_answer == password:
                print('You are in, baby!')
                y = 3
                x = 3
            elif password_answer != password:
                y = y + 1
                print('WRONG, you have ' + str(4 - y) + ' attempts left')
                password_answer = input()
                if y == 3:
                    print("I'm sorry, you are out of tries")
                    x =3
    elif answer != user_name:
        x = x + 1 
        print("try again! You have " + str(4 - x) + " attempts left")
        answer = input()
        if x == 3:
            print("I'm sorry, you are out of tries")
        
        
    

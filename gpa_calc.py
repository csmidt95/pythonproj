##This will calculate your GPA!
def grades_list_and_credit_hours_list():
    classes = int(input("How many classes are you enrolled in? "))
    grades_with_hours = []
    letter_grades_list = []
    credit_hours_list = []
    while classes > 0:
        grades_and_hours = input("Input your letter grade followed by class hour ")
        grades_and_hours = grades_and_hours.split(',')
        grades_with_hours.append(grades_and_hours)
        classes = classes - 1
    for i in range(0, len(grades_with_hours)):
        letter_grades = (grades_with_hours[i][0])
        letter_grades_list.append(letter_grades)
    for i in range(0, len(grades_with_hours)):
        credit_hours = (grades_with_hours[i][1])
        credit_hours_list.append(int(credit_hours))
    letter_grades_list_converter(letter_grades_list) 
    combined = list(zip(letter_grades_list, credit_hours_list))
    x = [a*b for a, b in combined]
    y = (sum(x)/sum(credit_hours_list))
    print()
    print (f"Your GPA is {y:.3f}")
           
def letter_grades_list_converter(letter_grades_list):
    for i in range(len(letter_grades_list)):
        if letter_grades_list[i] == "A+":
            letter_grades_list[i] = 4.3
        elif letter_grades_list[i] == "A":
            letter_grades_list[i] = 4.0
        elif letter_grades_list[i] == "A-":
            letter_grades_list[i] = 3.7
        elif letter_grades_list[i] == "B+":
            letter_grades_list[i] = 3.3
        elif letter_grades_list[i] == "B":
            letter_grades_list[i] = 3.0
        elif letter_grades_list[i] == "B-":
            letter_grades_list[i] = 2.7
        elif letter_grades_list[i] == "C+":
            letter_grades_list[i] = 2.3
        elif letter_grades_list[i] == "C":
            letter_grades_list[i] = 2.0
        elif letter_grades_list[i] == "C-":
            letter_grades_list[i] = 1.7
        elif letter_grades_list[i] == "D+":
            letter_grades_list[i] = 1.3
        elif letter_grades_list[i] == "D":
            letter_grades_list[i] = 1.0
    return (letter_grades_list)
        
grades_list_and_credit_hours_list()





    

    

    

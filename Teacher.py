#Functions a teacher would use
#Function to calculate average
#function to calculate weighted average
#function that reads a letter grade 
#function that gives a class average 

#gradebook for students
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
  }


def average(numbers): #average function 
    total = sum(numbers)
    return total / len(numbers)

#categorical weights
homework = .1
quizzes = .3
tests = .6

def weighted_average(student): #weighted average function 
    w_average = homework * average(student["homework"]) + quizzes * \
    average(student["quizzes"]) + tests * average(student["tests"])
    print(w_average)
    return w_average

def letter_grade(student): #function reporting grade lettter
    average = weighted_average(student)
    if average >= 90:
        print("A")
    elif average >= 80:
        print("B")
    elif average >= 70:
        print("C")
    elif average >= 60:
        print("D")
    else:
        print("Failure")
        
        
student_list = [tyler, alice, lloyd]
def class_average(list_of_students): #calculates class average 
    row = []
    for student in list_of_students:
        x = weighted_average(student)
        row.append(x)
    return average(row)
    
        
print(class_average(student_list))
        
        
     

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''HIGH SCHOOL UNWEIGHTED GPA CALCULATOR'''

from __future__ import print_function

'''Calculating the letter grade.'''
def convert(grade):
    grade = grade.upper()    # converts all of the characters to uppercase
    points = 0.0
    if grade[0] == 'A':
        points = 4.0  
    elif grade[0] == 'B':
        points = 3.0
    elif grade[0] == 'C':
        points = 2.0
    elif grade[0] == 'D':
        points = 1.0
    if len(grade) > 1:       # to get the length of the list and +/- .3
        if grade[1] == '+' and points > 0 and points != 4:
            points = points + 0.3
        elif grade[1] == '-' and points > 1:
            points = points - 0.3         
    return points

'''Calculating the GPA.'''
def calculateGPA(numCourses):
    totalCredits = 0.0
    totalPoints = 0.0
    for count in range(numCourses):
        course = raw_input(str(count+1)+') ').split() # to print(str(count+1)+')',end=' ') and split into courses
        grade = course[0]
        creds = 5.0
        totalCredits = totalCredits + creds
        totalPoints = totalPoints + creds * convert(grade)
    gpa = totalPoints / totalCredits
    return gpa

def main():
    print('Welcome to the High School unweighted GPA Calculator!')
    print('Enter your letter grades for each of your 5 courses:')
    courses = 5; gpa = calculateGPA(courses)
    print ('\r')
    print('Your unweighted GPA is', gpa);
    if gpa >= 3.5:
        print("Congratulations! Well Done!");
    if gpa < 2.0:
        print("Needs some work!")
        
main()

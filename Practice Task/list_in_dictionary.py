dept_courses ={
    'CSE' : ['PL','DS','OS'],
    'EEE' : ['CIRCUIT','DEVICE','DLC'],
    'ENGLISH' : ['E1','E2','E3']
}

for course, dept in dept_courses.items():
    print(f"\n{course.title()}'s courses are : ")
    for i in dept :
        print(f"\t{i.title()}")
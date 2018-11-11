score = eval(input('please enter the score:'))
if 0<=score<=100:
    if 90<=score<=100:
        grade='A'
    elif 70<=score<90:
        grade = 'B'
    elif 60<=score<70:
        grade = 'C'
    elif score<60:
        grade = 'D'
    print("分数",score,"对应等级为：",grade)
else:
    print("Error input")


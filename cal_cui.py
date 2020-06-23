import math
import sys

def check_exit(charset) :
    if (charset == 'exit') | (charset == 'EXIT') :
        sys.exit("종료코드 입력")

def input_num() :
    temp = input("계산할 수 입력 : ")

    check_exit(str(temp))

    if  temp.isdecimal() :
        return float(temp)
    else :
        return None

def input_opt() :
    print("지원 연산 - 사칙연산, sqre : 제곱연산, numer : 입력값을 분수의 분자로, root : 루트연산")
    temp = input("연산 선택 : ")
    
    check_exit(temp)

    if  (temp == '+') | (temp == '-') | (temp == '*') | (temp == '/') | (temp == 'sqre') | (temp == 'numer') | (temp == 'root'):
        return temp
    else :
        return None

control, res, num1, num2 = 0, 0, 0, 0
form = ''

while True :

    if control == 0 :
        num1 = input_num()
        if  num1 == None :
            print("숫자만 입력할 것\n")
            continue
    
        control = 1

    elif control == 1 :
        opt = input_opt()
        if  opt == None :
            print("약정된 기호만 입력할 것\n")
            continue
    
        form = form + opt
        if (opt == '+') | (opt == '-') | (opt == '*') | (opt == '/') :
            control = 2
        elif (opt == 'sqre') | (opt == 'numer') | (opt == 'root') :
            control = 3

    elif control == 2 :
        num2 = input_num()
        if  num2 == None :
            print("숫자만 입력할 것\n")
            continue   
    
        control = 3

    elif control == 3 :
        control = 4
        if opt == '+' :
            res = num1 + num2
            form = "{} + {}".format(num1, num2)
        elif opt == '-' :
            res = num1 - num2
            form = "{} - {}".format(num1, num2)
        elif opt == '*' :
            res = num1 * num2
            form = "{} * {}".format(num1, num2)
        elif opt == '/' :
            res = num1 / num2
            form = "{} / {}".format(num1, num2)
        elif opt == 'sqre':
            res = num1 * num1
            form = "sqre({})".format(num1)
        elif opt == 'numer' :
            res = 1 / num1
            form = "1/({})".format(num1)
        elif opt == 'root' :
            res = math.sqrt(num1)
            form = "root({})".format(num1)

    elif control == 4:
        print("입력된 수식은 " + form + " 입니다.\n")
        print("계산 결과는 {}입니다.".format(res))
        control, res, num1, num2 = 0, 0, 0, 0
        form = ''
    

    

    

    

    


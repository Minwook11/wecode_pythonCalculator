
def input_num():
    temp = input("계산할 정수 입력 : ")

    if  temp.isdecimal() :
        return int(temp)
    else :
        return None

def input_opt():
    temp = input("기호입력 : ")

    if  (temp == '+') | (temp == '-') | (temp == '*') | (temp == '/'):
        return temp
    else :
        return None

while True:
    res, temp, num1, num2 = 0, 0, 0, 0
    form = ''

    num1 = input_num()
    if  num1 == None :
        print("정수만 입력할 것\n")
        continue
    
    form = str(num1)

    opt = input_opt()
    if  opt == None :
        print("기호만 입력할 것\n")
        continue
    
    form = form + opt

    num2 = input_num()
    if  num2 == None :
        print("정수만 입력할 것\n")
        continue   
    
    form = form + str(num2)

    if opt == '+':
        res = num1 + num2
    elif opt == '-':
        res = num1 - num2
    elif opt == '*':
        res = num1 * num2
    elif opt == '/':
        res = num1 / num2
    else :
        print("사칙연산만 지원합니다.")

    print("입력된 수식은 " + form + " 입니다.\n")
    print("계산 결과는 {}입니다.".format(res))

    


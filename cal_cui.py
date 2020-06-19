while True:
    num = int(input("계산할 정수 입력 : "))
    opt = input("기호입력 : ")
    
    if opt == '+':
        num = num + int(input("계산할 정수 입력 : "))
    elif opt == '-':
        num = num - int(input("계산할 정수 입력 : "))
    elif opt == '*':
        num = num * int(input("계산할 정수 입력 : "))
    elif opt == '/':
        num = num / int(input("계산할 정수 입력 : "))
    else :
        print("사칙연산만 지원합니다.")

    print("계산 결과는 {}입니다.".format(num))

    


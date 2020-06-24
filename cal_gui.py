import sys
import math
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("cal_gui.ui")[0]


class WindowClass(QMainWindow, form_class) :
    num1, num2, opt = '0', '0', ''
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.numButton_0.clicked.connect(self.numButton0Function)
        self.numButton_1.clicked.connect(self.numButton1Function)
        self.numButton_2.clicked.connect(self.numButton2Function)
        self.numButton_3.clicked.connect(self.numButton3Function)
        self.numButton_4.clicked.connect(self.numButton4Function)
        self.numButton_5.clicked.connect(self.numButton5Function)
        self.numButton_6.clicked.connect(self.numButton6Function)
        self.numButton_7.clicked.connect(self.numButton7Function)
        self.numButton_8.clicked.connect(self.numButton8Function)
        self.numButton_9.clicked.connect(self.numButton9Function)
        self.backspaceButton.clicked.connect(self.backspaceFucntion)
        self.plusButton.clicked.connect(self.plusButtonFunction)
        self.minusButton.clicked.connect(self.minusButtonFunction)
        self.multiButton.clicked.connect(self.multiButtonFunction)
        self.divButton.clicked.connect(self.divButtonFunction)
        self.resultButton.clicked.connect(self.resultButtonFunction)
        self.clearButton.clicked.connect(self.clearButtonFunction)
        self.numeratorButton.clicked.connect(self.numeratorButtonFunction)
        self.squareButton.clicked.connect(self.squareButtonFunction)
        self.rootButton.clicked.connect(self.rootButtonFunction)

    def disp_num(self, text) :
        self.label.setText(str(text))

    def input_num(self, num) :
        if self.opt == '' :
            if num == 0 :
                if self.num1 == '0' :
                    self.num1 == '0'
                    self.disp_num(self.num1)
                else :
                    self.num1 += str(num)
                    self.disp_num(self.num1)
            if num != 0 :
                if self.num1 == '0' :
                    self.num1 = str(num)
                else :
                    self.num1 += str(num)
                self.disp_num(self.num1)

        else :
            if num == 0 :
                if self.num2 == '0' :
                    self.num2 == '0'
                    self.disp_num(self.num2)
                else :
                    self.num2 += str(num)
                    self.disp_num(self.num2)
            if num != 0 :
                if self.num2 == '0' :
                    self.num2 = str(num)
                else :
                    self.num2 += str(num)
                self.disp_num(self.num2)

    def input_backs(self) :
        if self.opt == '' :
            if len(self.num1) > 1 :
                self.num1 = self.num1[0:(len(self.num1) - 1)]
                self.disp_num(self.num1)
            elif len(self.num1) == 1 :
                self.num1 = '0'
                self.disp_num(self.num1)

        elif self.opt != '' :
            if len(self.num2) > 1 :
                self.num2 = self.num1[0:(len(self.num2) - 1)]
                self.disp_num(self.num2)
            elif len(self.num2) == 1 :
                self.num2 = '0'
                self.disp_num(self.num2)

    def input_result(self) :
        if self.opt == '+' :
            self.num1 = int(self.num1) + int(self.num2)
        elif self.opt == '-' :
            self.num1 = int(self.num1) - int(self.num2)
        elif self.opt == '*' :
            self.num1 = int(self.num1) * int(self.num2)
        elif self.opt == '/' :
            self.num1 = int(self.num1) / int(self.num2)
        
        self.disp_num(self.num1)
        self.opt, self.num1, self.num2 = '', '0', '0'

    def input_specopt(self, opt) :
        if opt == 'sqre' :
            self.num1 = int(self.num1) * int(self.num1)
        elif opt == 'numer' :
            temp = '{0:5f}'.format(1 / int(self.num1))
            self.num1 = temp
        elif opt == 'root' :
            temp = '{0:5f}'.format(math.sqrt(int(self.num1)))
            self.num1 = temp

        self.disp_num(self.num1)

    def numeratorButtonFunction(self) :
        self.input_specopt('numer')

    def squareButtonFunction(self) :
        self.input_specopt('sqre')

    def rootButtonFunction(self) :
        self.input_specopt('root')

    def clearButtonFunction(self) :
        self.num1, self.num2, self.opt = '0', '0', ''
        self.disp_num('0')

    def resultButtonFunction(self) :
        self.input_result()

    def plusButtonFunction(self) :
        self.opt = '+'

    def minusButtonFunction(self) :
        self.opt = '-'

    def divButtonFunction(self) :
        self.opt = '/'

    def multiButtonFunction(self) :
        self.opt = '*'

    def backspaceFucntion(self) :
        self.input_backs()

    def numButton0Function(self) :
        self.input_num(0)

    def numButton1Function(self) :
        self.input_num(1)

    def numButton2Function(self) :
        self.input_num(2)

    def numButton3Function(self) :
        self.input_num(3)

    def numButton4Function(self) :
        self.input_num(4)

    def numButton5Function(self) :
        self.input_num(5)

    def numButton6Function(self) :
        self.input_num(6)

    def numButton7Function(self) :
        self.input_num(7)

    def numButton8Function(self) :
        self.input_num(8)

    def numButton9Function(self) :
        self.input_num(9)

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
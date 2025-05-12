import sys,os
from calculator import calculate
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QGridLayout,QPushButton,QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QFontDatabase,QIcon

class MainWindow(QWidget):
    data=""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "calculator-icon.png")))

        self.display=QLabel("",self)
        self.num1=QPushButton("1",self)
        self.num2=QPushButton("2",self)
        self.num3=QPushButton("3",self)
        self.num4=QPushButton("4",self)
        self.num5=QPushButton("5",self)
        self.num6=QPushButton("6",self)
        self.num7=QPushButton("7",self)
        self.num8=QPushButton("8",self)
        self.num9=QPushButton("9",self)
        self.num0=QPushButton("0",self)
        self.clear=QPushButton("C",self)
        self.delete=QPushButton("D",self)
        self.plus=QPushButton("+",self)
        self.minus=QPushButton("-",self)
        self.multiply=QPushButton("*",self)
        self.power=QPushButton("^",self)
        self.divide=QPushButton("/",self)
        self.open=QPushButton("(",self)
        self.closed=QPushButton(")",self)
        self.equal=QPushButton("=",self)

        self.myfont=QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), "Lato-black.ttf"))
        self.fontfamily=QFontDatabase.applicationFontFamilies(self.myfont)[0]
        self.fontstyle=QFont(self.fontfamily)

        self.initgui()

    def initgui(self):
        layout=QGridLayout()
        layout.addWidget(self.display,0,0,2,4)
        layout.addWidget(self.clear,2,0,1,1)
        layout.addWidget(self.delete,2,1,1,1)
        layout.addWidget(self.power,2,2,1,1)
        layout.addWidget(self.num1,3,0,1,1)
        layout.addWidget(self.num2,3,1,1,1)
        layout.addWidget(self.num3,3,2,1,1)
        layout.addWidget(self.num4,4,0,1,1)
        layout.addWidget(self.num5,4,1,1,1)
        layout.addWidget(self.num6,4,2,1,1)
        layout.addWidget(self.num7,5,0,1,1)
        layout.addWidget(self.num8,5,1,1,1)
        layout.addWidget(self.num9,5,2,1,1)
        layout.addWidget(self.open,6,0,1,1)
        layout.addWidget(self.num0,6,1,1,1)
        layout.addWidget(self.closed,6,2,1,1)
        layout.addWidget(self.equal,6,3,1,1)
        layout.addWidget(self.divide,2,3,1,1)
        layout.addWidget(self.multiply,3,3,1,1)
        layout.addWidget(self.minus,4,3,1,1)
        layout.addWidget(self.plus,5,3,1,1)
        self.setLayout(layout)

        self.plus.setFont(self.fontstyle)
        self.minus.setFont(self.fontstyle)
        self.multiply.setFont(self.fontstyle)
        self.divide.setFont(self.fontstyle)
        self.power.setFont(self.fontstyle)
        self.equal.setFont(self.fontstyle)
        self.closed.setFont(self.fontstyle)
        self.open.setFont(self.fontstyle)
        self.clear.setFont(self.fontstyle)
        self.delete.setFont(self.fontstyle)
        self.display.setFont(self.fontstyle)
        self.num1.setFont(self.fontstyle)
        self.num2.setFont(self.fontstyle)
        self.num3.setFont(self.fontstyle)
        self.num4.setFont(self.fontstyle)
        self.num5.setFont(self.fontstyle)
        self.num6.setFont(self.fontstyle)
        self.num7.setFont(self.fontstyle)
        self.num8.setFont(self.fontstyle)
        self.num9.setFont(self.fontstyle)
        self.num0.setFont(self.fontstyle)

        self.multiply.setObjectName("Operations")
        self.divide.setObjectName("Operations")
        self.plus.setObjectName("Operations")
        self.minus.setObjectName("Operations")
        self.equal.setObjectName("Operations")

        self.clear.setObjectName("Up")
        self.delete.setObjectName("Up")
        self.power.setObjectName("Up")

        self.setStyleSheet(""" 
                QWidget{
                           background-color:black;}
                QPushButton{
                           border-radius:50%;
                           border:0;
                           background-color:white;
                           font-size:50px;
                           padding:20px 50px;
                           }
                QPushButton#Operations{
                           background-color:orange;}
                QPushButton#Up{
                           background-color:Grey;}
                QLabel{
                           background-color:black;
                           color:white;
                           border:0;
                           border-radius:5%;
                           font-size:80px;
                           padding:50px; }

                QPushButton:hover{
                           background-color:#dce0dd;}
            """)
        
        self.num0.clicked.connect(self.on_click0)
        self.num1.clicked.connect(self.on_click1)
        self.num2.clicked.connect(self.on_click2)
        self.num3.clicked.connect(self.on_click3)
        self.num4.clicked.connect(self.on_click4)
        self.num5.clicked.connect(self.on_click5)
        self.num6.clicked.connect(self.on_click6)
        self.num7.clicked.connect(self.on_click7)
        self.num8.clicked.connect(self.on_click8)
        self.num9.clicked.connect(self.on_click9)
        self.clear.clicked.connect(self.on_click10)
        self.delete.clicked.connect(self.on_click11)
        self.open.clicked.connect(self.on_click12)
        self.closed.clicked.connect(self.on_click13)
        self.equal.clicked.connect(self.on_click14)
        self.power.clicked.connect(self.on_click15)
        self.multiply.clicked.connect(self.on_click16)
        self.divide.clicked.connect(self.on_click17)
        self.plus.clicked.connect(self.on_click18)
        self.minus.clicked.connect(self.on_click19)

    def on_click0(self):
        current_text = self.display.text()
        self.display.setText(current_text + "0")
        self.data+='0'

    def on_click1(self):
        current_text = self.display.text()
        self.display.setText(current_text + "1")
        self.data+='1'

    def on_click2(self):
        current_text = self.display.text()
        self.display.setText(current_text + "2")
        self.data+='2'

    def on_click3(self):
        current_text = self.display.text()
        self.display.setText(current_text + "3")
        self.data+='3'

    def on_click4(self):
        current_text = self.display.text()
        self.display.setText(current_text + "4")
        self.data+='4'

    def on_click5(self):
        current_text = self.display.text()
        self.display.setText(current_text + "5")
        self.data+='5'

    def on_click6(self):
        current_text = self.display.text()
        self.display.setText(current_text + "6")
        self.data+='6'

    def on_click7(self):
        current_text = self.display.text()
        self.display.setText(current_text + "7")
        self.data+='7'

    def on_click8(self):
        current_text = self.display.text()
        self.display.setText(current_text + "8")
        self.data+='8'

    def on_click9(self):
        current_text = self.display.text()
        self.display.setText(current_text + "9")
        self.data+='9'

    def on_click10(self):
        self.display.setText("")
        self.data=""

    def on_click11(self):
        current_text = self.display.text()
        self.display.setText(current_text[:-1])
        self.data=self.data[:-1]
    
    def on_click12(self):
        current_text = self.display.text()
        self.display.setText(current_text + "(")
        self.data+='('

    
    def on_click13(self):
        current_text = self.display.text()
        self.display.setText(current_text + ")")
        self.data+=')'
    
    def on_click14(self):
        s=calculate(self.data)
        self.display.setText(str(s))

    def on_click15(self):
        current_text = self.display.text()
        self.display.setText(current_text + "^")
        self.data+='^'

    def on_click16(self):
        current_text = self.display.text()
        self.display.setText(current_text + "*")
        self.data+='*'

    def on_click17(self):
        current_text = self.display.text()
        self.display.setText(current_text + "/")
        self.data+='/'

    def on_click18(self):
        current_text = self.display.text()
        self.display.setText(current_text + "+")
        self.data+='+'

    def on_click19(self):
        current_text = self.display.text()
        self.display.setText(current_text + "-")
        self.data+='-'
    
    
app=QApplication(sys.argv)

window=MainWindow()
window.show()
sys.exit(app.exec_())

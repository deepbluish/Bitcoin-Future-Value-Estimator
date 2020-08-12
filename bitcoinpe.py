##Created with:

## Python 3.7.7, by Guido Van Rossum: https://www.python.org/

## QT, a GUI builder: https://www.qt.io/licensing/

## PYQT5, Python bindings for QT: https://www.riverbankcomputing.com/software/pyqt/

## Requests, an HTTP library for Python: https://requests.readthedocs.io/en/master/
       
       #Copyright 2019 Kenneth Reitz

       #Licensed under the Apache License, Version 2.0 (the “License”); you may not use this file except in compliance with the License. You may obtain a copy of the License at

       #https://www.apache.org/licenses/LICENSE-2.0
       #Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## App by WJE: https://harmonicwebsolutions.com

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import QMessageBox
from datetime import date
import requests, json

def getBitcoinPrice():
    URL = 'https://www.bitstamp.net/api/ticker/'
    r = requests.get(URL)
    priceFloat = float(json.loads(r.text)['last'])
    return priceFloat

cbcp = getBitcoinPrice() 
datnow = QDateTime.currentDateTime().addDays(7)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 460)
        self.label_a = QtWidgets.QLabel(Dialog)
        self.label_a.setObjectName("label_a")
        self.label_a.setGeometry(QtCore.QRect(6, 165, 10, 10))
        self.label_b = QtWidgets.QLabel(Dialog)
        self.label_b.setObjectName("label_b")
        self.label_b.setGeometry(QtCore.QRect(6, 235, 10, 10))
        self.label_c = QtWidgets.QLabel(Dialog)
        self.label_c.setObjectName("label_c")
        self.label_c.setGeometry(QtCore.QRect(6, 304, 10, 10))
        self.label_d = QtWidgets.QLabel(Dialog)
        self.label_d.setObjectName("label_d")
        self.label_d.setGeometry(QtCore.QRect(6, 374, 10, 10))
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(9, 124, 511, 23))
        self.label_4.setObjectName("label_4")
        self.howmuchb = QtWidgets.QLineEdit(Dialog)
        self.howmuchb.setGeometry(QtCore.QRect(20, 155, 144, 33))
        self.howmuchb.setValidator(QtGui.QDoubleValidator(notation=QtGui.QDoubleValidator.StandardNotation))
        self.howmuchb.setObjectName("howmuchb")
        self.Title = QtWidgets.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(9, 194, 395, 23))
        self.Title.setObjectName("Title")
        self.whatprice = QtWidgets.QLineEdit(Dialog)
        self.whatprice.setGeometry(QtCore.QRect(20, 225, 144, 33))
        self.whatprice.setValidator(QtGui.QDoubleValidator(notation=QtGui.QDoubleValidator.StandardNotation))
        self.whatprice.setObjectName("whatprice")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(9, 264, 140, 23))
        self.label.setObjectName("label")
        self.selldate = QtWidgets.QDateEdit(Dialog)
        self.selldate.setGeometry(QtCore.QRect(20, 294, 102, 33))
        self.selldate.setMinimumDateTime(datnow)
        self.selldate.setObjectName("selldate")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(9, 333, 478, 23))
        self.label_2.setObjectName("label_2")
        self.howmuchd = QtWidgets.QLineEdit(Dialog)
        self.howmuchd.setGeometry(QtCore.QRect(20, 364, 144, 33))
        self.howmuchd.setValidator(QtGui.QDoubleValidator(notation=QtGui.QDoubleValidator.StandardNotation))
        self.howmuchd.setPlaceholderText("")
        self.howmuchd.setObjectName("howmuchd")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 410, 279, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(9, 9, 291, 109))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.btcprice = QtWidgets.QLabel(Dialog)
        self.btcprice.setGeometry(QtCore.QRect(310, 40, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btcprice.setFont(font)
        self.btcprice.setWordWrap(True)
        self.btcprice.setObjectName("btcprice")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(430, 30, 81, 81))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("BC_Logo_.png"))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.onButtonClicked)
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bitcoin Future Portfolio Estimator"))
        self.label_a.setText(_translate("Dialog", "$"))
        self.label_b.setText(_translate("Dialog", "$"))
        self.label_c.setText(_translate("Dialog", ">"))
        self.label_d.setText(_translate("Dialog", "$"))
        self.label_4.setText(_translate("Dialog", "What is the value (USD) of the Bitcoin you currently own?"))
        self.Title.setText(_translate("Dialog", "What price do you think Bitcoin will be when you sell?"))
        self.label.setText(_translate("Dialog", "When will you sell?"))
        self.label_2.setText(_translate("Dialog", "How much (USD) will you add per week until your sell date?"))
        self.pushButton.setText(_translate("Dialog", "Calculate Estimated Portfolio Value"))
        self.label_3.setText(_translate("Dialog", "Bitcoin Future Portfolio Estimator"))
        self.btcprice.setText(_translate("Dialog", "1 BTC = $" + str(cbcp)))
        
    def onButtonClicked(self):
        if self.howmuchd.text() == "" or self.whatprice.text() == "" or self.howmuchb.text() == "":
            self.show_error("Please fill all required fields.")
        else:
            self.processValues(self.selldate.date().toPyDate(), self.howmuchd.text(), self.whatprice.text(), self.howmuchb.text())
        
    def weeksbetweendates(self, d1):
        d2 = QDate.currentDate().toPyDate()
        result = (d1-d2).days//7
        #print(result)
        return(result)
          
    def processValues(self, wkss, das, tvs, cvs):
        wks = self.weeksbetweendates(wkss)
        myString = tvs.strip("\"")
        myString2 = cvs.strip("\"")
        myString3 = das.strip("\"")
        tv = float(myString.replace(',',''))
        cv = float(myString2.replace(',',''))
        da = float(myString3.replace(',',''))
        final = self.masterformula(wks, da, tv, cv)
        final = str(final)
        self.show_popup(final)
        
    def masterformula(self, wks, da, tv, cv):
        #wks = weeks until sell date 
        #da = USD added per week
        #tv = bitcoin target value at sale
        #cv = current portfolio (USD) value
        #cbcp = current bitcoin price (USD)[defined at beginning of program]
        
        #dollars added per week multiplier
        mtpl = tv/cbcp
        #increment for lessening mtpl
        inc = mtpl/wks
       
        list1 = []
        
        for i in range(wks):
            x = mtpl * da
            list1.append(x)
            mtpl = (mtpl - inc)
            
        a = (sum(list1))
        j = cv * (tv/cbcp)
        c = a + j
        return(round(c, 2))
        
    def show_popup(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("BFPE")
        msg.setText("Estimated value on " + str(self.selldate.date().toPyDate()) + ": $" + '{0:,.2f}'.format(float(text)))
        x = msg.exec_()
    
    def show_error(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("BFPE")
        msg.setText(text)
        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

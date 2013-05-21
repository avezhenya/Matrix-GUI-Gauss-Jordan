#!usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'avezhenya'

from PyQt4 import QtCore, QtGui
import interface
import Matrix

class MyWindow(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = interface.Ui_Form()
        self.ui.setupUi(self)
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.Zadat_matrix)
        self.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.Schet)


    def Zadat_matrix (self):
        col = int(self.ui.lineEdit.text())
        self.ui.tableWidget.setRowCount(col)
        self.ui.tableWidget.setColumnCount(col)
        self.ui.tableWidget_2.setRowCount(col)
        self.ui.tableWidget_2.setColumnCount(col)

    def Schet(self):
        col = int(self.ui.lineEdit.text())
        a = Matrix.matrix(col,col)
        for i in range(col):
            for j in range(col):
                a.set_value(i,j,self.ui.tableWidget.item(i,j).text())
        if a.determinant() :
            b = a.Gauss_Jordan_inverse()
            for i in range(col):
                for j in range(col):
                    self.ui.tableWidget_2.setItem(i,j,QtGui.QTableWidgetItem(str(b[i][j])))


if __name__=="__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

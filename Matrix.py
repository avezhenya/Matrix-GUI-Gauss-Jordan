#!usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'avezhenya'


class matrix (object):
    rows = 0
    cols = 0
    values = [[]]

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = [[0 for i in range(cols)] for i in range(rows)]

    def getRow(self, row):
        return self.values[row]

    def getCol(self, col):
        return [self.rows[col] for self.rows in self.values]

    def identity(self):
        """The identity matrix"""
        arr = self.values[:]
        if self.cols != self.rows:
            raise Exception ('Matrix is not square!')
        for i in range(self.rows):
            for j in range(self.cols):
                if i == j :arr[i][j]=1
                else: arr[i][j]=0
        return arr

    def output_value(self, row, col):
        """Get_value"""
        return self.values[row][col]

    def set_value(self, row, col, value):
        value = float(value)
        self.values[row][col] = value

    def Gauss_Jordan_inverse(self):
        #Only if determinant() = True
        arr = self.values[:]
        #Add identity matrix on the right
        for i in range(self.rows):
            for j in range(self.cols):
                if j == i:
                    arr[i].append(1)
                else:
                    arr[i].append(0)
        #Reset all that is below the main diagonal
        for i in range(self.rows):
            arr[i] = [round(x * (1/arr[i][i]), 4) for x in arr[i]]
            for j in range(self.cols):
                try:
                    j += i
                    arr1 = [round(x * (-arr[j+1][i]),4) for x in arr[i]]
                    arr[j+1] = map(lambda x,y: round(x+y, 4), arr[j+1], arr1 )
                except IndexError:
                    break
        #Reset all that is above the main diagonal
        for i in range(self.rows-1, -1,  -1):
            arr[i] = [round(x * (1/arr[i][i]), 4) for x in arr[i]]
            for j in range(self.cols-1, 0, -1):
                if j <= i:
                    arr1 = [round(x * (-arr[j-1][i]),4) for x in arr[i]]
                    arr[j-1] = map(lambda x, y: round(x+y, 4), arr[j-1], arr1)
        arr2 = [arr[l][self.rows:] for l in range(self.rows)]
        return arr2

    def determinant(self):
        """The determinant of the matrix"""
        if self.cols != self.rows:
            raise Exception ('Matrix is not square!')
        for i in range(self.rows):
            if self.values[i][i] == 0:
                raise Exception ('There is  zero on the main diagonal')
            #TODO: Rearrange the lines, that the main diagonal don't have a zero values 

        arr = self.values[:]
        for i in range(self.rows):
            for j in range(self.cols):
                diag = [arr[l][p] for p in range(self.cols) for l in range(self.rows) if l == p  ]
                if i > j :
                    arr2 = arr[i][j]/diag[j]
                    arr1 = [round(x * arr2, 4) for x in arr[i-i+j]]
                    arr[i] = map(lambda x,y: round(x - y, 4) , arr[i], arr1  )

        diag = [arr[l][p] for p in range(self.cols) for l in range(self.rows) if l == p  ]
        det = 1
        for i in range(len(diag)):
            det *= diag[i]
        if det != 0 :
            return True
        else:
            return False

    def show_Matrix(self):
        """Вывод матрицы"""
        for row in range(self.rows):
            for col in range(self.cols):
                print self.output_value(row, col)
            print

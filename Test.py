#!usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'avezhenya'

import Matrix

b = Matrix.matrix(3,3)
b.set_value(0,0,-4)
b.set_value(0,1,3)
b.set_value(0,2,6)
b.set_value(1,0,5)
b.set_value(1,1,-10)
b.set_value(1,2,4)
b.set_value(2,0,-9)
b.set_value(2,1,-1)
b.set_value(2,2,1)
print b.determinant()
b.Gauss_Jordan_inverse()
b.show_Matrix()

"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
"""
a = 1
b = 2
c = 3
if a + b > c and a + c > b and b + c > a:
    print('ok')
else:
    print('not ok')


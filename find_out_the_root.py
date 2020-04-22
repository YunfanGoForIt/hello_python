a=input('二次项系数')
b=input('一次项系数')
c=input('常数项')
float_a=float(a)
float_b=float(b)
float_c=float(c)
delta=float_b**2-4*float_a*float_c
print('delta=%f'%(delta))
if delta >= 0:
    root_1=(-float_b+delta**0.5)/(2*float_a)
    root_2=(-float_b-delta**0.5)/(2*float_a)
    print('root_1=%f'%(root_1))
    print('root_2=%f'% (root_2))
else:
    print("no root")


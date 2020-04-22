'''for i in range(1,10):
    a=2
    j=1
    list_01 = []
    while j<a:
        for k in range(1,i+1):
            res=k*i
            list_01.append(str(k)+'*'+str(i)+'='+str(res))
            j+=1
    a+=1
    print(list_01)'''



for i in range(1,10):     #控制行数
    for j in range(1,i+1):  #控制一行有几个，以及每个算式的第一个乘数
        print('{0}*{1}={2} '.format(j,i,i*j),end='')    #end=''控制不换行输出
    print('')  #换行  结束一个母for循环（一行）换一次行

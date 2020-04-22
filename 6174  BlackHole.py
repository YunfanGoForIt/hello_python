def Rank(a,b,c,d):
    list_1=[a,b,c,d]
    list_1.sort()
    res_list_1=1000*list_1[0]+100*list_1[1]+10*list_1[2]+list_1[3]
    list_2=list_1
    list_2.reverse()
    res_list_2=1000*list_2[0]+100*list_2[1]+10*list_2[2]+list_2[3]
    res_round1 = res_list_2- res_list_1
    print('第1次循环得到%d '%(res_round1))
    count=1
    if res_round1!=6174:
        while res_round1!=6174:
            list_res_round1=[int(x) for x in str(res_round1)]
            list_res_round1.sort()
            res_list_1_1 = 1000 * list_res_round1[0] + 100 * list_res_round1[1] + 10 * list_res_round1[2] + list_res_round1[3]
            list_2_2 = list_res_round1
            list_2_2.reverse()
            res_list_2_2 = 1000 * list_2_2[0] + 100 * list_2_2[1] + 10 * list_2_2[2] + list_2_2[3]
            res_round1 = res_list_2_2-res_list_1_1
            count+=1
            print('第%d次循环得到%d'%(count,res_round1))
    else:
        print('循环%d次得到6174' % (1))
print('欢迎探索6174黑洞')
print('6174黑洞是什么？')
print('  取任意一个4位数（4个数字均为同一个数的，以及三个数字相同，另外一个数与这个数相差1，如1112，,6566等除外），\n将该数的4个数字重新组合，形成可能的最大数和可能的最小数，再将两者之间的差求出来；对此差值重复同样过程，\n最后你总是至达卡普雷卡尔黑洞6174，到达这个黑洞最多需要14个步骤。')
while True:
    int_input=int(input('输入1进入下一步/重新开始  '))
    if int_input==1:
        int_input_2=int(input('如果你想验证你喜欢的一个数,请按1\n如果你想验证部分四个数字不相同的数字组合是否符合，请按2\n'))
        if int_input_2==1:
            int_inpur_3=int(input('请输入你想验证你喜欢的一个四位数  '))
            res_int_inpur_3=[int(x) for x in str(int_inpur_3)]
            Rank(res_int_inpur_3[0],res_int_inpur_3[1],res_int_inpur_3[2],res_int_inpur_3[3])
        elif int_input_2==2:
            all = [1234, 1345, 1456, 1567, 1678, 1789, 2345, 2456, 2567, 2678, 2789, 3456, 3567, 3678, 3789, 4567, 4678,
                   4789, 5678, 5789, 6789]
            for item in all:
                times =item
                print('下面验证%d：'%(item))
                res_times = [int(x) for x in str(times)]
                Rank(res_times[0],res_times[1],res_times[2],res_times[3])
                print('')
        else:
            print('瞎搞什么，讨厌！')
    else:
        print('瞎搞什么，讨厌！')






def hannuota(n,x,y,z):
    if n == 1:
        print(x,'-->',z)
    else:
        hannuota(n-1,x,z,y)#讲将n-1个盘子从x移动到y上
        print(x,'-->',z)#将最后一个盘子从x移动到z上
        hannuota(n-1,y,x,z)#将y上的n-1个盘子移动到z上

n = int (input('请输入汉诺塔的层数：'))
hannuota(n,'X','Y','Z')

def plus(num_1,num_2):
    print("输入“q”可终止")
    while True:
        try:
            num_1 = input("请输入数字1：")
            if num_1 == "q":
                break
            num_1 = int(num_1)
            
            num_2 = input("请输入数字2：")
            if num_2 == "q":
                break
            num_2 = int(num_2)
        except ValueError:
            print("请重新输入，要求输入数字。")
        else:
            num_sum = num_1 + num_2
            print("结果为:" + str(num_sum))
   


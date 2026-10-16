def main():

    # # 1.会员等级评定
    # user_points = 6500  #会员积分
    # user_purchases = 800    #会员消费金额
    # if user_points >= 10000 and user_purchases >= 1000:
    #     print("您是钻石会员")
    # elif user_points >= 5000 and user_purchases >= 500:
    #     print("您是白金会员")
    # elif user_points >= 2000 and user_purchases >= 200:
    #     print("您是黄金会员")
    # elif user_points >= 1000 and user_purchases >= 100:
    #     print("您是白银会员")
    # elif user_points >= 500:
    #     print("您是青铜会员")
    # else:
    #     print("您是普通会员")

    # 2.物流费用计算
    # 接收物品重量和地区编号
    weight = float(input("请输入物品重量(kg): "))
    print("编号01: 华东地区 编号02: 华南地区 编号03: 华北地区")
    place = input("请输入地区编号：")
    # 判断物品重量是否超过首重
    if weight <= 2:
        # 处理没超过首重的情况
        if place == '01':
            print("快递费用为13元")
        elif place == '02':
            print("快递费用为12元")
        elif place == '03':
            print("快递费用为14元")
    else:
        # 处理超过首重的情况
        excess_weight = weight - 2   # 计算续重
        if place == '01':
            money = excess_weight * 3 + 13
            print(f"快递费用为{money:.2f}元")
        elif place == '02':
            money = excess_weight * 2 + 12
            print(f"快递费用为{money:.2f}元")
        elif place == '03':
            money = excess_weight * 4 + 14
            print(f"快递费用为{money:.2f}元")


    # # 3.登录检测
    # count = 0    # 记录用户输错密码的次数
    # while count < 3:
    #     username = input("请输入您的账号：")
    #     password = input("请输入您的密码：")
    #     if username == 'admin' and password == 'admin123':  # 账号与密码正确
    #         print('登录成功')
    #         break     # 跳出循环
    #     else:  # 账号或密码错误
    #         print("用户名或密码错误")
    #         count += 1          # 错误次数累加一次
            
    #         if count == 3:  # 判断输错密码的次数是否等于三次
    #             print("输入错误次数过多，请稍后再试")
    #         else:
    #             print(f"您还有{3-count}次机会")     # 显示剩余次数

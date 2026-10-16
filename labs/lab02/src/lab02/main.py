def main():
    # # 1.时间间隔计算器

    # # 输入起始时间
    # start_h = int(input("请输入起始时间的小时数："))
    # start_m = int(input("请输入起始时间的分钟数："))

    # # 输入结束时间
    # end_h = int(input("请输入结束时间的小时数："))
    # end_m = int(input("请输入结束时间的分钟数："))

    # # 计算时间间隔
    # start_total_m = start_h * 60 + start_m  # 将起始时间转换为分钟数
    # end_total_m = end_h * 60 + end_m  # 将结束时间转换为分钟数

    # total_duration_m = end_total_m - start_total_m  # 计算时间段的总分钟数
    # duration_h = total_duration_m // 60  # 将分钟数转换为小时数
    # duration_m = total_duration_m % 60  # 计算剩余的分钟数

    # # 输出结果
    # print(f"时间间隔为：{duration_h} 小时 {duration_m} 分钟")

    # 2.打印购物小票
    usb_price        = float(input("扫描金士顿U盘8G的价格: "))
    tfcard_price     = float(input("扫描胜创16GTF卡的价格: "))
    cardreader_price = float(input("扫描读卡器的价格："))
    cable_price      = float(input("扫描网线2米的价格: "))
    # 数量（本单都是 1 件）
    qty = 1
    # 金额 = 数量 × 单价
    usb_amount        = qty * usb_price
    tfcard_amount     = qty * tfcard_price
    cardreader_amount = qty * cardreader_price
    cable_amount      = qty * cable_price
    # 汇总
    total = usb_amount + tfcard_amount + cardreader_amount + cable_amount
    paid  = float(input("请输入实收金额："))
    change = paid - total

    print(".....................................................")
    print("单号: DH202609210001")
    print("时间: 2026-09-21 10:28:15")
    print(".................................")
    print(f"{'名称':<14}{'数量':<6}{'单价':<8}{'金额':<8}")
    print(f"{'金士顿U盘8G':<14}{qty:<6}{usb_price:<8}{usb_amount:<8.2f}")
    print(f"{'胜创16GTF卡':<14}{qty:<6}{tfcard_price:<8}{tfcard_amount:<8.2f}")
    print(f"{'读卡器':<14}{qty:<6}{cardreader_price:<8}{cardreader_amount:<8.2f}")
    print(f"{'网线2米':<14}{qty:<6}{cable_price:<8}{cable_amount:<8.2f}")
    print(".....................................................")
    print(f"总数: 4          总额: {total:.2f}")
    print(f"折后总额: {total:.2f}")
    print(f"实收: {paid:.2f}     找零: {change:.2f}")
    print("收银：管理员")
    print(".................................")
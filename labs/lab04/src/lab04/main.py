def make_business_cards() -> None:

    name = input('请输入您的姓名：')        	# 姓名
    position = input('请输入您的职位：')    	# 职位
    phone = input('请输入您的电话：')       	# 电话
    email = input('请输入您的邮箱：')       	# 邮箱
    print('=============================')
    print('姓名：{}'.format(name))       	# 使用{}标注姓名插入的位置
    print('职位：{}'.format(position))   	# 使用{}标注职位插入的位置
    print('电话：{}'.format(phone))      	# 使用{}标注电话插入的位置
    print('邮箱：{}'.format(email))      	# 使用{}标注邮箱插入的位置
    print('=============================')

def filter_words() -> None:

    text = '我们拥有多年的品牌战略规划及标志设计、商标注册经验；' \
       '专业提供公司标志设计与商标注册一条龙服务。\n'\
       '我们拥有最优秀且具有远见卓识的设计师，使我们的策略分析严谨，' \
       '设计充满创意。\n 我们有信心为您缔造最优秀的品牌形象设计服务，' \
       '将您的企业包装得更富价值。'

    print('过滤前文本：\n' + text)

    sensitive_word = '最优秀'                      # 设立不良词语
    replace_word = '较优秀'                        # 替换后词语
    result = text.find(sensitive_word)            # 在文本中查找不良词语是否存在
    if result != -1:       # 找到不良词语
        text = text.replace(sensitive_word, replace_word) # 替换不良词语
        print('过滤后的文本：\n' + text)
    else:                  # 没有找到不良词语
        print("无不良词语！")

def format_time() -> None:
    # 用户输入的时间信息
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入日期："))
    hour = int(input("请输入小时："))
    minute = int(input("请输入分钟："))
    second = int(input("请输入秒钟："))

    country = input("请输入要转换的国家（中国、美国、英国、德国、俄罗斯、澳大利亚、法国、加拿大）：")

    # 转换为指定国家的时间格式
    match country:
        case '中国':
            formatted_time = f"{year:04d}年{month:02d}月{day:02d}日 {hour:02d}:{minute:02d}:{second:02d}"
        case '美国':
            formatted_time = f"{month:02d}/{day:02d}/{year:04d} {hour:02d}:{minute:02d}:{second:02d}"
        case '英国' | '澳大利亚' | '法国':
            formatted_time = f"{day:02d}/{month:02d}/{year:04d} {hour:02d}:{minute:02d}:{second:02d}"
        case '德国' | '俄罗斯':
            formatted_time = f"{day:02d}.{month:02d}.{year:04d} {hour:02d}:{minute:02d}:{second:02d}"
        case '加拿大':
            formatted_time = f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"
        case _:
            formatted_time = '不支持该国家的时间格式转换'

    print(formatted_time)

def main() -> None:
    # make_business_cards()
    # filter_words()
    format_time()


if __name__== "__main__":
    main()
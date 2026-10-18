def word_chain() -> None:

    first_idiom = '万事如意'
    end_str = first_idiom[-1]
    new_li = [first_idiom]
    li = ['发愤图强', '笑容满面', '意气风发', '强颜欢笑']
    for index in range(len(li)):
        for i in li:
            if end_str == i[0]:
                new_li.append(i)
                li.remove(i)
                end_str = i[-1]
                break
    print(new_li)


def chinese_numerals_chart() -> None:

    num_str = input("请输入要转换的数字（例如 123456789.10）:")
    
    digits = ("零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖")
    units_int = ("", "拾", "佰", "仟")
    units_section = ("", "万", "亿", "兆")
    
    if '.' in num_str:
        int_part, dec_part = num_str.split('.')
    else:
        int_part, dec_part = num_str, ""
        
    if not int_part.isdigit() or (dec_part and not dec_part.isdigit()):
        print("输入格式错误！")
        return
        
    result_int = ""
    if int_part == '0':
        result_int = "零"
    else:
        sections = []
        while int_part:
            sections.append(int_part[-4:])
            int_part = int_part[:-4]

        for i in range(len(sections) - 1, -1, -1):
            sec_str = sections[i]
            sec_len = len(sec_str)
            zero_flag = False
            
            for j in range(sec_len):
                digit = int(sec_str[j])
                pos = sec_len - j - 1
                
                if digit == 0:
                    zero_flag = True
                else:
                    if zero_flag and result_int:
                        result_int += "零"
                    zero_flag = False
                    result_int += digits[digit] + units_int[pos]
            
            if sec_str != "0000" and sec_str != "":
                result_int += units_section[i]
                if sec_str[-1] == '0' and i > 0:
                    zero_flag = True

    result_dec = ""
    if dec_part:
        result_dec += "点"
        for d in dec_part:
            result_dec += digits[int(d)]
            
    print("转换结果：", result_int + result_dec)


def word_count() -> None:

    text = input("请输入英文内容：").lower()

    text = text.replace(",", " ").replace(".", " ")

    words = text.split()

    unique_words = set(words)

    word_count = {}
    for word in unique_words:
        word_count[word] = words.count(word)

    print("--------------------")

    for word in word_count:
        print(f"{word:10}: {word_count[word]}次")


def phone_contacts() -> None:
    person_info = []

    print("=" * 20)
    print('欢迎使用通讯录：')
    print("1.添加联系人")
    print("2.查看通讯录")
    print("3.删除联系人")
    print("4.修改联系人")
    print("5.查找联系人")
    print("6.退出")
    print("=" * 20)

    while True:
        per_dict = {}
        fun_num = input('请输入功能序号:')
        if fun_num == '1':
            per_name = input('请输入联系人的姓名：')
            phone_num = input('请输入联系人的手机号：')
            per_email = input('请输入联系人的邮箱：')
            per_address = input('请输入联系人的地址：')

            if per_name.strip() == '':
                print('请输入正确信息')
                continue
            else:
                per_dict.update({'姓名': per_name,
                                '手机号': phone_num,
                                '电子邮箱': per_email,
                                '联系地址': per_address})
                person_info.append(per_dict)
                print('保存成功')
        elif fun_num == '2':
            if len(person_info) == 0:
                print('通讯录无信息')
            for i in person_info:
                for title, info in i.items():
                    print(title + ':' + info)

        elif fun_num == '3':
            if len(person_info) != 0:
                del_name = input('请输入要删除的联系人姓名：')
                for i in person_info:
                    if del_name in i.values():
                        person_info.remove(i)
                        print(person_info)
                        print('删除成功')
                    else:
                        print('该联系人不在通讯录中')
            else:
                print('通讯录无信息')

        elif fun_num == '4':
            if len(person_info) != 0:
                modi_info = input('请输入要修改联系人姓名：')
                for i in person_info:
                    if modi_info in i.values():
                        index_num = person_info.index(i)
                        dict_cur_perinfo = person_info[index_num]
                        for title, info in dict_cur_perinfo.items():
                            print(title + ':' + info)
                        modi_name = input('请输入新的姓名：')
                        modi_phone = input('请输入新的手机号：')
                        modi_email = input('请输入新的邮箱：')
                        modi_address = input('请输入新的地址：')
                        dict_cur_perinfo.update(姓名=modi_name)
                        dict_cur_perinfo.update(手机号=modi_phone)
                        dict_cur_perinfo.update(电子邮箱=modi_email)
                        dict_cur_perinfo.update(联系地址=modi_address)
                print('修改成功')
            else:
                print('通讯录无信息')

        elif fun_num == '5':
            if len(person_info) != 0:
                query_name = input('请输入要查找的联系人姓名：')
                for i in person_info:
                    if query_name in i.values():
                        index_num = person_info.index(i)
                        for title, info in person_info[index_num].items():
                            print(title + ':' + info)
                        break
                else:
                    print('该联系人不在通讯录中')
            else:
                print('通讯录无信息')

        elif fun_num == '6':
            print('退出成功')
            break

def main() -> None:
    # word_chain()
    # chinese_numerals_chart()
    # word_count()
    phone_contacts()

if __name__ == "__main__":
    main()
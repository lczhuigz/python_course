#  聊天机器人
class chats_robot:
    def __init__(self) -> None:
        self.problem_dict = {
            "诗仙是谁": "李白",
            "中国第一个朝代": "夏朝",
            "三十六计的第一计是什么": "瞒天过海",
            "天府之国是中国的哪个地方": "四川",
            "中国第一长河": "长江"
        }
        self.work = True
        self.flag = "c"

    def train(self, arg_question, arg_answer) -> None:
        self.problem_dict[arg_question] = arg_answer
        print(f"小智：训练成功，我现在会回答{len(self.problem_dict)}个问题了！")
        print("--------------------")
        num = 1
        for key in self.problem_dict.keys():
            print(str(num) + "、" + key)
            num += 1
        print("--------------------")

    def exchange(self, words) -> None:
        self.work = False
        for key in self.problem_dict.keys():
            if words == key:
                print(f"小智：{self.problem_dict[key]}")
                self.work = True
                break
            else:
                self.work = False
        if not self.work:
            print("小智：抱歉，这个问题我还不会回答！")
            self.work = True

    def run(self) -> None:
        print("小智：你好，我是小智！")
        while self.flag == "c" or self.flag == "t":
            input_flag = input("你可以选择和我聊天(c)训练对话(t)让我离开(q)\n我:")
            if input_flag in ["c", "t", "q"]:
                self.flag = input_flag
            if input_flag == "t":
                question = input("小智：请输入问题\n我:")
                answer = input("小智：请输入答案\n我:")
                self.train(question, answer)
                continue
            elif input_flag == "c":
                if len(self.problem_dict) == 0:
                    print("小智：我现在还不会回答哦，请先训练我！")
                    continue
                char_word = input("小智：很开心和你聊天，你想问我什么!\n我:")
                self.exchange(char_word)
            elif input_flag == "q":
                print("小智：好的，下次再见！")
                break
            else:
                print("小智：请输入正确的指令！")

# 饮品自动售货机
class vending_machine:
    def __init__(self) -> None:
        self.goods = {"可口可乐": 2.5, "百事可乐": 2.5, "冰红茶": 3, "脉动": 3.5,
         "果缤纷": 3, "绿茶": 3, "茉莉花茶": 3, "尖叫": 2.5
        }

    def show_goods(self) -> None:
        print("--------------------")
        for name,  price in self.goods.items():
            print(name, ":", str(price) + "元")
        print("--------------------")

    def total(self, goods_dict):
        count = 0
        for name, num in goods_dict.items():
            total_money = self.goods[name] * num
            count += total_money
        print("需要支付金额：", count, "元")

    def run(self) -> None:
        print("欢迎使用饮品自动售货机！")
        self.show_goods()
        goods_dict = {}
        while True:
            goods_name = input("请输入您要购买的商品（按q完成选择）：")
            if goods_name == 'q':
                break
            if goods_name in [g_name for g_name in self.goods.keys()]:
                goods_num = input("请输入购物数量：")
                if goods_num.isdigit():
                    goods_dict[goods_name] = int(goods_num)
                else:
                    print('商品数量不合法！')
            else:
                print('请输入正确的商品名称！')
        self.total(goods_dict)
        print("完成支付！期待下次惠顾!")

# 兔子序列
def fibonacci(month):
    if month == 0 or month == 1:
        return 1
    else:
        return fibonacci(month - 1) + fibonacci(month - 2)

# 商品推荐
class product_recommend:
    def __init__(self) -> None:
        self.products = [
            {'name': '华为P60', 'price': 4887.00, 'sales': 210},
            {'name': '华为Mate 40E Pro', 'price': 4699.00, 'sales': 90},
            {'name': '华为nova 10 青春版', 'price': 1698.00 , 'sales': 102},
            {'name': '华为P50 pro', 'price': 3987.00, 'sales': 88},
            {'name': '华为畅享', 'price': 999.00, 'sales': 152}
        ]

    def product_sort(self, top_n=3):
        sorted_products = sorted(self.products, key=lambda x: x['sales'], reverse=True)
        return sorted_products[:top_n]

    def run(self) -> None:
        print("=== 销量推荐 ===")
        sorted_products = self.product_sort()
        for product in sorted_products:
            print(f"推荐：{product['name']}，价格：{product['price']}，销量：{product['sales']}")

# main方法
def main() -> None:
    # robot = chats_robot()
    # robot.run()
    # machine = vending_machine()
    # machine.run()
    # print(fibonacci(12))
    product = product_recommend()
    product.run()

if __name__ == "__main__":
    main()
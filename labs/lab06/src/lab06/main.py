def chats_robot() -> None:
    problem_dict = {
        "诗仙是谁": "李白",
        "中国第一个朝代": "夏朝",
        "三十六计的第一计是什么": "瞒天过海",
        "天府之国是中国的哪个地方": "四川",
        "中国第一长河": "长江"
    }

    work = True
    flag = "c"

    def train(arg_question, arg_answer):
        problem_dict[arg_question] = arg_answer
        print(f"小智：训练成功，我现在会回答{len(problem_dict)}个问题了！")
        print("--------------------")
        num = 1
        for key in problem_dict.keys():
            print(str(num) + "、" + key)
            num += 1
        print("--------------------")

    def exchange(words):
        global work
        for key in problem_dict.keys():
            if words == key:
                print(f"小智：{problem_dict[key]}")
                work = True
                break
            else:
                work = False
        if not work:
            print("小智：抱歉，这个问题我还不会回答！")
            work = True

    print("小智：你好，我是小智！")
    while flag == "c" or flag == "t":
        input_flag = input("你可以选择和我聊天(c)训练对话(t)让我离开(q)\n我:")
        if input_flag in ["c", "t", "q"]:
            flag = input_flag
        if input_flag == "t":
            question = input("小智：请输入问题\n我:")
            answer = input("小智：请输入答案\n我:")
            train(question, answer)
            continue
        elif input_flag == "c":
            if len(problem_dict) == 0:
                print("小智：我现在还不会回答哦，请先训练我！")
                continue
            char_word = input("小智：很开心和你聊天，你想问我什么!\n我:")
            exchange(char_word)
        elif input_flag == "q":
            print("小智：好的，下次再见！")
            break
        else:
            print("小智：请输入正确的指令！")



def main() -> None:
    chats_robot()


if __name__ == "__main__":
    main()
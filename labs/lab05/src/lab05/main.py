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


def main() -> None:
    word_chain()


if __name__ == "__main__":
    main()
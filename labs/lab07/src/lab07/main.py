import os

class file_backup:
    def __init__(self) -> None:
        back_path = input("请输入备份的目标目录：\n")
        file_path = input("请输入要备份的目录或文件:\n")
        # 目标目录不存在
        if os.path.exists(back_path) is False:
            # 创建目标目录
            os.mkdir(back_path)
            self.judge(back_path, file_path)
            print('备份成功!')
        # 指定目录存在
        else:
            self.judge(back_path, file_path)
            print('备份成功!')

    def file_backups(self, file_name, path):
        # 获取待备份文件的文件名
        file_back = file_name.split('\\')[-1]
        # 判断用户输入的内容是否为文件
        if os.path.isdir(file_name) is not True:
            with open(file_name, mode='r') as file_data:
                # 将目标路径与文件名拼接成完整路径
                new_path = path + '/' + file_back
                # 创建新文件 , 以只写的方式打开新文件
                with open(new_path, 'w') as file:
                    # 逐行将源文件的内容复制到新文件中
                    for line_content in file_data.readlines():
                        file.write(line_content)

    def judge(self, back_path, file_path):
        if os.path.isdir(file_path) is True:  # 是目录
            # 遍历当前目录下的文件
            file_li = os.listdir(file_path)
            for i in file_li:
                # 拼接文件名称
                new_file = file_path + '\\' + i
                self.file_backups(new_file, back_path)
        else:  # 是文件
            if os.path.exists((file_path)):
                self.file_backups(file_path, back_path)
            else:
                print("备份的文件不存在!")
                exit()

def main() -> None:
    file_backup()

if __name__ == "__main__":
    main()




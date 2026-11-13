import os

# 文件备份
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

# 用户账户管理
class account_manager:

    def __init__(self, file_path='.info.txt') -> None:
        self.file_path = file_path
        self.users = []
        self._ensure_file()
        self._load()

    def _ensure_file(self) -> None:
        if os.path.exists(self.file_path) is not True:
            with open(self.file_path, mode='w', encoding='utf8') as f:
                f.write('')

    def _parse_line(self, line):
        line = line.strip()
        if not line:
            return None
        try:
            step_one = line.replace('{', '').replace('}', '')
            step_two = step_one.split(':')
            name = step_one[1].split(',')[0].replace("'", '').strip()
            password = step_two[2].replace("'", '').strip()
            return {'姓名': name, '密码': password}
        except(IndexError, ValueError):
            return None
        
    def _load(self) -> None:
        self.users.clear()
        with open(self.file_path, mode='r', encoding='utf8') as f:
            for line in f:
                user = self._parse_line(line)
                if user is not None:
                    self.users.append(user)

    def _save(self) -> None:
        with open(self.file_path, mode = 'w', encoding = 'utf8') as f:
            for user in self.users:
                f.write(str(user) + '\n')

    def _find_user_index(self, name):
        for i, user in enumerate(self.users):
            if user['姓名'] == name:
                return i
        return -1
    
    def register(self):
        name = input("请输入注册用户名：\n").strip()
        if not name:   # 用户名已经存在
            print("用户名不能为空！")
            return
        if self._find_user_index(name) != -1:
            print("用户已注册！")
            return
        
        password = input("请输入注册密码：\n")
        self.users.append({'姓名': name, '密码': password})
        self._save()

        print("注册成功")

    # 用户登录
    def login(self):
        if not self.users:
            print("当前无数据，请先注册")
            return

        name = input("请输入登录用户名：\n").strip()
        password = input("请输入登录密码：\n")

        index = self._find_user_index(name)
        if index == -1:
            print("用户名不正确！")
            return

        if password == self.users[index]['密码']:
            print('登录成功')
        else:
            print('用户名或密码不正确')

    def cancel(self):
        if not self.users:
            print("当前无数据，请先注册")
            return
        cancel_name = input("请输入注销的用户名\n").strip()
        cancel_password = input("请输入密码\n")

        index = self._find_user_index(cancel_name)
        if index == -1:
            print('注销的用户不存在')
            return

        if cancel_password != self.users[index]['密码']:
            print('用户名或密码不正确')
            return

        self.users.pop(index)
        self._save()
        print('用户注销成功')

    def modify(self):
        if not self.users:
            print("当前无数据，请先注册")
            return

        modify_name = input("请输入用户名：\n").strip()
        old_password = input("请输入旧密码：\n")

        index = self._find_user_index(modify_name)
        if index == -1:
            print("用户名不正确")
            return

        if old_password != self.users[index]['密码']:
            print("用户名或密码不正确")
            return

        new_password = input("请输入新密码\n")
        self.users[index]['密码'] = new_password
        self._save()
        print("密码修改成功")

    def show_menu(self) -> None:
        print("欢迎使用账户管理程序！")
        print("====================")
        print("1.用户注册")
        print("2.用户登录")
        print("3.用户注销")
        print("4.修改密码")
        print("5.退出")
        print("====================")

    def run(self) -> None:
        self.show_menu()
        while True:
            option = input("请选择功能\n")
            if option == '1':    # 用户注册
                self.register()
            elif option == '2':  # 用户登录
                self.login()
            elif option == '3':  # 用户注销
                self.cancel()
            elif option == '4':  # 修改密码
                self.modify()
            elif option == '5':  # 退出
                break


def main() -> None:
    # file_backup()
    manager = account_manager('./info.txt')
    manager.run()

if __name__ == "__main__":
    main()
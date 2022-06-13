import employee_tools

if __name__ == '__main__':
    while True:
        employee_tools.show_menu()
        action_str = input("请输入您的操作：")
        if action_str == "1":
            # 1.添加员工信息
            employee_tools.add_info()
        elif action_str == "2":
            # 2.修改员工信息
            employee_tools.update_info()
        elif action_str == "3":
            # 3.删除员工信息
            employee_tools.delete_info()
        elif action_str == "4":
            # 4.显示所有员工信息
            employee_tools.show_all_info()
        elif action_str == "5":
            # 5.退出系统
            print("欢迎您再次使用员工管理系统!!!")
            break
        else:
            # 输入其他任意数字
            print("您输入的有误，请重新输入：")
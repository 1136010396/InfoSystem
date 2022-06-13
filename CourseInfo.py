import os

course_list = []  # 存储课程信息字典，课程信息用字典存，再用列表存储字典


# 菜单
def display_menu():
    print("-" * 30)
    print("   课程管理系统  ")
    print("1.添加课程信息")
    print("2.删除课程信息")
    print("3.查询课程信息")
    print("4.保存课程信息数据")
    print("5.打开课程信息数据")
    print("0.退出系统")
    print("-" * 30)


# 选择序号的获得
def get_choice():
    selected_key = input("请输入功能对应的数字：")
    return selected_key


# 检查课程编号是否重复或者有误
def check_id(new_id):
    flag = True
    while flag:
        if new_id.isdigit():
            for i in range(len(course_list)):
                if course_list[i]['id'] == new_id:
                    new_id = check_id(input("您输入的课程重复，请重新输入："))
            flag = False
        else:
            new_id = input("您输入的课程编号有误，请重新输入：")
    return new_id


# 添加课程信息
def add_course():
    print('-----------欢迎使用添加功能------------')
    new_info = {}
    new_id = check_id(input("请输入新的课程编号："))
    new_info['id'] = new_id
    new_name = input("请输入新课程名称：")
    new_info['name'] = new_name
    new_style = input("请输入新课程类型(专业课/基础课)：")
    new_info['style'] = new_style
    new_time = input("请输入新课程课时：")
    new_info['time'] = new_time
    new_point = input("请输入新课程学分：")
    new_info['point'] = new_point
    course_list.append(new_info)
    print("添加成功！")
    print('------------处理后的课程数据------------')
    print('课程编号', ' ', '课程类型', ' ', '课程学分', ' ', '课程课时', ' ', '课程名称')
    for course in course_list:
        print(course['id'], ' ' * 8, course['style'], ' ' * 5, course['point'], ' ' * 8, course['time'], ' ' * 5,
              course['name'])


# 打开课程信息数据
def find_all():
    print('-------------恭喜你，打开数据成功-------------')
    print('------------处理后的课程数据------------')
    print('课程编号', ' ', '课程类型', ' ', '课程学分', ' ', '课程课时', ' ', '课程名称')
    for course in course_list:
        print(course['id'], ' ' * 8, course['style'], ' ' * 5, course['point'], ' ' * 8, course['time'], ' ' * 5,
              course['name'])


# 删除课程信息
def del_course():
    del_id_is = input("请输入要删除的课程编号：")
    flag = False
    index = 0
    for i in range(len(course_list)):
        if course_list[i]['id'] == del_id_is:
            flag = True
            index = i
            break
    if flag:
        course_list.pop(index)
        print('-------------恭喜你，删除数据成功-------------')
        print('------------处理后的课程数据------------')
        print('课程编号', ' ', '课程类型', ' ', '课程学分', ' ', '课程课时', ' ', '课程名称')
    for course in course_list:
        print(course['id'], ' ' * 8, course['style'], ' ' * 5, course['point'], ' ' * 8, course['time'], ' ' * 5,
              course['name'])


# 查询单个课程信息
def find_course():
    find_id_is = input("请输入要查询的课程编号：")
    flag = False
    index = 0
    for i in range(len(course_list)):
        if course_list[i]['id'] == find_id_is:
            flag = True
            index = i
            break
    if flag:
        print('------------处理后的课程数据------------')
        print('课程编号', ' ', '课程类型', ' ', '课程学分', ' ', '课程课时', ' ', '课程名称')
        print(course_list[index]['id'], ' ' * 8, course_list[index]['style'], ' ' * 5, course_list[index]['point'],
              ' ' * 8, course_list[index]['time'], ' ' * 5, course_list[index]['name'])
    else:
        print('该课程未找到！')


# 保存课程信息
def save_cou():
    course = str(course_list)
    with open("course.txt", "w", encoding="utf-8") as f:
        f.write(course)

    print("保存成功！文件位置在" + os.getcwd())
    print('处理后的课程数据')
    print('课程编号', ' ', '课程类型', ' ', '课程学分', ' ', '课程课时', ' ', '课程名称')
    for course in course_list:
        print(course['id'], ' ' * 8, course['style'], ' ' * 5, course['point'], ' ' * 8, course['time'], ' ' * 5,
              course['name'])


# 恢复数据
def recover_data():
    global course_list
    try:
        with open("course.txt", "r", encoding="utf-8") as f:
            content = f.read()
            if content != '':
                course_list = eval(content)
    except:
        f = open("course.txt", "w")
        f.write("[]")

def main():
    recover_data()
    exit_course = True
    while exit_course:
        display_menu()
        key = get_choice()
        if key == '1':
            add_course()
        elif key == '2':
            del_course()
        elif key == '3':
            find_course()
        elif key == '4':
            save_cou()
        elif key == '5':
            find_all()
        elif key == '0':
            exit_course = input('确定退出吗？（yes/no）:')
            if exit_course == 'yes':
                exit()
            else:
                pass
        else:
            print("请输入正确的数值！")

if __name__ == '__main__':
    main()
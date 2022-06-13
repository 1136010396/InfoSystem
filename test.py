# 学生管理系统，包括录入学生信息、查找学生信息、删除学生信息、修改学生信息、显示学生信息。

# 录入学生信息
# 录入学生的信息包括学号、姓名、英语成绩、python成绩、数学成绩、总成绩
def input_info():
    infile_info = open('infile.txt', 'a')  # 以追加的方式向文件中写入数据，如果文件不存在就创建一个文件
    flag = 'y'
    # 向文件中录入学生信息，每一个学生的信息单独占一行
    while flag == 'y' or flag == 'Y':
        stu_id = input("请输入学生学号（如2020001）：")
        stu_name = input("请输入学生姓名：")
        stu_score_eng = input("请输入学生英语成绩：")
        stu_score_py = input("请输入学生Python成绩：")
        stu_score_math = input("请输入学生数学成绩：")
        stu_sum_score = int(stu_score_eng) + int(stu_score_py) + int(stu_score_math)
        stu_info = stu_id + '\t' + stu_name + '\t' + stu_score_eng + '\t' + stu_score_py + '\t' + \
                   stu_score_math + '\t' + str(stu_sum_score) + '\n'
        infile_info.write(stu_info)
        flag = input("是否继续添加学生信息？y/n")
    print("信息录入完毕！！！")
    infile_info.close()


# 查询学生信息
# 查询时分为按学号和按姓名查找两种
def find_info():
    flag = 'y'
    while flag == 'y' or flag == 'Y':
        n = 0
        m = 0  # 定义m，n是为了用作判断文件中是否有此人信息的标记
        findfile_info = open('infile.txt', 'r')  # 以可读方式打开文件
        line_info = findfile_info.readlines()
        find_nid = input("按学号查找请输入1，按姓名查找请输入2：")  # 查询方式分为按学号和按姓名
        if find_nid == '1':
            find_id = input('请输入学生学号：')
            for line in line_info:
                if find_id in line:
                    print(line)
                    n = n + 1
            if n == 0:
                print("没有查询到学生信息，无数据显示！！！")
        if find_nid == '2':
            find_name = input('请输入学生姓名：')
            for line in line_info:
                if find_name in line:
                    print(line)
                    m = m + 1
            if m == 0:
                print("没有查询到学生信息，无数据显示！！！")
        findfile_info.close()
        flag = input("是否继续查询学生信息？y/n")


# 删除学生信息
# 输入学号进行查找，查找到学生信息之后，对学生信息进行删除
def del_info():
    flag = 'y'
    while flag == 'y' or flag == 'Y':
        n = 0  # 用以查无此人时的标记
        defile_info1 = open('infile.txt', 'r')  # 以可读方式打开文件
        line_info = defile_info1.readlines()  # 将文件的信息按行全部读取出来，此时line_info是一个列表，每一行是一个元素
        defile_info2 = open('infile.txt', 'w')  # 以可写方式打开文件，用来将删除后的信息写入文件
        del_id = input("请输入要删除的学生的学号：")
        for line in line_info:  # 如果要删除的学生学号在文件存储的信息中，就将后面的信息向前移动覆盖这条信息
            if del_id in line:
                continue
            defile_info2.write(line)
            n = n + 1
        if n == len(line_info):
            print("无此学生信息，请核对后再操作！！！")
        else:
            print("学号为{0}的学生信息已被删除！！！".format(del_id))
        defile_info1.close()
        defile_info2.close()
        flag = input("是否继续删除学习信息？y/n")


# 修改学生信息
# 输入学号后，查询到学生信息之后，对学生信息进行修改
def mod_info():
    flag = 'y'
    while flag == 'y' or flag == 'Y':
        n = 0  # 用以查无此人时的标记
        mod_id = input("请输入要修改的学生学号：")
        modfile_file1 = open('infile.txt', 'r')  # 以可读方式打开文件，读取到line_info中，每一行就是一个列表的元素
        line_info = modfile_file1.readlines()
        modfile_file2 = open('infile.txt', 'w')  # 用以写入修改后的数据
        for line in line_info:  # 遍历列表
            if mod_id in line:  # 如果修改的学生信息存在，就重新写入学生信息
                print("已找到学生，请修改信息！")
                mod_name = input("请输入姓名：")
                mod_score_eng = input("请输入英语成绩：")
                mod_score_py = input("请输入python成绩：")
                mod_score_math = input("请输入数学成绩：")
                mod_sum_score = int(mod_score_eng) + int(mod_score_py) + int(mod_score_math)
                mod_stu_info = mod_id + '\t' + mod_name + '\t' + mod_score_eng + '\t' + mod_score_py + '\t' + \
                               mod_score_math + '\t' + str(mod_sum_score) + '\n'
                modfile_file2.write(mod_stu_info)
                print("修改成功！！！")
                continue
            modfile_file2.write(line)  # 由于w方式打开的文件重新后会覆盖原有数据，所以需要将原有数据写入
            n = n + 1
        if n == len(line_info):
            print("无此学生信息，请核对后再操作！！！")
        else:
            print("学号为{0}的学生信息已修改！！！".format(mod_id))
        modfile_file1.close()
        modfile_file2.close()
        flag = input("是否继续修改学习信息？y/n")

# 显示学生信息
def show_info():
    print("学号", end='\t\t')
    print("姓名", end='\t')
    print("英语成绩", end='\t')
    print("Python成绩", end='\t')
    print("数学成绩", end='\t')
    print("总成绩", end='\t')
    print('\n')
    showfile_info = open('infile.txt', 'r')
    line_info = showfile_info.readlines()
    for line in line_info:  # 遍历列表，输出各个元素
        print(line)
    showfile_info.close()


def show_choose():
    print("==========================学生信息管理系统==========================")
    print()
    print("-----------------------------功能菜单------------------------------")
    print()
    print("                         1.录入学生信息")
    print("                         2.查找学生信息")
    print("                         3.删除学生信息")
    print("                         4.修改学生信息")
    print("                         5.显示学生信息")
    print("                         0.退出信息管理系统")
    print()
    print("------------------------------------------------------------------")


def main():
    show_choose()
    choose_menu = input("请选择：")
    while choose_menu != '0':
        if choose_menu == '1':
            input_info()
        if choose_menu == '2':
            find_info()
        if choose_menu == '3':
            del_info()
        if choose_menu == '4':
            mod_info()
        if choose_menu == '5':
            show_info()
        show_choose()
        choose_menu = input("请选择：")

    print("欢迎您再次使用！！！")

main()


# 1打印功能提示
def show():
    print('=' * 50)
    print('名片管理系统')
    print('1:添加一个新的名片')
    print('2:删除一个名片')
    print('3:修改一个名片')
    print('4:查询一个名片')
    print('5:显示所有的名片')
    print('6:退出系统')
    print('=' * 50)

if __name__ == '__main__':
    # 用来存储名片
    card_infors = []

    while True:
        show()
        # 2获取用户选择
        num = input('请输入操作序号:')
        if num.isdigit():
            num = int(num)
            if num == 1:
                new_name = input('请输入名字：')
                new_qq = input('请输入QQ：')
                new_weixin = input('请输入微信：')
                new_addr = input('请输入新的住址：')

                # 定义一个新的字典，用来存储一个新的名片
                new_infor = {}
                new_infor['name'] = new_name
                new_infor['qq'] = new_qq
                new_infor['weixin'] = new_weixin
                new_infor['addr'] = new_addr

                # 将一个字典，添加到列表中
                card_infors.append(new_infor)
                #print(card_infors)  # for test
            elif num == 2:
                del_name = input("请输入要删除的名字：")
                find_flag = False
                for line in card_infors:
                    if line['name'] == del_name:
                        find_flag = True
                        card_infors.remove(line)
                        break
                if find_flag:
                    print("已删除！")
                else:
                    print("输入的用户名不存在")
                    # print(card_infors)   for test
            elif num == 3:
                old_name = input('请输入要修改的姓名：')
                flag = 0
                for line in card_infors:
                    if line['name'] == old_name:
                        new_name = input('姓名:')
                        new_qq = input('QQ:')
                        new_weixin = input('微信:')
                        new_addr = input('住址:')

                        line['name'] = new_name
                        line['qq'] = new_qq
                        line['weixin'] = new_weixin
                        line['addr'] = new_addr
                        flag = True
                        break
                if flag:
                    print("已修改！")
                else:
                    print('输入的用户不存在！')
            elif num == 4:
                find_nmae = input("请输入要查找的姓名：")

                find_flag = 0  # 默认表示没有找到

                for temp in card_infors:
                    if find_nmae == temp['name']:
                        print('%s\t%s\t%s\t%s' % (temp['name'], temp['qq'], temp['weixin'], temp['addr']))
                        find_flag = 1  # 表示找到了
                        break

                # 判断是否找到
                if find_flag == 0:
                    print('没有找到')

            elif num == 5:
                print("姓名\tQQ\t微信\t住址\t")
                for temp in card_infors:
                    print('%s\t%s\t%s\t%s\t' % (temp['name'], temp['qq'], temp['weixin'], temp['addr']))
            elif num == 6:
                break
            else:
                print('输入有误！请重新输入')
                continue
            print('')
        else:
            print("输入错误，请重新输入！")
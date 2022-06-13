import time
class ParkManage(object):
    """创建一个关于停车的类"""
    def __init__(self, max_car=100, ):  # 定义最大停车辆数
        self.max_car = max_car
        self.car_list = []
        self.cur_car = len(self.car_list)
    def info(self):
        """ #显示系统功能信息"""
        print("""
     —————————————————————————
     |***欢迎进入车辆管理系统***|
     —————————————————————————
    {1}  
    {2} 1)添加车辆信息{3}{2}
    {0}  
    {2} 2)查询车辆信息{3}{2}
    {0}
    {2} 3)显示车辆信息{3}{2}
    {0}
    {2} 4)删除车辆{3}{2}
    {0}
    {2} 5)退出系统{3}{2}
    {1}
     """.format("-" * 40, "=" * 40, "|", " " * 16))
    def add_car(self, car):
        """#添加车辆信息"""
        entrance_time = time.ctime()
        car["entrance_time"] = entrance_time
        for Car in self.car_list:
            if Car.car_number == car.car_number:
                print("车牌号信息有误，重新输入")
                break
        else:
            self.car_list.append(car)
            print("车牌号为%s的车入库成功" % car.car_number)
    def search_By_Number(self):
        """#按车牌号查询"""
        car_number = input("请输入你您要查找的车牌号：")
        for car in self.car_list:
            if car.car_number == car_number:
                print(car)
                break
        else:
            print("未找到车牌号为%s的车辆" % car_number)
    def search_By_Model(self):
        """#按车型查询"""
        car_model = int(input("(小汽车:0,小卡：1，中卡：2，大卡：3)\n请输入您要查找的车型："))
        if car_model in [0, 1, 2, 3]:
            for car in self.car_list:
                if car_model == int(car.car_model):
                    print(car)
                else:
                    print("未找到相关车辆信息")
        else:
            print("输入有误，请重新输入")
    def searchCar(self):
        """#查找车辆信息"""
        print("""\n1)按车牌号查找\n2)按车型查找\n""")
        search_chioce = input("输入您要查找的方式：")
        if search_chioce == '1':
            self.search_By_Number()
        elif search_chioce == '2':
            self.search_By_Model()
        else:
            print("输入有误，请重新输入")
    def display(self):
        """#显示车车辆信息"""
        if len(self.car_list) != 0:
            for car in self.car_list:
                print(car)
        else:
            print("车库为空")
    def delete_car(self, car):
        """#删除车辆信息"""
        exit_time = time.ctime()
        car["exit_time"] = exit_time
        car.slot_card()
        self.car_list.remove(car)
        print("车牌号为%s的车两成功删除" % car.car_number)

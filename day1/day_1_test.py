import pickle
import os

basedir = os.path.dirname(os.path.abspath(__file__))

"""

龙腾测试dev课程，通讯录程序

实现一个简单的通讯录，包含增删改查

"""

class test:
    def read_record_list(self):
        try:
            with open(basedir+ '\\record_list.dat', "rb") as f:
                return pickle.load(f)
        except:
            with open(basedir + '\\record_list.dat', "wb") as f:
                pickle.dump([], f)
                print('没有文件，重新建立')
            with open(basedir+ '\\record_list.dat', "rb") as f:
                return pickle.load(f)
    def read_record_id(self):
        try:
            with open(basedir+ '\\record_id.dat', "rb") as f:
                return pickle.load(f)
        except:
            with open(basedir + '\\record_id.dat', "wb") as f:
                pickle.dump(0, f)
                print('没有文件，重新建立')
            with open(basedir+ '\\record_id.dat', "rb") as f:
                return pickle.load(f)
    def write_record_list(self,data):
        with open(basedir+ '\\record_list.dat', "wb+") as f:
            pickle.dump(data, f)
    def write_record_id(self,data):
        with open(basedir+ '\\record_id.dat', "wb+") as f:
            pickle.dump(data, f)

class Mail_list(test):

    record_list = test().read_record_list()
    record_id = test().read_record_id()

    def __init__(self,name=''):
        self.name = name

    def input_record(self):
        name = input("请输入姓名:")
        phone_number = input("请输入电话:")
        record = {"name": name, "phone_number": phone_number}
        return record

    #增
    def add_record(self):
        record= self.input_record()
        # global record_id
        Mail_list.record_id += 1
        record["record_id"] = self.record_id
        self.record_list.append(record)
        self.write_record_id(Mail_list.record_id)
        self.write_record_list(Mail_list.record_list)
        return "添加成功"

    #查
    def query_record(self):
        query_result = []
        query_ids = []
        for record in self.record_list:
            if record["name"] == self.name:
                query_ids.append(record["record_id"])
                query_result.append(record)
        return query_ids, query_result

    #删
    def delete_record(self):
        query_ids, query_result = self.query_record()
        if len(query_ids) == 0:
            print("不存在")
        else:
            if len(query_result) > 1:
                for record in query_result:
                    print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
                record_id = input("请选择要删除的id:")
                if int(record_id) in query_ids:
                    for record in self.record_list:
                        if int(record_id) == record["record_id"]:
                            self.record_list.remove(record)

                else:
                    print("输入错误!!!")
            else:
                print("{}\t{}\t{}".format(query_result[0]["record_id"], query_result[0]["name"], query_result[0]["phone_number"]))
                while True:
                    s = input("是否确认删除(Y/N):")
                    if s in ["Y", "N"]:
                        if s == "Y":
                            self.record_list.remove(query_result[0])

                        else:
                            pass
                        break
                    else:
                        print("输入错误!!!")
        self.write_record_id(Mail_list.record_id)
        self.write_record_list(Mail_list.record_list)
    #改
    def change_record(self):
        query_ids, query_result = self.query_record()
        if len(query_ids) == 0:
            print("不存在!!!")
        else:
            if len(query_result) > 1:
                for record in query_result:
                    print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
                record_id = input("请选择要修改的id:")
                if int(record_id) in query_ids:
                    for record in self.record_list:
                        if int(record_id) == record["record_id"]:
                            phone_number =input("请输入修改后的电话号码:")
                            record["phone_number"] = phone_number
                            print("修改成功")

                            break
                else:
                    print("输入错误!!!")
            else:
                print("{}\t{}\t{}".format(query_result[0]["record_id"],
                                          query_result[0]["name"], query_result[0]["phone_number"]))
                phone_number = input("请输入修改后的电话号码:")
                query_result[0]["phone_number"] = phone_number
                print("修改成功")
        self.write_record_id(Mail_list.record_id)
        self.write_record_list(Mail_list.record_list)


if __name__ == "__main__":




    while True:
        menu = """
               通讯录
               1. 添加
               2. 查找
               3. 删除
               4. 修改
               5. 退出
               """
        print(menu)
        s = input("请选择操作:")
        if s in ["1", "2", "3", "4", "5"]:
            if s == "1":
                msg = Mail_list().add_record()
                print(Mail_list().record_list)
                print(msg)

            if s == "2":
                name = input("请输入姓名:")
                query_ids, query_result = Mail_list(name).query_record()
                if len(query_ids) == 0:
                    print("不存在")
                else:
                    for record in query_result:
                        print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
            if s == "3":
                name = input("请输入姓名:")
                Mail_list(name).delete_record()

            if s == "4":
                name = input("请输入姓名:")
                Mail_list(name).change_record()
            if s == "5":
                break
        else:
            print("输入错误")
            continue



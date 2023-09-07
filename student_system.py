import  student

class StudentManagerSystem(object):
    def __init__(self):
        self.stu_dicts={}
    @staticmethod
    def show_menu():
        print('1.添加学生信息')
        print('2.删除学生')
        print('3.修改学生信息')
        print('4.查询单个学生信息')
        print('5.查询所有学生信息')
        print('6.退出系统')

    def insert_student(self):
        #1.获取信息

        stu_id=input('学号：')
        if stu_id in self.stu_dicts:
            print('该学生信息已存在')
            return
        name=input('名字：')
        age=input('年龄：')
        gender=input('性别：')
        #2.创建对象
        stu=student.Student(stu_id,name,age,gender)
        #3.添加
        self.stu_dicts[stu_id]=stu
    def remove_student(self):
        stu_id=input('请输入学号：')
        if stu_id in self.stu_dicts:
            del self.stu_dicts[stu_id]
            print('学生已经删除')
        else:
            print('学生信息不存在，无法删除')

    def modify_student(self):
        stu_id=input('请输入学号：')
        if stu_id in self.stu_dicts:
            stu=self.stu_dicts[stu_id]#字典[key]
            stu.age=input('请输入新的年龄：')
            stu.name=input('请输入新的名字：')
            stu.gender=input('请输入新的性别:')
            print('信息修改成功')
        else:
            print('学生信息不存在，无法修改')

    def save(self):
        f=open('student.txt','w',encoding='utf-8')
        for stu in self.stu_dicts.values():
            f.write(str(stu)+'\n')#调用student类的__str__方法
        f.close()
    def search_student(self):
        stu_id=input('学号：')
        if stu_id in self.stu_dicts:
            stu=self.stu_dicts[stu_id]
            print(stu)
        else:
            print('学生信息不存在！')
    def load_info(self):
        try:
            f=open('student.txt','r',encoding='utf-8')
            buf_list=f.readlines()
            for buf in buf_list:
                buf=buf.strip()
                info_list=buf.split(',')
                stu=student.Student(*info_list)
                stu_id=info_list[0]
                self.stu_dicts[stu_id]=stu
            f.close()
        except Exception:
            pass



    def show_all_info(self):
        for stu in self.stu_dicts.values():
            print(stu)

    def start(self):
        self.load_info()
        while True:
            self.show_menu()
            opt=input('请输入操作编号：')
            if opt=='1':
                self.insert_student()
            elif opt=='2':
                self.remove_student()
            elif opt=='3':
                self.modify_student()
            elif opt=='4':
                self.search_student()
            elif opt=='5':
                self.show_all_info()
            elif opt=='6':
                self.save()
                print('欢迎再次使用')
                break
            else:
                print('输入错误，请重试')
                continue

            input('输入回车键继续...')


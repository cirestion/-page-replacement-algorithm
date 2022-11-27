"""
class Memory:
    memory_queue    内存队列
    max             内存最大容量
    fill            是否满了

    def delete      删除
    def addition    添加
    def str         显示当前内存队列

    class Arithmetic:算法类
        def opt


class Access:
    access_queue    访问队列
    point           指向下次访问页

    def __init__    初始化访问队列
    def get_page    获取下一次访问页
    def point_add   指针后移
    def str         打印等待队列

class Page:
    def __init__
        # 记录页号
        self.num = num
        #下次访问
        self.nextAccess = nextAccess
        # 记录驻留时间
        self.time = time
    def str


"""
import random

class Access:
    point=0
    access_queue = []

    # 获取下次访问页面
    def get_page(self):
        try:
            return self.access_queue[self.point]
        except:
            return -1

    # 访问指针后移
    def point_add(self):
        self.point+=1

    def __str__(self):
        s = "等待队列\n| "
        for i in self.access_queue:
            s += "{} | ".format(i)
        return s

class Page:
    def __init__(self, num, time=0, next_access=999) -> None:
        # 记录页号
        self.num = num

        self.next_access = next_access
        # 记录驻留时间
        self.time = time

    # 设置下一跳距离
    def set_next(self,access):
        i=0
        for j in range(access.point,len(access.access_queue)):
            if self.num == access.access_queue[j].num:
                break
            i+=1
        self.next_access=i
        return i

    def __str__(self) -> str:
        s="{}".format(str(self.num))
        return s

class Memory:
    memory_queue=[]
    max = 3
    fill=False
    max_time_page = Page(-1,-999)
    dic = {-1:999}
    min_counter_page = Page(-1)


    def delete(self,page):
        self.memory_queue.remove(page)

    def addition(self,page):

        self.memory_queue.append(page)
        if len(self.memory_queue)== self.max:
            self.fill =True

    def __str__(self):
        if len(self.memory_queue)<self.max:
            return ''
        text.insert("end", "+" + "---+" * self.max + "\n")
        s = "| "
        for i in self.memory_queue:
            s += '{} | '.format(i)
        return s

    class Arithmetic:
        missing_page = 0
        def __init__(self,memory,access):
            self.memory = memory
            self.access = access

        # 设置并返回访问次数最少的页
        def counter(self,page):
            try:
                self.memory.dic[page.num]+=1
            except:
                self.memory.dic[page.num]=1
            self.memory.min_counter_page = Page(-1)
            for i in range(0,len(self.memory.memory_queue)):
                m_page = self.memory.memory_queue[i]
                # 如果内存中页的调用次数小于上次设定的页的调用最小次数
                if self.memory.dic[m_page.num] < self.memory.dic[self.memory.min_counter_page.num]:
                    self.memory.min_counter_page = m_page

        def opt(self):
            # 如果读完,即结束方法
            if self.access.get_page()  == -1:
                text.insert("end","{}\n".format(self.memory))
                text.insert("end","+"+"---+"*self.memory.max+"\n")
                text.insert("end","opt算法:缺页率{},缺页次数{},共置换{}次".format(self.missing_page/len(self.access.access_queue),self.missing_page,len(self.access.access_queue)))
                # 重置内存队列
                self.memory.memory_queue.clear()
                self.missing_page = 0
                self.access.point = 0
                self.missing_page = Page(-1, -999)
                return

            # 如果内存中有下一次访问的页
            for i in range(0,len(self.memory.memory_queue)):
                if self.access.get_page().num == self.memory.memory_queue[i].num:
                    text.insert("end", "{}\n".format(self.memory))
                    # print("内存有{}".format(self.access.get_page().num))
                    self.access.point_add()
                    return self.opt()

            # 如果满了
            if self.memory.fill:
                li = []
                text.insert("end","{}\n".format(self.memory))
                #求出下一次调用的距离最的
                for i in range(0,self.memory.max):
                    # 重设下次访问时间
                    next_step = self.memory.memory_queue[i].set_next(self.access)
                    li.append(next_step)
                max_next_step=max(li)
                max_next_page_index = li.index(max_next_step)
                max_next_page = self.memory.memory_queue[max_next_page_index]
                # 删除最长时间不用的页
                self.memory.delete(max_next_page)
                text.insert("end","下次访问缺页,移出{},添加{}\n".format(max_next_page.num,self.access.get_page()))
                # 增加缺页次数
                self.missing_page+=1
                # 移入内存
                self.memory.addition(self.access.get_page())
                # 等待队列指针后移
                self.access.point_add()
                return self.opt()
            else:
                # 如果没满
                self.memory.addition(self.access.get_page())
                self.missing_page+=1
            self.access.point_add()
            return self.opt()

        def fifo(self):
            if len(self.memory.memory_queue) >= self.memory.max:
                text.insert("end", "{}\n".format(self.memory))

            if self.access.get_page() == -1:
                text.insert("end","+"+"---+"*self.memory.max+"\n")
                text.insert("end","FIFO算法:缺页率{},缺页次数{},共置换{}次\n".format(self.missing_page/len(self.access.access_queue),self.missing_page,len(self.access.access_queue)))
                self.memory.memory_queue.clear()
                self.missing_page = 0
                self.access.point = 0
                self.missing_page = 0
                return

            # 如果内存有下一次访问的页
            for i in range(0,len(self.memory.memory_queue)):
                if self.access.get_page().num == self.memory.memory_queue[i].num:
                    self.access.point_add()
                    return self.fifo()

            # 如果满了
            if self.memory.fill:
                text.insert("end","下次访问缺页,移出{},添加{}\n".format(self.memory.memory_queue[0],self.access.get_page()))
                self.memory.memory_queue.pop(0)
                self.memory.addition(self.access.get_page())
                self.access.point_add()
                self.missing_page+=1
                return self.fifo()
            else:
                # 如果没满
                self.memory.addition(self.access.get_page())
                self.access.point_add()
                self.missing_page+=1
            return self.fifo()

        def lru(self):
            if len(self.memory.memory_queue) >= self.memory.max:
                text.insert("end", "{}\n".format(self.memory))

            if self.access.get_page() == -1:
                text.insert("end","+"+"---+"*self.memory.max+"\n")
                text.insert("end", "LRU算法:缺页率{},缺页次数{},共置换{}次\n".format(self.missing_page/len(self.access.access_queue),self.missing_page,len(self.access.access_queue)))
                # 重置内存
                self.memory.memory_queue.clear()
                self.missing_page=0
                self.access.point=0
                self.missing_page=Page(-1,-999)
                return

            self.memory.max_time_page=Page(-1,-999)
            # 内存所有页访问时间加1
            for  i in range(0,len(self.memory.memory_queue)):
                self.memory.memory_queue[i].time+=1
                # 找出上次访问时间最长的
                if self.memory.max_time_page.time < self.memory.memory_queue[i].time:
                    self.memory.max_time_page = self.memory.memory_queue[i]

            # 如果内存中有访问的页
            for i in range(0,len(self.memory.memory_queue)):
                if self.access.get_page().num == self.memory.memory_queue[i].num:
                    # print("访问{},重置其上次访问时间".format(self.access.get_page().num))
                    self.memory.memory_queue[i].time=0
                    self.access.point_add()
                    return self.lru()

            # 如果内存满了
            if self.memory.fill:
                self.memory.delete(self.memory.max_time_page)
                self.memory.addition(self.access.get_page())
                text.insert("end","下次访问缺页,移出{},添加{}\n".format(self.memory.memory_queue[0],self.access.get_page()))
                self.access.point_add()
                self.missing_page+=1
                return self.lru()
            else:
                #如果内存没满
                self.memory.addition(self.access.get_page())
                self.access.point_add()
                self.missing_page+=1
            return self.lru()

        def lfu(self):
            if len(self.memory.memory_queue) >= self.memory.max:
                text.insert("end", "{}\n".format(self.memory))

            # 如果读完,即结束方法
            if self.access.get_page() == -1:
                text.insert("end","+"+"---+"*self.memory.max+"\n")
                text.insert("end","LFU算法:缺页率{},缺页次数{},共置换{}次\n".format(
                    self.missing_page / len(self.access.access_queue),
                    self.missing_page, len(self.access.access_queue)))

                # 重置内存
                self.memory.memory_queue.clear()
                self.missing_page = 0
                self.access.point = 0
                return

            self.counter(self.access.get_page())
            # 如果内存中有访问的页
            for i in range(0, len(self.memory.memory_queue)):
                if self.access.get_page().num == self.memory.memory_queue[i].num:
                    self.access.point_add()
                    return self.lfu()

            # 如果内存满了
            if self.memory.fill:
                self.memory.delete(self.memory.min_counter_page)
                self.memory.addition(self.access.get_page())
                text.insert("end","下次访问缺页,移出{},添加{}\n".format(self.memory.min_counter_page.num, self.access.get_page()))
                self.access.point_add()
                self.missing_page += 1
                return self.lfu()
            else:
                # 如果内存没满
                self.memory.addition(self.access.get_page())
                self.access.point_add()
            return self.lfu()





if __name__ == '__main__':
    import tkinter
    from tkinter import *
    from tkinter import ttk  # 导入ttk模块，下拉菜单控件位于ttk子模块中
    from tkinter.messagebox import showerror
    global text
    global dir
    dir = {"sf": "OPT", "size": 4}
    # 创建窗口
    win = tkinter.Tk()
    win.title("王建军,20220310629")
    win.geometry('1000x500')
    win.resizable(False, False)  # 横纵均不允许调整
    value = StringVar()
    value.set('OPT')
    # 选择算法
    combobox1 = ttk.Combobox(
        master=win,  # 父容器
        height=10,  # 高度,下拉显示的条目数量
        width=10,  # 宽度
        state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
        cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
        font=('', 16),  # 字体
        textvariable=value,  # 通过StringVar设置可改变的值
        values=["OPT", "FIFO", "LRU", "LFU"],  # 设置下拉框的选项
    )
    # 编写回调函数，绑定执行事件,向文本插入选中文本
    def func1(event):
        dir['sf'] = combobox1.get()
    # 绑定下拉菜单事件
    combobox1.bind("<<ComboboxSelected>>", func1)
    combobox1.place(relx=0.1, rely=0.1)
    value2 = StringVar()
    value2.set('4')
    combobox2 = ttk.Combobox(
        master=win,  # 父容器
        height=10,  # 高度,下拉显示的条目数量
        width=10,  # 宽度
        state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
        cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
        font=('', 16),  # 字体
        textvariable=value2,  # 通过StringVar设置可改变的值
        values=["3", "4", "5", "6","7"],  # 设置下拉框的选项
    )
    # 编写回调函数，绑定执行事件,向文本插入选中文本
    def func2(event):
        dir['size'] = int(combobox2.get())

    # 绑定下拉菜单事件
    combobox2.bind("<<ComboboxSelected>>", func2)
    combobox2.place(relx=0.1, rely=0.3)
    entry1 = ttk.Entry(win)

    # 创建动字符串
    Dy_String = tkinter.StringVar()
    # 放置输入框，并设置位置
    entry1 = ttk.Entry(win)
    # 插入默认文本
    entry1.place(relx=0.1, rely=0.2)
    entry1.insert(0, '9765300919047561')
    # 得到输入框字符串
    print(entry1.get())

    # 确认事件
    def click():
        # 如果不是数字
        if not entry1.get().isnumeric():
            showerror(title="错误",
                      message="等待序列应为纯数字!")
            return
        #修改配置
        dir["queue"] = entry1.get()
        list_=[]
        list_sz=[]
        for i in dir["queue"]:
            list_.append(Page(int(i)))
            list_sz.append(i)
        Access.access_queue=list_
        Memory.max=dir["size"]
        ari = dir['sf']
        if len(set(list_sz)) <= Memory.max-1:
            showerror(title="错误",
                      message="再来点不一样的页吧,现在连内存都装不满")
            return

        print(dir)
        m=Memory()
        m_ = m.Arithmetic(m, Access())
        text.delete("1.0","end")
        text.insert("end", "等待序列: "+str(dir["queue"])+"\n\n")

        if ari == 'OPT':
            m_.opt()
        elif ari == 'FIFO':
            m_.fifo()
        elif ari == 'LRU':
            m_.lru()
        elif ari == 'LFU':
            m_.lfu()
    tkinter.Button(win, text='开始', width=20, command=click).place(relx=0.1, rely=0.4)
    text=Text(win, width=50, height=30, undo=True, autoseparators=False)
    text.place(relx=0.25, rely=0.1)
    tkinter.Label(win, text="选择算法:", font=('宋体', 12), width=10, height=1).place(relx=0.0, rely=0.1)
    tkinter.Label(win, text="等待序列:", font=('宋体', 12), width=10, height=1).place(relx=0.0, rely=0.2)
    tkinter.Label(win, text="内存大小:", font=('宋体',   12), width=10, height=1).place(relx=0.0, rely=0.3)
    tkinter.Label(win, text="1:等待序列只可填入0-9   \n"
                            "2:内存大小需小于页的个数",
                  font=('宋体', 12), width=30, height=10).place(relx=0.61, rely=0.1)
    win.mainloop()

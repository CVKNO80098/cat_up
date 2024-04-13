class ConfTools:
    def __init__(self):
        self.__name_list = []
        self.__ignore_list = []
        if self.__test_file_exist("conf", 1):
            open("conf", "w").close()
        if self.__test_file_exist("igconf", 2):
            open("igconf", "w").close()

    def using_ignore_list(self, file_list):
        """
        应用忽视的文件于当前文件列表
        :return: list<str>: 文件列表
        """
        result = []
        for i in file_list:
            if i not in self.__ignore_list:
                result.append(i)
        return list(result)

    def search(self, file_list):
        """
        查询文件列表中文件分类
        :param file_list: 输入用于对比目标列表的文件列表
        :return: list[submitted, unsubmitted, undefined]
        """
        submitted = []
        unsubmitted = []
        define = []

        for i in self.__name_list:
            for j in file_list:
                if i in j:
                    submitted.append(i)
                    define.append(j)

        unsubmitted = self.diff_two_list(self.diff_two_list(self.__name_list, submitted), unsubmitted)
        undefined = self.diff_two_list(self.diff_two_list(file_list, submitted), define)

        return [submitted, unsubmitted, undefined]

    def get_name_list(self):
        return self.__name_list

    def get_ignore_list(self):
        return self.__ignore_list

    def __test_file_exist(self, file_name, fun_type):
        """
                检测文件是否存在,并初始化忽略与人员名单
                :param file_name: 文件名
                :param fun_type: 值为1时conf的检测并赋值，2为igconf的检测并赋值
                :return: bool
        """
        try:
            if fun_type == 1:
                with open(file_name, 'r', encoding='utf-8') as self.__conf_file:
                    line = self.__conf_file.readline().strip()
                    while line:
                        self.__name_list.append(self.__del_cr(line))
                        line = self.__conf_file.readline().strip()
            elif fun_type == 2:
                with open(file_name, 'r', encoding='utf-8') as self.__ignore_file:
                    line = self.__ignore_file.readline().strip()
                    while line:
                        self.__ignore_list.append(self.__del_cr(line))
                        line = self.__ignore_file.readline().strip()
            return False
        except FileNotFoundError:
            print(f'"{file_name}"文件未发现！正在创建文件，程序将退出，请注意修改')
            return True

    @staticmethod
    def diff_two_list(list1, list2):
        return list(set(list1) - set(list2))

    @staticmethod
    def __del_cr(string):
        """
        清除回车的
        :param string:
        :return: string:
        """
        result = []
        if not string:
            return False
        for i in string:
            if i != '\n':
                result.append(i)
        return "".join(result)

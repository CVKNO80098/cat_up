import os


class DirTools:
    def __init__(self, base_dir=os.getcwd()):
        # 默认为当前文件夹
        self.__files = os.listdir(base_dir)
        self.__unsubmitted_list = self.__files[:]

    def __add__(self, user_str):
        # 现在用不上，但是以后应该能用上，比如自动配置conf文件
        self.__files.append(user_str)

    def ignoring_file_list(self, file_list):
        """
        确认应用配置（忽略文件的），返回布尔值，删去本类中需要忽视的文件名单
        :param file_list:
        :return: bool
        """
        for file in file_list:
            if file in self.__files:
                self.__files.remove(file)

        __unsubmitted_list = self.__files[:]
        return True

    def get_unsubmitted_list(self):
        return self.__unsubmitted_list

    def get_files(self):
        return self.__files

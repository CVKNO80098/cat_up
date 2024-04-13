import os


class DirTools:
    def __init__(self, base_dir=os.getcwd()):
        self.__files = os.listdir(base_dir)
        self.__unsubmitted_list = self.__files[:]

    def __add__(self, user_str):
        self.__files.append(user_str)

    def ignoring_file_list(self, file_list):
        for file in file_list:
            if file in self.__files:
                self.__files.remove(file)

        __unsubmitted_list = self.__files[:]
        return True

    def searching_for_files(self, file_list):
        for file in file_list:
            if file in self.__unsubmitted_list:
                self.__unsubmitted_list.remove(file)

        return True

    def get_unsubmitted_list(self):
        return self.__unsubmitted_list

    def get_files(self):
        return self.__files

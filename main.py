"""

"""
import DirTools
import ConfTools
from colorama import Fore


def format_print(data):
    """
    Formats data for printing
    :param data:
    :return:
    """
    for i in range(len(data)):
        if i % 7 == 0:
            print("")  # 换行用的哈哈哈哈哈哈
        print(Fore.RESET, "{:>3s}".format(data[i]), end='\t')


if __name__ == '__main__':
    # class初始化一下
    conftools = ConfTools.ConfTools()
    dirtools = DirTools.DirTools(r"C:\Users\qc275\Desktop\Python作业")

    # 获取一下基本数据
    name_list = conftools.get_name_list()
    dir_list = dirtools.get_files()

    # 排除一下应该忽视的文件
    dir_list = conftools.using_ignore_list(dir_list)

    # 进行检查
    sub, unsub, undefined = conftools.search(dir_list)

    # 格式化输出
    print(Fore.LIGHTGREEN_EX, f"已交{len(sub)}人：")
    format_print(sub)

    print(Fore.LIGHTRED_EX, f"\n\n未交{len(unsub)}人：")
    format_print(unsub)

    print(Fore.LIGHTYELLOW_EX, f"\n\n共{len(unsub) + len(sub)}人\n")
    if len(undefined) > 0:
        user_input = input(Fore.LIGHTBLUE_EX + f"出现了{len(undefined)}个未定义文件，是否显示（y/n）：")
        format_print(undefined)
        print("\n")
    else:
        exit(0)

import DirTools
import ConfTools
from colorama import Fore

if __name__ == '__main__':
    # class初始化一下
    conftools = ConfTools.ConfTools()
    dirtools = DirTools.DirTools()

    # 获取一下基本数据
    name_list = conftools.get_name_list()
    dir_list = dirtools.get_files()

    # 排除一下应该忽视的文件
    dir_list = conftools.using_ignore_list(dir_list)

    # 进行检查
    sub, unsub, undefined = conftools.search(dir_list)

    # 格式化输出
    print(Fore.LIGHTGREEN_EX, f"已交{len(sub)}人：\n")
    for i in range(len(sub)):
        if i % 5 == 4:
            print("")  # 换行用的哈哈哈哈哈哈
        print("{:>3s}".format(sub[i]), end='\t')

    print(Fore.LIGHTRED_EX, f"\n\n未交{len(unsub)}人：\n")
    for i in range(len(unsub)):
        if i % 5 == 4:
            print("")  # 能跑就行
        print("{:>3s}".format(unsub[i]), end='\t')

    print(Fore.LIGHTYELLOW_EX, f"\n\n共{len(unsub)+len(sub)}人")
    if len(undefined) > 0:
        user_input = input(Fore.LIGHTBLUE_EX + f"\n\n出现了{len(undefined)}个未定义文件，是否显示（y/n）：")
        if user_input == "y":
            for i in range(len(undefined)):
                if i >= 5:
                    print("\n")
                print(undefined[i])
        else:
            exit(0)

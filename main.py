import DirTools
import ConfTools

if __name__ == '__main__':
    conftools = ConfTools.ConfTools()
    dirtools = DirTools.DirTools()

    name_list = conftools.get_name_list()
    dir_list = dirtools.get_files()

    dir_list = conftools.using_ignore_list(dir_list)

    sub, unsub, undefined = conftools.search(dir_list)

    print(sub, unsub, undefined)

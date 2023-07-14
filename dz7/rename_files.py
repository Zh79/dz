import pathlib
import os


def renameF(path, nname, oex, nex):
    """
    :param path:  путь к каталогу в котором нужно изменить имена и расширения, и в подкатологах тоже
    :param nname: новое имя файлов
    :param oex: старое расширение файлов
    :param nex: новое расширение файлов
    """
    allfiles = list(pathlib.Path(f"{path}").rglob("*"))
    count = 0
    for i in allfiles:
        if pathlib.Path(i).suffix == oex:
            oname = str(i).split('\\')[-1]
            print(oname)
            os.rename(i, f"{path}\\{oname}_{nname}_{count}{nex}")
            count += 1


from folderfolder import FF


def ex0():
    # Parsing and viewing folder structures
    start = "/home/niflheim/asbra/Work/ffpres/testfolder"
    ff = FF(path=start)
    print(ff)


def ex1():
    # Selecting specific files
    start = "/home/niflheim2/cmr/C2DB/BN"
    def file_filter(fobj):
        fname = str(fobj)
        return "g0w0.txt" in fname

    ff = FF(path=start, file_filter=file_filter)
    print(ff.count_files())


def ex2():
    # Selecting specific folders
    start = "/home/niflheim2/cmr/C2DB/BN"
    def folder_filter(fobjs):
        has_phon = any("phonons" in str(x) for x in fobjs)
        has_gw = any("g0w0" in str(x) for x in fobjs)
        return has_phon and has_gw

    ff = FF(path=start, folder_filter=folder_filter)

    print(ff.count_files())

        
def ex3():
    # Selecting specific folders and only certain files
    start = "/home/niflheim2/cmr/C2DB/BN"
    def folder_filter(fobjs):
        has_phon = any("phonons" in str(x) for x in fobjs)
        has_gw = any("g0w0" in str(x) for x in fobjs)
        return has_phon and has_gw

    def file_filter(fobj):
        fname = str(fobj)
        return "gs_gw_nowfs.gpw" in fname

    ff = FF(path=start, folder_filter=folder_filter, file_filter=file_filter)

    print(ff.count_files())
        

def ex4():
    # Mapping over files
    start = "/home/niflheim2/cmr/C2DB/BN"
    def folder_filter(fobjs):
        has_phon = any("phonons" in str(x) for x in fobjs)
        has_gw = any("g0w0" in str(x) for x in fobjs)
        return has_phon and has_gw

    def file_filter(fobj):
        fname = str(fobj)
        return "g0w0.txt" in fname

    ff = FF(path=start, folder_filter=folder_filter, file_filter=file_filter)

    def mapper(fobj):
        with open(fobj, "r") as f:
            data = f.read()
        print(data[:63])

    ff.map_files(mapper)


def splitter(string):
    return string.split("/")[-1]

def ex5():
    # Mapping over folders
    start = "/home/niflheim2/cmr/C2DB/BN"
    def folder_filter(fobjs):
        has_phon = any("phonons" in str(x) for x in fobjs)
        has_gw = any("g0w0" in str(x) for x in fobjs)
        return has_phon and has_gw

    def file_filter(fobj):
        fname = str(fobj)
        return "g0w0.txt" in fname or "phonons.done" in fname

    ff = FF(path=start, folder_filter=folder_filter, file_filter=file_filter)

    def mapper(fobjs):
        msg = "--".join(splitter(str(x)) for x in fobjs)
        print(msg)
        

    ff.map_folders(mapper)    


def ex5a():
    # Mapping over folders
    start = "/home/niflheim2/cmr/C2DB/BN"
    def folder_filter(fobjs):
        has_phon = any("phonons" in str(x) for x in fobjs)
        phon_notdone = not any("phonons.done" in str(x) for x in fobjs)
        has_gw = any("g0w0" in str(x) for x in fobjs)
        return has_phon and has_gw and phon_notdone

    def file_filter(fobj):
        fname = str(fobj)
        return "g0w0.txt" in fname

    ff = FF(path=start, folder_filter=folder_filter, file_filter=file_filter)

    def mapper(fobj):
        print("/".join(str(fobj).split("/")[:-1]))
        
    ff.map_files(mapper)


def ex6():
    # Folding over the structure
    start = "/home/niflheim2/cmr/C2DB/MoSSe"
    def folder_filter(fobjs):
        return any("em_circle" in str(x) for x in fobjs)

    def file_filter(fobj):
        fname = str(fobj)
        return "gs.gpw" in fname

    ff = FF(path=start, folder_filter=folder_filter, file_filter=file_filter)

    def print_six(acc, fobjs):
        if acc >= 6:
            return acc
        else:
            if len(fobjs) > 0:
                print("/".join(str(fobjs[0]).split("/")[-3:]))
                return acc + 1
            else:
                return acc

    ff.fold(print_six, 0)


def ex7():
    # Copying a folder structure
    start = "./testfolder"
    ff = FF(path=start)

    def rename_fct(fname):
        return "PREFIX" + fname
        

    ff.copy_folders(destination="./copyfolder", rename_fct=rename_fct)


if __name__ == "__main__":
    ex7()
    

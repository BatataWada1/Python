from os import getcwd
import os.path
from os import path
class Count_dir:

    def __init__(self,path):
        self.path = path

    def setup(self):
        """
        setup() :- This function do setup work for the program
        """
        count = 0
        lsit = []
                
    def dir_count(self):
        """
        file_count() : Retrun the count of the directory present in the specified path
        """
        self.setup()
        os.chdir(self.path)
        lsit = [i for i in (os.listdir()) if(path.isdir(i))]
        count = len(lsit)
        return (lsit,count)

    def file_count(self):
        """
        file_count(): Return the count of the file present in the specified path
        """
        self.setup()
        os.chdir(self.path)
        lsit = [ i for i in os.listdir() if(path.isfile(i)) ]
        count = len(lsit)
        return(lsit, count)

    def pdf_file(self):
        """
        pdf_file(): Return the count of MSDOC files present in the specified Path
        """
        self.setup()
        os.chdir(self.path)
        lsit = [ i for i in os.listdir() if (path.isfile(i) and i.endswith("docx") )  ]
        count = len(lsit)
        return(lsit, count)

userpath = input("Enter valid path: ")


if path.exists(userpath):
    cntobj = Count_dir(userpath)
    list1,count = cntobj.dir_count()
    print("No of directories present in {0} : {1}, {2} ".format(userpath, count, list1) )
    list1, count = cntobj.file_count()
    print("No of files present in {0} : {1}, {2} ".format(userpath, count, list1) )
    list1, count = cntobj.pdf_file()
    print("No of MSDOC files present in {0} : {1}, {2} ".format(userpath, count, list1) )
else:
    print ("Path Not Found "+str(path.exists(userpath)))



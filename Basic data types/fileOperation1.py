# File I/O

#File is name location on disk to store information
#Python has the built-in- function
"""
open():- retruns file object, also called handle.

Default reading is in text mode

mode:-

1) 'r' :- Open file for reading. (default)
2) 'w' :- Open file for writing. Create new file if not exist or truncate the existing file
3) 'x' :- Open a file for exclusive creation. If the file already exists, operation fails
4) 'a' :- Open file for appending at EOF. create new file if not exist
5) 't' :- Open file in text mode(default)
6) 'b' :- Open file in binary mode
7) '+' :- Open file for updating(reading and writing)

methods:-
1) close() :- Close an open file.It has no effect if file is already exist.
2) detach() :- Separate the underlying binary buffer from the TextIOBase and return it.
3) fileno() :- retrun an integer number (file descriptor) of the file
4) flush() :- Flush the write buffer of the file system
5) isatty() :- Retrun True if file stream is interactive
6) read(n) :- Read atmost n characters from the file. Reads till EOF if it is negative or non.
7) readable():- Return True if the file stream can be read from
8) readline(n = -1):- Read and return one line from file
9) readlines(n = -1):- Read and return a list of lines from the file
10) seek(offset, from=SEEK_SET) :- Change file position to offset bytes, in reference to "from" (start,current,end)
11) seekable() :- retrun true if file stream support random access
12) tell() :- retrun the current file location
13) truncate(size = None) :- Resize the file stream to "size" bytes. if "size" is not specified, resize to current location
14) writable() :- Return True if the file stream can be written to
15) wrtie(s) :- Write string "s" to the file and retrun the number of characters retrun
16) writelines(lines):- Write list of lines to the file.

"""

fileHandler = open(r"D:\Python\abc.txt", mode='a', encoding='UTF-8')
fileHandler.close()



#try:
#    fileHandler = open(r"D:\Python\x.txt", mode='r', encoding='UTF-8')
#finally:
#    fileHandler.close()

with  open(r"D:\Python\x.txt",mode='w', encoding='utf-8') as fileHandler:
    pass

f = open(__file__, 'a+', encoding='utf-8') 
print(f.closed) 
print(f.encoding) 
print(f.mode) 
print(f.newlines) 
print(f.softspace) 

print('hlo'); str2= 'mandaar' ; str1 = 'kej'; print(str2, str1)
import os
import os.path
print(os.getcwd())
for i in os.listdir():
    if i.endswith(".txt"):
        os.remove(i)

 

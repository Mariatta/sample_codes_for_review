"""
This is a sample code
Do not use
"""


import os

def do_delete_file(filename):
    """
    Delete the file
    """
    os.system("/bin/rm -rf %s" % filename)
    
def change_sys_dir(target_dir):
    """
    cd to the dir
    """
    os.system("cd %s" % target_dir)
     
if __name__ == '__main__':
    change_sys_dir("./some_strange_path")
    do_delete_file("somefile.txt")
    
    

"""
This is a sample code
Do not use
"""


import os

def do_delete_file(filename):
    """
    Delete the file
    """
    os.system("/bin/rm -rf {0}".format(filename))
    
def change_sys_dir(target_dir):
    """
    cd to the dir
    """
    os.system("cd {0}".format(target_dir))
     
if __name__ == '__main__':
    change_sys_dir("./some_strange_path")
    do_delete_file("somefile.txt")
    
    

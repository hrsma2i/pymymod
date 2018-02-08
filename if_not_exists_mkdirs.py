import os

def if_not_exists_mkdirs(dir_, verbose=True):
    if not os.path.exists(dir_):
        if verbose:
            print("mkdir", dir_)
        os.makedirs(dir_)
    
    

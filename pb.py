"""
clipboad read/write
"""
from subprocess import Popen

def read():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    return p.communicate()[0]
    
def write(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.communicate(data)

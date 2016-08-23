
"""
Created on Mon Aug 22 19:51:38 2016

@author: fs, copied from another source and modified
"""

import os
from path import path

SOURCE_DIRECTORY = '/Users/fs/BBId/img_dr'  
DEST_DIRECTORY = '/Users/fs/BBId/testdir'  # Destination directory

d = path(SOURCE_DIRECTORY)
dest_directory = path(DEST_DIRECTORY)

def transform():
    print "Transforming files from %s to %s" % (d, dest_directory)
    file_count = 0
    for i in d.walk():
        if i.isfile() and i.endswith('jpg'):
            file_count += 1
            print "Transforming %s" % i

# ***  between this comment and the one below is the place we place our transformation code

            i.copy(dest_directory)

# ***

    print 'Transformed %s files' % file_count


if __name__ == "__main__":
    transform()

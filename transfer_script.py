
"""
Created on Mon Aug 22 19:51:38 2016

@author: fs, copied from another source and modified
"""

import os
from path import path

DIRECTORY = '/Users/fs/BBId/img_dr'                  # source Directory
COPY_DIRECTORY = '/Users/fs/BBId/testdir'  # Destination directory

d = path(DIRECTORY)
copy_directory = path(COPY_DIRECTORY)

def transform():
    print "Copying Files from %s to %s" % (d, copy_directory)
    file_count = 0
    for i in d.walk():
        if i.isfile() and i.endswith('jpg'):
            file_count += 1
            print "Copying %s" % i

# ***  between this comment and the one below is the place we place our transformation code

            i.copy(copy_directory)

# ***

    print 'Transformed %s files' % file_count


if __name__ == "__main__":
    transform()

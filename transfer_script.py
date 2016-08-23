# -*- coding: utf-8 -*-
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


def transfer():
    print "Copying Files from %s to %s" % (d, copy_directory)
    file_count = 0
    for i in d.walk():
        if i.isfile() and i.endswith('jpg'):
            file_count += 1
            print "Copying %s" % i
            i.copy(copy_directory)

    print 'Transferred %s files' % file_count


if __name__ == "__main__":
    transfer()
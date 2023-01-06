import pytest
#
import sys
sys.path.append("..")
from ps1 import SystemDriveFinder

from Level6.db1connect import FileSearcher

class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual='C'
        assert self.expected==self.actual

    def test_searchfile(self):
        obj=FileSearcher()
        d=obj.task2('C:\\','one.txt')
        print(d)
        self.expected_filename=d
        self.actual_res='C:\\capstone\\one.txt'
        assert self.expected_filename==self.actual_res


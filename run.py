#coding=utf-8
__author__ = 'messageoom'

import time
import unittest
import HTMLTestRunner

def run():
    test_dir = './mCase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

    #指定生成报告的路径
    filePath = "./report/MsAutoTestResult.html"
    fp = file(filePath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='MsStock Test Report',description='This  is MsStock Test  Report')
    runner.run(suite)

if __name__ == "__main__":
    run()
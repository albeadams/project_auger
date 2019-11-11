'''
	Interface ot an Excel workbook that provides GUI to non-technical;
	The Excel workbook requires xlwings installed in the workbook and pip
'''
import xlwings as xw
import numpy as np

def testhelp():
	wb = xw.Book.caller()
	wb.sheets('Help').range('b4').value = 'This is the explanation'
from datamax_printer import DPLPrinter

print('---')
import os, sys
import win32print
import win32con

printer_name = win32print.GetDefaultPrinter()
#
# raw_data could equally be raw PCL/PS read from
#  some print-to-file operation
# #
# if sys.version_info >= (3,):
#     raw_data = bytes("This is a test", "utf-8")
# else:
#     raw_data = "This is a test"
#
# hPrinter = win32print.OpenPrinter(printer_name)
# try:
#     hJob = win32print.StartDocPrinter(hPrinter, 1, ("test of raw data", None, "RAW"))
#     try:
#         win32print.StartPagePrinter(hPrinter)
#         win32print.WritePrinter(hPrinter, raw_data)
#         win32print.EndPagePrinter(hPrinter)
#     finally:
#         win32print.EndDocPrinter(hPrinter)
# finally:
#     win32print.ClosePrinter(hPrinter)

# exit()
import win32ui as w


def start_document():
    doc = w.CreateDC()
    doc.CreatePrinterDC()
    doc.StartDoc('My Python Document')
    return doc


text = """
Батика premium brew 1 \n
Батика premium brew 10 \n
Батика premium brew 100 \n
Батика premium brew 1000 \n
Батика premium brew 1000 \n

"""


def getfontsize(dc, PointSize):
    inch_y = dc.GetDeviceCaps(win32con.LOGPIXELSY)
    return int(-(PointSize * inch_y) / 72)


dc = start_document()
fontsize = getfontsize(dc, 15)
fontdata = {'name': 'Consolas', 'height': fontsize}
font = w.CreateFont(fontdata)
dc.SelectObject(font)

dc.StartPage()
dc.TextOut(80, 40, 'Заказ: 198')

fontsize = getfontsize(dc, 8)
fontdata = {'name': 'Consolas', 'height': fontsize}
font = w.CreateFont(fontdata)
dc.SelectObject(font)

dc.TextOut(80, 100, 'Батика premium 10')
dc.TextOut(80, 130, 'Батика premium 20')
dc.TextOut(80, 160, 'Батика premium 30')

# dc.MoveTo(100, 100)
# dc.TextOut(100, 200, text)

# dc.LineTo(500, 102)
dc.EndPage()
dc.EndDoc()
#


# from win32 import win32ui
# printer = DPLPrinter('127.0.0.1')
# printer.configure()
# printer.start_document()
# # printer.set_qr_code(285, 120, 'https://www.innetag.ch/', 9)
# printer.set_label(300, 60, 'innetag.ch', 9, 10)
# printer.print()

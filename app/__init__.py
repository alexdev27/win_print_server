import win32con
import win32ui as w


def start_document():
    doc = w.CreateDC()
    doc.CreatePrinterDC()
    doc.StartDoc('My Python Document')
    return doc


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

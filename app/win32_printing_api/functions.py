import win32con
import win32ui as w


def start_document():
    doc = w.CreateDC()
    doc.CreatePrinterDC()
    doc.StartDoc('My Python Document')
    doc.StartPage()
    return doc


def attach_text(doc, x_offset=80, y_offset=40, text=''):
    """ y_offset - offset from the top of the page.
        x_offset - offset from the left of the page """
    # doc.TextOut(80, 130, 'Батика premium 20')
    doc.TextOut(x_offset, y_offset, text)


def end_document(doc):
    doc.EndPage()
    doc.EndDoc()


def _getfontsize(dc, desired_font_size: int):
    inch_y = dc.GetDeviceCaps(win32con.LOGPIXELSY)
    return int(-(desired_font_size * inch_y) / 72)


def apply_font(doc_obj, font_name, font_size):
    fz = _getfontsize(doc_obj, font_size)
    font_data = {'name': font_name, 'height': fz}
    font_obj = w.CreateFont(font_data)
    doc_obj.SelectObject(font_obj)

from app.win32_printing_api.functions import start_document, apply_font, attach_text, end_document

MAX_ACCEPTABLE_CHARS = 36
NORMAL_X_OFFSET = 90
CUSTOM_X_OFFSET = 130
START_Y_OFFSET = 100
INCREMENTAL_Y_OFFSET = 30


arr = [
    'Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться.',
    'Lorem Ipsum используют потому, что',
    'тот обеспечивает более или менее стандартное заполнение шаблона, '
]


def print_steakhouse_order(data):
    # # print(data)
    order_line = data.pop(0)
    doc = start_document()
    # # header of the order
    apply_font(doc, 'Consolas', 12)
    attach_text(doc, text=order_line)
    # # another information
    apply_font(doc, 'Consolas', 9)
    _process_strings(data, doc)
    end_document(doc)


def _split_long_string(num_chars: int, string: str):
    result = []
    is_need_offset = False
    _str = string[:]
    while bool(_str):
        part = _str[:num_chars]
        result.append((is_need_offset, part))
        if not is_need_offset:
            is_need_offset = True
        _str = _str[num_chars:]
    return result


def _process_strings(strings, doc):
    y_offset = START_Y_OFFSET

    for _str in strings:
        ready_strings = _split_long_string(MAX_ACCEPTABLE_CHARS, _str)
        for num, val in enumerate(ready_strings, 1):
            is_need_offset = val[0]
            string = val[1]
            x_offset = CUSTOM_X_OFFSET if is_need_offset else NORMAL_X_OFFSET
            attach_text(doc, x_offset, y_offset, string)
            y_offset += INCREMENTAL_Y_OFFSET

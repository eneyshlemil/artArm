import pytesseract as tess
from PIL import Image


# получить первый обработанный элемент
def get_first_prepared(row: list) -> list:
    return row.pop(0).split(' ')


# получить последний обработанный элемент
def get_last_prepared(row: list) -> list:
    return row.pop().split(' ')


# склеивание строки
def glue(row: list) -> str:
    return ' '.join(row)


# подготовка теста для дальнейшего преобразования
def prepare_bars(image_name: str) -> list:
    config = r'--oem 3 --psm 6'
    read_text = tess.image_to_string(Image.open(image_name), lang='rus+eng', config=config)

    return list(filter(lambda x: x != '', read_text.split('\n')))

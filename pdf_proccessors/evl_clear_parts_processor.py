import copy
import os.path

from PyPDF2 import PdfFileWriter, PdfFileReader

'''
шапка находится на высоте 142 пикселя сверху
и 140 снизу обрезаем
'''


# подготовка основной информации о файле
def trim_header_of_main_page(page):
    width = page.mediaBox.getUpperRight_x()
    height = page.mediaBox.getUpperRight_y()
    page.cropBox.lowerLeft = (50, height-142)
    page.cropBox.upperRight = (width-255, height-70)

    return page


# обрезка для
def trim_footer_of_header_of_main_page(page):
    width = page.mediaBox.getUpperRight_x()
    height = page.mediaBox.getUpperRight_y()
    page.cropBox.lowerLeft = (50, height-142)
    page.cropBox.upperRight = (width-255, height-120)

    return page

# обрезка для
def trim_footer(page):
    width = page.mediaBox.getUpperRight_x()
    height = page.mediaBox.getUpperRight_y()
    page.cropBox.lowerLeft = (324, 111)
    page.cropBox.upperRight = (width-185, height-715)

    return page

# обрезка для первой страницы
def trim_for_main_page(page):
    width = page.mediaBox.getUpperRight_x()
    height = page.mediaBox.getUpperRight_y()
    page.cropBox.lowerLeft = (70, 250)
    page.cropBox.upperRight = (width - 30, height - 142)

    return page


# обрезка для второй страницы
def trim_for_second_page(page):
    width = page.mediaBox.getUpperRight_x()
    height = page.mediaBox.getUpperRight_y()
    page.cropBox.lowerLeft = (70, 160)
    page.cropBox.upperRight = (width - 30, height - 225)

    return page


# обрезка для третьей страницы
def trim_for_third_page(page):
    width = page.mediaBox.getUpperRight_x()
    height = page.mediaBox.getUpperRight_y()
    page.cropBox.lowerLeft = (70, 400)
    page.cropBox.upperRight = (width - 30, height - 142)

    return page


# подготовка страниц PDF файла
def prepare_file(filename: str) -> str:
    with open(filename, "rb") as input_file:
        pdf_input = PdfFileReader(input_file)
        pdf_header_input_first = PdfFileReader(input_file)
        pdf_header_input_second = PdfFileReader(input_file)
        pdf_output = PdfFileWriter()

        pdf_output.addPage(trim_for_main_page(pdf_input.getPage(0)))
        pdf_output.addPage(trim_for_second_page(pdf_input.getPage(1)))
        pdf_output.addPage(trim_for_third_page(pdf_input.getPage(2)))
        pdf_output.addPage(trim_header_of_main_page(pdf_header_input_first.getPage(0)))
        pdf_output.addPage(trim_footer_of_header_of_main_page(pdf_header_input_second.getPage(0)))
        pdf_output.addPage(trim_footer(pdf_header_input_second.getPage(1)))

        new_name = f'prepared_{os.path.basename(filename)}'
        with open(new_name, "wb") as output_file:
            pdf_output.write(output_file)

        file_path = f'{os.path.dirname(filename)}/{new_name}'
        os.replace(new_name, file_path)

        return file_path

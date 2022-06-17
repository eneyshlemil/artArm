import fitz
import os


# каждую страницу файла преобразует в изображение
def convert_pdf_to_images(filename: str, pages: tuple = None) -> list:
    input_pdf = fitz.open(filename)
    output_files = []
    for pg in range(input_pdf.pageCount):
        if str(pages) != str(None):
            if str(pg) not in str(pages):
                continue
        page = input_pdf[pg]
        rotate = int(0)
        zoom_x = 2
        zoom_y = 2
        mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        output_file = f"{os.path.dirname(filename)}/{pg + 1}_{os.path.basename(filename)[:-4]}.png"
        pix.save(output_file)
        output_files.append(output_file)
    input_pdf.close()

    return output_files

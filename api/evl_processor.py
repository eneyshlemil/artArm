import os

from pdf_proccessors.evl_clear_parts_processor import prepare_file
from pdf_proccessors.pdf_pages_to_images_processor import convert_pdf_to_images
from image_processors.concat_images_processor import concat_images_vertical
from image_processors.main_info_evl_processor import get_processed_main_info
from image_processors.additional_info_evl_processor import get_processed_additional_info
from image_processors.extract_info_evl_processor import get_processed_extract_info
from image_processors.extract_date_info_evl_processor import get_processed_extract_date
from image_processors.generation_date_time_evl_processor import get_processed_generation_date_time


# подготавливает массив файлов для дальнейшей обработки
def prepare_images_to_parse(filepath: str) -> list:
    prepared_filename = prepare_file(filepath)
    images_list = convert_pdf_to_images(prepared_filename)
    ready_to_parse = []
    number = 0
    for i, image in enumerate(images_list, 1):
        if number == 1:
            concat_images_vertical(image, images_list[2])

        if i == 3:
            os.remove(image)
            continue

        number += 1
        new_image_name = f'{os.path.dirname(image)}/{number}_{os.path.basename(image)}'
        os.rename(image, new_image_name)
        ready_to_parse.append(new_image_name)

    os.remove(prepared_filename)

    return ready_to_parse


# функция формирования json'а
def make_json(files: list) -> dict:
    dict_for_json = get_processed_main_info(files[0])
    dict_for_json.update(get_processed_additional_info(files[1]))
    dict_for_json.update(get_processed_extract_info(files[2]))
    dict_for_json.update(get_processed_extract_date(files[3]))
    dict_for_json.update(get_processed_generation_date_time(files[4]))

    for file in files:
        os.remove(file)

    return dict_for_json


from image_processor import prepare_bars, get_first_prepared


# дата формирования документа
def get_processed_generation_date_time(image_name: str) -> dict:
    return {
        'generation_date_time': prepare_bars(image_name)[0],
    }

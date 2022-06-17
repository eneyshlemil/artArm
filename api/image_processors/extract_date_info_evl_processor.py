from image_processor import prepare_bars, get_first_prepared


# дата формирования документа
def get_processed_extract_date(image_name: str) -> dict:
    return {
        'extract_date': get_first_prepared(prepare_bars(image_name))[-1].replace('-', ''),
    }

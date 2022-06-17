from image_processor import prepare_bars, get_first_prepared


# номер выдачи и статус
def get_processed_extract_info(image_name: str) -> dict:
    bars = prepare_bars(image_name)

    return {
        'extract_number': get_first_prepared(bars)[0],
        'extract_status': get_first_prepared(bars)[-1],
    }

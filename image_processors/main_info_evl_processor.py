from image_processor import prepare_bars, get_first_prepared, get_last_prepared, glue


# основная информация о транспортном средстве
def get_processed_main_info(image_name: str) -> dict:
    bars = prepare_bars(image_name)
    vin = get_first_prepared(bars)[-1]
    brand = glue(get_first_prepared(bars)[1:])
    commercial_name = glue(get_first_prepared(bars)[2:])
    vehicle_category_russia = get_first_prepared(bars)[-1]

    get_first_prepared(bars)
    get_first_prepared(bars)

    vehicle_category_eacu = get_first_prepared(bars)[-1]
    engine_number = get_first_prepared(bars)[-1]
    chassis_number = get_first_prepared(bars)[-1]
    body_number = get_first_prepared(bars)[-1]
    body_color = glue(get_first_prepared(bars)[4:])
    manufacture_year = get_first_prepared(bars)[-1]
    get_last_prepared(bars)
    max_weight = get_last_prepared(bars)[-1]
    environmental_class = get_last_prepared(bars)[-1]
    get_first_prepared(bars)
    engines = []
    engine = ''
    while bars:
        bar = get_first_prepared(bars)
        if bar[0].lower().startswith('двигатель'):
            if engine:
                engines.append(engine)
            engine = glue(bar[5:])
        else:
            trimmed_bar = glue(bar).strip()
            if trimmed_bar.startswith('—') or trimmed_bar.startswith('-'):
                continue
            engine += glue(bar)
    else:
        engines.append(engine)

    return {
        'vin': vin,
        'brand': brand,
        'commercial_name': commercial_name,
        'vehicle_category_russia': vehicle_category_russia.upper(),
        'vehicle_category_eacu': vehicle_category_eacu.upper(),
        'engine_number': engine_number,
        'chassis_number': chassis_number,
        'body_number': body_number,
        'body_color': body_color,
        'manufacture_year': manufacture_year,
        'engines': engines,
        'environmental_class': environmental_class,
        'max_weight': max_weight,
    }

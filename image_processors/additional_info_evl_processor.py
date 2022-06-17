from image_processor import prepare_bars, get_first_prepared, get_last_prepared, glue


# извлечение данных из дополнения к выписке из электронного паспорта транспортного средства
def get_processed_additional_info(image_name: str) -> dict:
    bars = prepare_bars(image_name)
    issued_organization_name = f'{glue(get_first_prepared(bars)[3:])} {glue(get_first_prepared(bars)[3:])} {glue(get_first_prepared(bars)[2:])}'
    modification = glue(get_first_prepared(bars)[1:])
    color_shade = glue(get_first_prepared(bars)[5:])

    get_first_prepared(bars)
    get_first_prepared(bars)

    running_order_weight = get_first_prepared(bars)[-1]
    get_first_prepared(bars)

    wheel_formula = glue(get_first_prepared(bars)[3:])
    seats_number = glue(get_first_prepared(bars)[4:])
    transmission_type = f'{glue(get_first_prepared(bars)[2:])} {glue(get_first_prepared(bars))}'
    fuel_type = glue(get_first_prepared(bars)[2:])
    mandatory_safety_requirements_document = glue(get_first_prepared(bars)[3:])
    get_first_prepared(bars)
    emergency_call_device_id = glue(get_first_prepared(bars)[4:])
    get_first_prepared(bars)
    get_first_prepared(bars)
    manufacturer = glue(get_first_prepared(bars)[1:])

    bar = get_first_prepared(bars)
    while not bar[0].lower().startswith('адрес'):
        manufacturer += ' ' + glue(bar)
        bar = get_first_prepared(bars)
    else:
        manufacturer_address = glue(bar[2:])

    bar = get_first_prepared(bars)
    while not bar[0].lower().startswith('территория'):
        manufacturer_address += ' ' + glue(bar)
        bar = get_first_prepared(bars)
    else:
        active_status_applied_territory = glue(bar[4:])

    get_first_prepared(bars)
    customs_receipt_order_series_number = glue(get_first_prepared(bars)[4:])
    get_first_prepared(bars)
    customs_restriction = glue(get_first_prepared(bars)[2:]).capitalize()
    bar = get_first_prepared(bars)
    if bar[0].lower().startswith('собственник'):
        owner = glue(bar[1:])
        encumbrances_except_custom_restrictions = glue(get_first_prepared(bars)[4:])
    else:
        owner = ''
        encumbrances_except_custom_restrictions = glue(bar[4:])

    return {
        'issued_organization_name': issued_organization_name,
        'modification': modification,
        'color_shade': color_shade.capitalize(),
        'running_order_weight': running_order_weight,
        'wheel_formula': wheel_formula,
        'seats_number': seats_number,
        'transmission_type': transmission_type,
        'fuel_type': fuel_type,
        'mandatory_safety_requirements_document': mandatory_safety_requirements_document,
        'emergency_call_device_id': emergency_call_device_id,
        'manufacturer': manufacturer,
        'manufacturer_address': manufacturer_address,
        'active_status_applied_territory': active_status_applied_territory,
        'customs_receipt_order_series_number': customs_receipt_order_series_number,
        'customs_restriction': customs_restriction,
        'owner': owner,
        'encumbrances_except_custom_restrictions': encumbrances_except_custom_restrictions,
    }

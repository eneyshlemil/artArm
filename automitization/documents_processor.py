from docxtpl import DocxTemplate
import os
import requests

def prepare_doc(doc_name: str, content: dict) -> None:
    doc = DocxTemplate(doc_name)
    doc.render(content)
    doc.save(f"ready/{os.path.basename(doc_name)}")


def make_file(evl_filename: str, document_filename: str) -> str:
    files = {'file': open(evl_filename, 'rb')}
    try:
        data = requests.post('http://127.0.0.1:5000/evl/api', files=files).json()
    except:
        return

    vin = data['vin']
    content = {
        'extract_number': data['extract_number'],
        'issued_organization_name': data['issued_organization_name'],
        'extract_date': data['extract_date'],
        'vin': vin,
        'brand': data['brand'],
        'commercial_name': data['commercial_name'],
        'manufacture_year': data['manufacture_year'],
        'engine_number': data['engine_number'],
        'chassis_number': data['chassis_number'].upper(),
        'body_number': data['body_number'],
        'body_color': data['body_color'],
    }
    prepare_doc(document_filename, content)

    return vin

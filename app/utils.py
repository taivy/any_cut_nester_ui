import base64
import requests
from os import path

from app.config import Config


def create_items_list(file_list, items_quantity):
    items_list = []
    items_quantity_vals = items_quantity.split(",")
    for i, file_info in enumerate(file_list):
        if i >= len(items_quantity_vals):
            quantity = 1
        else:
            quantity = items_quantity_vals[i]
            if quantity.isdigit():
                quantity = int(quantity)
            else:
                quantity = 1
        items_list.append({
            'url': file_info['url'],
            'quantity': quantity
        })
    return items_list


def get_results(file_list, items_quantity, bin_size_x, bin_size_y, timeout):
    api_url = Config.BASE_URL
    data = {
        'items': create_items_list(file_list, items_quantity),
        'bin_size': [
            bin_size_x,
            bin_size_y
        ],
        'allow_flip': False,
        'rotations': [
            0,
            180
        ],
        'margin': 5,
        'timeout': timeout
    }
    response = requests.post(api_url, json=data, timeout=Config.API_REQUEST_TIMEOUT)
    if response.status_code == 200:
        encoded_img = str(base64.b64encode(response.content))[2:-1]
        return encoded_img
    return None

def process_files(request, app):
    file_list = []
    for f in request.files.values():
        file_path = path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(file_path)

        url = f"{app.config['APP_BASE_URL']}/uploads/{f.filename}"

        file_list.append({
            'url': url
        })
    return file_list

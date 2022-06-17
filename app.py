import os
import time
from flask import Flask, request, render_template
from evl.form import LoadFileForm
from evl_processor import make_json, prepare_images_to_parse
import json

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET'])
def show_main():
    form = LoadFileForm()
    return render_template('main.html', form=form)


# обработка через интерфейс
@app.route('/evl/ui', methods=['GET', 'POST'])
def get_evl_json_ui():
    form = LoadFileForm()
    if request.method == 'POST':
        loaded_file = form.file.data
        save_name = get_save_name()
        with open(save_name, 'wb') as f:
            tmp_file = loaded_file.stream
            tmp_file.seek(0)
            f.write(tmp_file.read())
        json_data = make_json(prepare_images_to_parse(save_name))
        os.remove(save_name)
        return render_template('load_ui.html', form=form, json_data=json_data)

    if request.method == 'GET':
        return render_template('load_ui.html', form=form)


# api обработка изображения и ответ json'ом
@app.route('/evl/api', methods=['GET', 'POST'])
def get_evl_json_api():
    if request.method == 'POST':
        save_name = get_save_name()
        request.files.get('file').save(save_name)
        json_data = json.dumps(make_json(prepare_images_to_parse(save_name)))
        os.remove(save_name)

        return json_data

    if request.method == 'GET':

        return render_template('guide_api.html')


# функция для создания временного имени файла
def get_save_name() -> str:
    return f'static/{hash(time.time())}.pdf'


if __name__ == '__main__':
    app.run(debug=True)

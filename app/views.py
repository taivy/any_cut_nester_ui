from os import environ, path

from flask import Flask, render_template, request, send_from_directory
from flask_dropzone import Dropzone

from app.utils import get_results, process_files
from app.forms import NestRequestForm


app = Flask(__name__)

if environ.get('ENV') == 'PROD':
    app.config.from_object('app.config.ProdConfig')
else:
    app.config.from_object('app.config.DevConfig')


dropzone = Dropzone(app)


@app.route('/', methods=['get', 'post'])
def index():
    form = NestRequestForm()

    print("request.method", request.method)
    if request.method == 'POST':
        if form.validate_on_submit():
            items_quantity = form.items_quantity.data
            bin_size_x = form.bin_size_x.data
            bin_size_y = form.bin_size_y.data
            timeout = form.timeout.data

        try:
            file_list = process_files(request, app)
        except Exception as err:
            return render_template('error.html', error=f'Error while processing uploaded files: {err}')

        try:
            results = get_results(file_list=file_list,
                                  items_quantity=items_quantity,
                                  bin_size_x=bin_size_x,
                                  bin_size_y=bin_size_y,
                                  timeout=timeout)

            return render_template('results.html', results=results)
        except Exception as err:
            return render_template('error.html', error=f'Error while getting results: {err}')

    return render_template('index.html', form=form, )


@app.route('/uploads/<path:filename>', methods=['GET'])
def download(filename):
    uploads = app.config['UPLOAD_FOLDER']
    return send_from_directory(directory=uploads, filename=filename)

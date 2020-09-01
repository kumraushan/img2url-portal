import os

from flask import Flask, render_template, request, redirect, send_file, url_for

from awsS3_functions import upload_file,get_url


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = 'uploadingimageandgettingurl'

#
# @app.route('/')
# def entry_point():
#     return 'Hello World!'


@app.route("/")
def storage():
    #contents = list_files("flaskdrive") , contents=contents
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(f.filename)
        upload_file(f"{f.filename}", BUCKET)
        url = get_url(f"{f.filename}", BUCKET)
        print(url)
        return render_template('index.html', img_url = url)


if __name__ == '__main__':
    app.run(debug=True)























#
# @app.route("/download/<filename>", methods=['GET'])
# def download(filename):
#     if request.method == 'GET':
#         output = download_file(filename, BUCKET)
#
#         return send_file(output, as_attachment=True)

import os
from flask import Flask, render_template, request, redirect, send_file, url_for
from awsS3_functions import upload_file,get_url


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = 'uploadingimageandgettingurl'


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def storage():
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        files = request.files.getlist('files[]')
        #print(files)
        url_list = []
        for file in files:
            if file and allowed_file(file.filename):
                #file.save(os.path.join(UPLOAD_FOLDER, file.filename))
                file.save(file.filename)
                upload_file(f"{file.filename}", BUCKET)
                url = get_url(f"{file.filename}", BUCKET)
                url_list.append(url)
        #print(url_list)
        return render_template('index.html', urllist = url_list)


if __name__ == '__main__':
    app.run(debug=True)























#
# @app.route("/download/<filename>", methods=['GET'])
# def download(filename):
#     if request.method == 'GET':
#         output = download_file(filename, BUCKET)
#
#         return send_file(output, as_attachment=True)

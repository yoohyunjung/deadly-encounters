import csv
from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__)  # Note the double underscores on each side!
app.static_folder = 'static'

def get_csv():
    csv_path = './static/hpd-fatal.csv'
    with open(csv_path, mode="rb") as stream:
        contents = stream.read()
        contents_utf = contents.decode('utf-8', 'ignore')
        csv_reader = csv.DictReader(contents_utf.splitlines())
        csv_list = list(csv_reader)

    print(csv_list)
    return csv_list

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['id'] == row_id:
            return render_template(template, object=row)
        abort (404)

if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)

import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Main page of the website
@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello, Sanket R!'


# Dynamically choose app route
@app.route('/<string:page_name>')
def click_page(page_name):
    return render_template(page_name)

# Store data into a local file
# def store_data(data):
#     with open('contactdata.txt','a') as fhand:
#         for k,v in data.items():
#             fhand.write(f'\n{k}, {v} ')

# Store data in csv format
def store_data_csv(data):
    with open('database.csv','a+',newline='') as csvfile:
        field_names = ['email','subject','message']
        csv_writer = csv.DictWriter(csvfile, fieldnames=field_names)
        csv_writer.writerow(data)
        csvfile.close()

# Get data from the server
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        store_data_csv(data)
        return redirect('thanks.html')
    else:
        return 'Something went wrong!'
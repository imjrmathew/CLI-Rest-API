# author: <Don Mathew>
# Server side CLI
# Necessary imports.
from flask import Flask, jsonify
from flask import *
import json
from collections import Counter
import click

# Intialization of Flask app.
app = Flask(__name__)

# intializing an empty list known as request_handler.
request_handler = []


# Routing
@app.route('/', methods=['GET','POST'])

# Function for handling both GET and POST methods.
def request_made():
    # If the request is a POST operation.
    # Then collect the datas from the request and pass it as an argument to the process().
    if request.method == 'POST':
        request_data = request.data
        data = json.loads(request_data)
        tempdata = process(data)
        request_handler.append(tempdata)
        return jsonify(request_handler)
    # If the request is GET operation.
    # Displaying the JSON file, which is enclosed in a list.
    else:
        if request_handler:
            return jsonify(request_handler)
        else:
            return 'Empty values in the list!'


# process() function handles all the operations on the server side.
# Collecting the neccesary information.
def process(data):
    try:
        overall_size = 0
        overall_extensions = []
        top_files = []
        for i in range(0, len(data)):
            overall_size += float(data[i]['size'].replace('MB',''))
            overall_extensions.append(data[i]['extension'])
            if i < 10:
                top_files.append(data[i])
        extension = Counter(overall_extensions).most_common(1)
        tempdata = {
            'NUMBER OF FILE RECIEVED': len(data),
            'MAXIMUM SIZE OF FILES': str(round(overall_size, 2))+'MB',
            'LIST OF EXTENSIONS': list(set(overall_extensions)),
            'MOST FREQUENTLT OCCURED EXTENSION': extension[0][0], 
            'MOST FREQUENTLT OCCURED EXTENSION (NUMBER)': extension[0][1],
            'TOP 10 FILES RECIEVED': top_files
        }
        return tempdata
    except:
        print("JSON should contain following fields (name, size(str), extension, path! and it should be enclosed in list e.g: [{ 'name': 'john'}])")


# errorhandler decorator is used to check whether the url is valid or not.
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# By using click module, we can turn the python script into CLI.
@click.command()
@click.option('--port', help="Specify the port number", required=True)
# Main method, running the app.
def run(port):
    """Inorder to start server type runserver --port <port_number>"""
    app.run(debug=True, port=int(port))
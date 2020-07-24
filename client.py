# author: <Don Mathew>
# Client side CLI
# Necessary imports.
import os
import json
from pathlib import Path
import requests
import click
from server import run


# Click package is used to turn the python script into CLI.
@click.command()
@click.option('--path',prompt="Enter the path", help='Specify the path, that you want to display', required=True)
@click.option('--port',prompt="Enter the PORT number that is used to start the server", help='Specify the PORT number, that you already used to start server', required=True)

# The value of @click.option (path and port) is passed to the function getfiles.
def getfiles(path, port):
     """Simple program that displays a list of files in the directory."""

     # Initializing an empty list variable called store_list.
     # Which is used to store the directory details.
     store_list = []

     # Checking whether the path is exist or not.
     if os.path.exists(path):
         # By using os.walk module we can generate files/folders from the provided path.
         for root, directories, files in os.walk(path):
             # We create a iterator known as take_file, which collects all the files under the directory.
             for take_file in files:
                 # Collecting files other than hidden files or hidden directories.
                 if not take_file.startswith('.') and not os.path.basename(root).startswith('.'):
                     # To get the path of the current file.
                     pathname = os.path.join(root,take_file)
                     # To get the information of that particular file.
                     stat = os.stat(pathname)
                     # Creating a dictionary to store the informations.
                     dicts = {
                         'name': take_file,
                         'path': pathname,
                         'size': str(round(stat.st_size/ (1024*1024), 2))+'MB',
                         'extension': Path(take_file).suffix
                     }
                     store_list.append(dicts)
         # Checking, whether there are files in the directory or not.
         if len(store_list) == 0:
             print('\nThere is no files inside the directory')
         # Else, send the dictionary to the server, through the valid PORT number.
         else:
             try:
                datas = json.dumps(store_list)
                url = 'http://localhost:{}/'.format(port)
                x = requests.post(url, data = datas)
                print("Please wait...")
                print('Sending data to server...')
                print("Success!")   
             except:
                 print("Invalid PORT number!")
     else:
         print('\nInvalid path!')   

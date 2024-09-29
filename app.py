from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Change this to your folder path
DIRECTORY_PATH = "./songs"  # Replace with the actual folder path

@app.route('/')
def list_folders():
    folders = os.listdir(DIRECTORY_PATH)
    return render_template('index.html', folders=folders)

@app.route('/songs/<foldername>')
def open_folder(foldername):
    folder_path = os.path.join(DIRECTORY_PATH, foldername)
    if os.path.exists(folder_path):
        files = os.listdir(folder_path)
        return render_template('folder.html', foldername=foldername, files=files)
    else:
        return "Folder not found", 404

@app.route('/songs/<foldername>/<filename>')
def download_file(foldername, filename):
    folder_path = os.path.join(DIRECTORY_PATH, foldername)
    return send_from_directory(folder_path, filename)

if __name__ == '__main__':
    app.run(debug=True)

import os
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from model_handler import predict

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def save_file_to_server(file_data, filename):
    try:
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'wb') as f:
            f.write(file_data)
        return True
    except Exception as e:
        print('Error saving file:', e)
        return False

@app.route('/', methods = ['GET'])
def get_pycode():
   result = predict()
   return jsonify({"mineral" : result})
  

@app.route('/upload', methods=['POST'])
def get_image():
    try:
        # Check if the 'photo' key is in the files
        if 'photo' not in request.files:
            return jsonify({"result": "Error: 'photo' not found in the files."})

        photo_file = request.files['photo']

        # Generate a random filename and save the file
        filename = secure_filename('uploaded_image.jpg')
        photo_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Process the image as needed
        result = predict()

        return jsonify({"Image": "Image saved successfully.",
                        "result": result})
    except Exception as e:
        print('Error processing image:', e)
        return jsonify({"result": "Error processing image. Please try again."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_pycode():
  return jsonify({'hello': 'mineral'})

@app.route('/upload', methods = ['POST'])
def get_image():
  return 'image'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5500, debug=True)

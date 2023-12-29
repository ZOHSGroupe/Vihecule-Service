from flask import Flask, request, jsonify
import methodes 


app = Flask(__name__)

vehicle = []

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    return jsonify({'vehicle': vehicle})

@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
     return methodes.add_vehicle()
    

    

if __name__ == '__main__':
    app.run(debug=True, port=5000)

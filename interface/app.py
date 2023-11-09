from flask import Flask, render_template, request, jsonify
from random import Random

app = Flask(__name__)

@app.route('/')
def index():
    status = {'light_status': False,
    'fan_status': False}
    return render_template('schedule.html', light_status=True, fan_status=True)

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/update_light_level', methods=['POST'])
def update_light_level():
    light_level = int(request.json['level'])
    # fan_speed = int(request.json['fan_speed'])
    print(light_level)
    # code to control the Green Wall HVAC System based on the submitted light level and fan speed

    return jsonify({'success': True})

@app.route('/update_fan_speed', methods=['POST'])
def update_fan_speed():
    fan_speed = int(request.json['speed'])
    # fan_speed = int(request.json['fan_speed'])
    print(fan_speed)
    # code to control the Green Wall HVAC System based on the submitted light level and fan speed

    return jsonify({'success': True})

@app.route('/temperature', methods=['GET'])
def get_temperature():
    return jsonify({'temperature': int(Random(100).random() * 100), 'humidity': int(Random(100).random() * 100)}, )

if __name__ == '__main__':
    
    app.run(debug=True, port=5001)

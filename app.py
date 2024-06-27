from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Применяем CORS ко всем маршрутам

# Данные об автомобилях (здесь можно добавить больше данных)
cars = [
    {
        'name': 'DAEWOO MATIZ',
        'image_url': 'https://avatars.mds.yandex.net/get-autoru-vos/6078333/834ae2ee1cd6d92602ace14d05878fdc/1200x900',
        'price_per_hour': 800
    },
    {
        'name': 'Daewoo Nexia I',
        'image_url': 'https://avatars.mds.yandex.net/get-autoru-vos/2164969/5ce63b654351614346c712548514e0f1/1200x900',
        'price_per_hour': 1000
    }
    # Добавьте другие автомобили по аналогии
]

@app.route('/api/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)

if __name__ == '__main__':
    app.run(debug=True)

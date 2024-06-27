from flask import Flask, render_template

app = Flask(__name__)

# Список машин для аренды
cars = [
    {
        'name': 'Daewoo Matiz',
        'image_url': 'https://avatars.mds.yandex.net/get-autoru-vos/6078333/834ae2ee1cd6d92602ace14d05878fdc/1200x900',
        'price_per_hour': 800
    },
    # Добавьте здесь другие машины по аналогии
]

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)

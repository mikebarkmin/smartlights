from flask import Flask, request, jsonify
from led import Led

app = Flask(__name__)

led = Led(0, 0, 0)


@app.route("/leds", methods=["GET", "POST"])
def handle_led():
    if request.method == "GET":
        return get_led()
    elif request.method == "POST":
        return post_led()


def get_led():
    return jsonify({"r": led.r, "g": led.g, "b": led.b})


def post_led():
    json = request.get_json()

    led.r = json.get("r", led.r)
    led.g = json.get("g", led.g)
    led.b = json.get("b", led.b)

    return jsonify({"message": "success"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

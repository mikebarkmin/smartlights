from flask import Flask, request, jsonify
from light import Light
from device import NetworkDevice

app = Flask(__name__)


@app.route("/devices", methods=["GET"])
def get_devices():
    """
    Gib alle IP Adressen der Netwerkgeräte
    """
    return jsonify([d.ip_address for d in NetworkDevice.all()])


@app.route("/lights", methods=["POST", "GET"])
def lights():
    if request.method == "GET":
        return get_lights()
    elif request.method == "POST":
        return post_lights()


def get_lights():
    """
    Gib alle Lampe
    """
    return jsonify([l.to_dict() for l in Light.all()])


def post_lights():
    """
    Füge eine neue Lampe hinzu
    :body name: Name der Lampe
    :body ip_address: IP Adresse der Lampe
    :body port: Port des HTTP-Servers der Lampe
    """
    json = request.get_json()

    if not json:
        return jsonify({'message': 'no data received'}), 400

    name = json.get('name')
    ip_address = json.get('ip_address')
    port = json.get('port')

    if not name or not ip_address or not port:
        return jsonify({'message': 'information is missing'}), 400

    light = Light(
        None,
        name,
        ip_address,
        port,
        r=json.get('r', 0),
        g=json.get('g', 0),
        b=json.get('b', 0)
    )

    light.save()

    return jsonify({'message': 'Light saved'}), 200


@app.route("/lights/<id>", methods=["DELETE", "PUT"])
def light(id):
    if request.method == "DELETE":
        return delete_light(id)
    elif request.method == "PUT":
        return put_light(id)


def delete_light(id):
    """
    Lösche eine Lampe
    """
    light = Light.get(id)
    if not light:
        return jsonify({'message': 'Light not found'}), 404
    light.delete()

    return jsonify({'message': 'Light deleted'}), 200


def put_light(id):
    """
    Setze den Status einer Lampe
    :body name (optional): Name der Lampe
    :body r (optional): Rotwert [0...255]
    :body g (optional): Grünwert [0...255]
    :body b (optional): Blauwert [0...255]
    """
    json = request.get_json()

    if not json:
        return jsonify({'message': 'no data received'}), 200

    light = Light.get(id)

    if not light:
        return jsonify({'message': 'Light not found'}), 404

    if json.get('name') is not None:
        light.name = json.get('name')

    if json.get('r') is not None:
        light.r = json.get('r')

    if json.get('g') is not None:
        light.g = json.get('g')

    if json.get('b') is not None:
        light.b = json.get('b')

    light.save()

    return jsonify({'message': 'Light saved'}), 200


if __name__ == '__main__':
    Light.create_table()

    app.run(host='0.0.0.0', port=8000, debug=True)

from flask import Flask, request, Response
from PIL import Image
import io

app = Flask(__name__)

@app.route('/generate_image', methods=['GET'])
def generate_image():
    # Get the parameters from the request
    width = request.args.get('width')
    height = request.args.get('height')
    color = request.args.get('color')
    img_format = request.args.get('format')

    # Check if the parameters are valid
    if not width.isdigit() or not height.isdigit():
        return Response("Invalid width or height", status=400)

    if color not in ['red', 'green', 'blue']:
        return Response("Invalid color", status=400)

    if img_format not in ['jpeg', 'png', 'gif']:
        return Response("Invalid format", status=400)

    # Generate the image array
    image = Image.new('RGB', (int(width), int(height)), color)

    # Convert the image array to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format=img_format)
    img_bytes.seek(0)

    # Return the image array as a response
    return Response(img_bytes, mimetype='image/' + img_format)

if __name__ == '__main__':
    app.run(debug=True)



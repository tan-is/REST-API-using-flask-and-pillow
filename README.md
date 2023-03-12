Flask Image Generation API
This is a simple Flask API that generates image arrays based on user-specified parameters. The API takes the following parameters:

width: the width of the image array in pixels (integer)
height: the height of the image array in pixels (integer)
color: the color of the image (string, one of 'red', 'green', 'blue')
format: the format of the image (string, one of 'jpeg', 'png', 'gif')

The API generates an image array according to the provided parameters using the Pillow library, and returns the generated image array as a response in the specified format using Flask's built-in functionality.

Installation and Setup
To run this API on your local machine, you will need to have Python 3 and the Flask and Pillow libraries installed. You can install these using pip, the Python package installer:

pip install flask pillow

Once you have installed the required libraries, you can start the Flask app by running the following command in your terminal:

python app.py

This will start the Flask app on your local machine at http://localhost:5000/.

Usage
To generate an image array, you can make a GET request to the /api/generate_image endpoint with the required parameters:

http://localhost:5000/api/generate_image?width=500&height=500&color=red&format=png

This will generate a red image with a width of 500 pixels and a height of 500 pixels in PNG format.

If any of the provided parameters are invalid, the API will return an appropriate error message with a 400 Bad Request status code.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was inspired by the Flask Mega-Tutorial by Miguel Grinberg.



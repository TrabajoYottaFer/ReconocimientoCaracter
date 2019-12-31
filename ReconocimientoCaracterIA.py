# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:54:32 2019

@author: Victor Poma
"""
import sys
from flask import Flask, request
from flask_restful import Resource, Api
from PIL import Image
from io import BytesIO
from flask_cors import CORS
import base64
import pytesseract
app = Flask(__name__)
api = Api(app)
CORS(app)
class Reconocimiento(Resource):
    
    def post(self):
        try:
            print("REsol")
            pytesseract.pytesseract.tesseract_cmd = (r"tesseract")
            img = request.form['img']
            x = str(pytesseract.image_to_string(Image.open(BytesIO(base64.b64decode(img)))))
            response = {
                    'correcto': True,
                    'Mensaje': "Reconocimiento Exitoso",
                    'data': {
                    'prediction': x,
#                   'nombrearchivo': img.filename
                    }
            } 
            return response, 200
        except:
            print("Error inesperado:", sys.exc_info())
            response = {
                    'Correcto': False,
                    'Mensaje': "Reconocimiento Fallido",
                    'Respuesta': ""
                    } 
            return response, 200
api.add_resource(Reconocimiento, '/reconocimiento/caracter')
if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=False)

from flask import Flask
from flask_restx import Api, Resource, fields
from despliegue_carro import predict_price
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(
    app,
    version='1.0',
    title='API PREDICCIÓN DE CARROS GRUPO 14 MIAD',
    description='Esta es una API que utiliza un modelo para predecir el precio de un carro basado en características específicas del vehículo.'
)

ns = api.namespace('predict', description='Predictor precio del carro')

parser = api.parser()
parser.add_argument('Year', type=int, required=True, help='Año del carro', location='args')
parser.add_argument('Mileage', type=int, required=True, help='Kilometraje del carro', location='args')
parser.add_argument('State', type=str, required=True, help='Estado donde se encuentra el carro', location='args')
parser.add_argument('Make', type=str, required=True, help='Marca del carro', location='args')
parser.add_argument('Model', type=str, required=True, help='Modelo del carro', location='args')

resource_fields = api.model('Resource', {
    'Predicción': fields.Float,
})

@ns.route('/')
class CarPriceApi(Resource):
    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        # Llamamos a predict_price pasando un diccionario con los atributos del carro
        prediction = predict_price(args)

        return {"Predicción": prediction[0]}, 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)

#!/usr/bin/python

import pandas as pd
import joblib
import sys
import os

def predict_price(car_attributes):
    # Cargamos el modelo de predicción de precios y el transformador
    clf = joblib.load(os.path.join(os.path.dirname(__file__), 'carros.pkl'))
    transformador = joblib.load(os.path.join(os.path.dirname(__file__), 'transformador.pkl'))

    # Creamos un DataFrame con los atributos del carro
    df_input = pd.DataFrame([car_attributes], columns=car_attributes.keys())

    # Aplicamos la transformación al dato de entrada usando el transformador
    transformacion = transformador.transform(df_input)

    # Hacemos la predicción
    precio_predicho = clf.predict(transformacion)

    return precio_predicho

if __name__ == "__main__":
    # Esperamos que los atributos del carro sean pasados como argumentos al script
    if len(sys.argv) < 6:
        print("Por favor ingrese todos los atributos requeridos: Year, Mileage, State, Make, Model")
    else:
        car_attributes = {
            'Year': int(sys.argv[1]),
            'Mileage': int(sys.argv[2]),
            'State': sys.argv[3],
            'Make': sys.argv[4],
            'Model': sys.argv[5]
        }

        p1 = predict_price(car_attributes)
        
        print(f'La predicción del precio del automóvil es: {p1[0]}')

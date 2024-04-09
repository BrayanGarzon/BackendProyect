from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'archivo_excel' not in request.files:
        return 'No se ha proporcionado ningún archivo'
    
    archivo = request.files['archivo_excel']

    if archivo.filename == '':
        return 'Ningún archivo seleccionado'

    if archivo:
        try:
            # Guardar el archivo en el servidor (opcional)
            archivo.save(archivo.filename)
            
            # Leer el archivo Excel con Pandas
            df = pd.read_excel(archivo)

            # Convertir el DataFrame a JSON
            data_json = df.to_json(orient='records')

            # Crear un mensaje de éxito
            mensaje_exito = 'Archivo Excel cargado y procesado con éxito'


            # Enviar los datos JSON al frontend
            return jsonify({'data': data_json, 'message': mensaje_exito})
        
        except Exception as e:
            return f'Error al procesar el archivo: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)

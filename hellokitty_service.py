python
from flask import Flask, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/hellokitty', methods=['GET'])
def get_hellokitty():
    # Aquí va tu código para dibujar a Hello Kitty y devolver la imagen como base64
    img = Image.new('RGB', (400, 400), color='pink')
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run()
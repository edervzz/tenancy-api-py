# tenancy-api-py
Tenancy API built on Python


## 1. Crear enviroment
En caso de trabajar con un monorepo y VSCODE, será necesario hacer esta instalación abriendo la carpeta asignada al proyecto en Python, y luego cambiar a la carpeta del proyecto principal. Para confirmar que venv esta corriendo en la consola, abrir una terminar dentro de VSCODE y poner el mouse encima de la terminal seleccionada. 
```bash
$ python -m venv .venv
```

## 2. Instalación de Flask
```bash
$ pip install flask  
```

## 3. Punto de entrada
Crear un archivo llamado _app.py_ donde colocaremos 
```python
from flask import Flask

app = Flask(__name__)  # el archivo debe llamarse app así como esta variable

stores = [ # ejemplo de response body
    {
        "name": "My store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]


@app.get("/store") # decorador para verbo GET
def get_store(): # endpoint
    """_summary_"""
    return {"store": stores}
```

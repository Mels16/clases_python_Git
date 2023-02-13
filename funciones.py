
from nis import match

def area_rectangulo(x:float, y:float) -> float:
    """
    funcion que calcula el area de un rectangulo 

    ```params```
    -x(float) es la base de un rectangulo 
    -y(float) es la altura de un rectangulo 

     ```return```
    -area(float): es el area de un rectangulo 

     """
    return x * y 

def distancia_dos_puntos(x_1:float, x_2:float, y_1:float, y_2:float) -> float: 
    x = match.pow(x_2 - x_1, 2)
    y = match.pow (y_2 - y_1, 2)
    d = match.sqrt(x + y)

    return d
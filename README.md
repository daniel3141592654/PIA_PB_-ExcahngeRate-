# PIA_PB_-ExcahngeRate-
Este código *(que aún no existe porque soy un procrastinador ligeramente compulsivo)* para ser compilado en **su máquina** requiere la instalación de
python 3.11 o superior (si no ha instalado python, hágalo desde la siiguiente liga https://www.python.org/ ) y de algunas librerías externas que se
listarán debajo:

- Módulo io => https://docs.python.org/es/3/library/io.html#module-io
  - *para leer-escribir los archivos de texto*
- Módulo os => https://docs.python.org/es/3/library/os.html
  - *para tener los paths del directorio y todo eso XD*
- Módulo externo openpyxl => https://openpyxl.readthedocs.io/en/stable/tutorial.html
  - *Para leer y escribir libros y hojas de cálculo de excel*
- Módulo externo matplotlib => https://matplotlib.org/
  - *Puede que se use para hacer gráficas, si no se usan las de excel* 
- Módulo externo requests => https://pypi.org/project/requests/
  - *Se usará para hacer las requests a la API*

Recomiendo ampliamente revisar la documentación de estos módulos. Aún nos queda por cubrir la parte de los **JASON**.

## Instalaciones

- Openpyxl:
  Copiar el siguiente comando en terminal (cmd para Windows, bash, zsh, etc.):
  
  `pip install openpyxl`
  
- Matplotlib:
  Copiar el siguiente comando en terminal (cmd para Windows, bash, zsh, etc.):
  
  `pip install matplotlib`
  
- Requests:
  Copiar el siguiente comando en terminal (cmd para Windows, bash, zsh, etc.):
  
  `pip install requests`

## Fundamentos del código

Aquí voy a poner las ideas más básicas sobre cómo hacer las tareas del programa. Estos son muy seguramente códigos de ejemplo obtenidos de la
documentación de los módulos externos que estaremos trabajando en este proyecto.

### ExchangeRate requests en python

```python
import requests #módulo externo instalado con pip

url = 'https://v6.exchangerate-api.com/v6/TU-LLAVE-DEL-API/latest/USD'

# aquí debajo está el request:
response = requests.get(url)
data = response.json() # y lo guardamos con un jason!!!

print data
```

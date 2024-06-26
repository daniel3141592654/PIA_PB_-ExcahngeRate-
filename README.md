# PIA_PB_-ExcahngeRate-
Este código *(que aún no existe porque soy un procrastinador ligeramente compulsivo)* para ser compilado en **su máquina** requiere la instalación de
python 3.11 o superior (si no ha instalado python, hágalo desde la siiguiente liga https://www.python.org/ ) y de algunas librerías externas que se
listarán debajo:

- Módulo io => https://docs.python.org/es/3/library/io.html#module-io
  - *para leer-escribir los archivos de texto*
- Módulo os => https://docs.python.org/es/3/library/os.html
  - *para tener los paths del directorio y todo eso XD*
- Módulo para interpretar JSON => https://docs.python.org/es/3/library/json.html
  - `import json` 
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

print (data)
```

De igual forma, creo que es conveniente observar un json ejemplo generado por este simple código:

```json
{'result': 'success', 'documentation': 'https://www.exchangerate-api.com/docs', 'terms_of_use': 'https://www.exchangerate-api.com/terms',
'time_last_update_unix': 1714608001, 'time_last_update_utc': 'Thu, 02 May 2024 00:00:01 +0000', 'time_next_update_unix': 1714694401,
'time_next_update_utc': 'Fri, 03 May 2024 00:00:01 +0000',
'base_code': 'USD', 'conversion_rates': {'USD': 1, 'AED': 3.6725,
'AFN': 72.6104, 'ALL': 93.9282, 'AMD': 388.11, 'ANG': 1.79, 'AOA': 846.6323, 'ARS': 864.75, 'AUD': 1.5333, 'AWG': 1.79, 'AZN': 1.7005, 'BAM': 1.8271,
'BBD': 2.0, 'BDT': 109.8053, 'BGN': 1.827, 'BHD': 0.376, 'BIF': 2867.9919, 'BMD': 1.0, 'BND': 1.3617, 'BOB': 6.9257, 'BRL': 5.1902, 'BSD': 1.0,
'BTN': 83.4886, 'BWP': 13.8824, 'BYN': 3.2655, 'BZD': 2.0, 'CAD': 1.3726, 'CDF': 2772.0977, 'CHF': 0.917, 'CLP': 950.4617, 'CNY': 7.2362,
'COP': 3892.5629, 'CRC': 508.4119, 'CUP': 24.0, 'CVE': 103.0057, 'CZK': 23.4683, 'DJF': 177.721, 'DKK': 6.9662, 'DOP': 58.7234, 'DZD': 134.4385,
'EGP': 47.8508, 'ERN': 15.0, 'ETB': 57.396, 'EUR': 0.9342, 'FJD': 2.2613, 'FKP': 0.7982, 'FOK': 6.967, 'GBP': 0.7982, 'GEL': 2.6809,
'GGP': 0.7982, 'GHS': 13.7041, 'GIP': 0.7982, 'GMD': 66.5309, 'GNF': 8576.5276, 'GTQ': 7.7733, 'GYD': 209.2373, 'HKD': 7.8224, 'HNL': 24.7074,
'HRK': 7.0385, 'HTG': 132.5309, 'HUF': 364.8815, 'IDR': 16251.6195, 'ILS': 3.7487, 'IMP': 0.7982, 'INR': 83.4906, 'IQD': 1309.6862,
'IRR': 42028.6006, 'ISK': 140.3455, 'JEP': 0.7982, 'JMD': 156.2265, 'JOD': 0.709, 'JPY': 156.2678, 'KES': 134.8414, 'KGS': 88.9714,
'KHR': 4053.8218, 'KID': 1.5337, 'KMF': 459.5789, 'KRW': 1381.4981, 'KWD': 0.308, 'KYD': 0.8333, 'KZT': 442.0476, 'LAK': 21568.7934, 'LBP': 89500.0,
'LKR': 297.254, 'LRD': 193.6636, 'LSL': 18.6031, 'LYD': 4.8663, 'MAD': 10.1096, 'MDL': 17.6614, 'MGA': 4430.7055, 'MKD': 57.4157, 'MMK': 2098.5075,
'MNT': 3369.0677, 'MOP': 8.057, 'MRU': 39.432, 'MUR': 46.2952, 'MVR': 15.4406, 'MWK': 1738.402, 'MXN': 16.9722, 'MYR': 4.7718, 'MZN': 63.8494,
'NAD': 18.6031, 'NGN': 1358.3044, 'NIO': 36.8552, 'NOK': 11.0429, 'NPR': 133.5818, 'NZD': 1.6885, 'OMR': 0.3845, 'PAB': 1.0, 'PEN': 3.7648,
'PGK': 3.8197, 'PHP': 57.748, 'PKR': 278.5485, 'PLN': 4.0397, 'PYG': 7478.3162, 'QAR': 3.64, 'RON': 4.6612, 'RSD': 109.748, 'RUB': 93.6463,
'RWF': 1299.8681, 'SAR': 3.75, 'SBD': 8.4974, 'SCR': 13.7898, 'SDG': 511.4094, 'SEK': 10.941, 'SGD': 1.3617, 'SHP': 0.7982, 'SLE': 22.7233,
'SLL': 22723.343, 'SOS': 571.1372, 'SRD': 33.7365, 'SSP': 1586.7426, 'STN': 22.887, 'SYP': 12938.48, 'SZL': 18.6031, 'THB': 37.0507,
'TJS': 10.9199, 'TMT': 3.4984, 'TND': 3.1462, 'TOP': 2.3518, 'TRY': 32.3856, 'TTD': 6.7584, 'TVD': 1.5337, 'TWD': 32.5533, 'TZS': 2589.365,
'UAH': 39.5923, 'UGX': 3806.9317, 'UYU': 38.2699, 'UZS': 12593.787, 'VES': 36.473, 'VND': 25331.8854, 'VUV': 120.7431, 'WST': 2.7658,
'XAF': 612.7719, 'XCD': 2.7, 'XDR': 0.7591, 'XOF': 612.7719, 'XPF': 111.4757, 'YER': 250.1308, 'ZAR': 18.5928, 'ZMW': 26.7268, 'ZWL': 13.4301}}
```

De igual forma, dicho json se puede (y de hecho se debería) convertir a un diccionario de python, para así trabajarlo en el código .py que hicimos.
Debajo un ejemplo simple para traducir objetos de json a diccionarios de python:

```python
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
```

Usando el módulo de json, podemos guardar estos datos en una estructura propia de python ampliando el código:

```python
import requests
import json

url = 'https://v6.exchangerate-api.com/v6/TU-LLAVE-DEL-API/latest/USD'

# aquí debajo está el request:
response = requests.get(url)
data = response.json() # y lo guardamos con un jason!!!

data = json.dumps(data) # lo convertimos a string para así traducirlo un diccionario

dictData = json.loads(data)

print(dictData['result'])
```

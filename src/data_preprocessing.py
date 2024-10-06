import pandas as pd

# Importamos las datos en raw
infos = pd.read_csv("data/raw/infos.csv", delimiter="|")
items = pd.read_csv("data/raw/items.csv", delimiter="|")
orders = pd.read_csv("data/raw/orders.csv", delimiter="|")

# Combinamos los datos raw para que queden en un solo archivo
combined_data = orders.merge(infos, on="itemID").merge(items, on="itemID")
# Los exportamos para poder trabajar con ellos y tener una mejor organización
combined_data.to_csv("data/processed/processed_data.csv", index=False)

# Los importamos al script para trabajar con ellos
processed_data = pd.read_csv("data/processed/processed_data.csv")

# Usamos Feature engeneering para sacar la variable que nos ayudará a saber qué demanda tienen los productos
processed_data['demand'] = processed_data.groupby('itemID')['order'].transform('sum')

# Convertimos los datos de fecha de string a datetime
processed_data['time'] = pd.to_datetime(processed_data['time'])

# Una vez convertido a datetime los dividimos en año, mes, día, día de la semana y hora para un mejor manejo de los datos para el modelo
processed_data['year'] = processed_data['time'].dt.year
processed_data['month'] = processed_data['time'].dt.month
processed_data['day'] = processed_data['time'].dt.day
processed_data['dayofweek'] = processed_data['time'].dt.dayofweek
processed_data['hour'] = processed_data['time'].dt.hour

# Quitamos la columna de "time" porque ya los tenemos en divisiones
processed_data = processed_data.drop(columns=['time'])

# La columna de promoción para que no tenga valores nulos los convertimos con one-hot-encoding
processed_data['promotion'] = processed_data['promotion'].notna().astype(int)

processed_data.to_csv("data/processed/processed_data.csv", index=False)
import numpy as np
import pandas as pd
import random
from datetime import date , timedelta

random.seed(42)

regions = ['Nort', 'East','West']
products = ['Small', 'Medium', 'Large']

base = {"Small":100, "Medium":200, "Large":300}
rows = []

start = date.today() - timedelta(days = 730)
for i in range(730):
    d = start + timedelta(days = i)
    region = random.choice(regions)
    product = random.choice(products)
    volume = base[product] + random.randint(-30 , 30)
    if d.weekday() >=5:
        volume = volume * 1.2
    rows.append([d, round(volume, 2), region, product])    

data = pd.DataFrame(rows, columns = [ "date", "volume_litres", "region", "product_type"])
data.to_csv("data.csv", index = False)
print(len(data))
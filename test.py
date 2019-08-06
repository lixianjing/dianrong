
import pandas as pd
import datetime

res = pd.DataFrame(columns=('lib', 'qty1', 'qty2'))
res = res.append([0,1,0], ignore_index=True)
print(res.head())
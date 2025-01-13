import pandas as pd

l = pd.date_range('2024-08-15','2025-12-31', 
              freq='MS').strftime("%Y-%b").tolist()
print(l)

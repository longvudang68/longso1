import np as np
import pandas as pd
import numpy as np
data = pd.read_csv('D:\\New folder\\datagg.csv')
df = pd.DataFrame(data,columns=["Age", "Name"])
a = df[df.Name != 'Steve']
print(a["Age"].nlargest(2))
print(df)
























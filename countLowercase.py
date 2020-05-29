import pandas as pd
data = pd.read_csv("C:\\Users\\Admin\\Desktop\\New folder\\datagg.csv")

df =pd.DataFrame(data)
df.shape

# for row in df.itertuples():
#     print(row[1],row[2],row[3])
def fiandMaxAge(df):
    maxAge = df.Age[0]
    nem=df.Name[0]
    for row in df.itertuples():
        if maxAge < row[3]:
            maxAge = row [3]
            name = row[2]
    return name
print(fiandMaxAge(df))
def averageAgeRating(df1):
    sumAge = 0
    countIndex = 0
    sumRating = 0
    for row in df.itertuples():
        sumAge +=row[3]
        sumRating+=row[4]
        countIndex+=1
    return sumAge/countIndex,sumRating/countIndex
print(averageAgeRating(df))










import pandas as pd
import random
columns = pd.read_csv("header.csv")
print(len(columns.columns))
organizations = ["COL","BGS","MAN","APO","FOR"]
data_list=[]
for i in range(1000):
    data = []
    p_id = "P"+str(i)
    data.append(p_id)
    for each in range(25):
        data.append(random.randint(0, 1))
    data_list.append(data)
for i in range(15):
    data = []
    p_id = "P"+str(i+1000)
    data.append(p_id)
    for each in range(25):
        data.append(random.randint(1, 1))
    data_list.append(data)
for i in range(1005):
    data = []
    p_id = "P"+str(i+1015)
    data.append(p_id)
    for each in range(10):
        data.append(random.randint(1, 1))
    for each in range(15):
        data.append(random.randint(0, 1))
    data_list.append(data)

print(data_list)
df=pd.DataFrame(data_list,columns=columns.columns)
print(df)
df.to_csv('patient_cluster.csv')

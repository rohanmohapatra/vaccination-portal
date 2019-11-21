import pandas as pd
import random
import pandas as pd
import random


classes = ["poor","complete","medium"]
columns = pd.read_csv("header_2.csv")
print(len(columns.columns))
data_list=[]
listVac = [1,5,4,4,2,2,1]
for i in range(1000):
    data = []
    p_id = "P"+str(i)
    data.append(p_id)
    for each in range(7):
        data.append(random.randint(0, listVac[each]))
    data.append(classes[0])
    data_list.append(data)
for i in range(15):
    data = []
    p_id = "P"+str(i+1000)
    data.append(p_id)
    for each in range(7):
        data.append(random.randint(listVac[each], listVac[each]))
    data.append(classes[1])
    data_list.append(data)
for i in range(1005):
    data = []
    p_id = "P"+str(i+1015)
    data.append(p_id)
    for each in range(4):
        data.append(random.randint(listVac[each], listVac[each]))
    for each in range(3):
        data.append(random.randint(0, listVac[each]))
    data.append(classes[2])
    data_list.append(data)

print(data_list)
df=pd.DataFrame(data_list,columns=columns.columns)
print(df)
df.to_csv('patient_classes2.csv')

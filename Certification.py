# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot = pd.DataFrame(columns=['robot', 'human'])

for i in range(len(data['whoAmI'])):
    if data['whoAmI'][i] == 'robot':
        one_hot = pd.concat([one_hot, pd.DataFrame({'robot': [1], 'human': [0]})], ignore_index=True)
    else:
        one_hot = pd.concat([one_hot, pd.DataFrame({'robot': [0], 'human': [1]})], ignore_index=True)

data = data.drop('whoAmI', axis=1)
data = data.join(one_hot)

data.head()

import time
start_time = time.time()

import pickle
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.instagram.com/m__ali__hasnain/")
print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())



pickled_model = pickle.load(open('data/model.pkl', 'rb'))

vector_x = {'profile pic':[0],
'nums/length username':     [0.42],
'fullname words':          [1.0],
'nums/length fullname':     [0.0],
'name==username' :          [0.0],
'description length' :     [0.0],
'external URL'   :          [0.0],
'private'      :            [0.0],
'#posts'       :            [0.0],
'#followers'   :        [16.0],
'#follows'    :            [2.0]
}

df_vector_x = pd.DataFrame(vector_x)
y_pred = pickled_model.predict(df_vector_x)
print('Real' if y_pred==[1] else 'Fake')
print("--- %s seconds ---" % (time.time() - start_time))
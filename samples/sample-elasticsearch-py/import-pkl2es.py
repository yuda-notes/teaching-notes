# pandas version 2.3.1
import pandas as pd
import numpy as np
np.float_ = np.float64

# es version 7.13.4
from elasticsearch import Elasticsearch

# initialize ES
es = Elasticsearch("http://localhost:9200")

# read pickle sample
df = pd.read_pickle('survey-stack-overflow-2022.pkl')

# perform import
for i, r in df.iterrows():
    doc = r.to_json()
    res = es.index(
        index="survey-stack-overflow-2022",
        body=doc
    )

print("all set!")

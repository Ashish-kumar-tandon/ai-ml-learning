
import pandas as pd
from sklearn.cluster import DBSCAN

data = {
    'study_hours': [1, 2, 3, 2, 4, 5, 6, 7, 8, 9, 3, 6, 8, 4, 9],
    'attendance': [30, 40, 50, 35, 55, 70, 80, 85, 90, 95, 45, 75, 95, 60, 98]
}

df = pd.DataFrame(data)

X = df[['study_hours', 'attendance']]

model = DBSCAN(eps=8, min_samples=3)

model.fit(X)

df['cluster'] = model.labels_

print(df)


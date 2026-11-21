# Principal Component Analysis

import pandas as pd
from sklearn.decomposition import PCA

data = {
    'study_hours': [1, 2, 3, 2, 4, 5, 6, 7, 8, 9, 3, 6, 8, 4, 9],
    'attendance': [30, 40, 50, 35, 55, 70, 80, 85, 90, 95, 45, 75, 95, 60, 98],
    'assignment_score': [20, 30, 40, 35, 50, 65, 75, 80, 85, 95, 45, 70, 90, 55, 98],
    'previous_marks': [25, 35, 45, 30, 55, 70, 80, 85, 90, 95, 40, 75, 92, 60, 98]
}

df = pd.DataFrame(data)

X = df

model = PCA(n_components=2)

X_pca = model.fit_transform(X)

df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])

print(df_pca)


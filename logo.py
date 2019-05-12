from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

import pandas as pd
a = pd.DataFrame(cancer.data, columns=cancer.feature_names)


print(a)
import pandas as pd

iris = pd.read_csv('Iris.csv')

iris.info()
 
# melihat informasi dataset pada 5 baris pertama
iris.head()


iris.drop('Id',axis=1,inplace=True)


# X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm' ]]
# y = iris['Species']
 
# # Membagi dataset menjadi data latih & data uji
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=123)
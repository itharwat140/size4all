from dis import dis
from unittest import result
import pandas as pd
from math import dist, sqrt
from datahandling import main
from sklearn.neighbors import KNeighborsClassifier

def get_neighbors (k, height, weight, data_source):
    dists= []
    for point in data_source:
        x = point [1]
        y = point [2]
        size = point [3]
        dist = sqrt((weight-x)**2 + (height-y)**2)
        dists.append({'dist' : dist, 'size' : size})
    dists.sort(key = lambda d: d['dist'])
    return dists[:k]

def predict(neighbors):
    allSize = {}
    for dist_item in neighbors:
        size = dist_item ['size']
        if size in allSize:
            allSize [size] += 1
            else:
                allSize [size] = 1
    k = len(neighbors)
    return {size : value / k * 100 for size, value in allSize.items()}

def main (): 
    data_male = pd.read_csv ('../male.csv')
    data_femal = pd.read_csv ('C:\size4all\female.csv')

    df = data_male.values.tolist() + data_male.values.tolist()

    n = int(sqrt(len(df)))
    k_values = [3, 5, 7, 9, 11, n]

    height = int (input('How tall are you?   '))
    Weight = int (input('How fat are you?    '))

    for k in K_values:
        neighbours = get_neighbors(k, weight, height, df)
        result = predict(neighbors)
        print(f'I think you should buy a shirt size : (k={k}')
        for size, proc in result.items():
            print (f\t{size} with a confidence of {proc :.2f}%')
        print('-'*40)
        weights = [data[1] for data in df]
        heights = [data[2] for data in df]
        labels = [data [4] for data in df]
        data = list(zip(weights, heights))
        knn_model = KNeighborsClassifier(n_neighbors = k)
        knn_model.fit(data, labels)
        print(f'sklearn predicted: {knn_model.predict([[weight, height]])} for k={k}')

if __name__ == '__main__':
    main()





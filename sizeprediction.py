import pandas as pd
from math import sqrt
from sklearn.neighbors import KNeighborsClassifier

def get_neighbours(k, height, weight, data_list):
    dists = []
    for point in data_list:
        x = point[2]
        y = point[1]
        size = point[4]
        dist = sqrt((weight-x)**2 + (height-y)**2)
        dists.append({'dist': dist, 'size': size})

    dists.sort(key=lambda d: d['dist'])
    return dists[:k]

def predict(neighbours):
    sizes = {}
    for dist_item in neighbours:
        size = dist_item['size']
        if size in sizes:
            sizes[size] += 1
        else:
            sizes[size] = 1

    k = len(neighbours)
    return {size: value / k * 100 for size, value in sizes.items()}


def main():
    data_female = pd.read_csv('sorted_female_db.csv')
    data_male = pd.read_csv('sorted_male_db.csv')

    df = data_female.values.tolist() + data_male.values.tolist()
    n = int(sqrt(len(df)))
    k_values = [3, 5, 7, 9, 11, n]
    height = int(input('How tall are you?  '))
    weight = int(input('How much do you weight?  '))

    for k in k_values:
        neighbours = get_neighbours(k, height, weight, df)
        result = predict(neighbours)
        print(f'you should buy a shirt size: (k={k})')
        for size, proc in result.items():
            print(f'\t{size} with a confidence of {proc :.2f}%')
        print('-'*40)
        heights = [data[1] for data in df]
        weights = [data[2] for data in df]
        labels = [data[4] for data in df]
        data = list(zip(weights, heights))
        knn_model = KNeighborsClassifier(n_neighbors=k)
        knn_model.fit(data, labels)
        print(f'sklearn predicted: {knn_model.predict([[weight, height]])} for k={k}')
        print('-'*40)

if __name__ == '__main__':
    main()
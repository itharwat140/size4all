import pandas as pd


class Person:
    def __init__(self, age, height, weight, chest, size):
        self.age = age
        self.height = height
        self.weight = weight
        self.chest = chest
        self.size = size

    def __str__(self):
        return f'{self.age},{self.height},{self.weight},{self.chest},{self.size}\n'


def prepare_data(df, file_name):
    ages = df.Age.tolist()
    heights = [s/10 for s in df.stature.tolist()]
    weights = [w/10 for w in df.weightkg.tolist()]
    chests = [c/10 for c in df.chestcircumference.tolist()]

    with open(file_name, 'w') as out_file:
        out_file.write('Age,Height,Weight,Chest,Size\n')
        for i in range(len(ages)):
            chest = chests[i]

            if chest < 84:
                size = 'XXS'
            elif chest < 90:
                size = 'XS'
            elif chest < 95:
                size = 'S'
            elif chest < 102:
                size = 'M'
            elif chest < 112:
                size = 'L'
            elif chest < 123:
                size = 'XL'
            elif chest < 133:
                size = 'XXL'
            else:
                size = 'XXXL'

            person = Person(ages[i], heights[i], weights[i], chest, size)
            out_file.write(str(person))


def main():
    df = pd.read_csv('female.csv')
    prepare_data(df, 'sorted_female_db.csv')
    df = pd.read_csv('male.csv')
    prepare_data(df, 'sorted_male_db.csv')


if __name__ == '__main__':
    main()
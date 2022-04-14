from multiprocessing.spawn import prepare
import pandas as pd

class Customer:
    def __init__(self, age, weight, height, size, chest ):
        self.age = age
        self.weight = weight
        self.hight = height
        self.size = size
        self.chest = chest

    def __str__(self):
        return f'{self.age}, {self.weight}, {self.height}, {self.size}, {self.chest}\n'

def prepare_data (df, file_name):
    ages = df.Age.tolist()
    weights = [w/10 for w in df.weightkg.tolist()]
    heights = [h/10 for h in df.stature.tolist()]
    chests = [c/10 for c in df.chestcircumference.tolist()]

    with open(file_name, 'w') as out_file:
        out_file.write('Age, Weight, Height, Size, Chest\n')
        for i in range(len(ages)):
            chest = chests[i]
            if chest < 84:
                size = 'xxs'
            elif chest < 90:
                size = 'xs'
            elif chests < 95:
                size = 's'
            elif chest < 102:
                size = 'M'
            elif chest < 112:
                size = 'L'
            elif chest < 123:
                size = 'XL'
            elif chest < 133:
                size = 'xxl'
            else:
                size = 'XXXL'

            customer = Customer(ages[i], weights[i], heights[i], size, chest)
            out_file.write(str(customer))


def main():
    df = pd.read_csv('C:\size4all\male.csv')
    prepare_data (df, 'C:\size4all\ready_male_database.csv')
    df = pd.read_csv('C:\size4all\female.csv')
    prepare_data (df, 'C:\size4all\ready_female_database.csv')
if __name__ == '__main__':
    main()
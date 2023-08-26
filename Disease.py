import csv

def list_column_names(csv_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        return reader.fieldnames

if __name__ == '__main__':
    csv_file_path = "dataset/Training.csv"
    column_names = list_column_names(csv_file_path)

    print("Column names:")
    for name in column_names:
        print(name)
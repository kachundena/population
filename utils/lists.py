import csv
def getListFromCSV(file):
    file = open(file, "r", encoding="utf8")
    csv_reader = csv.reader(file)
    _list = []
    for row in csv_reader:
        _list.append(row)
    return _list

def getValueListFromPosition(list, position):
    value = list[position]
    return value
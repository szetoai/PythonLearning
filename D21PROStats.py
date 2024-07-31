import statistics as st

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
class data():
    def __init__(self, input):
        self.data = input
    def count(self):
        return st.count(self.data)
    
output = data(ages)
print(output.count())
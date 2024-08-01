import statistics as st


class data():
    def __init__(self, input):
        self.info = input
    def count(self):
        return len(self.info)
    def sum(self):
        out = 0
        for x in self.info:
            out += x
        return out
    def min(self):
        low = self.info[0]
        for x in self.info:
            if low < x:
                low = x
        return low
    def min(self):
        return min(self.info)
    def max(self):
        return max(self.info)
    def range(self):
        return max(self.info) - min(self.info)
    def mean(self):
        return st.mean(self.info)
    def median(self):
        return st.median(self.info)
    def mode(self):
        return st.mode(self.info)
    def stdev(self):
        return st.stdev(self.info)
    def variance(self):
        return st.variance(self.info)
    def frequency(self):
        return st.NormalDist(self.info)

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
output = data(ages)
print(f"Count: {output.count()}")
print(f"Sum: {output.sum()}")
print(f"Min: {output.min()}")
print(f"Max: {output.max()}")
print(f"Range: {output.range()}")
print(f"Mean: {output.mean()}")
print(f"Median: {output.median()}")
print(f"Mode: {output.mode()}")
print(f"Variance: {output.variance()}")
print(f"StDev: {output.stdev()}")

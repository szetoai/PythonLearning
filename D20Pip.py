'''
installing: pip install numpy, pip install pandas
deleting: pip uninstall packagename
see installed packages: pip list
show package info: pip show packagename
'''

import numpy as np, pandas as pd, webbrowser as wb

print(np.version.version)
lst = [1, 2, 3, 4, 5]
np_arr = np.array(lst)
print(np_arr)
print(len(np_arr))
print(np_arr * 2 + 3)
wb.open_new_tab("youtube.com")
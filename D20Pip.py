'''
installing: pip install numpy, pip install pandas
deleting: pip uninstall packagename
see installed packages: pip list
show package info: pip show packagename ("show --verbose" for more details)
show packages used: pip freeze
'''

import numpy as np, pandas as pd, webbrowser as wb

"""
# numpy
print(np.version.version)
lst = [1, 2, 3, 4, 5]
np_arr = np.array(lst)
print(np_arr)
print(len(np_arr))
print(np_arr * 2 + 3)
# webbrowser
wb.open_new_tab("youtube.com")


# requests
import requests
response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200 
print(response.json())  # response as json
print(response.text) # response as text
print(response.headers) # response's headers
"""

"""
CHECK OUT PACKAGES LATER
"""
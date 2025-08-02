#numpy
import micropip

await micropip.install("numpy")
await micropip.install("pandas")

# Now you can import and use them
import numpy as np
import pandas as pd
""""
print(f'NumPy version: {np.__version__}')
print(f'Pandas version: {pd.__version__}')

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
"""
import os
import numpy as np

random = np.random.randn(1)

with open(file='db.txt', mode='w', encoding='utf-8') as txt:
    txt.write(str(random[0]))

print(random)
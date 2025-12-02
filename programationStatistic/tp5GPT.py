import matplotlib.pyplot as plt
import pandas as pd
import math

notes = [8, 10, 11, 12, 13, 13, 14, 15, 17, 18, 20, 21, 25]

notes.sort()

if len(notes)%2 == 0:
    data = len(notes) // 2
    Q2 = (notes[data] + notes[data-1]) / 2
else:
    Q2 = len(notes) // 2

print(notes[Q2])    

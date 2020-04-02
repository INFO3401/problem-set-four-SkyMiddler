import pandas as pd
import matplotlib.pyplot as plt


def loadAndCleanData(fileName):
    openFile = pd.read_csv(fileName)
    openFile.fillna(value = 0, inplace = True)
    return openFile

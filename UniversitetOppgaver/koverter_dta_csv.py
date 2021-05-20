import pandas as pd
data = pd.io.stata.read_stata('D:/Samfunnsøkonomi/Semester 6/ECON343/Empirisk_forskningsdesign/Data/analysefil.dta')
data.to_csv('my_stata_file.csv')
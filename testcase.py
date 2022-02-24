from fits2jd.convert import fits2jd
import pandas as pd

x = fits2jd("./data/sample_input.csv")
y = x.transform()
print(y)

# optional
# y = pd.Series(y)
# print(y)

# pd.Series(y).to_csv("test.csv", header=False, index=False)
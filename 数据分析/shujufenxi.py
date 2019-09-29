from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

t = np.array((np.arange(12))).reshape(3, 4)
print("array:\n", t)

t1 = pd.Series(np.arange(5), index=list("abcde"))
print("Series:\n", t1)

df = pd.DataFrame(t, columns=list("ABCD"))
print("DataFrame:\n", df)


# plt.plot(t.flatten()[:5], list(t1))
# plt.show()

data = pd.read_csv("./911.csv")
data['timeStamp'] = pd.to_datetime(data['timeStamp'])
data.set_index('timeStamp', inplace=True)
counts = data.resample("M").count()['title']
print(counts.index)
_x = [i.strftime("%Y%m%d") for i in counts.index]
print(_x)

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(np.arange(len(counts.index)), counts.values)
plt.xticks(np.arange(len(counts.index)), _x, rotation=45)
plt.show()



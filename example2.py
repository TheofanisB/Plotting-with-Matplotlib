import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('dedomena.xlsx')
print(data)


df = pd.DataFrame(data, columns=['T*C*S*R', 'PostCMA', 'T*C*R', 'T*C'])
df.plot(kind='line')
plt.show()

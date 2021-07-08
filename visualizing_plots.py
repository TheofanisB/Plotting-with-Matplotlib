import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Setting the directory
# Creating the dataflow
# The xlsx file should be on the same folder as the python file, otherwise we have to change the file path
df = pd.read_excel('data_file_to_pull_data_from.xlsx', 'Sheet1')


# Creating the subplots

# 10 charts , sharing x and y axis and setting the figure size to 20 by 20
fig, axs = plt.subplots(10, sharex=True, sharey=True, figsize=(20, 20))
fig.suptitle('Power Consumption Charts')#Example title
plt.tight_layout(pad=5.0)
axs[0].plot(df['Timestamp'], df['No 1']) #giving the dataframe a title
axs[0].set_title('No 1')
axs[0].set_facecolor('#C0C0C0')#graph background color
axs[0].plot(color='m')#magenta 
axs[1].plot(df['Timestamp'], df['No 2'])
axs[1].set_title('No 2')
axs[1].set_facecolor('#C0C0C0')
axs[1].plot(color='m')
axs[2].plot(df['Timestamp'], df['No 3'])
axs[2].set_title('No 3')
axs[2].set_facecolor('#C0C0C0')
axs[2].plot(color='m')
axs[3].plot(df['Timestamp'], df['No 4'])
axs[3].set_title('No 4')
axs[3].set_facecolor('#C0C0C0')
axs[3].plot(color='m')
axs[4].plot(df['Timestamp'], df['No 5'])
axs[4].set_title('No 5')
axs[4].set_facecolor('#C0C0C0')
axs[4].plot(color='m')
axs[5].plot(df['Timestamp'], df['No 6'])
axs[5].set_title('No 6')
axs[5].set_facecolor('#C0C0C0')
axs[5].plot(color='m')
axs[6].plot(df['Timestamp'], df['No 7'])
axs[6].set_title('No 7')
axs[6].set_facecolor('#C0C0C0')
axs[6].plot(color='m')
axs[7].plot(df['Timestamp'], df['No 8'])
axs[7].set_title('No 8')
axs[7].set_facecolor('#C0C0C0')
axs[7].plot(color='m')
axs[8].plot(df['Timestamp'], df['No 9'])
axs[8].set_title('No 9')
axs[8].set_facecolor('#C0C0C0')
axs[8].plot(color='m')
axs[9].plot(df['Timestamp'], df['No 10'])
axs[9].set_title('No 10')
axs[9].set_facecolor('#C0C0C0')
axs[9].plot(color='m')
print('The Average values are:')
print(df[['No 1']].mean(), '\n', df[['No 2']].mean(), '\n', df[['No 3']].mean(), '\n', df[['No 4']].mean(), '\n', df[['No 5']].mean(
), '\n', df[['No 6']].mean(), '\n', df[['No 7']].mean(), '\n', df[['No 8']].mean(), '\n', df[['No 9']].mean(), '\n', df[['No 10']].mean())
plt.show()

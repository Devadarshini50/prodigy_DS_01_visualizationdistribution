
import pandas as pd
import matplotlib.pyplot as plt

# Bar chart for categorical data
labels = ['Male', 'Female', 'Other']
counts = [50, 45, 5]

plt.bar(labels, counts, color=['blue', 'pink', 'green'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Distribution')
plt.show()

# histogram for continuous data
ages = [22, 25, 30, 22, 40, 35, 29, 30, 25, 28, 32, 31, 29, 40, 41, 30, 28, 35, 36, 38]

plt.hist(ages, bins=5, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()

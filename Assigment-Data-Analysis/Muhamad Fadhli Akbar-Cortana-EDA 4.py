import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Membuat dataframe dari 2019_Yellow_Taxi_Trip_Data.csv
df = pd.read_csv('2019_Yellow_Taxi_Trip_Data.csv')

# 2. Mencari dimensi (baris dan kolom) dari dataframe
print("Dimensi dataframe:")
print(f"Jumlah baris: {df.shape[0]}")
print(f"Jumlah kolom: {df.shape[1]}")

# 3. Menghitung summary statistics
columns_of_interest = ['fare_amount', 'tip_amount', 'tolls_amount', 'total_amount']
summary_stats = df[columns_of_interest].describe()
print("\nSummary Statistics:")
print(summary_stats)

# 4. Membuat tabel khusus untuk perjalanan terpanjang
longest_trip = df.loc[df['trip_distance'].idxmax()]
print("\nTabel untuk perjalanan terpanjang:")
print(longest_trip[columns_of_interest])

# 5. Membuat scatter plot, joint plot, dan scatter plot dengan legenda
# Catatan: Kita tidak memiliki 'petal length' dan 'petal width' dalam dataset ini.
# Kita akan menggunakan 'trip_distance' dan 'total_amount' sebagai gantinya.

plt.figure(figsize=(10, 6))
plt.scatter(df['trip_distance'], df['total_amount'])
plt.xlabel('Trip Distance')
plt.ylabel('Total Amount')
plt.title('Scatter Plot: Trip Distance vs Total Amount')
plt.savefig('scatter_plot.png')
plt.close()

sns.jointplot(x='trip_distance', y='total_amount', data=df, kind='scatter')
plt.savefig('joint_plot.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='trip_distance', y='total_amount', hue='payment_type', data=df)
plt.xlabel('Trip Distance')
plt.ylabel('Total Amount')
plt.title('Scatter Plot: Trip Distance vs Total Amount (with Payment Type)')
plt.savefig('scatter_plot_with_legend.png')
plt.close()

# 6. Membuat boxplot dan strip plot
# Catatan: Kita tidak memiliki 'PetalWidthCm' dalam dataset ini.
# Kita akan menggunakan 'total_amount' dikelompokkan berdasarkan 'payment_type' sebagai gantinya.

plt.figure(figsize=(10, 6))
sns.boxplot(x='payment_type', y='total_amount', data=df)
plt.xlabel('Payment Type')
plt.ylabel('Total Amount')
plt.title('Box Plot: Total Amount by Payment Type')
plt.savefig('box_plot.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.stripplot(x='payment_type', y='total_amount', data=df, jitter=True)
plt.xlabel('Payment Type')
plt.ylabel('Total Amount')
plt.title('Strip Plot: Total Amount by Payment Type')
plt.savefig('strip_plot.png')
plt.close()

print("Semua plot telah disimpan sebagai file gambar.")
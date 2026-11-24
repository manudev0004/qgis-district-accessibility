import pandas as pd


df = pd.read_csv('pa.csv') 

# df = pd.DataFrame(data)
average_df = df.groupby('name')['Norm_Final'].mean().reset_index()
# average_df = df.groupby('NAME_2')['Rail_Length'].sum().reset_index()

print(average_df)


average_df.to_csv('avg_pa.csv', index=False)

import pandas as pd

# Create a sample DataFrame with null values
data = {'A': [1, 2, None, 4, 5],
        'B': [None, 2, 3, None, 5]
       
        }

df = pd.DataFrame(data)

# Detect null values in the DataFrame
null_df = df.isnull()

# Summarize the number of null values in each column
null_counts = null_df.sum()

# Summarize the number of null values in the entire DataFrame
total_null_count = null_df.sum().sum()

val={'A':-1,'B':10}

res = df.fillna(val)
print("Null values in each column:")
print(null_counts)

print(f"Total null values in the DataFrame: {total_null_count}")

   

   
   
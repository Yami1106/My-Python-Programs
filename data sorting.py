import pandas as pd

data = """
270454.ANTYA   $ lucky.s $ serialq  xoopic_0.* 243403   1   1    --  360:0 R 48:35
270458.ANTYA   $ suruj.k $ mediumq  spot_k1.0*  76343   4   8    --  48:00 R 39:04
270459.ANTYA   $ suruj.k $ mediumq  spot_k4.0* 196850   4   8    --  48:00 R 38:56
270474.ANTYA   $ sagar.c $ mediumq  n16_non_l* 264967  48  15    --  48:00 R 26:45
"""

df = pd.read_csv(io.StringIO(data), header=None, names=['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8'])

# Center the column names
df.columns = df.columns.str.center(15)

# Print the DataFrame with the column names right above the columns
print(df.style.set_properties(**{'text-align': 'center'}).to_string(index=True))

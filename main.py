import pandas as pd
import math

# Define a matrix containing link station x,y, the reach and device points
data = [
    [0, 0, 10, 0, 0],
    [0, 0, 10, 100, 100],
    [0, 0, 10, 15, 10],
    [0, 0, 10, 18, 18],
    [20, 20, 5, 0, 0],
    [20, 20, 5, 100, 100],
    [20, 20, 5, 15, 10],
    [20, 20, 5, 18, 18],
    [10, 0, 12, 0, 0],
    [10, 0, 12, 100, 100],
    [10, 0, 12, 15, 10],
    [10, 0, 12, 18, 18]
]

# Convert the matrix into DataFrame
df = pd.DataFrame(data, columns=['x1', 'y1', 'r', 'x2', 'y2'])
print("Given Dataframe :\n", df)

# iterate through each row and select
# 'x1', 'y1', 'r', 'x2' and 'y2' column respectively.

for i in range(len(df)):
    distance = math.sqrt((df.loc[i, "x2"] - df.loc[i, "x1"])**2 + (df.loc[i, "y2"] - df.loc[i, "y1"])**2)
    print("\nDistance between link station and device: ", distance)
    if distance > df.loc[i, "r"]:
        power = 0
        print("\nNo link station within reach for point x,y")
    else:
        power = (df.loc[i, "r"] - distance)**2
        print("\nBest link station for point x,y is x,y with power z: ", power)
#note has been inserted

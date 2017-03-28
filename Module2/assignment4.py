import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
df = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')[0]


# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
headers = df.iloc[1]
df_headers = df[2:]
df_headers = df_headers.rename(columns = headers)


# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
df_fournan = df_headers.dropna(axis = 0, thresh = 4)


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#


# TODO: Get rid of the 'RK' column
#
df_header_fix.drop('RK', axis = 1)

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..



# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
# .. your code here ..



# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
# .. your code here ..


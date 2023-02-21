import pandas as pd

# Load the tweets data into a pandas dataframe
df = pd.read_csv('your_original_csv_file.csv')

# Create a new dataframe for the edges
edges_df = pd.DataFrame(columns=['Source', 'Target', 'Weight'])

# Loop through each user and their retweeted users to create the edges
for user, retweets in zip(df['user.screen_name'], df['retweeted_status.user.screen_name']):
    if pd.isna(retweets):
        continue
    # Split the retweeted users string into a list
    retweeted_users = retweets.strip('][').split(', ')
    
    # Loop through the retweeted users and add an edge to the edges dataframe
    for retweeted_user in retweeted_users:
        edges_df = pd.concat([edges_df, pd.DataFrame({'Source': [user], 'Target': [retweeted_user.strip("'")], 'Weight': [1]})])

# Save the edges dataframe to a CSV file
edges_df.to_csv('your_oriignal_csv_file_gephi.csv', index=False)

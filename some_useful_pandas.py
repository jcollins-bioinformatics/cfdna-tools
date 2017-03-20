

# Split header and all rows of df that was not properply delimited,
# & reassign by proper separation of cells 
new_df = pd.DataFrame(columns=df.columns.str.split()[0])
for row in df.iterrows():
    fields = str(row[1].values)[1:-1].split()
    for i,col in enumerate(new_df.columns):
       new_df.loc[row[0], col] = fields[i]


# Convert strings to float and skip over NaN's
new_df['#CHROM'] = new_df['#CHROM'].apply(lambda f: float(f[1:])
                                                    if pd.notnull(f) else f)



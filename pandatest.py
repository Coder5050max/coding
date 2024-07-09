import pandas as pd

# Load the datasets
df1 = pd.read_excel('Copy of Student(1).xlsx')
df2 = pd.read_excel('Copy of Marks(1).xlsx')

# Perform an inner join (choose one type of merge for the final dataset)
df = pd.merge(df1, df2, on="Roll_Number", how="inner")
print("Merged DataFrame:\n", df)

# Normalize the names for comparison
df['First_Name'] = df['First_Name'].str.strip().str.lower()
df['Last_Name'] = df['Last_Name'].str.strip().str.lower()

# List of students absent in particular exams
es_absent = df[df['ES'].isna()]
dlld_absent = df[df['DLLD'].isna()]
pps_absent = df[df['PPS'].isna()]
hnm_absent = df[df['HNM'].isna()]
ist_absent = df[df['IST'].isna()]
etw_absent = df[df['ETW'].isna()]

print("ES Absent:\n", es_absent)
print("DLLD Absent:\n", dlld_absent)
print("PPS Absent:\n", pps_absent)
print("HNM Absent:\n", hnm_absent)
print("IST Absent:\n", ist_absent)
print("ETW Absent:\n", etw_absent)

# Fill NaN values and update DataFrame
marksheet_filled = df.fillna(9)
print("DataFrame with filled NaN values:\n", marksheet_filled)

# Update the DataFrame
df.update(marksheet_filled)

# Save the updated DataFrame to a new Excel file to avoid overwriting the original
df.to_excel('Updated_Marks.xlsx', index=False)

# Load the updated Excel file to confirm changes
new_df = pd.read_excel('Updated_Marks.xlsx')
print("Updated DataFrame from Excel:\n", new_df)

# Normalize the names in the new DataFrame as well
new_df['First_Name'] = new_df['First_Name'].str.strip().str.lower()
new_df['Last_Name'] = new_df['Last_Name'].str.strip().str.lower()

# Filter for Sairaj Bahirat's marksheet
sairaj_marksheet = new_df.loc[
    (new_df['First_Name'] == 'sairaj') & 
    (new_df['Last_Name'] == 'bahirat')
]

print("Sairaj Bahirat's Marksheet:\n", sairaj_marksheet)
# My percenatge
subject_columns = [ 'ES', 'DLLD', 'PPS', 'HNM','IST','ETW']
total_marks_obtained = sairaj_marksheet[subject_columns].sum(axis=1).values[0]
total_possible_marks = 10 * len(subject_columns)
percentage = (total_marks_obtained / total_possible_marks) * 100

print(percentage)

sahil_marksheet=new_df.loc[
    (new_df['First_Name']== 'sahil') &
    (new_df['Last_Name']== 'sharma')
]

print(sahil_marksheet)

# SahiL Sharma Marksheet
subject_columns = [ 'ES', 'DLLD', 'PPS', 'HNM','IST','ETW']
total_marks_obtained = sahil_marksheet[subject_columns].sum(axis=1).values[0]
total_possible_marks = 10 * len(subject_columns)
percentage = (total_marks_obtained / total_possible_marks) * 100
print(percentage)

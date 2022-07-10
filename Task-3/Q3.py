import pandas as pd 
df= pd.read_csv('Cognizance\Resources\Task-3\Q3.csv')
df=df.drop(columns=['ID','Gender','DOB','10board','12board','Degree','CollegeID','12graduation','CollegeCityID','CollegeState','ComputerScience', 'MechanicalEngg', 'ElectricalEngg', 'TelecomEngg',
       'CivilEngg', 'conscientiousness','Specialization','agreeableness','CollegeCityTier','GraduationYear','extraversion',
       'nueroticism'])
print(df.head())
# Here we have successfully made the data clean and clear so that any ML techniquie is used to figure the output.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

patients = pd.read_csv('Hospital-project\\Data\\patients.csv')
admissions = pd.read_csv('Hospital-project\\Data\\admissions.csv')
labs = pd.read_csv('Hospital-project\\Data\\labs.csv')
medications = pd.read_csv('Hospital-project\\Data\\medications.csv')
readmissions = pd.read_csv('Hospital-project\\Data\\readmissions.csv')
print("All files are loaded successfully!")

admissions = admissions.merge(patients[['patient_id' , 'dob']] , on= 'patient_id' , how= 'left')
print("Merged Data:" , admissions)
admissions['dob'] = pd.to_datetime(admissions['dob'])
admissions['admit_datetime'] = pd.to_datetime(admissions['admit_datetime'])
admissions['age'] = ((admissions['admit_datetime'] - admissions['dob']).dt.days / 365).astype(int)
print("Age:" , admissions['age'])

admissions['discharge_datetime'] = pd.to_datetime(admissions['discharge_datetime'])
admissions['los'] = (admissions['discharge_datetime'] - admissions['admit_datetime']).dt.days
print("Length of days:" , admissions['los'])

labs['abnormal'] = ((labs['test_value'] < labs['normal_low']) | (labs['test_value'] > labs['normal_high']))
print("Test is abnormal or not:" , labs['abnormal'])
labs_data = labs.groupby('admit_id')['abnormal'].sum().reset_index()
labs_data.rename(columns= {'abnormal' : 'Test Results'} , inplace= True)
print("Final table" , labs_data)

admissions_lab_merged = admissions.merge(labs_data , left_on= 'admission_id' , right_on= 'admit_id' , how= 'left')
print("Admission and labs data merged:" , admissions_lab_merged)

med = medications.groupby('admit_id')['med_name'].nunique().reset_index()
print("Total number of meds:" , med)
med.rename(columns={'med_name' : 'num_med'} , inplace= True)
admissions_lab_meds_merged = admissions_lab_merged.merge(med , left_on= 'admission_id' , right_on= 'admit_id' , how= 'left')
print("Admissions ,Labs and Meds merged:" , admissions_lab_merged)

final_df = admissions_lab_meds_merged.merge(readmissions[['patient_id' , 'readmitted_within_30d']] , on= 'patient_id' , how= 'left')
print("Final data!!" , final_df)

graph = sns.displot(data= final_df , x = 'age' , y = 'patient_id' , kind= 'hist')
graph.figure.suptitle(" sns.displot(data= final_df , x = 'age' , y = 'patient_id' , kind= 'hist')")
graph.figure.show()
read = input("Wait for me...")

graph = sns.barplot(data= final_df , x = 'department' , y = 'readmitted_within_30d' , legend= False)
graph.figure.suptitle("sns.barplot(data= final_df , x = 'department' , y = 'readmitted_within_30d' , legend= False)")
graph.figure.show()
read = input("Wait or me...")

final_df['risk_score'] = (
    final_df['age']  * 0.02 +
    final_df['los'] *  0.1 +
    final_df['Test Results'] * 0.05 +
    final_df['num_med'] * 0.08
)
print("Risk score:" , final_df['risk_score'])

final_df['risk_prob'] = (final_df['risk_score'] - final_df['risk_score'].min()) / (final_df['risk_score'].max() - final_df['risk_score'].min() )
print("Risk propability:" , final_df['risk_prob'])

top_patients = final_df[['patient_id','department','age','los','risk_prob']].sort_values(by= 'risk_prob' , ascending= False).head(10)
print("Top patients:" , top_patients)

final_df.to_csv('Hospital-Project\\Data\\Final-Readmission-Results.csv' , index= False)
print("Final Readmission file is done!!")

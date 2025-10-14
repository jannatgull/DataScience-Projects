# ==============================
# 🏥 Hospital Readmission Project
# ==============================

# Step 1 — Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2 — Load all CSV files
patients = pd.read_csv('Hospital-Project/Data/patients.csv')
admissions = pd.read_csv('Hospital-Project/Data/admissions.csv')
labs = pd.read_csv('Hospital-Project/Data/labs.csv')
meds = pd.read_csv('Hospital-Project/Data/medications.csv')
readmit = pd.read_csv('Hospital-Project/Data/readmissions.csv')

print("✅ All files loaded successfully!")

# Step 3 — Basic info check
print(patients.head())
print(admissions.head())

# Step 4 — Merge dob with admissions to calculate AGE
admissions = admissions.merge(patients[['patient_id','dob']], on='patient_id', how='left')
print("after merge:" , admissions)
admissions['dob'] = pd.to_datetime(admissions['dob'])
admissions['admit_datetime'] = pd.to_datetime(admissions['admit_datetime'])
admissions['age'] = ((admissions['admit_datetime'] - admissions['dob']).dt.days / 365).astype(int)
print("Final:" , admissions['age'])
print("Dtypes:" , admissions.dtypes)

# Step 5 — Calculate Length of Stay (LOS)
admissions['discharge_datetime'] = pd.to_datetime(admissions['discharge_datetime'])
admissions['los_days'] = (admissions['discharge_datetime'] - admissions['admit_datetime']).dt.days

print(admissions[['patient_id','age','los_days']].head())

# Step 6 — Lab abnormal check (simple)
labs['is_abnormal'] = (labs['test_value'] < labs['normal_low']) | (labs['test_value'] > labs['normal_high'])
lab_flags = labs.groupby(['admit_id'])['is_abnormal'].sum().reset_index()
lab_flags.rename(columns={'is_abnormal':'abnormal_tests'}, inplace=True)

# Step 7 — Add abnormal labs count to admissions
admissions = admissions.merge(lab_flags, left_on='admission_id', right_on='admit_id', how='left')
admissions['abnormal_tests'] = admissions['abnormal_tests'].fillna(0)

# Step 8 — Polypharmacy (count unique meds per admit)
poly = meds.groupby('admit_id')['med_name'].nunique().reset_index()
poly.rename(columns={'med_name':'num_meds'}, inplace=True)
admissions = admissions.merge(poly, left_on='admission_id', right_on='admit_id', how='left')
admissions['num_meds'] = admissions['num_meds'].fillna(0)

# Step 9 — Merge with readmission info
final_df = admissions.merge(readmit[['patient_id','readmitted_within_30d']], on='patient_id', how='left')
final_df['readmitted_within_30d'] = final_df['readmitted_within_30d'].fillna(0)

print("✅ Final merged dataset ready!")

# Step 10 — Data Visualization (EDA)
sns.set(style="whitegrid")

# Age distribution
plt.figure(figsize=(7,4))
sns.histplot(final_df['age'], bins=10, kde=True)
plt.title("Age Distribution of Patients")
plt.show()

# Readmission by Department
plt.figure(figsize=(8,4))
sns.barplot(x='department', y='readmitted_within_30d', data=final_df, estimator=np.mean)
plt.title("Average Readmission Rate by Department")
plt.xticks(rotation=45)
plt.show()

# Correlation heatmap
num_cols = ['age','los_days','abnormal_tests','num_meds','readmitted_within_30d']
plt.figure(figsize=(8,5))
sns.heatmap(final_df[num_cols].corr(), annot=True, cmap="Blues")
plt.title("Feature Correlation Heatmap")
plt.show()

# Step 11 — Simple Risk Score (manual formula)
final_df['risk_score'] = (
    (final_df['age'] * 0.02) +
    (final_df['los_days'] * 0.1) +
    (final_df['abnormal_tests'] * 0.05) +
    (final_df['num_meds'] * 0.08)
)

# Normalize risk score between 0 and 1
final_df['risk_prob'] = (final_df['risk_score'] - final_df['risk_score'].min()) / (final_df['risk_score'].max() - final_df['risk_score'].min())

# Step 12 — Show top risky patients
top_patients = final_df[['patient_id','department','age','los_days','risk_prob']].sort_values(by='risk_prob', ascending=False).head(10)
print("🏥 Top 10 High-Risk Patients:")
print(top_patients)

# Step 13 — Save final results
final_df.to_csv('data/final_readmission_results.csv', index=False)
print("✅ Project completed successfully! Results saved in data/final_readmission_results.csv")

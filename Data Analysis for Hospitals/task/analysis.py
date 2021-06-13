import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

general = pd.read_csv('test\general.csv')
prenatal = pd.read_csv('test\prenatal.csv')
sports = pd.read_csv('test\sports.csv')

prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)
prenatal['gender'].fillna('f', inplace=True)
hospitals = pd.concat([general, prenatal, sports], ignore_index=True)
hospitals.drop(['Unnamed: 0'], axis=1, inplace=True)
hospitals['gender'].replace(['female', 'woman'], 'f', inplace=True)
hospitals['gender'].replace(['male', 'man'], 'm', inplace=True)
for column in ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']:
    hospitals[column].fillna(0, inplace=True)

hospitals['hospital'].value_counts().plot(kind='bar')
print("The answer to the 1st question is general")
plt.show()

hospitals['diagnosis'].value_counts().plot(kind='pie')
print("The answer to the 2nd question is pregnancy")
plt.show()

print("A violin plot of growth distribution by hospitals")
sns.catplot(data=hospitals['height'], kind="violin", x=hospitals['hospital'], y=hospitals['height'], split=True)
plt.show()

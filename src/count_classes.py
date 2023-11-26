import pandas as pd

# read in wisconsin breast cancer data
data = pd.read_csv('data/cancer_train.csv', index=None)

result = data.groupby('diagnosis').size().reset_index(name='count')
result = result.rename(columns={'diagnosis': 'Class'})

data.to_csv('results/cancer/class_count.csv', index=False)

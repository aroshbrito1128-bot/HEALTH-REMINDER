import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("dataset.csv")

data['water_intake'] = data['water_intake'].map({
    'low':0,
    'medium':1,
    'high':2
})

X = data[['study_hours','water_intake','sleep_time','break_interval']]
y = data['reminder_needed']

model = DecisionTreeClassifier()
model.fit(X,y)

def predict_reminder(study, water, sleep, break_time):

    water_map = {'low':0,'medium':1,'high':2}

    prediction = model.predict(
        [[study, water_map[water], sleep, break_time]]
    )

    return prediction[0]

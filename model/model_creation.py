import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import pickle
df = pd.read_csv("model/bank_note_authentication.csv")

### Independent and Dependent features
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
### Implement Random Forest classifier


classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)
## Prediction
y_pred = classifier.predict(X_test)
score = accuracy_score(y_test, y_pred)
pickle_out = open("model/classifier.pkl", "wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()
print(classifier.predict([[2, 3, 4, 1]]))
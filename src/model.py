import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

# Load TF-IDF features and labels
X = pd.read_csv(r'C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\data\tfidf_matrix.csv')
df = pd.read_csv(r'C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\data\processed_dataset.csv')
y = df['label']  # Replace 'label' with the actual name of your label column

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save the model

# with open('model.pkl','wb') as f:
#     pickle.dump(model,f)

# save heatmap of confusion matrix:

sns.heatmap(confusion_matrix(y_test, y_pred), annot=True)
# plt.savefig('confusion_matrix.png')
plt.show()

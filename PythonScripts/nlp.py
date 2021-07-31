import nltk
import re

# Import pre-processing
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.corpus import stopwords
# Import models
from sklearn.svm import SVC
# Import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
# Import Pickle
import pickle



# Load data and split into text data and labels
topic_data = load_files(r'path\to\folder')
X, y = topic_data.data, topic_data.target



docs = []

tizer = WordNetLemmatizer()

for sentence in range(0, len(X)):
    
    # Remove special characters
    doc = re.sub(r'\W', ' ', str(X[sentence]))
    
    # Remove single characters
    doc = re.sub('r\s+[a-zA-Z]\s+', ' ', doc)
    
    # Remove single characters from start of string
    doc = re.sub(r'\^[a-zA-Z]\s+', ' ', doc)

    # Replace multiple whitespaces with 1 space
    doc = re.sub(r'\s+', ' ', doc)
    
    # Convert all text to lowercase
    doc = doc.lower()
    
    # Do the lemmatization
    doc = doc.split()
    
    doc = [tizer.lemmatize(word) for word in doc]
    doc = ' '.join(doc)
    
    # Add document to list
    docs.append(doc)
    
    
# Count vectorizer. Parameters may need adjusted
cvec = CountVectorizer(max_features=1000, min_df=3, max_df=0.7, 
                     stop_words=stopwords.words('english'))

X = cvec.fit_transform(docs).toarray()

# Pickle Count vectorizer for future use
with open('count_vectorizer', 'wb') as cvec_file:
    pickle.dump(cvec, cvec_file)


# TfidfTransformer
tfidf = TfidfTransformer()
X = tfidf.fit_transform(X).toarray()


# Split into training and test sets
SEED = 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)


# Train, test, evaluate, and save models

# RandomForestClassifier
# Commenting out for the time being
# Linear-SVM has consistently better scores
"""
rf = RandomForestClassifier(n_estimators=1500, random_state=SEED)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)

print(classification_report(y_test, y_pred_rf))
print(confusion_matrix(y_test, y_pred_rf))
print(accuracy_score(y_test, y_pred_rf))

with open('random_forest', 'wb') as rf_file:
    pickle.dump(rf,rf_file)
"""

# Linear SupportVectorMachine
lin_svc = SVC(kernel='linear', C=10.0, random_state=SEED)
lin_svc.fit(X_train, y_train)

y_pred_svc = lin_svc.predict(X_test)

print(classification_report(y_test, y_pred_svc))
print(confusion_matrix(y_test, y_pred_svc))
print(accuracy_score(y_test, y_pred_svc))

with open('linear_svc', 'wb') as svc_file:
    pickle.dump(lin_svc,svc_file)





    
    
    
    
    
    
    
    
    
    
    
    
# case-prediction-tool
This repository contains the case decision tool app trained on the Supreme Court of the Philippines cases.

Check it out @ https://share.streamlit.io/shebna12/case-prediction-tool/main/case_pred.py

# Preliminary Abstract

The Supreme Court of the Philippines (SC), which serves as the
highest court, has always been facing the problem of having case
backlogs. Within a year, 93% of the cases received by the SC are
remaining unresolved. Effective strategy-making of lawyers are
also critical in the litigation process of a case. Overconfidence can
affect the case’s outcome which can be prevented with an objective
case prediction tool to assist lawyers. In this paper, the researcher
addresses these problems by exploring different NLP-based feature
extraction techniques and determining how it affects the results
of machine learning models. A comparison between bag-of-words
and term frequency-inverse document frequency (TF-IDF), lemma-
tization and stemming, and choice of N-grams are evaluated on
how a specific combination of feature extraction method affect the
Support Vector Machine and Artificial Neural Network Models. The
best performing system (TF-IDF + lemmatization + bigrams + SVM)
achieves an **overall accuracy of 91.80%** and an **F1-score of 95%** when classifying criminal cases into two case decision categories.

##  Note:
 - The full paper for this project is currently under review for conference submission. Kindly stay tuned for more updates in the future.
- The dataset for this project will be published publicly once permission from the website source has been secured.

# case-prediction-tool
This repository contains the case decision tool app trained on the Supreme Court of the Philippines cases.

Check it out @ https://share.streamlit.io/shebna12/case-prediction-tool/main/case_pred.py

## In case the app link above crashes, you can run this locally by:
1. Clone the repository
2. Open your terminal on the folder directory.
3. Type in your terminal, `pip install -r requirements.txt` . Press Enter.
4. Then, type `streamlit run case_pred.py` . Press Enter.
5. Copy the localhost link shown in your terminal to your browser to use the app. 

# V1 Preliminary Abstract

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

# V2 Preliminary Abstract

The Supreme Court of the Philippines (SC), which serves as the
highest court, has always been facing the problem of having case
backlogs. Within a year, 93% of the cases received by the SC are
remaining unresolved. To address this, a machine learning-based
prediction framework is introduced, one using classical machine
learning methods and the other are deep learning methods. Both are
processed by turning them into numerical quantities like vectors
or tokens and trained them using SVM,ANN or transformer based
BERT. Different methods of class balancing are investigated like
SMOTE and Generative Adversarial Methods. Our results show
slight improvement using SVM at weighted F1-score of 91% compared
to using LegalBERT at pure supervised training at 89%, followed
by semi-supervised training (GAN-BERT) at 88%. The resource
limitations in training deep learning models support the results.


##  Note: UPDATE 2022 - Addditional studies regarding the use of deep learning models for this problem was performed in 2022.
 - The full paper for this project is currently under review for conference submission. Kindly stay tuned for more updates in the future.
 - The dataset for this project will be published publicly once permission from the website source has been secured.
 - Feel free to create an issue in case you have any questions or concerns. I'll get back to you as soon as I can.

2025 International Conference on Computational,Communication and Information Technology (ICCCIT)
Collating Random Forest Classifier and Artificial
Neural Networks for the Risk Detection of
Maternal Health
Sneha Nahatkar Adityaraj Sanjay Belhe Vedant Vinay Ganthade
Electronics & Comp Engg Department AIDS Department AIDS Department
PICT Pune Vishwakarma University Pune Vishwakarma University Pune
Pune, India Pune, India Pune, India
scnahatkar@pict.edu 202000611@vupune.ac.in 202001143@vupune.ac.in
Prathamesh Suhas Uravane Tareek Pattewar
AIDS Department Computer Engineering Department
Vishwakarma University Pune Vishwakarma University Pune
Pune, India Pune, India
202001369@vupune.ac.in tareek.pattewar@vupune.ac.in
Abstract— This paper compares the performance of ANN figure out the solutions for the complications during
models to Random Forests on benchmarking a test pregnancy. Obstetricians are the branch of doctors that
dataset against the risk levels of maternal health as low, deals with pregnancy & childbirth-related cases. A good
mid, or high. The features considered are clinical obstetrician is essential for the smooth delivery of a baby.
features, namely age, blood pressure, and heart rate. The Imagine what if the obstetrician or the gynecologist that a
certain pregnant woman is consulting for the unwrinkled
dataset was imbalanced and needed adapting the ANN
process of delivery isn’t qualified [1]. According to the
architecture by fitting class weights and dropout
Indian Express, possibly about 35,000 Obstetricians or
regularization. The best test accuracy obtained in this
gynecologists in India aren't registered with the,
fashion was 73%. As the ANN had learned many of the
‘Federation of Obstetrics and Gynecological Societies of
complex data patterns in the dataset, it was, however, still
India’ (FOGSI). Hence, the risk factors that should be
limited by the moderate size and skewness of the dataset. identified well before the delivery and treated timely,
The Random Forest model with grid search produced a
aren’t executed. Risk factors for any pregnant woman are
much better accuracy of 85.71% compared with ANN,
the decisive aspect as finding them on time is important
thereby suggesting relatively high generalization across and treating them as well. These risk factors include high
all the classes for better minority risk level classes. An blood pressure, asthma, obesity, consuming alcohol,
ensemble approach of the Random Forest method smoking, cholesterol levels, etc. These factors decide the
appears to better serve toward high accuracy along with health of the pregnant woman & treating them on time
interpretability for clinical decision support in maternal decides the level of complications that she or her baby
health risk assessment. may face.
All the levels of risk factors vary from woman to
woman and their conditions also differ every time hence
Keywords—Maternal health, ANN, Random forest, risk, Keras.
doctors can't predict the surety of risk level that women
I. INTRODUCTION may face [2]. In the modern era where technology has
advanced and every and all amount of data that we
demand is available to us, we all tend to solve these
Pregnancy is a delicate and beautiful process that
problems. Machine Learning learning and deep learning requires care and quite a lot of monitoring of all the
are the two essential techniques that handle huge data
processes that directly or indirectly affect it. From the
appropriately, process them faster, and discover results
prehistoric era to the modern world, though the methods
accurately. Basically, we need a method to predict
of delivery may have changed, the scenario hasn’t. For
whether a pregnant woman with certain risk factors may
example, the risks involved during pregnancy remained
have a threat during delivery or not [3].
the same. The risks for every maternal woman differ from
person to person, but if there are some patterns in these The main task of artificial intelligence is not to reduce
cases and if they are extracted then we would certainly human efforts, but to enhance the results bringing more
know the risk factors or could predict the risk level for precision to those tasks that humans couldn’t do at a good
every pregnant woman. The risks involved during rate of time or accurately. This is the true need for AI in
pregnancy and delivery of the baby are serious concerns healthcare as this is a serious issue that needs to be
for the family of the respective woman and we all may addressed on a high scale. Withthe help of data analysis,
face this at some point in our life. Doctors aren’t able to dashboards could be made for those pregnant women
979-8-3315-1296-5/25/$31.00 ©2025 IEEE
446
DOI:10.1109/ICCCIT.2025.73
19872901.5202.29526TICCCI/9011.01
:IOD
|
EEEI
5202©
00.13$/52/5-6921-5133-8-979
|
)TICCCI(
ygolonhceT
noitamrofnI
dna
noitacinummoC
,lanoitatupmoC
no
ecnerefnoC
lanoitanretnI
5202
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:04:08 UTC from IEEE Xplore. Restrictions apply.

whom the ML or DL model has predicted as high risk, for compare the advantages and disadvantages of each type of
their personalized treatment and asses them more nicely. model within this classification task and gain insight into
practical applicability in the context of maternal healthcare
risk prediction.
II. RELATED WORKS
The dataset of the present study contained clinical
Research predicting maternal health has examined data from
features relevant to maternal health, namely Age, SystolicBP,
various hospitals and clinics. This data includes blood
DiastolicBP, BS-bloodo sugar levels, HeartRate, and
pressure (both systolic and diastolic), blood sugar levels,
BodyTemp. Such features are well known to determine
body temperature, age, heart rate, and risk levels. Some
maternal health conditions and are usually checked in
methods that combine different techniques, like DR-BiLTCN
pregnancies. The target variable, RiskLevel, categorizes the
(which uses decision trees and support vectors together), can
patients into three distinct classes: low, medium, and high
be very accurate - up to 98% [4]. Other studies have checked
risk. This is a multiclass classification problem that would be
out machine learning methods that learn from examples such
appropriate for both ANN and Random Forest models but
as k-Nearest Neighbor and Random Forest. These studies
presents some technical considerations. The first issue with
used data about blood pressure when the baby was delivered,
the dataset in question is related to class imbalance-class
the mother's age how many pregnancies she's had, and her
imbalance means that there is an unbalanced number of
heart health. These methods were able to get it right up to
classes in proportion. More precisely, the cases of low risk
95% of the time [5], [6].
occur considerably more frequently than the medium and
high-risk cases. To overcome this, we implemented class
Researchers have put Random Forest to good use in looking
weights for the Random Forest and used class balancing
at healthcare trends with the Nationwide Inpatient Sample
techniques such as SMOTE (where applicable) so that both
(NIS) getting it right about 88.79% of the time [7]. They've
ANN and Random Forest models are trained to view the data
dug deeper into things that can affect moms and babies, like
in a balanced manner. Additionally, we preprocessed the data
stillbirth, to better grasp the key terms and methods in this
through scaling of features to improve the performance of the
field [8]. Also, scientists have taken a long hard look at
ANN model.
Artificial Neural Networks (ANN) to see how well they can
mimic the tricky relationships in health data. These ANNs,
We have used both ANN and Random Forest models in
which are made up of fake brain cells hooked up in layers,
an attempt to compare which one will be able to perform
have found their way into solving all sorts of real-world data
better on this classification task. The ANN is a particularly
puzzles [9], [10].
powerful deep learning model that will be able to learn
complex, non-linear relationships between different features-
For example, studies [11], [12], and [13] showed Random
and there can be nothing more empirically fruitful than this
Forest works well with uneven datasets and gives clearer
for healthcare data, where interactions among clinical factors
results when sorting risks during pregnancy. Research by [14]
so often critically impact outcomes. However, the effect of an
brought in AI models you can understand showing how
ANN is that it generally requires large datasets and careful
important this is in medical settings. In the same way, work
tuning to avoid overfitting, meaning that it is computationally
in [15] looked at old statistical methods next to ML models
intensive. In contrast, Random Forest is the robust and
proving ML does better at predicting risks of heavy bleeding
interpretable model in machine learning that constructs an
after birth. Studies [16] and [17] looked into mixed models
ensemble of decision trees for prediction. It is well known for
that use ANN and Random Forest together getting better
its ability to well handle datasets of sizes from small to
accuracy and speed when sorting maternal risks. At the same
medium sizes, and also handles imbalanced data very well. It
time, [18] made a system to spot pregnancy risks that went
is able to provide insights into the importance of features;
beyond Random Forest adding in mental health factors. New
thus, it will be an appropriate choice. Given that our dataset
research, like [19] and [20], talked about using many types of
is relatively modest in size, the alternative for us would be
data sources and new datasets like OxMat leading to strong
Random Forest to cope with the noise in the data while
AI tech in mother and baby health. In the end, these steps
providing interpretable results with less risk of overfitting
forward show how AI and ML are changing aiming to
than deep learning models.
improve mother's health outcomes with reliable tools that
make predictions you can understand.
Such a comparison of ANN against Random Forest
III. METHODOLOGY allows for a cross-analysis of performance trade-offs and
dictates the requisites for selecting deep learning and machine
Considering the fact that the complications associated with
learning approaches in maternal health risk classification.
maternal health have very serious consequences in terms of
This comparison is important because it showcases the
health, proper categorization of risk levels into three-low,
capacities and limitations of both models, providing useful
medium, and high-and at the clinical parameter level is
insights for healthcare professionals and data scientists who
desirable. This can help the health practitioners identify at-
handle identical data. For instance, although ANN may
risk cases at an early stage so interventions might be
perform better in certain cases, the interpretability and
attempted in time to save lives. To this end, we use ANN as
efficiency of Random Forest make this model a good
well as a machine learning model, Random Forest, on a
contender for clinical deployment when model
judiciously selected dataset of clinical variables to classify
interpretability is of importance. In that sense, this work
the risk levels for maternal health. This will enable us to
contributes to the field by outlining and determining which
447
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:04:08 UTC from IEEE Xplore. Restrictions apply.

type of model would best classify risk across different this healthcare dataset since different features will have
conditions to aid in the successful development of reliable ranges and units. We first encoded the target variable, Risk
and actionable predictive tools in maternal healthcare. Level, to the Label Encoding, which converts classes into
integer labels: high risk = 0, low risk = 1, mid risk = 2. All
A. ANN
the input features, Age, Systolic BP, Diastolic BP, BS, Body
Temp, and Heart Rate are of different scales; therefore,
The ANN model as shown in table 1 is built using the Standard Scaler is used for standardization. Standardization
Keras Sequential API and consists of multiple dense layers, implies that it brings the data to have a mean of 0 and a
including ReLU activation and dropout layers to prevent standard deviation of 1, and this allows stability to the
overfitting. The architecture is as follows: AI Check here. optimization and accelerates the convergence speed by
reducing the difference in range among features.
TABLE I. ANN MODEL SUMMARY With preprocessing completed, the dataset was split into
training and testing in order to use an 80-20 split, thus
Layer (type) Output Shape Param # reserving part of the data for model evaluation, allowing us
to gauge the generalization performance of the model on
dense (Dense) (None, 64) 448 unseen samples.
dropout (Dropout) (None, 64) 0 The target variable in this dataset exhibits class imbalance
as it comprises a greater number of high-risk instances over
dense_1 (Dense) (None, 128) 8320 low-risk and mid-risk classes. Class imbalance can lead to the
model's bias towards the majority class while ignoring the
dropout_1 (Dropout) (None, 128) 0 classification of the minority classes. In this study, we tackled
class imbalance by applying class weights, whereby the
dense_2 (Dense) (None, 64) 8256 classes with lesser occurrences would have higher values
assigned over those with higher occurrences. The class
weights were calculated based on the inverse frequency of
dropout_2 (Dropout) (None, 64) 0
each class to ensure that errors in predicting minority classes
(e.g., high risk and mid risk) receive greater punishment than
dense_3 (Dense) (None, 32) 2080
errors for the majority class. By applying class weights, we
make the model more sensitive to the minority classes,
dense_4 (Dense) (None, 3) 99
improving performance metrics like recall and F1 score for
those classes. The final classification report, however,
Total params: 19,203
revealed comparatively higher precision and recall scores for
Trainable params: 19,203
the high-risk class, thereby indicating that the model was
Non-trainable params: 0
successful in incorporating and prioritizing the high-risk
category, given its smaller representation in the dataset.
The model starts with an input layer set to 64 units and
ReLU activation. It has been selected due to its capability to
This model was trained for up to 100 epochs with early
introduce non-linearity and correct the vanishing gradient
stopping on validation loss: it stops the training if there's not
issue, which made it capable for working on deep neural
an improvement at all for 10 consecutive epochs. Early
networks. Each dense layer is followed by a dropout layer
stopping is a very important part of neural network training
that is set at a rate of 0.3; that is, for each training epoch, 30%
since it avoids overfitting by stopping the process as soon as
of the neurons are randomly disabled. That is, 30% of the
the model stops generalizing better on the validation data.
neurons should be disabled during each training epoch. This
Training history shows that the model's training and
dropout rate helps in avoiding overfitting as the model
validation accuracy progressively improved over the first few
generalizes across the training data rather than memorizing
epochs as its loss reduces, which was a sign of learning
them.
success. During early epochs, accuracy gradually increasing
from about 37% to the end, around 70% for both the training
The final layer of the model is a dense layer with three
and validation sets. There could be fluctuations in validation
units. This layer represents the three risk levels, namely high
accuracy and loss, which can be mainly due to layers of
risk, low risk, and mid risk. In this case, the softmax
dropout, particularly complicated patterns in the data.
activation function has been utilized. Softmax is a very
However, at last, the model reached a test accuracy of around
important function in the multiclass classification
73%, which proves that the model was capable enough to
environment as it produces a probability distribution across
output proper classification under maternal health risk levels.
the three classes; hence, for any instance, the model can
determine the most-likely risk category. The loss function is
sparse_categorical_crossentropy, which gives a better fit for
B. Random Forest
integer-encoded target classes, and the evaluation metric is
accuracy.
The Random Forest algorithm is well known as an
Effective preprocessing of the data will be very important ensemble learning approach that also happens to be robust,
for the good performance of the ANN model, especially in interpretable, and efficient-more so with classification tasks
448
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:04:08 UTC from IEEE Xplore. Restrictions apply.

on structured data. During training, it builds a number of exhaustive search evaluates various parameter combinations,
decision trees, where each tree will be considered an selecting the one that maximizes cross-validated accuracy.
individual "weak learner." Finally, the end classification will
be determined by aggregating all predictions from the trees; The parameter grid was defined as follows:
this is typically done using majority voting. It reduces the
high variance often reported for a single decision tree and 1. n_estimators: [100, 200, 300] – varying the number
hence improves generalization to unseen data. This will of trees helps determine the ideal balance between
automatically reduce the class imbalance pertaining to the model complexity and computational efficiency.
maternal health dataset. Class weighting applies more 2. max_depth: [None, 10, 20, 30]-this hyperparameter
weighting to underrepresented classes, thereby limiting the avoids overfitting via tree complexity.
chances that the classifier becomes biased towards the 3. min_samples_split: [2, 5, 10]-this is the minimum
majority classes. This, coupled with the inherent ability of samples required to allow a node to be split into
Random Forests to handle imbalanced data by averaging over different parts; thus, higher values will yield simpler
many trees, makes it quite specifically a good application. trees.
Random Forest is less sensitive to class imbalance than most 4. min_samples_leaf: [1, 2, 4]-it affects the minimum,
other machine learning methods, such as Support Vector causing splits that are too specific.
Machines or k-Nearest Neighbors, even as its explicit class
weighting serves to advantage. The use of grid search with cross-validation to select
parameters was to check the degree of generalization of the
The preprocessing pipeline for the Random Forest model corresponding accuracy scores across different data
begins with Label Encoding of the target variable Risk Level. partitions. Following cross-validation, the combination of
It then directly maps classes into integer values: high and low parameters that gave the best results were employed to fit the
risk are mapped onto the numbers 0 and 1, mid risk is put final Random Forest model on the whole training data set.
onto number 2, which is necessary if targeting a supervised
learning task where such numerical value is considered We fitted it onto the training data and checked the test set
necessary for the classification by the model. We then once the model was trained with the best parameters. The
standardized the input features: Age, Systolic BP, Diastolic Random Forest model had a test accuracy of 85.71%. This
BP, BS, Body Temp, and Heart Rate using Standard Scaler. was significantly higher as compared to the corresponding
Although Random Forest models do not, in fact, rely on 73% accuracy achieved by the ANN model. It could be
feature scaling, like algorithms based on distance calculation attributed to the following reasons:
do, scaling sometimes can be useful here to ensure that all
features are similarly weighted; it is particularly relevant 1. Unlike ANNs, which often require huge datasets with
when cross-validating with other algorithms that require careful regularization against overfitting, Random Forests are
scaling. The dataset was split into a training set and a test set intrinsically robust even when using small to medium-sized
using an 80-20 split, so we could check the model's structured datasets. In this application, the ensemble nature of
generalization on unseen data. the algorithm allowed Random Forest to expose complex
patterns in the data without overfitting and hence produced
Target variable class imbalance may further influence the better generalization.
power of the model in correct classification of the minority
classes, especially since our classes are not well distributed. 2. Feature Importance and Interpretability: Random Forest
The weight is adjusted inversely proportional to class features the importance of feature attribution, which allowed
frequencies, so misclassifications will be weighed more us to understand which clinical features significantly
heavily for classes poorly represented with more risk and mid contributed to maternal health risk prediction. Such
risk. This technique permits the classifier to dynamically set interpretability is very advantageous for healthcare
the weights such that it is inherently better prepared for applications where understanding the model's decision-
dealing with all classes and ultimately detects cases from the making is critical.
minority classes. Class balancing in Random Forests is
automated, hence a greater penalty per split for the particular 3. Balance Treatment of Classes: Balancing class problem
minority class at each split of each single tree is assigned to was far better treated in the model by the application of
preserve representative splits. This approach has proven to be class_weight = "balanced." This helped in enabling the model
highly effective, as evidenced by the classification report and to identify cases both from minority classes. This resulted in
final model accuracy, where the risk classes achieved the model to have a high recall and precision for the two
reasonable recall and precision, thus resulting in a high classes as reflected in the classification report.
degree of balance in class treatment.
IV. RESULTS
Hyperparameter tuning was essential in Random Forest
models, since parameters like the number of trees Our maternal health risk classification task does indeed
(n_estimators), maximum tree depth (max_depth), minimum differ in the characteristics of performance by each model. In
samples required for a split (min_samples_split), and using multiple dense layers with dropout for regularization
minimum samples per leaf (min_samples_leaf) are quite and having an accuracy of 73%, the ANN model is
influential. Based on a grid search, we tested a combination outperformed significantly by the Random Forest model,
of hyperparameters with 5-fold cross-validation. This which reached an accuracy of 85.71%. It goes on to illustrate
449
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:04:08 UTC from IEEE Xplore. Restrictions apply.

how ensemble-based approaches like Random Forest can
even benefit from structured datasets with moderate
complexity. Further inspection by graphical analysis of the
training and validation loss and accuracy curves yields
additional insights as shown in the figures 1, 2, 3 and 4.
Learning curves for ANN model represented fluctuation in
validation accuracy and loss, indicating slight overfitting due
to the dropout layers because the model was unable to
generalize beyond the training set. In comparison, Random
Forest has stable accuracy at cross-validation; therefore, its
general performance is more consistent in its test samples.
Fig. 4 ANN Testing Loss
As both models depict a classification report as shown in
the figures 5 and 6, the Random Forest model is seen to have
very evenly distributed precision, recall, and F1-scores for all
classes. For instance, in class high risk, the recall had actually
been better than the model of ANN, thereby identifying more
true cases as high risk. It was particularly hard in the mid-risk
class because feature distributions of this class overlap hugely
Fig. 1 ANN Training Accuracy. with the other classes, yet the Random Forest model does
expose a recall improvement of the ANN, demonstrating its
robustness to the minority classes, helped in turn by the usage
of class_weight="balanced".
Fig. 5 ANN Classification Report.
Fig. 2 ANN Training Loss.
Fig. 6 Random Forest Classification Report.
The confusion matrices as shown in the figure 7, further
expose these differences. For ANN, mid risk was largely
confused with other classes. This ANN model seems more
inclined to put some cases in the low risk class. This can most
likely be attributed to the greater variance of the ANN model
and its higher sensitivity with regard to feature scaling. On
the contrary, with Random Forest's confusion matrix having
fewer misclassifications, particularly in distinguishing high-
risk from low-risk and also mid-risk, it could support the idea
of ensemble voting in the separation of classes.
Fig. 3 ANN Testing Accuracy.
450
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:04:08 UTC from IEEE Xplore. Restrictions apply.

[5] Khaled Fawagreh & Mohamed Medhat Gaber." Resource-efficient fast
prediction in healthcare data analytics: A pruned Random Forest
regression approach," 09 January 2020.
[6] Muhammad Zain Amin, Amir Ali."Performance Evaluation of
Supervised Machine Learning Classifiers for Predicting Healthcare
Operational Decisions," January 2017.
[7] Mohammed Khalilia, Sounak Chakraborty & Mihail
Popescu."Predicting disease risks from highly imbalanced data using
random forest," 29 July 2011.
[8] Gardosi, J., Madurasinghe, V., Williams, M., Malik, A., & Francis, A.
(2013), “Maternal and fetal risk factors for stillbirth: population based
study,” BMJ, 346(jan24 3), f108. https://doi.org/10.1136/bmj.f108
[9] S Agatonovic-Kustrin, R Beresford."Basic concepts of artificial neural
network (ANN) modeling and its application in pharmaceutical
research," Journal of Pharmaceutical and Biomedical Analysis, June
2000.
[10] Jinming Zou Ph.D., Yi Han Ph.D. & Sung-Sau So Ph.D."Overview of
Artificial Neural Networks," Methods in Molecular Biology™ book
Fig. 7 Random Forest Confusion Matrix.
series (MIMB, volume 458).
[11] M. M. Hosaain, M. A. Kashem and N. M. Nayan, "Artificial
V. CONCLUSION
Intelligence-Driven Approach for Predicting Maternal Health Risk
This paper provides a case study on the risk classification for Factors," 2024 9th South-East Europe Design Automation, Computer
Engineering, Computer Networks and Social Media Conference
maternal health using ANN and Random Forest models
(SEEDA-CECNSM), Athens, Greece, 2024, pp. 153-158, doi:
within a risk management framework. Even though the ANN
10.1109/SEEDA-CECNSM63478.2024.00035.
was able to learn complex, non-linear patterns, the algorithm
[12] Togunwa, T. O., Babatunde, A. O., & Abdullah, K. (2023). “Deep
was limited due to a small number of samples and class hybrid model for maternal health risk classification in pregnancy:
imbalance as it attained a test accuracy of 73 percent only. synergy of ANN and random forest,” Frontiers in Artificial
Intelligence, 6. https://doi.org/10.3389/frai.2023.1213436
Random Forest model on the other hand surpassed ANN as
[13] Subhashini, A., Nataraju, K., Rani, S. S., & Raju, P. K. (2024).
its test accuracy reached 85.71%, proving to be more robust,
“Maternal Health Risk Analysis and Classification Using Random
productive in relation to the problem of data imbalance as Forest Model with Hyperparameter Tuning,” In Lecture notes in
well as more interpretable. As each of those trees was based electrical engineering (pp. 511–523). https://doi.org/10.1007/978-981-
on different subsets of the input data, Random Forest 97-8422-6_41
provided reliable accuracy across the models and good [14] “Explainable AI based Maternal Health Risk Prediction using Machine
Learning and Deep Learning,” IEEE Conference Publication IEEE
balance of all the risk classes specifically the small ones. It
Xplore. https://ieeexplore.ieee.org/document/10174540, 7 June 2023.
can therefore be concluded that Random Forest has the best
[15] Ahmadzia, H. K., Dzienny, A. C., Bopf, M., Phillips, J. M., Federspiel,
predictive performance for the clinical decision making J. J., Amdur, R., Rice, M. M., & Rodriguez, L. “Machine Learning for
process in maternal healthcare because it is efficient, Prediction of Maternal Hemorrhage and Transfusion (Preprint),” JMIR
Bioinformatics and Biotechnology, 5, e52059.
consistent, requires little interpretation and is well suited for
https://doi.org/10.2196/52059, (2023).
practice in situations where the amount of data and
[16] Irfan, N., Zafar, S., & Hussain, I. “Holistic Analysis and Development
transparency of the model are the issues. It would be of a Pregnancy Risk Detection Framework: Unveiling Predictive
worthwhile to investigate combined approaches or use Insights Beyond Random Forest,” SN Computer Science, 5(8).
datasets with greater sample sizes to overcome the https://doi.org/10.1007/s42979-024-03409-9, (2024).
weaknesses identified in this work in the future. [17] Arslan, Naciye & Arslan, Merve & Şahin, Emrullah. “Automated
Classification Of Maternal Risks In Pregnancy: Analysis Using
Machine Learning And Artificial Neural Networks,” (2023).
REFERENCES
[18] Maternal Health Risk Prediction with Machine Learning Methods.
IEEE Conference Publication | IEEE Xplore.
[1] Abantika Ghosh, "Paediatrics to gynae, here are the surgeons, https://ieeexplore.ieee.org/document/10493737, 22 February 2024.
physicians,"April 20, 2015, 08:27 IST. [19] Mennickent, D., Rodríguez, A., Opazo, M. C., Riedel, C. A., Castro,
[2] Ron Southwick,"Using AI to predict risks for pregnancy & delivery," E., Eriz-Salinas, A., Appel-Rubio, J., Aguayo, C., Damiano, A. E.,
Chief health care executive August 31, 2022. Guzmán-Gutiérrez, E., & Araya, J. Machine learning applied in
[3] Greg Dastrup, "How Technology has Improved the Experience of maternal and fetal health: a narrative review focused on pregnancy
Pregnancy," informaconnect 25 Mar 2019. diseases and complications. Frontiers in Endocrinology, 14.
https://doi.org/10.3389/fendo.2023.1130139, (2023).
[4] Ali Raza, Hafeez Ur Rehman Siddiqui, Kashif Munir, Mubarak
Almutairi, Furqan Rustam, Imran Ashraf. "Ensemble learning-based [20] Khan, M. J., Duta, I., Albert, B., Cooke, W., Vatish, M., & Jones, G.
feature engineering to analyze maternal health during pregnancy and D. The OxMat dataset: a multimodal resource for the development of
health risk prediction," November 9, 2022. AI-driven technologies in maternal and newborn child health.
arXiv.org. https://arxiv.org/abs/2404.08024, 11 April 2024.
451
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:04:08 UTC from IEEE Xplore. Restrictions apply.
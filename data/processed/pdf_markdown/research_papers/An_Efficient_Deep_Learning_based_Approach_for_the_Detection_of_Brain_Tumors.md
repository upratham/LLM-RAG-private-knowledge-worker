2022 5th International Conference on Contemporary Computing and Informatics (IC3I)
An Efficient Deep Learning based Approach for the
Detection of Brain Tumors
Adityaraj Sanjay Belhe Vedant Vinay Ganthade Prathamesh Suhas Uravane
Research Center of Excellence for Research Center of Excellence for Research Center of Excellence for
Health Informatics Health Informatics Health Informatics
Vishwakarma University Vishwakarma University Vishwakarma University
Pune, India. Pune, India. Pune, India.
202000611@vupune.ac.in 202001143@vupune.ac.in 202001369@vupune.ac.in
Janvi Anand Pagariya Mamoon Rashid
Research Center of Excellence for Research Center of Excellence for
Health Informatics Health Informatics
Vishwakarma University Vishwakarma University
Pune, India. Pune, India.
202001239@vupune.ac.in mamoon.rashid@vupune.ac.in
Abstract— Deep learning has stretched out its roots even neurologists to treat is appallingly small, which is our
more in our daily lives. As a society, we are witnessing small devastating reality [4].
changes in lifestyle such as self-driving cars, Google Assistant,
The typical technique used by neurologists to identify
Netflix recommendations, and spam email detection. Similarly,
brain tumors and their stage or type is generally done with a
deep learning is also evolving in healthcare, and today many
doctors often use it more comfortably. Using deep learning magnetic resonance imaging (MRI) scan, which usually uses
models we can detect severe brain tumors with the help of MRI a huge, round-shaped machine that uses magnetic beams to
scans, in fact in the Covid era, deep learning evolved majorly to create a complete scan of the inside of the patient's body. body.
detect the disease with the help of Lung X-Rays. Magnetic Compared to computed tomography (CT) scans, MRI is quite
Resonance Imaging (MRI) is used when a person has a brain often performed by neurologists because CT scanning
tumor to detect it. Brain tumors can fall into any category, and machines use a rapid chain of X-rays that are assembled to
MRI scans of these millions of people are needed to determine if create a complete image of a patient's organ [5, 6]. The
they have the disease and if so, which category they belong to. complexity of CT scans degrades it compared to MRI. And
Determining the type of brain tumor can be a rigid task and the person who performed the MRI scan was often called the
deep learning models play an important role here. For the radiologist who communicates with the neurologists about
proposed deep learning model, we have implemented
any patient's scan. Now the real challenge also begins where
convolution neural networks (CNN) through which our model
the above-discussed ratio of neurologists to tumor cases
has achieved a testing accuracy of 96.5%. Also, along with this,
comes into play, because according to the "Cleveland Clinic"
the libraries of Keras and Tensorflow have been explored by the after obtaining the MRI scans, they go to a radiologist who
authors in this research.
analyses them and later forwards them to a neurologist. He
then studies these scans. It takes him at least a day to come to
Keywords— Deep learning, Neural networks, CNN, Brain
a conclusion. Nowadays, the time to treat the patient is wasted
tumor, Keras, classification, accuracy.
and it may happen that the tumor reaches the central nervous
I. INTRODUCTION system of the patient [7, 8].
The brain tumor is a serious disease that also needs to be We cannot change the process of obtaining MRI scans, we
dealt with as soon as possible. The different types of tumors cannot produce more neurologists in a short period of time,
at each stage make it difficult for the health system to identify and we cannot change the treatment tactics of these surgeons.
them at the right time, and it is very important that the patient So, what we can do is nullify the time between getting the MRI
shall receive fair treatment. During a brain tumor, rogue cells scans and the neurologist giving the verdict, which takes days
grow in the nervous system [1]. Medically recognized, there in real-time. This process can be largely replaced by deep
are three main types of brain tumors identified: glioma, learning, which takes minutes to predict the type of brain
meningioma, and pituitary, some of which are prone to cancer tumor or whether or not a brain tumor is present on an MRI
and some are invulnerable. According to a survey by the scan. There are often irregularities in brain size and tumor
International Association of Cancer Registries (IACR) in types that are difficult to identify, and efforts must be made to
2018, this disease was ranked as the 10th most common type identify the exact tumor from these scans. The lack of
of disease. Every year more than 28,000 cases of brain tumors qualified neurosurgeons in developing countries is also a
are detected in India and this number is increasing day by day. major reason why the sector is trying to replicate this process
More than 24,000 people die from this disease annually [2]. In using some advanced technology that is apparently cost-
a 2019 NITI Aayog report presented by Dr. Vinod Paul, the effective, accurate, and fast. The rise of efficient algorithms
number of brain tumor specialists also identified as and neural networks, which have taken a significant step in
neurologists in India is only 2,500, which is only nearly 9 introducing artificial intelligence to the world, has been made
percent of the total number of reported cases of the disease [3]. possible by advances in durable hardware that utilizes the
The ratio of the total number of cases to the total number of Graphics Processing Unit (GPU) and developments in
417
979-8-3503-9826-7/22/$31.00 ©2022 IEEE
90237001.2202.14265I3CI/9011.01
:IOD
|
EEEI
2202©
00.13$/22/7-6289-3053-8-979
| )I3CI(
scitamrofnI
dna
gnitupmoC
yraropmetnoC
no
ecnerefnoC
lanoitanretnI
ht5
2202
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:06:24 UTC from IEEE Xplore. Restrictions apply.

2022 5th International Conference on Contemporary Computing and Informatics (IC3I)
libraries that are essential for machine learning and deep III. DATASET
learning from multinational companies like Google. They
The brain tumor dataset used here contains 3000 plus MRI
developed and released TensorFlow publicly, and the AI
scans that have been converted into JPG images for easy
society witnessed new dawn of well-organized intelligent
interpretation by the proposed deep learning model. A dataset
models [9, 10].
is the most important part of any deep learning project. This
The outline of the paper is arranged as follows: section II dataset is divided into two components, training and testing.
gives the view of other authors that have worked on similar Within these folders are four subcategories named after tumor
problems. Section III gives us an understanding of the dataset type, and each type folder contains images of a brain tumor.
we have used. Section IV deep dives in the methodology The number of images each category contains in the training
proposed for building the deep learning model using and testing set is given in Table I.
convolutional neural networks. Section V tells us about the
TABLE I. NUMBER OF IMAGES IN EACH CATEGORY
results that we have obtained so far using our model on various
parameters, and section VI concludes our proposed model.
Tumor Type Training Testing
II. RELATED WORK
Meningioma 822 115
In one of brain tumor classification paper, the author
suggests that classifying some types of brain tumor problems
Glioma 826 100
can be solved using the same deep learning, but the approach
used here transfers learning. They have used GoogLeNet for Pituitary 827 74
training their model and it has provided them with an accuracy
of 98%.[11]. The author has suggested that every technology No Tumor 395 105
is ever required for taking scans of the brain. They have
described the use of CT scans, MRI scans, and ultrasound
imaging to detect brain tumors. They have used the approach Each image contains 512 x 512 pixels and consists of 3
of using CNN for classification and they have achieved 97.5% RGB channels. The RGB channels are the main red, green and
accuracy by this method [12]. Following another paper, the blue frames that make up the entire image. This dataset has
authors have described the use of recently invented been intentionally used to maintain a large number of image
technologies that radiologists often used for the brain tumor batch sizes, and when needed to increase the number of
scanning task. They have extensively used data augmentation datasets, image augmentation comes into play where multiple
in their project [13]. batches of the same but visually altered images are generated
to meet the additional needs of the image dataset. This
The authors have prepared a large five-class dataset for
technique is also used to change brightness, rotate grayscale,
their project. They have used two approaches for this 1. CNN,
zoom in and out, or rotate any set of images to any extent. The
2. transfer learning-based model using six machine learning
same process can be done using OpenCV, which also provides
classification methods [14]. The author has suggested using a
the same feature set and is mostly used in the computer vision
transfer learning approach for classifying brain tumors, where
domain. Given below are the various images of each category
this approach conveys us using ResNet50, DenseNet201,
of a brain tumor in Figure 1.
MobileNet V2, and InceptionV3. Also, they have compared
the accuracy of every transfer learning approach [15]. The
authors of the following paper have written that the brain
tumor classification can be done by using techniques like
GLCM, CNN, and DWT, and has got high accuracy in their
model and also by using advanced techniques of SVM can
also help to detect MRI images of brain tumors [16].
Regarding this paper, the author has mentioned the
significance of using segmentation for medical imaging
classification; they have also used several methods like canny
h detector, and region growing algorithms to execute their
project. They have also detected and classified other datasets
of bone fractures and blood cells [17]. In this paper, the author
has heavily discussed the problem of brain tumors. They have
also used techniques of data mining, along with CNN, and the
approach they have used is segmentation. They have also
applied several layers to train their model [18].
The description given by the author suggests that they
have used three techniques to classify their brain tumor
problem. These steps are nothing but divided into three stages,
where the first is pre-processing of the image, the second stage
Fig. 1. Different tumor images of each category.
is consisting of the segmentation of pre-processed brain tumor
images and the final stage includes morphological operations IV. PROPOSED METHODOLOGY
of the tumor later removing the unused segmented pixels [19].
A. Why deep learning?
The term neural network was first coined by Warren
McCullough and Walter Pitts in 1944. These neural networks
418
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:06:24 UTC from IEEE Xplore. Restrictions apply.

2022 5th International Conference on Contemporary Computing and Informatics (IC3I)
had parameters and weights, but there wasn’t much containing RGB value 0 i.e., black and white images. But, the
development in this field. The first neural networks were image with 3 RGB channels containing thousands of images
designed by keeping the human brain in mind, like how each isn’t a huge task for CNN, as it detects features within an
neuron in our brain is connected to each other and passes image. In the case of pandas, CNN detects pandas’ ears,
information. Later with advancements in technologies with mouths, eyes, black patches, etc. Based on these features, it
time, the backpropagation algorithm was developed which
could easily identify which of the following is a panda. As
proved to be futuristic. This algorithm was the base of all
discussed above, neural networks were originally inspired by
upcoming artificial intelligence applications because of the
the human brain. Like a normal human brain identifies almost
ability to learn from its mistakes. This ability of neural
any animal from some significant features like ears, eyes,
networks used in deep learning makes it unique from other
mouth, skin, hair, etc. The same process is carried out by
elementary machine learning algorithms. Deep Learning is a
CNN. For feature extraction, CNN uses a kernel. It's nothing
subset of Machine Learning and ML is a subset of Artificial
but a filter used to extract the features of any image. These
Intelligence. The role of these technologies has evolved due to
convolutional filters are trained to extract features of any
efficient hardware, large amounts of data, and an
understanding of the importance of neural networks. image. Also, each step of our model starting from feature
extraction to predicting image class is given below in Figure
B. Data Preprocessing 2.
Any deep learning model built always accepts the input data
as an array because the model cannot process straight images.
Each image comprises pixels and pixel values range from 0
to 256. The color scale of the image is determined by what
pixel value is present. Just as the black part of any image is
more like 0 and the white part is more like 256. Since pixel
values range from 0 to 256, leaving zero will have a range of
255. So the division of all 255 values is in the range of 0 to 1.
Before the training model, each image is converted to an
array by dividing by 255. This process is called
normalization, which is mainly done to reduce computational
effort. The most important part for later prediction and overall
model training depends on the labels assigned to the images.
The four brain tumor labels for each relevant image are most
likely in English and cannot be processed by a deep learning
model. Data must be entered in integer format only. So here
we have done One Hot Label Encoding which simply assigns
an integer label to each image category. It makes it easy for
us to prepare Y-train and Y-test data to make predictions and
train neural networks accordingly. We used the Scikit Learn
library to split the data into training and test sets, getting back
X-train, X-test, Y-train, and Y-test, where X-train consists of
the training image data and Y-train consists of from their
respective labels and the same happens with testing one. After
this process, we use NumPy functions to convert all the X-
train and X-test data consisting of images into a set of arrays.
Here, data augmentation is also performed to create slightly
different sets of modified image data, created using existing
image data. Model accuracy is improved by using data
augmentation in the process. The hyperparameters defined
during data augmentation were zoom range, rotation range,
horizontal flip, width shift, and many more.
C. Convolutional Neural Networks.
Convolutional neural networks (CNN) are mainly used for Fig. 2. Step-by-step Explanation of Model.
tasks like image classification, because of their ability to
extract features from any image and decide whether the given
image belongs to which class without any human V. RESULTS
intervention. For example, we have been given a dataset Before training the model, there are some hyperparameters
containing images of Pandas and we have to train our model that contribute extensively throughout the training process.
for the image classification. The old engineering process These hyperparameters were:
would take effort as it would simply scan all images, which
1. Batch Size: It is nothing but a number of representatives
could take days, and even if it did that, any other image
that shall pass through the network at the same time.
slightly different from the normal image would be rejected by
Depending upon the learning rate, the batch size should be
it. In the deep learning method, though Artificial neural
networks could be a solution they can classify images
419
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:06:24 UTC from IEEE Xplore. Restrictions apply.

2022 5th International Conference on Contemporary Computing and Informatics (IC3I)
decided, as it affects the training procedure time. In this case, have also prepared a classification report stating how our
we have opted for the batch size of 20. model performs on each benchmark of evaluating metrics in
Table. II.
2. Epochs: It is simply a number that would decide how
many times a training algorithm would work through a single
dataset. In our model, they are 25.
3. Validation Split: Validation data is a type of unseen data
TABLE II. ALL METRICS’ PERFORMANCE FOR OUR MODEL.
apart from training data, which is used to evaluate the
hyperparameters during the training process. The validation Tumor Type Precision Recall F1_Score Support
split we have assigned to our model is 0.10. After training the
model for 25 epochs, we got a training accuracy of 99% and Meningioma
0.98 0.92 0.95 86
the validation accuracy was 96%. From these obtained
numbers, we can say that there is no overfitting in our model. Glioma
0.97 0.98 0.97 97
We have specifically used the dropout layer to overcome this
problem. Both the accuracies are no doubt, indicating to us the Pituitary 0.86 0.96 0.91 26
great result ahead. Take a look at our model’s loss results in
the Figure 3. No Tumor 0.99 1.00 0.99 78
1. Precision: The first evaluation metric of machine
learning states how good a model is in predicting a specific
kind of set, which is a tumor in our case. This is calculated as
per eqn.1:
(cid:1)(cid:2)(cid:3)(cid:4) (cid:6)(cid:7)(cid:8)(cid:9)(cid:10)(cid:9)(cid:11)(cid:4)
Precision= (1)
(cid:1)(cid:2)(cid:3)(cid:4) (cid:6)(cid:7)(cid:8)(cid:9)(cid:10)(cid:9)(cid:11)(cid:4)(cid:12)(cid:13)(cid:14)(cid:15)(cid:8)(cid:4) (cid:6)(cid:7)(cid:8)(cid:9)(cid:10)(cid:9)(cid:11)(cid:4)
2. Recall: In this case, if our recall metric is higher,
more positive samples are detected. This is calculated as per
eqn.2:
(cid:1)(cid:2)(cid:3)(cid:4) (cid:6)(cid:7)(cid:8)(cid:9)(cid:10)(cid:9)(cid:11)(cid:4)
Recall= (2)
(cid:1)(cid:2)(cid:3)(cid:4) (cid:6)(cid:7)(cid:8)(cid:9)(cid:10)(cid:9)(cid:11)(cid:4)(cid:12)(cid:13)(cid:14)(cid:15)(cid:8)(cid:4) (cid:16)(cid:4)(cid:17)(cid:14)(cid:10)(cid:9)(cid:11)(cid:4)
3. F1 Score: This metric combines the first two
evaluating metrics into a single metric with the help of their
harmonic mean. This is calculated as per eqn.3:
(cid:18)∗(cid:2)(cid:4)(cid:20)(cid:14)(cid:15)(cid:15)∗(cid:21)(cid:2)(cid:4)(cid:20)(cid:9)(cid:8)(cid:9)(cid:7)(cid:22)
Fig. 3. Loss vs Epoch Graph. F measure = (3)
(cid:21)(cid:2)(cid:4)(cid:20)(cid:9)(cid:8)(cid:9)(cid:7)(cid:22)(cid:12)(cid:2)(cid:4)(cid:20)(cid:14)(cid:15)(cid:15)
And now, we will see the model’s training and validation 4. Support: This metric states the number of test
accuracies with each other in the Figure 4. samples that are found in each category should be true.
Also, there is one more metric that proves to be important
while evaluating our model’s performance and that is the
confusion matrix. In Figure 5. we can understand the situation
of the confusion matrix.
Fig. 4. Training and Validation Accuracy vs Number of Epochs
Graph.
Now, in terms of testing accuracy, we are just evaluating
how our model will perform for the testing data which is
hidden from the model during the training phase. And for
this phase, the testing accuracy achieved was 96.5%. We Fig. 5. Confusion Matrix.
420
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:06:24 UTC from IEEE Xplore. Restrictions apply.

2022 5th International Conference on Contemporary Computing and Informatics (IC3I)
In this matrix, the rows are the actual or true values to be [11] S.Deepak, P.M.Ameer”, Brain tumor classification using deep CNN
expected and the columns are showing the predicted outcome features via transfer learning”, computers in biology, and medicine
(2019).
that our model has made. According to this matrix, our deep
[12] J.Seetha & S, Selvakumar Raja,” Brain Tumor Classification Using
learning model did a very decent job in predicting testing data.
Convolutional Neural Networks”, Department of Computer Science
VI. CONCLUSION
and Engineering, Sathyabama University, Chennai, India(2018).
[13] Muhammad Sajjada, Salman Khan, Khan Muhammad, Wanqing Wu,
This study reveals the use of several techniques for this Amin Ullah, Sung WookBaik. "Multi-grade brain tumor classification
model to get accurate predictions. It has given great results to using deep CNN with extensive data augmentation." Journal of
computational science 30, pp. 174-182., 2019
our model and we hope these deep learning models may help
doctors to recover patients as soon as possible due to [14] Ahmad Saleh, Rozana Sukaik, Samy S.Abu-Naser,” Brain Tumor
Classification Using Deep Learning”, Published at an international
immediate scan results of brain tumors, so it will not take long
conference on assistive and rehabilitation technologies (iCareTech) in
for doctors as well as patients. We can also make use of new 2020.
techniques like transfer learning, advanced optimization
[15] Tariq Sadad, Amjad Rehman, Asim Munir, Tanzila Saba, Usman
layers as well as filters to make brain tumor classification Tariq, Noor Ayesha, Rashid Abbasi.” Brain tumor detection and multi-
models more powerful and helpful. Such a model and classification using advanced deep learning techniques”, Microscopy
applying more features and algorithms in the future will help Research and technique Wiley(2020).
several health care problems, etc. Deep learning will have [16] Bichitra panda, Chandra Sekhar Panda,” A Review on Brain Tumor
Classification Methodologies”, International journal of scientific
tremendous and remarkable benefits ahead.
research in science and technology(2019).
ACKNOWLEDGMENT [17] D.P.Gaikwad, P.Abhang, P.Bedekar,” Medical image segmentation for
brain tumor detection”, ICWET '11: Proceedings of the International
The authors are thankful to the Research Center of Conference & Workshop on Emerging Trends in Technology(2011).
Excellence of Health Informatics, Vishwakarma University, [18] G.Hemanth, M.Janardhan, L.Sujihelen, ”Design and Implementing
Pune for providing us a chance to use their high performance Brain Tumor Detection Using Machine Learning Approach”, 3rd
laboratory for training model in this work. international conference on trends in electronics and
informatics(2019), IEEE Xplore.
REFERENCES [19] M. Usman Akram, Anam Usman,” Computer-aided system for brain
tumor detection and segmentation”, International Conference on
[1] Mohsen, Heba, El-Sayed A. El-Dahshan, El-Sayed M. El-Horbaty, and Computer Networks and Information Technology (ICCNIT),(2011),
Abdel-Badeeh M. Salem. "Classification using deep learning neural IEEE Xplore.
networks for brain tumors." Future Computing and Informatics
Journal, vol. 3, no. 1, pp. 68-71, 2018.
[2] Kaur, Amanpreet, Mamoon Rashid, Ali Kashif Bashir, and Shabir
Ahmad Parah. "Detection of Breast Cancer Masses in Mammogram
Images with Watershed Segmentation and Machine Learning
Approach." In Artificial Intelligence for Innovative Healthcare
Informatics, pp. 35-60. Springer, Cham, 2022.
[3] Siar, Masoumeh, and Mohammad Teshnehlab. "Brain tumor detection
using deep neural network and machine learning algorithm." In 2019
9th international conference on computer and knowledge engineering
(ICCKE), pp. 363-368. IEEE, 2019.
[4] Kumar, Abhishek, Jyoti Rawat, Indrajeet Kumar, Mamoon Rashid,
Kamred Udham Singh, Yasser D. Al‐Otaibi, and Usman Tariq.
"Computer ‐ aided deep learning model for identification of
lymphoblast cell using microscopic leukocyte images." Expert
Systems, vol. 39, no. 4, e12894, 2022.
[5] Sajid, Sidra, Saddam Hussain, and Amna Sarwar. "Brain tumor
detection and segmentation in MR images using deep learning."
Arabian Journal for Science and Engineering, vol. 44, no. 11, pp. 9249-
9261, 2019.
[6] Saba, Tanzila, Ahmed Sameh Mohamed, Mohammad El-Affendi,
Javeria Amin, and Muhammad Sharif. "Brain tumor detection using
fusion of hand crafted and deep learning features." Cognitive Systems
Research, vol. 59, pp. 221-230, 2020.
[7] Kumar, Indrajeet, Sultan S. Alshamrani, Abhishek Kumar, Jyoti
Rawat, Kamred Udham Singh, Mamoon Rashid, and Ahmed Saeed
AlGhamdi. "Deep learning approach for analysis and characterization
of COVID-19." Computers, Materials and Continua, pp. 451-468,
2021.
[8] Amin, Javaria, Muhammad Sharif, Anandakumar Haldorai, Mussarat
Yasmin, and Ramesh Sundar Nayak. "Brain tumor detection and
classification using machine learning: a comprehensive survey."
Complex & Intelligent Systems, pp. 1-23, 2021.
[9] Gore, Deipali Vikram, and Vivek Deshpande. "Comparative study of
various techniques using deep Learning for brain tumor detection." In
2020 International conference for emerging technology (INCET), pp.
1-4. IEEE, 2020.
[10] Jha, Nishant, Deepak Prashar, Mamoon Rashid, Mohammad Shafiq,
Razaullah Khan, Catalin I. Pruncu, Shams Tabrez Siddiqui, and M.
Saravana Kumar. "Deep learning approach for discovery of in silico
drugs for combating COVID-19." Journal of healthcare engineering
2021.
421
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:06:24 UTC from IEEE Xplore. Restrictions apply.
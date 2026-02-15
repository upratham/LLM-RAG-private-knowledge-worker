Traitement du Signal
Vol. 42, No. 5, October, 2025, pp. 2913-2922
Journal homepage: http://iieta.org/journals/ts
Efficient Segmentation Approach for The Traceability of Breast Cancer Tissues to Improve
Diagnostic Accuracy in Ultrasound Images
Prathamesh Suhas Uravane1 , Vedant Vinay Ganthade2 , Adityaraj Sanjay Belhe3 , Mamoon Rashid4* ,
Shakila Basheer5 , Mariyam Aysha Bivi6
1 Science Academy, College of Computer, Mathematical, and Natural Sciences, University of Maryland,
Maryland 20742, USA
2 Ira A. Fulton Schools of Engineering, Arizona State University, Arizona 85281, United States
3 Department of AI and Engineering, Wednesday Solutions, Pune 411013, India
4 School of Information Communication and Technology, Bahrain Polytechnic, Isa Town 33349, Bahrain
5 Department of Information Systems, College of Computer and Information Science, Princess Nourah bint Abdulrahman
University, Riyadh 11671, Saudi Arabia
6 Department of Computer Science, College of Computer Science, King Khalid University, Abha 61421, Saudi Arabia
Corresponding Author Email: mamoon873@gmail.com
Copyright: ©2025 The authors. This article is published by IIETA and is licensed under the CC BY 4.0 license
(http://creativecommons.org/licenses/by/4.0/).
https://doi.org/10.18280/ts.420540 ABSTRACT
Received: 19 August 2025 Breast cancer continues to be a leading concern in global health, reaching across diverse
Revised: 26 August 2025 populations, and requires correct detection through early intervention. This is especially the
Accepted: 22 September 2025 case considering the complexity of breast tissue analysis and the increasing data volumes.
In this connection, emerging data aligns with the urgency in the transformation of rapid,
Available online: 31 October 2025
precise interpretation of complex ultrasound images using Artificial Intelligence (AI) to
advance in diagnosis and therapy. This research provides a new approach to applying
Keywords:
segmentation in healthcare for the traceability of every breast tissue to improve diagnostic
machine learning, feature extraction, deep
accuracy. The latest innovations of this study are in the new preprocessing pipeline with
learning, breast cancer, preprocessing,
advanced image preprocessing techniques of normalization, CLAHE, Gaussian Blur, and
segmentation
augmentation to handle noise, artefacts, and muscle regions that may lead to high false
favorable rates. The two state-of-the-art deep learning-based instance segmentation
frameworks are used, i.e., U-Net, MultiResUNet, and DeepLabV3 with a ResNet-50
encoder-decoder. The overall accuracy of the study achieved is 96% for all algorithms.
Furthermore, the segmentation results showed good agreement with Jaccard indices
consistently achieving 70%. Integrating the segmentation technique into our preprocessing
pipeline allows for providing better clinical insights, speeding up diagnosis, and elevating
patient care.
1.INTRODUCTION with a sonographer is actively involved in the successful
capturing of an ultrasound image, as the reflected waves detail
Breast cancer is a serious global disease, and it has raised the anatomy of the breast tissue in numerous ways. This
concern over several nations and communities with an therefore creates a different kind of perspective compared to
alarming overall statistic of more than 2.3 million new cases, X-rays or MRIs. While X-rays and MRIs depend on different
with 685,000 deaths from breast cancer alone in the year 2020 forms of radiation and magnetic fields respectively, ultrasound
[1]. Though medical science has made certain strides to utilizes sound waves to create images with limited risks
orchestrate hope, the immediacy of this crisis looms large, associated with using it on patients [4-6]. Oncologists,
more so in regions where access to healthcare resources is representing the first line of treatment against the diagnosis of
disproportionately skimpy. For example, India is a billion-plus breast cancer, very often represent hope and counsellors,
country that is suffering from an acute shortage of medical needed by patients combating this terrible disease. The
professionals. With only over 2,000 oncologists serving 10 magnitude of the problem is serious. The ratio is too
million patients [2], the skills shortage is conspicuous. imbalanced for the number of patients is concerned with the
Similarly, less than 10,000 radiologists for the whole country number of oncologists and sonographers. The demands for
point to the towering task of making diagnoses on time and diagnosis and care of breast cancer are so high, yet availability
correctly [3]. But the diagnosis of breast cancers is complex is at an all-time low. In such a case, the role of a sonographer,
and requires full acquaintance with the basic sciences of the an expert conducting ultrasound examinations, becomes
imaging modalities, particularly ultrasound. It plays a very highly important. However, the imbalance in patient and
important role in breast imaging, where a radiologist together workforce numbers underlines how imperative it is to look for
2913

newer ways of bridging the gap. step-by-step technique used in our novel data preprocessing
In this research, ultrasound images and their corresponding pipeline.
masks, that are referred to as annotations or ground truth, are (3) Integrating our pipeline with custom-tuned algorithms
useful. Ultrasound is the most common imaging modality in DeepLabV3 and ResNet50, U-Net, and MultiResUNet and
which to probe for breast cancer because it can be used non- comparing the results based on the Jaccard Index Comparisons.
invasively in real-time. But these images can have a subjective The rest of the paper has been organized into the following
interpretation, which is where masks come in. Masks, which sections: Section 2 provides a detailed literature review.
are generated via fine segmentation, indicate various regions Section 3 provides the detailed methodology of the proposed
of interest (ROI), such as tumors in ultrasound pictures. In this segmentation technique. The experimental test and results are
work, they were used as a reference or gold standard for the presented in Section 4. Finally, the paper concludes in section
development and validation of deep learning algorithms for 5.
automated tumor detection and analysis later in this paper with
the assistance of deep learning. This means that the AI model
can not only correctly characterize and delimit dubious areas 2. LITERATURE REVIEW
in ultrasound images but also provide an exact location on
what is being primarily concerned. Deep learning may In this section, the existing works in the field of ultrasound
automatically reveal the hidden important information from an images and their involvement with AI, segmentation, and
ultrasound image beyond what a human observer would be computer vision techniques used in medical imaging, are been
able to distinguish. Extracted features include complex texture discussed. Several papers in this section used advanced
patterns that indicate malignancy and forms. By exploring medical imaging techniques to handle complex ultrasound
these characteristics, the model can provide a comprehensive images. The use of an end-to-end integrated pipeline for the
analysis. Particularly in medical diagnoses, the consistency of classification of breast cancer ultrasonography images has
deep learning-based models is very important. It rapidly helps been used here, and the methods that are used are K Means++,
analyze images and decreases inter-radiologist variation, SLIC and have also used four different transfer learning
elevating a higher degree of accurate diagnosis for oncologists models such as VGG16, VGG19, DenseNet121 and ResNet50
to promptly act upon. [7, 8] A framework with a stepwise approach for data
In this work, we suggest a novel data preprocessing pipeline augmentation has been proposed along with some pre-trained
to facilitate segmentation for breast cancer ultrasound imaging. DarkNet-53, transfer learning, two RDE and RGW
An efficient and accurate data preprocessing pipeline unlocks optimization algorithms, probability-based methods and
the powerful application of different deep learning algorithms, finally, some machine learning-based classifications [9, 10].
including DeepLabV3 with ResNet-50, U-Net, and The solution to the problem of limited ultrasound labelled data
MultiResUNet for segmentation. Our study is based on has been solved here by producing a novel asymmetric semi-
ultrasound images, as they serve as a safe and real-time supervised GAN (ASSGAN), utilizing two generators and a
modality for imaging. It involves several key steps, such as discriminator. These generators create reliable segmentation
noise reduction using Gaussian blur, applying CLAHE for guidance without labels, leveraging unlabeled data for
contrast enhancement, data augmentation to increase the size effective training. Compared with fully supervised and semi-
of our dataset for generalization purposes, and image supervised methods on diverse datasets, including a new
normalization. Starting from the raw ultrasound images up to collection, ASSGAN excels with limited labelled images,
the format consumable by the algorithms mentioned above, showing promise in addressing data scarcity challenges in
each step in this pipeline deals with one of the issues pertaining breast ultrasound image segmentations [11].
to making sense out of ultrasound imaging. These The authors have created a completely automated and multi-
segmentation masks, precise outlines of the tumor edge, layer process for segmenting and classifying breast lesions
provide utility for improving diagnostic accuracy and clinical from ultrasound pictures. They have also compared the
decision-making in breast cancer. performance of different convolutional neural network
Diagnosis of breast cancer segmentation is mainly relied on architectures combining network performance with the help of
the precise interpretation of ultrasound images. However, an ensemble, and they are presenting a unique step of cyclic
manual delineation of tumor boundaries consumes more time, mutual optimization that helps utilize classification step
subjective, and prone to the inter-observer variability among results to improve segmentation outcomes [12]. The next
radiology experts. To underline these challenges, our study research emphasized more on ultrasonic image segmentation's
focuses on the segmentation of breast tissues, which allows noise and contrast challenges. Traditional methods struggle,
automated identification of tumor regions with high accuracy. but local phase-based approaches, like level set propagation
Precise segmentation assists to reduce the diagnostic using local phase and orientation, show promise. Cauchy
inconsistencies and assists oncologists in planning kernels improve feature extraction over log-Gabor filters.
personalized treatment, including surgery, chemotherapy, and Results confirm noise handling and precise boundary capture
radiotherapy. By connecting the technological advances of our capabilities. The prevalence of breast ultrasound (BUS) for
preprocessing pipeline and deep learning models with clinical cancer detection has highlighted the significance of accurate
results, our approach bridges the gap between computational tumor segmentation to assist doctors and AI diagnosis systems.
research and real-world medical solutions, ultimately While U-Net is a popular choice, it often produces false-
improving diagnostic accuracy and enhancing patient positive mass predictions in normal scans, a concern for
outcomes. routine AI-based screening. Current studies center on
The main contributions of this research are: designing fine-tuned U-Net architectures, fusion of multiple-
(1) Proposed a segmentation approach using deep learning modal data, and alternatives to machine learning techniques
algorithms to generate better segmentation masks. such as CNNs and random forests. It addresses issues relating
(2) This research provides a thorough explanation for every to increasing the accuracy of segmentation and to minimize
2914

false positives in BUS images, especially for automated fibroglandular tissue, and vessels and provide critical tools for
screening applications. The manuscript introduces an adaptive clinical applications. These further underline the increasing
region segmentation algorithm within a Bayesian framework reliance on AI in personalized treatment for cancers [20-25].
that processes noisy images. It is based on a multiresolution
wavelet approach, applicable to 2D and 3D data [13].
The authors of this study introduced a geometric model and 3. METHODOLOGY
computational algorithm for ultrasound image segmentation.
In our proposed work, we used a segmentation strategy to
A partial differential equation-based flow was formulated for
enhance the precision in the localization of tumors of breast
maximum likelihood segmentation using grey-level density
cancer from ultrasound images. We employed three
probability and smoothness constraints. The classic Rayleigh
algorithms of deep learning specifically U-Net, MultiResUNet,
probability distribution models grey-level behavior in
and DeepLabV3 along with ResNet-50 and each of them is
ultrasound images. The flow's steady state yields optimal
known for its excellence regarding complex patterns and sharp
segmentation. A finite difference approximation was
outline of bounders in an ultrasound image. This process is
developed and validated through some numerical experiments,
made possible using an encoder-decoder architecture, which
and demonstrated on fetal echography and echocardiography
also enables the precise localization of tumors within the
ultrasound images. This study developed a computer-aided
images and the extraction of high-level features. The precise
diagnosis (CAD) system for breast mass classification using
design of a novel data preprocessing pipeline that includes
ultrasonography. The system showed high-performance
methods Gaussian blur, CLAHE, data augmentation, and
classification from the use of CNN ensemble with VGG19 and
normalization is important, producing more accurate
ResNet152 models. The dataset consisted of 1536 breast
segmentation results.
masses: 897 malignant, 639 benign. The CAD system based
However Gaussian Blur, CLAHE, normalization and
on CNN offered an opportunity for clinical breast cancer
augmentation are separately established techniques, the
diagnosis. Importantly, CNN architecture was not focused on
innovation lies in their combination and sequencing with
masses themselves that proved crucial for accurate
optimization. The preprocessing pipeline starts with the
classification [14].
Gaussian Blur to reduce high frequency noise, followed by
Recent works related to breast cancer imaging tend to apply
CLAHE to enhance local contrast. Normalization helps to
deep learning to the segmentation and classification of tumors
ensure the consistency of pixel intensity distribution through
automatically. A host of techniques involves the use of CNNs,
the images and augmentation integrates variation to improve
automation of full-image analysis, to enhance image analysis,
model generalization. Compared to conventional
for ultrasound and MRI examinations. Such models aim at
preprocessing techniques our pipeline structure is carefully
improving diagnostic accuracy by effectively segmenting
tuned for breast cancer ultrasound characteristics, allowing
breast masses and providing support to classify them, focusing
more accurate tumor boundary detection. as presented in Table
on real-time and large-scale data processing. In addition,
1, the proposed preprocessing pipeline improves segmentation
benchmarks for segmentation and the development of
accuracy from 35% to 96.7%, establishing its effectiveness,
preoperative assessments are indicative of an increasingly
novelty and clinical relevance. A detailed explanation of how
embedded AI system in both the diagnostic and surgical
the whole process is carried out is visualized in Figure 1.
planning environment—one that fosters more personalized
Our research makes use of ultrasound images and their
medical care [15-19]. Authors of these studies emphasized the
respective segmentation masks, which can also be coined as
use of deep learning and segmentation techniques in their
annotations. Originally, the image and mask data were
approaches for the purpose of enhancing breast cancer
combined in the same directory for three different labels. The
imaging and diagnostic accuracies. Many have employed 3D
authors here built an algorithm for separating the image and
image segmentation, as witnessed in predictive analysis on
described the technique as essential for organizing and
chemotherapy response and enhancement in analyzing MRI
optimizing the breast cancer ultrasound dataset. By
breast tissue. Segmentation of ultrasound images makes use of
systematically segregating images and corresponding masks
both global and local statistical methods, with current evidence
into separate directories, the technique streamlines data access
suggesting a shift to more robust multi-resolution techniques.
and ensures data consistency. The stepwise data preparation
Finally, publicly available deep learning models and datasets
algorithm is given in Algorithm 1.
advance the research in the segmentation of breast tissue,
Table 1. Algorithm performance with and without using pipeline
Pipeline Algorithm Accuracy F1-Score Jaccard Precision Recall
DeeplabV3+Resnet50 0.35177 0.19793 0.12234 0.12273 0.99659
Without Normalization MultiResUnet 0.34240 0.19607 0.12099 0.12134 0.99674
Unet 0.20948 0.17227 0.10372 0.10372 1.00000
DeeplabV3+Resnet50 0.95761 0.77901 0.69673 0.86729 0.78945
With Normalization MultiResUnet 0.95386 0.73817 0.69673 0.86431 0.73878
Unet 0.95650 0.67809 0.59712 0.78527 0.74600
DeeplabV3+Resnet50 0.95892 0.76974 0.68537 0.85848 0.77802
Data+Normalization+Gaussian
MultiResUnet 0.95818 0.75359 0.67176 0.83724 0.77136
blur
Unet 0.95874 0.72032 0.63576 0.83508 0.73800
DeeplabV3+Resnet50 0.95929 0.77179 0.68552 0.85275 0.77854
Data+Normalization+Gaussian
MultiResUnet 0.96020 0.76420 0.68558 0.88728 0.75417
blur+CLAHE
Unet 0.96017 0.72845 0.64810 0.84648 0.75781
DeeplabV3+Resnet50 0.96454 0.79516 0.71453 0.80500 0.85555
Data+Normalization+Gaussian
MultiResUnet 0.96553 0.79380 0.71990 0.79534 0.88684
blur+CLAHE+Augmentation
Unet 0.96735 0.82284 0.74445 0.82933 0.87565
2915

the image with a Gaussian kernel, essentially averaging the
pixel values in a localized neighborhood, authors used it to
leverage the drawbacks of noisy data. This feature has mainly
two purposes: first, smoothing out minor irregularities that
helped the model to focus on more prominent features relevant
to breast cancer diagnosis. It mitigates the influence of noise
and fine-grained details present in ultrasound images and
enhances image clarity. After examining the drawbacks of the
noisy data, Gaussian blur further reduced the impact of outliers
and extreme intensity variations that had persisted.
Additionally, smoothing out minor irregularities helped the
model to focus on more prominent features relevant to breast
cancer diagnosis. The usage of a large kernel size (5,5) results
in substantial blurring effects, and kernel size influences the
amount of smoothing required as well as data characteristics.
High-frequency noise is diminished by using a large kernel
size. It also controls the amount of blurring added to the image.
Here, (5,5) is the size of the neighborhood in the Gaussian
kernel. Careful consideration was given to this parameter, as it
finds out how much noise will be terminated as well as
information lost in the process. The combined Gaussian blur
method used after normalization upgrades data quality to
further initial processing, resulting in more precise and noise-
robust empirical classifier performance for breast cancer
image analysis relevant to clinical practice.
3.2 Implementing CLAHE
The next process in the pipeline employed is Contrast
Limited Adaptive Histogram Equalization (CLAHE), which is
one of the key techniques for improving ultrasound image
quality. CLAHE is contrast enhancement using adaptive
histogram equalization, which modifies the image so that its
intensity distribution achieves a desired average local contrast
[6]. This method increases the effectiveness of preprocessing
if used together with normalization and Gaussian blur.
Although normalization aligns pixel values and Gaussian blur
Figure 1. Overall system representation diagram (smoothing) reduces the noise and fine details, CLAHE
addresses the problems of intensity variations caused by a
Algorithm 1. Stepwise Data Preparation algorithm machine and uneven illumination, particularly apparent in
ultrasound images. This stage increases the prominence of
both fine and subtle features in the images by spreading pixel
Input: Directory path containing raw image and mask data.
values with the aim to allow more efficient image analysis.
Output: Separated directories for images and masks.
CLAHE, along with normalization and Gaussian blur,
1. Initialize variable path with the path of the data directory.
encompasses an entire method to enhance ultrasound images
2. Initialize counter counter with a value of 1.
by accentuating salient diagnostic features of the image and
3. While there are images and masks to process:
facilitating their accurate identification in breast cancer
Construct image_path using path, class_names, and counter:
characteristics detection. CLAHE also covers the uniform
image_path=path+class_names+counter_value.png
blurring effect caused by excessive usage of Gaussian blur,
Construct mask_path using path, class_names, counter, and
resulting in losing fine details and edges that are very
mask:
important in the segmentation purposes. Enhancing local
mask_path=path+class_names+counter_mask.png
contrast and mitigating over usage of noise, a more balanced
4. Read the image from image_path and the mask from
way of pixel redistribution occurs across the image.
mask_path.
5. Create two separate directories to store images and masks.
3.3 Data augmentation
6. Store the image in the image’s directory and the mask in the
mask’s directory.
The authors integrated data augmentation into the breast
7. Increment the counter value.
cancer ultrasound image segmentation pipeline to overcome
8. Repeat steps 3 to 7 until all images and masks are processed.
challenges posed by limited datasets and enhance their model's
performance. Data augmentation involves introducing
3.1 Noise reduction through gaussian blur
controlled variations to the pre-processed ultrasound images
through techniques of flips and rotations. By doing so, we
The subsequent step in the pipeline, Gaussian blur, was
aimed to address multiple critical goals.
introduced as one of the critical preprocessing techniques. As
(1) We achieved a better pixel-wise representation with
Gaussian blur is a filtering process that involves convolving
2916

spiculated mass not just at the centroids but also by by our optimized preprocessing pipeline, guarantees reliable
augmenting images to reflect real-life variations during image segmentation performance, as illustrated by the notable
acquisition and resulting in different angles for the learning of enhancement in Jaccard indices and accuracy metrics reported
the model. in Section 4. Figure 2 provides a much more explicit
(2) The model was made less sensitive to variations because explanation of how encoder-decoder architecture seems to be
it was trained on features extracted from images that simulated working.
various conditions like real-world imaging scenarios. Also, the
model was saved from overfitting, which is a risk of failing to
generalize to new data because it only remembers instances
instead of learning how to setup rules based on standard
examples.
(3) The identified augmented dataset improved the model
generalization over different image variations, which is
fundamental for a reliable breast cancer diagnosis. The authors
then constructed a data augmentation training strategy that
incorporated data augmentation into their work to achieve
optimal generalizations of identifying key breast cancer
characteristic behavior from MRI in a range of images.
Figure 2. Working of encoder and decoder architecture
3.4 Normalizing data
Normalization is an important part of data preprocessing, as 4. RESULTS
it has increased the utility of the ultrasound image data for
further analysis. Pixel values are scaled to a unified range In this section, a novel preprocessing pipeline incorporating
between 0 and 1. Uniformity in pixel values in images was a a wide variety of deep learning algorithms has achieved an
major task in the context of breast cancer ultrasound images accuracy of up to 96%. We present their findings through a
having varying intensity levels. This process balanced the combination of graphical representations, evaluation metrics,
scale of information within each image. Outliers in very high and visual figures illustrating the disparities between actual
extreme intensities could easily skew the model training. The and predicted segmentation masks. The processes Gaussian
authors have worked on taking away the differences in pixel blur, CLAHE, augmentation, and normalization were carried
range, which in turn helps models such as DeepLabV3 and out extensively and methodically to unveil the pivotal role of
ResNet50, MultiResNet, and Unet converge significantly the novel pipeline in enhancing model performance. The
when training. As a result, the models can identify relevant impact of each deployed technique is systematically
features in the images more accurately and generally. The scrutinized by the authors, which gives insights about how
pipeline used normalization to lay a consistent foundation for they contribute to improve results collectively. The
subsequent techniques of segmentation. This alignment of data comprehensive research reveals the enhancement in quality of
characteristics allows models to focus on meaningful patterns segmentation achieved with the integration of the pipeline. In
within images, resulting in more robust and accurate breast general, the results section is indeed an intensive study with
cancer diagnostic outcomes. great depths of understanding that covers the trend of results
obtained using various techniques and the progressive
3.5 Deep learning algorithms for segmentation refinement incorporated due to the new data preprocessing
pipeline.
In this study, we used three advanced deep learning
architectures U-Net, MultiResUNet, and 4.1 Experimental setup
DeepLabV3+ResNet50 selected based on their performance in
medical image segmentation and their additional strengths. U- Experiments were implemented on a system with an
Net was used as the baseline model because of its all-round NVIDIA GeForce RTX 3050 GPU (4GB VRAM) and an
adoption in medical imaging and its ability to accurately AMD Ryzen 7 6800H CPU. The dataset was sub divided into
capture both low-level and high-level features using an 70% training, 15% validation, and 15% testing, and 5-fold
encoder-decoder architecture. MultiResUNet, an extension of cross-validation was performed to examine robustness.
U-Net, comes with multi-resolution convolutional blocks that Models were trained using the Adam optimizer with a learning
allow the network to extract fine-grained texture patterns, rate of 1e-3, a batch size of 6, and 60 epochs. A combined
making it particularly effective for identifying small lesions Binary Cross-Entropy and Dice loss was used, with early
and subtle breast tissue variations in ultrasound images. The stopping (patience=20) and a ReduceLROnPlateau scheduler
architecture of DeepLabV3+ResNet50, allows to detect non (factor=0.1, patience=9, min_lr=1e-7) to overcome overfitting.
similar tumor regions while maintaining boundary precision. To overcome on generalization, we integrated data
The integration of these three models comes up with a augmentation: Horizontal Flip (p=1.0), Vertical Flip (p=1.0),
comprehensive framework for performance comparison. This and Rotation (limit=±45°, p=1.0). This scaled the dataset 4
diversity allows us to evaluate segmentation performance times and integrated the variation in dataset. For noise
under different complexities of breast ultrasound images. The reduction, Gaussian Blur with a kernel size of (5,5) was
encoder-decoder architectures used in the networks of these applied to suppress high-frequency noise while securing tumor
models efficiently extract image features through the encoder boundaries. A fixed random seed (42) was used to certify
and reconstruct accurate segmentation maps through the reproducibility across dataset splitting, augmentation, and
decoder. The strategic selection these architectures, supported training.
2917

4.2 Results without pre-processing score of 0.12, that underscores the inadequacy of the initial
model performance for the given breast cancer ultrasound
In Figure 3, the breast cancer image segmentation dataset image segmentation problem.
has been subjected to the DeepLabV3+ResNet50 algorithm by The initial segmentation results from the chosen algorithms
the authors without applying pre-processing to the dataset. without the use of our preprocessing pipeline resulted in poor
Thus, the algorithm is drawn to the raw image data which performance. The natural reasons can be attributed to these
appears to be the case from the output the algorithm is giving. inherent complexities in ultrasound images, such as the
The output is sub-optimal. The values of its accuracy and presence of noise and generally poor contrast along with
Jaccard Scores are also very low. significant variations in both texture and intensity. Because of
Similarly, if we check the performance of MultiResUNet, such complexities, the algorithms get confused, and thus it
and Unet in Figures 4 and 5 respectively, we can say that becomes challenging for them to accurately demarcate the
without using the data preprocessing pipeline, we cannot boundaries of the tumor. Without preprocessing, the
achieve better results for the segmentation. algorithms used may not be able to extract as good features
and reduce noise as much. In this case, segmentation masks
produced would be less accurate and their overall performance
would be lower Jaccard scores.
However, promisingly, the coming sections hold the
promise of unveiling how such initial results are transformed
by this preprocessing pipeline. The authors demonstrate
impact on improvement in terms of accuracy and other means
of evaluation, thus shedding light on transformation from
Figure 3. Segmentation using DeepLabV3+ResNet50 modest outcomes to refined and more accurate segmentation
without using the pipeline results while promising tangible improvement in the challenge
of confronting this complex medical image segmentation task.
4.3 Results with pre-processing
We successfully merged our novel data preprocessing
pipeline into our workflow to understand the initial set of
challenges and improve our segmentation results. We began
this process with analysing noise reduction—a crucial step in
improving the accuracy of our masks. We expect a progressive
Figure 4. Segmentation using MultiResUnet without using improvement in the quality and precision of our breast cancer
pipeline tumor segmentations as we progressively add each part of the
pipeline that includes noise reduction, contrast enhancement,
data augmentation, and normalization. This systematic process
shall increasingly improve our results and the performances of
our deep learning algorithms as we advance with each stage of
this preprocessing pipeline.
Figure 5. Segmentation using Unet without using pipeline
Figure 7. Noise reduction using Gaussian blur on an image
Figure 6. Training and validation accuracy graph for the
DeepLabv3+ResNet50 algorithm Figure 8. CLAHE on the denoised ultrasound image
The obtained training accuracy of 35%, as shown in Figure The results shown in Figure 7 are using the Gaussian blur
6, along with precision and Jaccard indexes are both at a mere noise reduction technique, and it provides improved results.
2918

The pipeline's first preprocessing step is Gaussian blur, which mapped to be between about the same range; in no case does
starts to progressively enhance the quality of the results of the pixel intensities in individual images dominate the training
segmentation. Noise in ultrasound images starts to be sorted due to variance resulting from differences in illumination. This
out through this stage, which is obviously quite critical, minimizes effects due to variance in illumination conditions
particularly with breast cancer ultrasounds, which are known and increases the degree to which the model will generalize
for intricate details and subtle changes. For making the image patterns related to breast cancer features in different images.
more stable and visually coherent, the Gaussian blur feature The overall effect of the whole preprocessing pipeline is a
smoothes sharp transitions and tends to minimize noise- significant advancement in segmentation research. The
induced inconsistencies. Although this is the first step ahead pipeline systematically handles inherent challenges created by
in the more complex process, the improvement has set a base breast cancer ultrasound images, ranging from noise and low
on which subsequent stages are built to further enhance the contrast to minimal tissue appearance variations. With
precision of the segmentation task. techniques such as sequence Gaussian blur, CLAHE,
Future elements of this preprocessing pipeline involve the augmentation, and normalization, the pipeline processes raw
usage of CLAHE and how the application of this technique images toward a standardized dataset. This fined dataset is
would subsequently increase the chances of better used to train some sophisticated deep learning models such as
segmentation results, as in Figure 8. The improvement marked DeepLabV3 and ResNet-50 that permits them to capture
in the predicted image mask can be attributed to the fact that minute features that are fundamental to accurate
CLAHE could preserve and highlight the required features segmentations. In Table 2, every highlight of the algorithms
better for accuracy in segmentation results. This keeps the performs within the pipeline. Also, we are comparing the
local improvement provided by CLAHE to preserve the numerical results of every algorithm performing under every
dependencies between the various constituents of an image stage of our pipeline, which is shown in Figures 11-13.
and thereby provide the original ground truth mask with more
faithful segmentations. Hence, this improvement speaks well
for the effectiveness of CLAHE in adapting to the subtleties of
medical images in producing better reliability and accuracy in
their segmentations.
The obtained results with the second part of the pipeline
involving augmentation. Figure 9 shows the involvement of
this phase and how augmentation helps segmentation achieve
better results. Introducing variations in the form of horizontal
and vertical flips and many other operations have helped
Figure 9. Augmented segmented mask
generate better data to accompany the original data and help
algorithms to train these sets altogether. This makes the model
more resilient to variations of several imaging conditions,
patient poses, and probe orientations, and ultimately leads to a
more generalized segmentation model. Augmentation further
reduces the threat of overfitting—an ordinary issue in
operating with limited medical imaging datasets. By
introducing controlled variations, the model learned to extract
and prioritize salient features regardless of minor image
alterations, and finally, arriving at the final stage of the
pipeline. Figure 10 shows how normalizing pixel values helps
Figure 10. Final Segmentation results after the use of the
our model generate better masks.
preprocessing pipeline
Normalization improves training since pixel values are
Figure 11. Performance of DeepLabV3+ResNet50 with the pipeline
2919

Figure 12. Performance of MultiResUnet with the pipeline
Figure 13. Performance of Unet with the pipeline
Table 2. Comparison of state-of-the-art segmentation methods and proposed method on breast ultrasound images
Research Work /Paper Title Model/Technique Result Year
0.9674 (Acuuracy)
Your Best Model (Proposed) UNet+Gaussian+CLAHE +Augmentation 2025
0.74 (Jaccard)
DBU-Net: Dual branch U-Net [26] U2-MNet 0.9378 (Acuuracy) 2023
AAU-net [27] Adaptive Attention U-Net 0.6910 (Jaccard) 2022
Attention U-Net [28] CNN-based Segmentation 0.9500 (Acuuracy) 2024
Table 1 presents the segmentation performance of the three The proposed preprocessing pipeline plays a vital role in
architectures evaluated in this study. Notably U-Net attained achieving these results. Prior to preprocessing, segmentation
the highest accuracy (96.7%) with the complete preprocessing accuracy was limited (35.1% for DeepLabV3+ResNet50, 34.2%
pipeline, proving its strong resilience and efficient encoder- for MultiResUNet, 20.9% for U-Net) primarily caused by
decoder structure for ultrasound image segmentation. The noise, poor contrast, and complex textures in ultrasound
second evaluated architecture MultiResUNet achieved 96.5% images. Performing normalization improved performance to
due to its multi-resolution convolutional blocks, which acquire roughly 95% throughout all models by fortifying pixel
subtler structural details efficiently. The final architecture intensities. Gaussian blur further helps to refine accuracy by
DeepLabV3+ResNet50 achieved 96.4% accuracy for suppressing high-frequency noise, while CLAHE boosts local
extracting multi-scale contextual features by leveraging atrous contrast and tumor boundary visibility, achieving 96.73%
spatial pyramid pooling (ASPP). Although three architectures accuracy. These results confirm that the pipeline significantly
aided from advanced preprocessing, the results suggest that U- enhances segmentation performance across diverse
Net demonstrates better for heterogeneous ultrasound data. architectures.
2920

Table 2 provides a comparison between existing state-of- Ultrasonics, 65: 51-58.
the-art segmentation methods for breast ultrasound images and https://doi.org/10.1016/j.ultras.2015.10.023.
our proposed pre-processing pipeline. This highlights the [6] Hesaraki, S., Mohammed, A.S., Eisaei, M., Mousa, R.
significant performance improvement achieved through our (2025). Breast cancer ultrasound image segmentation
optimized pipeline. using improved 3DUnet++. WFUMB Ultrasound Open,
3(1): 100068.
https://doi.org/10.1016/j.wfumbo.2024.100068
5. CONCLUSION [7] National Breast Cancer Foundation. Breast cancer
ultrasound. https://nbcf.org.au/about-breast-
In this study, we developed a novel preprocessing pipeline cancer/detection-and-awareness/breast-cancer-
that contains Gaussian blur, CLAHE, normalization, and ultrasound/.
augmentation to enhance segmentation accuracy for breast [8] Wu, G.G., Zhou, L.Q., Xu, J.W., Wang, J.Y., Wei, Q.,
ultrasound images. By integrating this optimized Deng, Y.B., Cui, X.W., Dietrich, C.F. (2019). Artificial
preprocessing techniques with three state-of-the-art deep intelligence in breast ultrasound. World Journal of
learning models U-Net, MultiResUNet, and Radiology, 11(2): 19-26.
DeepLabV3+ResNet50, we achieved prominent https://doi.org/10.4329/wjr.v11.i2.19
improvements in diagnostic precision. Our approach obtained [9] Inan, M.S.K., Alam, F.I., Hasan, R. (2022). Deep
a segmentation accuracy of 96.7% and a Jaccard index of 0.74, integrated pipeline of segmentation guided classification
outperforming several existing methods and demonstrating the of breast cancer from ultrasound images. Biomedical
clinical relevance of our method for tumor traceability. Signal Processing and Control, 75: 103553.
Despite these promising results, we admit certain https://doi.org/10.1016/j.bspc.2022.103553
limitations of proposed study. The proposed approach requires [10] Nasser, M., Yusof, U.K. (2023). Deep learning based
additional computational costs due to the multi-step methods for breast cancer diagnosis: A systematic review
preprocessing. In addition, challenging cases such as small and future direction. Diagnostics, 13(1): 161.
tumors, heterogeneous tissue textures, and low-contrast https://doi.org/10.3390/diagnostics13010161
ultrasound images remain challenging to segment with high [11] Jabeen, K., Khan, M.A., Alhaisoni, M., Tariq, U., Zhang,
precision. Y.D., Hamza, A., Mickus, A., Damaševičius, R. (2022).
There exists a future scope for implementing high Breast cancer classification from ultrasound images
performance and enhanced preprocessing stages, lightweight using probability-based optimal deep learning feature
deep learning networks which requisite lesser computation and fusion. Sensors, 22(3): 807.
leveraging attention-based hybrid models to improve https://doi.org/10.3390/s22030807
segmentation accuracy. Overall, our results illustrate that the [12] Martinez, R.G., Van Dongen, D.M. (2023). Deep
proposed framework significantly enhances segmentation learning algorithms for the early detection of breast
accuracy and offers a strong foundation for advancing cancer: A comparative study with traditional machine
computer-assisted breast cancer diagnostic. learning. Informatics in Medicine Unlocked, 41: 101317.
https://doi.org/10.1016/j.imu.2023.101317
[13] Zhai, D., Hu, B., Gong, X., Zou, H., Luo, J. (2022). ASS-
FUNDING GAN: Asymmetric semi-supervised GAN for breast
ultrasound image segmentation. Neurocomputing, 493:
This research is supported by Princess Nourah bint 204-216. https://doi.org/10.1016/j.neucom.2022.04.021
Abdulrahman University Researchers Supporting Project [14] Abo-El-Rejal, A., Ayman, S., Aymen, F. (2024).
number (PNURSP2025R195), Princess Nourah bint Advances in breast cancer segmentation: A
Abdulrahman University, Riyadh, Saudi Arabia. comprehensive review. Acadlore Transactions on AI and
Machine Learning, 3(2): 70-83.
https://doi.org/10.56578/ataiml030201
REFERENCES [15] Podda, A.S., Balia, R., Barra, S., Carta, S., Fenu, G.,
Piano, L. (2022). Fully-automated deep learning pipeline
[1] World Health Organization. Breast cancer. for segmentation and classification of breast ultrasound
https://www.who.int/news-room/fact- images. Journal of Computational Science, 63: 101816.
sheets/detail/breast-cancer. https://doi.org/10.1016/j.jocs.2022.101816
[2] Mehrotra, R., Yadav, K. (2022). Breast cancer in India: [16] Bilic, A., Chen, C. (2024). BC-MRI-SEG: A breast
Present scenario and the challenges ahead. World Journal cancer MRI tumor segmentation benchmark. In 2024
of Clinical Oncology, 13(3): 209-218. IEEE 12th International Conference on Healthcare
https://doi.org/10.5306/wjco.v13.i3.209 Informatics (ICHI), Orlando, USA, pp. 674-678.
[3] Kalyanpur, A. (2008). Commentary 3-radiology in India: https://doi.org/10.1109/ICHI61247.2024.00107
The next decade. Indian Journal of Radiology and [17] Belaid, A., Boukerroui, D., Maingourd, Y., Lerallut, J.F.
Imaging, 18(3): 191-192. https://doi.org/10.4103/0971- (2010). Phase-based level set segmentation of ultrasound
3026.41869 images. IEEE Transactions on Information Technology
[4] U.S. Food and Drug Administration. Ultrasound imaging. in Biomedicine, 15(1): 138-147.
https://www.fda.gov/radiation-emitting- https://doi.org/10.1109/TITB.2010.2090889
products/medical-imaging/ultrasound-imaging. [18] Chen, M., Xing, J., Guo, L. (2024). MRI-based deep
[5] Gu, P., Lee, W., Roubidoux, M.A., Yuan, J., Wang, X., learning models for preoperative breast volume and
Carson, P.L. (2015). Automated 3D ultrasound image density assessment assisting breast reconstruction.
segmentation to aid breast cancer image interpretation. Aesthetic Plastic Surgery, 48(23): 4994-5006.
2921

https://doi.org/10.1007/s00266-024-04074-2 learning model and dataset for segmentation of breast,
[19] Zhang, S., Liao, M., Wang, J., Zhu, Y., Zhang, Y., Zhang, fibroglandular tissue, and vessels in breast MRI.
J., Zheng, R., Lv, L., Zhu, D., Chen, H., Wang, W. (2023). Scientific Reports, 14(1): 5383.
Fully automatic tumor segmentation of breast ultrasound https://doi.org/10.1038/s41598-024-54048-2
images with deep learning. Journal of Applied Clinical [24] Sarti, A., Corsi, C., Mazzini, E., Lamberti, C. (2005).
Medical Physics, 24(1): e13863. Maximum likelihood segmentation of ultrasound images
https://doi.org/10.1002/acm2.13863 with Rayleigh distribution. IEEE Transactions on
[20] Ranjitha, K.V., Pushphavathi, T.P. (2024). Improving Ultrasonics, Ferroelectrics, and Frequency Control,
prediction accuracy for neo-adjuvant chemotherapy 52(6): 947-960.
response in breast cancer through 3D image https://doi.org/10.1109/TUFFC.2005.1504017
segmentation and deep learning techniques. Artificial [25] Tanaka, H., Chiu, S.W., Watanabe, T., Kaoku, S.,
Intelligence in Medicine, 137-162. Yamaguchi, T. (2019). Computer-aided diagnosis
https://www.taylorfrancis.com/chapters/edit/10.1201/97 system for breast ultrasound images using deep learning.
81003369059-12/improving-prediction-accuracy-neo- Physics in Medicine & Biology, 64(23): 235013.
adjuvant-chemotherapy-response-breast-cancer-3d- https://doi.org/10.1088/1361-6560/ab5093
image-segmentation-deep-learning-techniques-ranjitha- [26] Pramanik, P., Pramanik, R., Schwenker, F., Sarkar, R.
pushphavathi. (2023). DBU-Net: Dual branch U-Net for tumor
[21] Boukerroui, D., Baskurt, A., Noble, J.A., Basset, O. segmentation in breast ultrasound images. Plos One,
(2003). Segmentation of ultrasound images- 18(11): e0293615.
multiresolution 2D and 3D algorithm based on global and https://doi.org/10.1371/journal.pone.0293615
local statistics. Pattern Recognition Letters, 24(4-5): 779- [27] Chen, G., Li, L., Dai, Y., Zhang, J., Yap, M.H. (2022).
790.https://doi.org/10.1016/S0167-8655(02)00181-2 AAU-net: An adaptive attention U-net for breast lesions
[22] Forghani, Y., Timotoe, R., Figueiredo, M., Marques, T., segmentation in ultrasound images. IEEE Transactions
Batista, E., Cordoso, F., Cardoso, M.J., Santinha, J., on Medical Imaging, 42(5): 1289-1300.
Gouveia, P. (2024). Breast tissue segmentation in MR https://doi.org/10.1109/TMI.2022.3226268
images using deep-learning. European Journal of Cancer, [28] Lu, Y.M. (2024). Breast ultrasound image segmentation
200(S1): 113876. based on attention U-Net. In Proceedings of the 2nd
https://doi.org/10.1016/j.ejca.2024.113876 International Conference on Machine Learning and
[23] Lew, C.O., Harouni, M., Kirksey, E.R., Kang, E.J., Dong, Automation, CONF-MLA 2024, Adana, Turkey.
H., Gu, H., Grimm, L.J., Walsh, R., Lowell, D.A., https://doi.org/10.4108/eai.21-11-2024.2354629
Mazurowski, M.A. (2024). A publicly available deep
2922
2023 6th International Conference on Contemporary Computing and Informatics (IC3I)
Fall Detection Methods for Elderly People- A
Comprehensive Survey
Vedant Vinay Ganthade Adityaraj Sanjay Belhe Prathamesh Suhas Uravane
Research Center of Excellence Research Center of Excellence Research Center of Excellence
for Health Informatics for Health Informatics for Health Informatics
Vishwakarma University Vishwakarma University Vishwakarma University
Pune, India. Pune, India. Pune, India.
202001143@vupune.ac.in 202000611@vupune.ac.in 202001369@vupune.ac.in
Abhiraj Sandeep Gadade Mamoon Rashid
Research Center of Excellence Research Center of Excellence
for Health Informatics for Health Informatics
Vishwakarma University Vishwakarma University
Pune, India. Pune, India.
202001236@vupune.ac.in mamoon.rashid@vupune.ac.in
Abstract— This survey research gives a thorough analysis physical injuries like fractures and head trauma, as well as
of sensor technology and picture preprocessing methods for fall psychological effects like fear of falling again and a decline
detection systems for elderly people. Caretakers face serious in overall mobility. As the average age of the falling elderly
health hazards and difficulties when an older person falls.
population varies by region, it is crucial to examine the
Numerous sensor-based and vision-based solutions have been
specific risks faced by different countries and cultures.
put forth to deal with this problem. This survey talks about the
difficulties with effective implementation of these techniques,
With an increasing trend of global mobility, many
such as sensor location, data fusion, and power management. It
also examines several pictures’ preprocessing methods, children of aging parents now reside abroad, making it
including background removal, object detection, tracking, and challenging for them to be physically present to offer
feature extraction, which are crucial for improving the precision immediate assistance in times of need. This geographical
and responsiveness of vision-based systems. This study also separation can be particularly distressing during serious fall
examines the benefits and drawbacks of the various sensor incidents, as elderly individuals may find themselves without
technologies used, such as accelerometers, gyroscopes, depth
immediate access to family members who can provide help
cameras, infrared sensors, pressure mats, and wearables.
or coordinate emergency responses. The inability to receive
Important data on elderly falls is also provided to further
prompt aid from loved ones can exacerbate the physical and
emphasize how urgent it is to have effective fall detection
emotional consequences of a fall, leaving the elderly person
systems. With the help of improved fall detection systems, this
study will serve as a significant resource for researchers and feeling isolated and vulnerable. In such circumstances,
practitioners, leading future developments to increase the safety technology-driven solutions that enable remote monitoring,
and well-being of senior people automatic fall detection, and communication with family
members or healthcare providers become vital lifelines,
Keywords— Computer Vision, Machine Learning, Deep offering a sense of security and support despite the physical
Learning, Sensors, Image Preprocessing, CNN, LSTM, Fall,
distance. The information obtained from the World health
Detection. organization WHO shows that the approximate rate of falling
65 age people is 28 to 35%, and the 32 to 42% of age 70 is
I. INTRODUCTION
increasing day by day.
The phenomenon of falls among elderly individuals has
In recent years, modern technology has revolutionized
become a matter of utmost importance and concern in today's
the way we care for elderly individuals, with one particularly
aging societies. As the world's population continues to age,
impactful application being the detection of falls and timely
the impact of falls on the health and well-being of older adults
alerts to their caregivers. Falls among the elderly are a
has garnered significant attention. Understanding the
significant concern, often resulting in serious injuries and
intricacies of how and why these falls occur is essential for
reduced quality of life. Leveraging the power of advanced
developing effective fall prevention and monitoring
technologies, such as motion sensors, wearable devices, and
strategies. Elderly individuals often experience falls due to
smart home automation, allows for the development of
various factors, including age-related changes in balance and
unobtrusive and effective fall detection systems. By
mobility, chronic health conditions, medication side effects,
harnessing the potential of modern technology, we can
and environmental hazards. Their postures during falls can
enhance the well-being of our elderly population and ensure
vary, with common patterns including trips, slips, and
that they receive the prompt care and support they need to
missteps, often leading to sudden loss of balance. The
lead fulfilling lives.
consequences of such falls are far-reaching, encompassing
2477
979-8-3503-0448-0/22/$31.00 ©2023 IEEE
11879301.3202.71195I3CI/9011.01
:IOD
|
EEEI
3202©
00.13$/32/0-8440-3053-8-979
|
)I3CI(
scitamrofnI
dna
gnitupmoC
yraropmetnoC
no
ecnerefnoC
lanoitanretnI
ht6
3202
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:06:11 UTC from IEEE Xplore. Restrictions apply.

2023 6th International Conference on Contemporary Computing and Informatics (IC3I)
A significant increase in studies examining various daily activities to detect falls by watching their movements.
sensor and image preprocessing based techniques for They have analyzed a number of methodologies and
precisely identifying falls among the elderly has been classified them according to their strengths and weaknesses.
observed recently in the field of fall detection research. This The methods they have discussed fall primarily into three
survey paper aims to comprehensively review and compare categories [2]. This research displays the performance,
these sensor and image-based methodologies, shedding light difficulties, and restrictions of the fall detection system's
on their individual strengths, limitations, and applicability in multisensory data fusion as well as the most recent
real-world scenarios. Furthermore, we will delve into the approaches and trends are discussed in this paper. In
challenges faced by these approaches when deployed in comparison to single sensor approaches, this paper
today's dynamic and diverse environments, seeking to emphasizes the benefits of developing multimodal fall
identify potential areas of improvement and avenues for detection systems and discusses issues that will be helpful
further research to foster the development of robust and going forward [3]. Similarly, the authors here have prepared
effective fall detection systems. By presenting an in-depth the survey for different fall detection systems and their
analysis of the state-of-the-art techniques, this survey aims to underlying algorithms and the methods of fall detection are
contribute to the advancement of fall detection technology categorized into three groups: wearable device-based, vision
and facilitate its integration into the lives of the elderly, device-based, and ambience device-based. These methods are
promoting their safety and well-being in an increasingly contrasted with one another and may be used in future
aging society. research [4]. The authors of this paper have presented the
three stages of a fall, including prediction, prevention, and
The major contributions of this survey are discussed as detection. They have created a fall diagnosis system that
follows: includes edge, fog, and cloud layer illustrations. For
upcoming work, they have also discussed the difficulties of
• This survey efficiently points down all the major fall diagnosis [5]. The authors of this survey claim to be
contributions of authors who have made their researching the specifications needed for fall detection
contributions for the fall detection systems in the systems, as well as showcasing recent works on the subject
past five years. using a machine learning approach. They have also analyzed
the difficulties encountered in fall detection systems using
• In this survey, we have noted down the two main literature survey [6]. The survey here conveys three different
approaches and their detailed explanations, used by categories of fall detection algorithms: wearable technology,
all researchers world-wide, i.e., sensor based and which is affordable, inconvenient, but accurate; audio-based
image-based approaches. technology, which is affordable but convenient compared to
wearable technology; and video-based technology, which is
• Sensor based and image-based systems possess accurate and simple to install, and these three technologies
many challenges in their way to deployment and will perform best. [7]. In this survey paper, the authors
after deployment too. This survey mentions down all discuss various fall detection systems based on Field
the challenges of the well-known research in this Programmable Gate Arrays [FPGAs] and provides an
domain. explanation of key theoretical concepts, practical
applications, and algorithms for accelerometer-based fall
• This survey is designed in such a way that all detection systems. The authors also provide the main design
scholars and students would get the idea of fall steps for fall detection systems [8]. The authors of this paper
detection systems and their applicability. have used the Neyman-Pearson framework to design the
detection method. In order to gather information about the
• Detailed methodology of the fall detection systems movement of elderly people, they have also attached a
including feature extraction methods and signal TelosW mote with an accelerometer to their waists. They
preprocessing for the sensors are also mentioned have spent a lot of time working on this to increase the
down. effectiveness and accuracy of the detection system [9].
II. RELATED WORKS III. METHODOLOGY
The authors of this research have provided a summary of Sensor-based and machine learning (ML) based
the fall detection research and have also covered the key approaches have gained popularity in the last five years of
issues surrounding fall detection. For this, they have gathered research regarding fall detection for elderly people due to
and analyzed relevant documents, and facts. Out of all the their combined effectiveness and practicality. Sensor-based
documents, they have only selected a few articles based on methods leverage a diverse range of devices, such as
three criteria: sensor, performance, and algorithms [1]. The accelerometers, gyroscopes, and pressure sensors, to capture
authors in this research have discussed a number of automatic motion and environmental data, enabling accurate and
techniques as well as methods that will track elderly people's unobtrusive fall detection in real-time. These sensors are
2478
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:06:11 UTC from IEEE Xplore. Restrictions apply.

2023 6th International Conference on Contemporary Computing and Informatics (IC3I)
readily available, affordable, and non-intrusive, making them are applied to differentiate between fall and non-fall patterns
suitable for continuous monitoring of the elderly without based on the extracted features. These algorithms are
disrupting their daily activities. On the other hand, ML-based provided with rule-based threshold values that conclude
techniques offer the ability to process and analyze large instances of both fall and non-fall movements. Once trained,
volumes of sensor data, enabling the creation of sophisticated the system can accurately recognize fall events in real-time
fall detection algorithms. Machine learning models can learn based on new incoming sensor data. This approach leverages
patterns indicative of falls from labeled datasets, allowing for the advantages of sensor technology to provide prompt and
continuous improvement and adaptability to different reliable fall detection, offering increased safety and timely
scenarios and individuals. The combination of sensor-based assistance for individuals at risk of falls.
and ML-based approaches harnesses the strengths of both
technologies, resulting in robust and reliable fall detection Let us now discuss the three important steps of the
systems. As research progresses, the integration of these sensor-based systems.
methods holds great promise in enhancing the safety and care
of elderly individuals, reducing the risk of fall-related 1. Signal Preprocessing: Signal preprocessing is the
injuries, and providing timely assistance when needed. initial step in the fall detection process, aimed at
enhancing the quality of the raw sensor data. This
In Figure number 1, a detailed flowchart of how this involves techniques such as noise filtering, data
whole process carries out, and how sensor based and image- resampling, and signal conditioning. The sensor data
based approaches work are displayed. collected from accelerometers, gyroscopes, and
other sensors can contain noise and artifacts due to
various factors, including sensor inaccuracies,
movement irregularities, and environmental
interference. Preprocessing techniques are applied
to remove or reduce these unwanted components,
ensuring that the data is accurate and reliable for
further analysis.
2. Feature Extraction: Feature extraction involves
identifying specific characteristics or patterns in the
pre-processed sensor data that are indicative of fall
events. These features act as discriminative markers
that distinguish between normal activities and fall-
related movements. Features can include statistical
parameters (mean, variance, skewness), frequency
domain components (spectral energy), and time-
domain characteristics (jerk, orientation changes).
The choice of features depends on the sensor
modality, the type of movements being detected, and
Figure 1. Flow Diagram for the Fall Detection systems the complexity of the analysis. Effective feature
extraction is essential for providing relevant
A. Sensor Based Approach information to the classification stage.
The methodology for fall detection using sensor-based 3. Classification Stage: In the classification stage, the
systems involves the integration of various sensors to capture extracted features are used to differentiate between
the movements and behaviors of individuals. These sensors, fall and non-fall events. Rule-based threshold
such as accelerometers, gyroscopes, and sometimes systems involve setting predefined thresholds for
magnetometers, are strategically placed on the body or within specific features based on empirical observations or
the environment to collect motion-related data. This data is expert knowledge. When the extracted feature
then processed and analyzed to detect sudden and abnormal values exceed these thresholds, the system classifies
changes that might indicate a fall event. The fall detection the event as a fall. For instance, if the magnitude of
process typically encompasses signal preprocessing, feature acceleration surpasses a certain threshold within a
extraction, and classification stages. Preprocessing involves short time frame, it could indicate a rapid fall
filtering and noise reduction to enhance the quality of the movement. Rule-based approaches are
sensor data. Feature extraction involves identifying relevant straightforward to implement and require no
characteristics from the sensor signals that can help extensive training; however, they may be limited in
distinguish between normal activities and fall events. Finally, their adaptability to different scenarios and
classification techniques, often machine learning algorithms, individuals.
2479
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:06:11 UTC from IEEE Xplore. Restrictions apply.

2023 6th International Conference on Contemporary Computing and Informatics (IC3I)
image acquisition, preprocessing, feature extraction, and
In a rule-based threshold system, the decision-making classification, go into the creation of image-based fall
process is determined by a set of predetermined rules that detection systems. In order to improve their quality and
dictate when a fall is detected based on specific feature values eliminate noise, images or frames from video streams are
and their relationships. While these systems can provide recorded and pre-processed. Then, using feature extraction
quick and simple fall detection, they might lack the techniques, pertinent traits are found, including body posture,
adaptability and customization that machine learning-based movement direction, and spatial correlations. To identify fall
approaches offer. and non-fall activities based on the extracted features,
machine learning techniques, such as deep neural networks,
Sensors are the heart of this approach. The kind of support vector machines, or decision trees, are trained on
sensors that are generally used by the researchers to support labelled datasets. In order to identify abrupt changes in
their methodology are shown in the table number 1. posture or unusual motions suggestive of a fall, the trained
model can then analyse real-time visual data. Since wearable
TABLE I. POPULAR SENSORS AND THEIR FUNCTIONALITIES devices are not necessary for unobtrusive fall detection,
Sensors Functionality image-based solutions are suited for a variety of settings and
Measures acceleration forces in various
user preferences.
directions. Detects changes in motion and
Accelerometer
orientation, crucial for identifying sudden
falls. The development of precise and dependable systems for
Measures angular velocity and rate of image-based fall detection has previously investigated a
Gyroscope rotation. Provides information about variety of computer vision techniques. These investigations
rotational movements and helps determine
looked into how to capture human postures and motions using
body orientation.
RGB cameras, depth sensors, and combinations of the two.
Measures magnetic field strength and To extract pertinent information from image data, techniques
Magnetometer direction. Used in combination with other
including human posture estimation, motion analysis, and
sensors to determine orientation relative to
the Earth's magnetic field. spatial-temporal modelling have been used. Convolutional
and recurrent neural networks, among other deep learning
Measures changes in atmospheric pressure.
Pressure Sensor architectures, have been successfully used to distinguish
Can be used to detect posture changes, such
as sitting or lying down. between fall and non-fall activities. To improve system
robustness, researchers have tackled issues like occlusion,
Inertial Combines accelerometer, gyroscope, and
changing lighting, and various surroundings. Numerous
Measurement Unit sometimes magnetometer data to provide
(IMU) comprehensive information about motion, studies have also looked at real-time performance, taking into
orientation, and angular velocity. account how quickly and effectively fall detection systems
may be put into operation. The goal of image-based fall
Also, the capabilities and efficacy of sensor-based fall detection research is to develop precise, non-intrusive
detection systems are improved by the Internet of Things technologies that can improve people's safety and well-being,
(IoT) technology integration. Real-time data gathering, especially the elderly, by facilitating quick help in the event
analysis, and response are made possible by IoT, which of fall accidents.
enables seamless connectivity and communication
across various sensors, wearable technology, and IV. CHALLENGES IN SENSOR AND IMAGE BASED
centralized platforms. Systems for detecting falls that are APPROACHES
IoT-enabled can send sensor data, such as acceleration
and orientation data, to a processing server or cloud There are a number of difficulties involved in creating
platform. As a result, fall incidents can be continuously sensor-based fall detection systems that must be carefully
monitored for and quickly detected, allowing automated taken into account. To enable correct analysis, integrating
alarms to be sent to family members, carers, or data from heterogeneous sensors—each with unique
emergency services. IoT also enables remote monitoring, properties—requires meticulous synchronisation and
allowing carers to check a person's history of falls and harmonisation. It is essential to choose the best sensor
daily activity patterns via mobile applications or web placements to provide both effective fall detection and user
interfaces. comfort. Noise and artefacts can degrade the quality of sensor
data, which makes the development of advanced noise
B. Image Based Approach reduction algorithms necessary. The system must be able to
adapt to a variety of settings, which is made difficult by the
Computer vision techniques are used by mages-based real-world unpredictability in human movements and
fall detection systems to analyse photos or video streams and behaviours. To achieve high detection accuracy while
find instances of falls. These systems frequently include reducing false positives, specialised algorithms are required
cameras, depth sensors, or other visual input devices to record for unbalanced datasets when falls are uncommon relative to
people's postures and motions. Several phases, including everyday activity. It is crucial to choose the right threshold
2480
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:06:11 UTC from IEEE Xplore. Restrictions apply.

2023 6th International Conference on Contemporary Computing and Informatics (IC3I)
values for fall detection because improper settings can result
in missed falls or pointless alarms. Effective algorithm design In the Table number 2, a detailed work description of all
is necessary since wearable devices have limited the research work of this expertise and their challenges are
computational and battery capacity. It can be difficult to noted down.
guarantee real-time performance for timely warnings,
especially on devices with limited capabilities.
TABLE II. RELATED WORKS WITH THEIR CHALLENGES
Researchers Approach Methodology Challenges Accuracy Year
VMR Anakala, etc. Threshold based system, with a CNN 1. Lack of AI Generalization
[10]
Sensor Based.
classifier model. 2. Accuracy and False Positives
N/A 2023
Sakshi Shukralia, etc.
ISBFD (Inertial Sensor Based Fall
1. Data Variability
[11]
Sensor Based. Detection) concept, utilizing real-time
2. Ethical and Privacy Concerns
93% 2023
accelerometer data from smartphones.
A fall detection technique utilizing a
combination of 1-D point cloud and 1. Practicality and User Acceptance
Nader Maray, etc. [12] Combined.
doppler velocity data as inputs to a Long 2. Model Drift across devices
N/A 2023
Short-Term Memory (LSTM) network.
Chainarong 1. Data Collection and Variation
Kittiyanpunya, etc. Machine Learning.
Machine Learning with multimodal
2. Feature Selection and Input 99.50% 2023
dataset
[13] Dimensionality
Created LSTM network employed as
Chainarong Millimeter -Wave intelligent classifier and millimeter wave
N/A 99.50% 2023
Kittiyanpunya, etc.[14] Radar -Based. frequency modulated continuous wave for
collection of radar signals
Sakorn
Using Hybrid deep residual neural 1. Always attached to body
Mekruksavanich etc. Wearable Based
network. 2. Model optimization
95.1% 2022
[15]
Discussing about different metrics that
Ekram Alam a, etc.
Vision Based. helps in assess performance of fall N/A N/A 2022
[16]
detection system.
1. Sensor Modalities Integration 99.56%
Xiaodan Wu a, etc.
Mobile Sensors.
Using deep learning technology for
2. Difficult to determine complex and 2022
[17] automatic fall detection.
fall. 60.69%
V. CONCLUSION
[1] Xu, Tao, Yun Zhou, and Jing Zhu. 2018. "New Advances and
The necessity to improve the safety and wellbeing of Challenges of Fall Detection Systems: A Survey" Applied Sciences 8,
no. 3: 418. https://doi.org/10.3390/app8030418.
elderly people has resulted in notable breakthroughs in the
[2] F. Hijaz, N. Afzal, T. Ahmad and O. Hasan, "Survey of fall detection
field of fall detection systems. Utilizing accelerometers, and daily activity monitoring techniques," 2010 International
gyroscopes, and other sensors on wearable technology, Conference on Information and Emerging Technologies, Karachi,
sensor-based techniques record motion data. These Pakistan, 2010, pp. 1-6, doi: 10.1109/ICIET.2010.5625702.
[3] V. -R. Xefteris, A. Tsanousa, G. Meditskos, S. Vrochidis and I.
techniques address issues such data heterogeneity, the best
Kompatsiaris, "Performance, Challenges, and Limitations in
location for sensors, and real-time performance. Image-based Multimodal Fall Detection Systems: A Review," in IEEE Sensors
systems, on the other hand, use computer vision techniques Journal, vol. 21, no. 17, pp. 18398-18409, 1 Sept.1, 2021, doi:
to overcome obstacles including appearance variability, 10.1109/JSEN.2021.3090454.
[4] Muhammad Mubashir, Ling Shao, Luke Seed, “A survey on fall
occlusions, and privacy issues related to camera use. Machine
detection: Principles and approaches”,Neurocomputing,Volume
learning algorithms that span from conventional approaches 100,2013,Pages 144-152, ISSN 0925-
like rule-based threshold systems to complex deep learning 2312,https://doi.org/10.1016/j.neucom.2011.09.037.
models support both approaches. We face challenges like [5] Nassim Mozaffari, Javad Rezazadeh, Reza Farahbakhsh, Samaneh
Yazdani, Kumbesan Sandrasegaran, Practical fall detection based on
dataset variability, resource limitations, and ethical concerns
IoT technologies: A survey, Internet of Things, Volume 8, 2019,
as we go through sensor-based and image-based fall 100124, ISSN 2542-6605, https://doi.org/10.1016/j.iot.2019.100124.
detection. The convergence of technology, user-centric [6] Anita Ramachandran, Anupama Karuppiah."A Survey on Recent
design, and ethical responsibility holds the key to solving Advances in Wearable Fall Detection Systems".BioMed Research
International.Volume 2020 | Article ID 2167160 |
these problems. Fall detection systems will effectively protect
https://doi.org/10.1155/2020/2167160.
the independence and dignity of our older population in the [7] O. Mohamed, H. -J. Choi and Y. Iraqi, "Fall Detection Systems for
future thanks to the convergence of IoT connection, machine Elderly Care: A Survey," 2014 6th International Conference on New
learning process, and a dedication to user acceptance. Technologies, Mobility and Security (NTMS), Dubai, United Arab
Emirates, 2014, pp. 1-4, doi: 10.1109/NTMS.2014.6814018.
[8] Chen, Gorong & Islam, Mohaiminul. (2019). Big Data Analytics in
Healthcare. 10.1109/IICSPI48186.2019.9095872.
REFERENCES [9] Y. Li, G. Chen, Y. Shen, Y. Zhu and Z. Cheng, "Accelerometer-based
fall detection sensor system for the elderly," 2012 IEEE 2nd
2481
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:06:11 UTC from IEEE Xplore. Restrictions apply.

2023 6th International Conference on Contemporary Computing and Informatics (IC3I)
International Conference on Cloud Computing and Intelligence
Systems, Hangzhou, China, 2012, pp. 1216-1220, doi:
10.1109/CCIS.2012.6664577.
[10] Anakala, Vijay Mohan Reddy, et al. "Fall Detection and Elderly
Monitoring System Using the CNN." Machine Learning and
Computational Intelligence Techniques for Data Engineering:
Proceedings of the 4th International Conference MISP 2022, Volume
2. Vol. 998. Springer Nature, 2023.
[11] Shukralia, Sakshi, M. P. S. Bhatia, and Pinaki Chakraborty. "Fall
Detection of Elderly in Ambient Assisted Smart Living Using CNN
Based Ensemble Approach." E-business technologies conference
proceedings. Vol. 3. No. 1. 2023.
[12] Maray, Nader, et al. "Transfer learning on small datasets for improved
fall detection." Sensors 23.3 (2023): 1105.
[13] C. Kittiyanpunya, P. Chomdee, A. Boonpoonga and D. Torrungrueng,
"Millimeter-Wave Radar-Based Elderly Fall Detection Fed by One-
Dimensional Point Cloud and Doppler," in IEEE Access, vol. 11, pp.
76269-76283, 2023, doi: 10.1109/ACCESS.2023.3297512.
[14] C. Kittiyanpunya, P. Chomdee, A. Boonpoonga and D. Torrungrueng,
"Millimeter-Wave Radar-Based Elderly Fall Detection Fed by One-
Dimensional Point Cloud and Doppler," in IEEE Access, vol. 11, pp.
76269-76283, 2023, doi: 10.1109/ACCESS.2023.3297512.
[15] Mekruksavanich, S., Jantawong, P., Hnoohom, N., Jitpattanakul, A.
(2022). Wearable Fall Detection Based on Motion Signals Using
Hybrid Deep Residual Neural Network. In: Surinta, O., Kam Fung
Yuen, K. (eds) Multi-disciplinary Trends in Artificial Intelligence.
MIWAI 2022. Lecture Notes in Computer Science(), vol 13651.
Springer, Cham. https://doi.org/10.1007/978-3-031-20992-5_19.
[16] Ekram Alam, Abu Sufian, Paramartha Dutta, Marco Leo, Vision-based
human fall detection systems using deep learning: A review, Computers
in Biology and Medicine, Volume 146, 2022, 105626, ISSN 0010-
4825, https://doi.org/10.1016/j.compbiomed.2022.105626.
[17] Xiaodan Wu, Yumeng Zheng, Chao-Hsien Chu, Lingyu Cheng,
Jungyoon Kim, Applying deep learning technology for automatic fall
detection using mobile sensors, Biomedical Signal Processing and
Control, Volume 72, Part B, 2022, 103355, ISSN 1746-8094,
https://doi.org/10.1016/j.bspc.2021.103355.
2482
Authorized licensed use limited to: University of Maryland College Park. Downloaded on February 15,2026 at 04:06:11 UTC from IEEE Xplore. Restrictions apply.
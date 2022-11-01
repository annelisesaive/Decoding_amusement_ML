# A Time-Resolved ML Model to Predict the Intensity of Amusement during Video Viewing

### *Code for the paper "Wait for it! Predicting the time course of humorous amusement using machine learning"*

### Abstract and goal of the research paper
The present study aims to implement and validate a machine learning approach to predict the intensity of amusement evoked by viewing humorous video clips. We used a supervised Random Forest (RF) algorithm to predict 1) amusement intensity over time using participants' facial expressions and features of the viewed videos, 2) track its temporal dynamics, and 3) explore its long-term impact on subsequent trials. We found that viewing videos that were perceived as being amusing was associated with a higher propensity to smile (% Smile) - a combination of raising cheek (AU6) and pulling corner (AU12) - and that movement and saliency of humorous videos - known to reflect movies' genre (ex: action, romance, horror) - was significantly different than neutral videos. We also found that participants' tendency to smile was the most significant contribution to a successful prediction (R=0.522, p.001), and peaked toward the end of the videos with significant carry-over effects from one video over to the next. Our results highlight methodological avenues for refining basic and clinical humour research protocols by identifying the best time window for measuring and tracking amusement and characterizing the duration of the potentiating effect of humor across trials.

### Technologies, libraries and frameworks used
- **Language**: Python (Jupyter Notebook)
- **Data Manipulation**: Pandas, Numpy
- **Visualization**: Seaborn, Matplotlib
- **Machine-Learning & Stats**: Scikit-Learn, Scipy, Statsmodels
- **Task Creation**: Psychopy3
- **Features Creation**: OpenFace2, OpenCV, Natural Language Toolkit (NLTK)

## Project Folder

-   **Behavioral Task** : The task created in Psychopy3 to collect behavioral data and record facial expressions of the participant

-   **Features Creation** : Features extraction from video-recordings

-   **ML Pipeline** : ML model to predict the intensity of amusement during watching humorous videos

### Contributors
The code was primarily wrote by [Gabrielle Toupin](https://github.com/Rammen/) and was reviewed by [Anne-Lise Saive](https://github.com/annelisesaive), [Arthur Deghan](https://github.com/arthurdehgan) and [Karim Jerbi](https://github.com/k-jerbi)

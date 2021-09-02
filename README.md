# Master Thesis:  *Characterization of funniness intensity perceived by people using machine learning techniques*

This repo contains scripts that I wrote for my master's thesis in Cognitive neuroscience and Applied Machine Learning.

Funniness perception varies significantly between people, and most clinical studies do not consider how funny the patient finds the content. My thesis project aims to set foundations to identify objectively how funny the patient perceives the content. I explore how information from the video itself (e.g. movement) and the participant (e.g. facial expression) help predict the funniness of a video.  

*Link to the thesis will be added once it is approved by the comitee*

### Technologies, libraries and frameworks I used
- **Language**: Python (Jupyter Notebook)
- **Data Manipulation**: Pandas, Numpy
- **Visualization**: Seaborn, Matplotlib
- **Machine-Learning & Stats**: Scikit-Learn, Scipy, Statsmodels
- **Task Creation**: Psychopy3
- **Features Creation**: OpenFace2, OpenCV, Natural Language Toolkit (NLTK)

### Scientific Articles
Fundamental Research Article (main thesis article):
- Toupin, G.,  Saive, A.-L. & Jerbi, K. *Decoding the intensity of humour appreciation over time.* Manuscrit in preparation for Physiology & Behavior.

Applied Research Article:
- Toupin, G.,  Benlamine, S., Frasson, C. (2021). *Prediction of amusement intensity based on brain activity*. Frontiers in Artificial Intelligence and Applications


## Project Folder

In this repo, you can found the code I wrote for the fundamental research article used in my thesis:

-   **Behavioral Task** : The task I created in Psychopy3 to collect behavioral data and record facial expression of the participant

-   **Features Creation** : How I extracted the different information (e.g. movement) from each video

-   **ML Pipeline** : The pipeline I put in place to explore how facial expression and video content impact the rating of funinness

## Fundamental Article (abstract)

Humour is a complex cognitive process that can result in a positive emotional state of mirth that has several health benefits. Research and clinical trials use humour as treatment but never actually consider the large variabilities between different individuals. A reliable and objective measure of humour appreciation could benefit futures studies employing humour. In this study, 40 participants watched and rated humorous videos while their facial expressions were recorded. For each video clip, we extracted the movement, saliency and two measures of semantic distance. We used physiological reactions and video characteristics at three moments during the trial (beginning, middle, end of the video) to predict how funny (neutral, funny, very funny) the participant would rate the video. Video characteristics were good at predicting between neutral and humorous video but not the intensities of humorous video (accuracy=64.1%). The proportion of smiles was the only feature to fluctuate drastically in time, showing that physiological information is better to identify the humorous moment in the video. Smiles were also better than video characteristics to predict amusement intensities within humorous videos. Furthermore, this study shows that humour appreciation is impacted by how the previous video is perceived. Videos are perceived more funny when the one preceding is funnier (r=0.477, p<0.001). Smiling associated with a humorous video lasts until the middle of the following one showing that funniness is incremental and can last even when the humorous situation is completed. More than only lasting after the content, the correlation between smiles and funniness rating is stronger after the video (r=0.703, p<0.001) than during (r=0.324, p<0.001). This study supports that different humorous content can induce different emotional states. Using physiological information such as facial expression is easy to add to an experiment and would highly benefit further studies using humour.

## Application in real-life

I completed a complementary project in a public partnership with the company [Beam Me Up](https://www.bmu.co/). In this project, we train an LSTM model to predict amusement intensity of the participant in real-time based on its brain activity while watching the video (14 electrods x 128 epochs). 

While the code of this section is confidential, details about this project will be published in September 2021 in [Frontiers in Artificial Intelligence and Applications](https://www.iospress.com/catalog/book-series/frontiers-in-artificial-intelligence-and-applications). 

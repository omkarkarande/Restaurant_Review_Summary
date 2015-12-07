Download the yelp dataset from the link https://www.yelp.com/dataset_challenge/dataset and extract it. The code needs NLTK and spacey.io library installed on the machine. It also requires NLTK Vader, the file for which is included in the /Vader folder in the submission.

The code scripts have to be executed in the following order:

1. preprocessing/preprocessing.py 
   USAGE: python preprocessor.py <dir to yelp files>

2. feature_detection/features.py
   USAGE: python features.py "<path to reviews folder>"  > redirect to out file

3. feature_detection/frequency_distribution.py
   USAGE: python frequency_distribution.py <path to features.py output file>

4. feature_detection/label_generator.py 
   USAGE: python frequency_distribution.py <path to "categorial words" file> <path to word freq file>

5. feature_detection/basebuilder.py 
   USAGE: python basebuilder.py <path to labels folder>

6. sentiment_analysis/sentiment_analysis.py
   USAGE: python preprocessor.py <dir to yelp files>

7. feature_detection/feature_detector.py 
   USAGE: python feature_detector.py <features.model file> <path to review_sentiment dir>  > redirect to out file

8. food list/getMenus.py
   USAGE: python preprocessor.py <path to reviews folder>

9. food list/combineMenus.py
   USAGE: python preprocessor.py <path to menus folder>

10.food list/getRecommendedFood.py
   USAGE: python preprocessor.py <path to menufile.txt> <path to review_sentiments folder> 

The /food folder will contain the list of food items and the output file of feature_detector.py will contain the rating values for individual categories.



#importing Textblob library and Naivebayesanalyzer to analyze the statement
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer #The analyzer consists of Positive and Negative datasets

review = open('movieReviews.txt', 'r') #Sample Movie reviews are stored in a separate file
review1 = review.read()
review.close()

#using naivebayseanalyzer method on the texts of the file
blob = TextBlob(review1,analyzer=NaiveBayesAnalyzer()) 

positive = blob.sentiment.p_pos #It analyzes total positive value from the review and stored it in a separate variable
negative = blob.sentiment.p_neg #It analyzes total negative value from the review and stored it in a separate variable

prating = round(positive*100) #converts float to integer value
nrating = round(negative*100)

if positive > 0.5:
    print("{}% Positive Reviews for the Movie".format(prating))
elif negative > 0.5:
     print("{}% Negative Reviews for the Movie".format(nrating))
else:
    print("Neutral Reviews")

from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy

def extract_features(words):
    return dict([(word, True) for word in words])


if __name__=='__main__':
    fileids_pos = movie_reviews.fileids('pos')
    fileids_neg = movie_reviews.fileids('neg')

    features_pos = [(extract_features(movie_reviews.words(
        fileids=[f])), 'Positive') for f in fileids_pos]
    features_neg = [(extract_features(movie_reviews.words(
        fileids=[f])), 'Negative') for f in fileids_neg]

threshold = 0.8
num_pos = int(threshold * len(features_pos))
num_neg = int(threshold * len(features_neg))

features_train = features_pos[:num_pos] + features_neg[:num_neg]
features_test = features_pos[num_pos:] + features_neg[num_neg:]

print('\nNumber of training datapoints:', len(features_train))
print('Number of test datapoints:', len(features_test))

classifier = NaiveBayesClassifier.train(features_train)
print('\nAccuracy of the classifier:', nltk_accuracy(classifier, features_test))

N = 15
print('\nTop ' + str(N) + ' most informative words:')
for i, item in enumerate(classifier.most_informative_features()):
    print(str(i+1) + '. ' + item[0])
    if i == N - 1:
        break

input_reviews = [
    "It achieves all of that without ever being trite, corny, or even unbelievable. See it with your family, your date, yourself, or whomever. It cannot disappoint you.",
    "I loved this film. I perfect balance of story, humour and sincerity along with excellent acting and a wonderful cast.",
    " It's a brilliant film that raises in the viewer's mind all sorts of important questions about life, love and loyalty. Do go and see it. 10/10. ",
    "About Time was one of the greatest movies I have ever seen. I was immediately captured, and the cast is so brilliant, I believed every single line. Thank you for this film, I am still under the influence of this movie. ",
    "Without doubt one of the worst films I have ever seen. Storyline - banal bordering on silly. Every character totally miscast. ",
    "Majority of the critics are fake here and thats the only reason for such a high rating for this dumb movie ! Don't watch ! Total waste ! Wish I could time travel and bring those valuable time back.",
    "What a waste of potential, what a waste. This movie is nothing more, just 2 hours of dull and boring cinema with almost no plot at all. The story is absolutely about nothing."
    ]

print("\nMovie review predictions:")
for review in input_reviews:
    print("\nReview:", review)

    probabilities = classifier.prob_classify(extract_features(review.split()))

    predicted_sentiment = probabilities.max()

    print("Predicted sentiment:", predicted_sentiment)
    print("Probability:", round(probabilities.prob(predicted_sentiment), 2))

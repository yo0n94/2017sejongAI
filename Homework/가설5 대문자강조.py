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
    "The Notebook is the best movie I have seen in a very long time! I love the story, the actors, the scenery...everything. I have NEVER cried when I watched a movie and this one made me cry like a baby in the theater. Which was very embarrassing if you ask me. But anyway, The Notebook is the most touching love story I have ever seen.",
    "The Notebook is the BEST movie I have seen in a very long time! I LOVE the story, the actors, the scenery...everything. I have never cried when I watched a movie and this one made me cry like a baby in the theater. Which was very embarrassing if you ask me. But anyway, The Notebook is the MOST TOUCHING LOVE STORY I have ever seen.",
    "The characters are dull! Noah is what? Manic-depressive? Manic in the first 5 minutes, and throughout the rest of the movie depressive. The music is simply unbearable! And sooooooo many other bugs... Damn I don't even know why I'm writing this. I feel like one of Jeffrey Dahmer's zombies. Even that should feel better than being this numb after watching this piece of... you know what.!!",
    "The characters are DULL! Noah is what? MANIC-DEPRESSIVE? Manic in the first 5 minutes, and throughout the rest of the movie depressive. The music is simply UNBEARABLE! And sooooo many other BUGS... Damn I don't even know why I'm writing this. I feel like one of Jeffrey Dahmer's zombies. Even that should feel better than being this numb after watching this piece of... you know what.!!",
    "Now here's the romance of the decade. Heart-warming doesn't even come close to describing 'If Only' It's a story about love in it's purest form. About realizing that any moment some one you care for can be taken away and you have the be certain you did everything to make your life meaningful with that some one. If you're looking for a movie that will make you smile, make you think, make you cry and leave you touched. If Only is the way to go.",
    "Now here's the ROMANCE of the decade. HEART-WARMING doesn't even come close to describing 'If Only' It's a story about LOVE in it's PUREST form. About realizing that any moment some one you care for can be taken away and you have the be certain you did everything to make your life meaningful with that some one. If you're looking for a movie that will make you SMILE, make you think, make you cry and leave you touched. If Only is the way to go."
    ]

print("\nMovie review predictions:")
for review in input_reviews:
    print("\nReview:", review)

    probabilities = classifier.prob_classify(extract_features(review.split()))

    predicted_sentiment = probabilities.max()

    print("Predicted sentiment:", predicted_sentiment)
    print("Probability:", round(probabilities.prob(predicted_sentiment), 2))

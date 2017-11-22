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
    "I loved that movie for all what was said before I do, but I see one additional plus: maybe the genius side of the writer and the Director: You can see the movie two ways: 1 - Like the probable intention of the author: a couple, on the breaking point, because he is too busy to love freely; an accident, she dies. He is drowning in his grief, and his conscience makes him re-live the story where he realizes his shortcomings, his losses, and punishing himself, he dies at the end. 2 - The movie start on what we can around the middle believe it's a dream (premonition?). When he wakes up, relieved, he understood the message of his dream 'love fully, for 5 minutes or 50 years, but fully'. He apply this lesson, 'as if it is his last day', touches the happiness of love, and, in a twist of the fate, dies in the accident he was dreaming, the night before that his love lost her life. No matter the way you watch this movie, it's a piece of Art; the makers are geniuses How about an award? would it not deserve one?",
    "I DO NOT WANT TO WRITE 10 LINES. I JUST want to tell u all who haven't seen it yet that its really PERFECT. Maybe my best movie ever. all rest lines from now on are just for get the minimum 10 lines. no actually need to read if you do not want. The passion. the love. the feelings this movie emit are all so ...HUGE. I feel so happy than even after 10 years of movies creation i found it. i had no idea this film even exist. i feel that for some maybe this movie will be even life changer. both actors were v good . all were marvelous. songs. landscapes. everything. masterpiece !! ending ? one of best ever seen. so simple but same time so great. take your wife / husband .. hug him/her and stay this way till the end of film. without kids, just u 2.",
    "This movie fails on every level. I can't recall ever seeing such trivial drivel pathetically attempting to masquerade as a meaningful story. The plot? There wasn't one. The characters? Stupid and shallow. Good points? That it finally ended. Why I watched it to the end? The hope that beats eternal. Don't waste your money, not even as a weekly video for two bucks. If it comes on free-to-air, bypass it. The last movie I recall that was as bad as this was Kramer versus Kramer. This was an attempt to take a teenybopper B grade comic-book love story and turn it into a meaningful movie. For whom? Pre-pubescent fairytalers probably, and I imagine it even failed for them.",
    "This is one of the very worst movies I have ever rented.... the acting was terrible, apart from the taxi driver played by Tom Williamson.. what was he doing in a movie as poor as this? Paul Nicholas (who looks a little like Jude Law, but in this case thats as far as it goes..) has the most terrible Northern English accent I have heard. I have not seen or heard of this actor before, but would not go out of my way to see him again, I could have played the part better and I am a five foot 2 female. Jennifer Love Hewitt was perfectly sickly, I am sure I have seen her do better than this. Apart from the awful acting, the storyline was just way too cheesy and it took forever to end, the twist at the end didn't work... it came an hour too late (real time...). ",

    "I loved that movie for all what was said before I do, but I see one additional plus: maybe the genius side of the writer and the Director. No matter the way you watch this movie, it's a piece of Art; the makers are geniuses How about an award? would it not deserve one?",
    "I JUST want to tell u all who haven't seen it yet that its really PERFECT. Maybe my best movie ever. The passion. the love. the feelings this movie emit are all so ...HUGE. I feel so happy than even after 10 years of movies creation.",
    "This movie fails on every level. I can't recall ever seeing such trivial drivel pathetically attempting to masquerade as a meaningful story. The plot? There wasn't one. The characters? Stupid and shallow.",
    "This is one of the very worst movies I have ever rented.... the acting was terrible. The most terrible Northern English accent I have heard. Apart from the awful acting, the storyline was just way too cheesy and it took forever to end."
    ]

print("\nMovie review predictions:")
for review in input_reviews:
    print("\nReview:", review)

    probabilities = classifier.prob_classify(extract_features(review.split()))

    predicted_sentiment = probabilities.max()

    print("Predicted sentiment:", predicted_sentiment)
    print("Probability:", round(probabilities.prob(predicted_sentiment), 2))

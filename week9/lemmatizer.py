from nltk.stem import WordNetLemmatizer

input_words = ['reading', 'calves', 'be', 'were', 'bought', 'longer','brushes', 'horse', 'memorize', 'possibly', 'unforgettable', 'hosts', 'kept', 'inconvenience', 'subsequently', 'vehicles',
'coding', 'impending']

lemmatizer = WordNetLemmatizer()

lemmatizer_names = ['NOUN LEMMATIZER', 'VERB LEMMATIZER']
formatted_text = '{:>24}' * (len(lemmatizer_names) + 1)
print('\n', formatted_text.format('INPUT WORD', *lemmatizer_names), '\n', '='*75)


for word in input_words:
    output = [word, lemmatizer.lemmatize(word, pos='n'),
        lemmatizer.lemmatize(word, pos='v')]
    print(formatted_text.format(*output))

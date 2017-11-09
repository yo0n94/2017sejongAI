from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer

input_words = ['reading', 'calves', 'be', 'were', 'bought', 'longer','brushes', 'horse', 'memorize', 'possibly', 'unforgettable', 'hosts', 'kept', 'inconvenience', 'subsequently', 'vehicles',
'coding', 'impending']


porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')


stemmer_names = ['PORTER', 'LANCASTER', 'SNOWBALL']
formatted_text = '{:>16}' * (len(stemmer_names)+1)
print('\n', formatted_text.format('INPUT WORD', *stemmer_names), '\n', '='*68)


for word in input_words:
    output=[word, porter.stem(word), lancaster.stem(word), snowball.stem(word)]
    print(formatted_text.format(*output))

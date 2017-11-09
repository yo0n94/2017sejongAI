from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer

input_text = "'We want a vibrant trade relationship with China, Trump said. 'We also want a fair and reciprocal one. Today, I discussed with President Xi the chronic imbalance in our relationship as it pertains to trade and the concrete steps."

print("\nSentence Tokenizer:")
print(sent_tokenize(input_text))


print("\nWord tokenizer : ")
print(word_tokenize(input_text))


print("\nWord Punct Tokenizer : ")
print(WordPunctTokenizer().tokenize(input_text))

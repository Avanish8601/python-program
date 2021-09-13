import nltk
from nltk.corpus import names
nltk.download('names')
nltk.download('stopwords')
print(names.words())
from nltk.corpus import stopwords
print(stopwords.words('english'))



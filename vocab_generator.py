import sys
import operator
import pandas as pd
from collections import Counter
train_file = sys.argv[1]
eval_file = sys.argv[2]
out_dir = sys.argv[3]
train_data = pd.read_csv(train_file,delimiter='\t',header=None)
train_data.columns = ['title', 'title_pos', 'title_ner', 'article', 'article_pos', 'article_ner']
#valid_data = pd.read_csv(eval_file,delimiter='\t',header=None)
#valid_data.columns = ['title', 'title_pos', 'title_ner', 'article', 'article_pos', 'article_ner']
#all_text = list(train_data['title'].values)+list(train_data['article'].values)+list(valid_data['title'].values) + list(valid_data['article'].values)

all_text = list(train_data['title'].values)+list(train_data['article'].values)
vocab = Counter()
for text in all_text:
    vocab.update(text.lower().strip().split())

vocab = sorted(vocab.items(), key=operator.itemgetter(1),reverse=True)
fw = open('{}/vocab'.format(out_dir), 'w')
for (key,value) in vocab:
    fw.write('{} {}\n'.format(key,value))
fw.close()

###### POS vocab
#all_text = list(train_data['title_pos'].values)+list(train_data['article_pos'].values)+list(valid_data['title_pos'].values) + list(valid_data['article_pos'].values)
all_text = list(train_data['title_pos'].values)+list(train_data['article_pos'].values)
vocab = Counter()
for text in all_text:
    vocab.update(text.lower().strip().split())

vocab = sorted(vocab.items(), key=operator.itemgetter(1),reverse=True)
fw = open('{}/pos'.format(out_dir), 'w')
for (key,value) in vocab:
    fw.write('{} {}\n'.format(key,value))
fw.close()

###### NER vocab
#all_text = list(train_data['title_ner'].values)+list(train_data['article_ner'].values)+list(valid_data['title_ner'].values) + list(valid_data['article_ner'].values)
all_text = list(train_data['title_ner'].values)+list(train_data['article_ner'].values)
vocab = Counter()
for text in all_text:
    vocab.update(text.lower().strip().split())

vocab = sorted(vocab.items(), key=operator.itemgetter(1),reverse=True)
fw = open('{}/ner'.format(out_dir), 'w')
for (key,value) in vocab:
    fw.write('{} {}\n'.format(key,value))
fw.close()
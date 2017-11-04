import sys
import operator
import pandas as pd
from collections import Counter

def run(train_file, eval_file, out_dir):
	train_data = pd.read_csv(train_file,delimiter='\t',header=None)
	train_data.columns = ['article', 'article_pos', 'article_ner', 'title', 'title_pos', 'title_ner']
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

def run2(train_file, eval_file, out_dir):
	text = []
	pos = []
	ner = []
	f = open(train_file)
	for line in f:
		(article, article_pos, article_ner, abstract, abstract_pos, abstract_ner) = line.strip().split('\t')
		text.append(abstract)
		text.append(article)
		pos.append(article_pos)
		pos.append(abstract_pos)
		ner.append(article_ner)
		ner.append(abstract_ner)
	f.close()
	print('done reading the data...')
	print('writing to vocab files')
	vocab = Counter()
	for t in text:
	    vocab.update(t.lower().strip().split())
	vocab = sorted(vocab.items(), key=operator.itemgetter(1),reverse=True)
	fw = open('{}/vocab'.format(out_dir), 'w')
	for (key,value) in vocab:
	    fw.write('{} {}\n'.format(key,value))
	fw.close()

	###### POS vocab
	vocab = Counter()
	for t in pos:
	    vocab.update(t.lower().strip().split())
	vocab = sorted(vocab.items(), key=operator.itemgetter(1),reverse=True)
	fw = open('{}/pos'.format(out_dir), 'w')
	for (key,value) in vocab:
	    fw.write('{} {}\n'.format(key,value))
	fw.close()

	###### NER vocab
	vocab = Counter()
	for t in ner:
	    vocab.update(t.lower().strip().split())
	vocab = sorted(vocab.items(), key=operator.itemgetter(1),reverse=True)
	fw = open('{}/ner'.format(out_dir), 'w')
	for (key,value) in vocab:
	    fw.write('{} {}\n'.format(key,value))
	fw.close()

train_file = sys.argv[1]
eval_file = sys.argv[2]
out_dir = sys.argv[3]

run2(train_file, eval_file, out_dir)
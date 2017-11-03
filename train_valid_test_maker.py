import sys, os
from glob import glob
from random import shuffle
import numpy as np

def maker(indir, filelist, fw):
    data = []
    for fl in filelist:
        fal = open('{}/article_spacy_line/{}'.format(indir,fl))
        lines = []
        for line in fal:
            line = ' '.join(line.strip().split(' ')[0:-1])
            line = '<s> {} </s>'.format(line)
            lines.append(line)
        fal = '<d> {} </d>'.format(' '.join(lines))

        fap = open('{}/article_spacy_pos/{}'.format(indir,fl))
        lines = []
        for line in fap:
            line = ' '.join(line.strip().split(' ')[0:-1])
            line = '<s> {} </s>'.format(line)
            lines.append(line)
        fap = '<d> {} </d>'.format(' '.join(lines))

        fan = open('{}/article_spacy_ner/{}'.format(indir,fl))
        lines = []
        for line in fan:
            line = ' '.join(line.strip().split(' ')[0:-1])
            line = '<s> {} </s>'.format(line)
            lines.append(line)
        fan = '<d> {} </d>'.format(' '.join(lines))

        ftl = open('{}/title_spacy_line/{}'.format(indir,fl))
        lines = []
        for line in ftl:
            line = ' '.join(line.strip().split(' ')[0:-1])
            line = '<s> {} </s>'.format(line)
            lines.append(line)
        ftl = '<d> {} </d>'.format(' '.join(lines))

        ftp = open('{}/title_spacy_pos/{}'.format(indir,fl))
        lines = []
        for line in ftp:
            line = ' '.join(line.strip().split(' ')[0:-1])
            line = '<s> {} </s>'.format(line)
            lines.append(line)
        ftp = '<d> {} </d>'.format(' '.join(lines))

        ftn = open('{}/title_spacy_ner/{}'.format(indir,fl))
        lines = []
        for line in ftn:
            line = ' '.join(line.strip().split(' ')[0:-1])
            line = '<s> {} </s>'.format(line)
            lines.append(line)
        ftn = '<d> {} </d>'.format(' '.join(lines))

        fw.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(fal, fap, fan, ftl, ftp, ftn))

def run(indir, outdir, train_split):
    filelist = glob('{}/article_spacy_line/*'.format(indir))
    print('loaded {} files...'.format(len(filelist)))
    shuffle(filelist)
    trainlist = [k.split('/')[-1] for k in filelist[0:int(np.round(train_split*len(filelist)))]]
    testlist = [k.split('/')[-1] for k in filelist[int(np.round(train_split*len(filelist))):]]
    print("len train: {}\tlen test: {}".format(len(trainlist),len(testlist)))

    fw = open('{}/train.txt'.format(outdir),'w')
    maker(indir, trainlist, fw)
    fw.close()
    
    fw = open('{}/test.txt'.format(outdir),'w')
    maker(indir, testlist, fw)
    fw.close()

#indir = sys.argv[1]
#outdir = sys.argv[2]
#train_split = float(sys.argv[3])
run(indir, outdir, train_split)

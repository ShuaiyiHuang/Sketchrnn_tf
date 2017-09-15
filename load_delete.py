import numpy as np
from magenta.models.sketch_rnn.sketch_rnn_train import *
from magenta.models.sketch_rnn.model import *
from magenta.models.sketch_rnn.utils import *
from magenta.models.sketch_rnn.rnn import *

droot= '/home/hsy/work/hsy/repertory/data/sketch-rnn-datasets/'
dataset_name='cat/cat.npz'
dataset_name_full='cat/cat.full.npz'
dataset_name_owl='owl/owl.npz'
dataset_name_owl_full='owl/owl.full.npz'
dataset_name_merge='merge/cat_elephant_owl_pig.npz'

# cat_notfull=np.load(data_dir+dataset_name)
# cat_full=np.load(data_dir+dataset_name_full)
# owl_notfull=np.load(data_dir+dataset_name_owl)
# owl_full=np.load(data_dir+dataset_name_owl_full)
merge=np.load(droot + dataset_name_merge)

# cat_train_full=cat_full['train']
# cat_train_notfull=cat_notfull['train']
# owl_train_notfull=owl_notfull['train']
#
# print type(cat_train_notfull[0])
# print len(cat_notfull['train']),type(cat_train_notfull),cat_train_notfull.shape
# print len(cat_full['train']),type(cat_train_full)
# print len(owl_notfull['train']),type(owl_train_notfull),owl_train_notfull.shape
# print len(owl_full['train'])

# model_params = sketch_rnn_model.get_default_hparams()
# [train_set, valid_set, test_set, hps_model, eval_hps_model, sample_hps_model] = load_dataset(data_dir+dataset_name_full, model_params)


# max_nutfull=utils.get_max_len(cat_train_notfull)
# max_full=utils.get_max_len(cat_full['test'])
# max_owl_notfull=utils.get_max_len(owl_notfull['train'])
# max_owl_full=utils.get_max_len(owl_full['train'])
#
# print max_full,max_nutfull,max_owl_notfull,max_owl_full
#
# print utils.get_max_len(owl_full['train']),utils.get_max_len(owl_full['test']),utils.get_max_len(owl_full['valid'])
# print utils.get_max_len(owl_notfull['train']),utils.get_max_len(owl_notfull['test']),utils.get_max_len(owl_notfull['valid'])
print utils.get_max_len(merge['train']),utils.get_max_len(merge['test']),utils.get_max_len(merge['valid'])

# dataset_concate=np.concatenate([cat_train_notfull,owl_train_notfull],1)
# dataset_concat_1=[]
# dataset_concat_2=[]
# for item in zip(cat_train_notfull,owl_train_notfull):
#     print item[0].shape,item[1].shape
#     concat=np.concatenate([item[0],item[1]],0)
#     if concat.shape[0]>300:
#         dataset_concat_1.append(concat)
#     else:
#         dataset_concat_2.append(concat)
# print len(dataset_concat_1),len(dataset_concat_2)
#
# dataset_concat1=np.array(dataset_concat_1)
# dataset_concat2=np.array(dataset_concat_2)
# print 'concat:',utils.get_max_len(dataset_concat1),utils.get_max_len(dataset_concat2)

count=0
for item in merge['train']:
    if len(item)>=300:
       count+=1
print 'train count>=300',count

count=0
for item in merge['valid']:
    if len(item)>=300:
       count+=1
print 'valid count>=300',count

count=0
for item in merge['test']:
    if len(item)>300:
       count+=1
print 'test count>=300',count

def count(dataset):
    count = 0
    for item in dataset['train']:
        if len(item) > 300:
            count += 1
    print 'train count>300', count

    count = 0
    for item in dataset['valid']:
        if len(item) > 300:
            count += 1
    print 'valid count>300', count

    count = 0
    for item in dataset['test']:
        if len(item) > 300:
            count += 1
    print 'test count>300', count

def preprocess(dataset,limit,droot,targetname):
    train_list=[]
    for item in dataset['train']:
        print type(item)
        if len(item)>limit:
            train_list.append(item)
    valid_list=[]
    for item in dataset['valid']:
        if len(item)>limit:
            valid_list.append(item)
    test_list=[]
    for item in dataset['test']:
        if len(item)>limit:
            test_list.append(item)
    train=np.array(train_list)
    valid=np.array(valid_list)
    test=np.array(test_list)
    print('processed length for train:{},valid:{},test:{}'.format(len(train),len(valid),len(test)))
    np.savez_compressed(os.path.join(droot,targetname),train=train,valid=valid,test=test)

preprocess(merge,300,droot,'merge/cat_elephant_owl_pig_processed.npz')
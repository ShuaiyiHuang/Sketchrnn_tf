import os
import numpy as np
namelist=[]
import logging

logFormat = logging.Formatter("%(asctime)s %(message)s")
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.INFO)


def merge(dataset1,dataset2,droot,name):
    train1,train2= (item['train'] for item in (dataset1,dataset2))
    valid1,valid2=(item['valid'] for item in (dataset1,dataset2))
    test1,test2=(item['test'] for item in (dataset1,dataset2))
    def concate_numpyarray(array1,array2):
        concat_list=[]
        assert (array1.shape==array2.shape)
        for data in zip(array1,array2):
            concat_data=np.concatenate((data[0],data[1]),0)
            concat_list.append(concat_data)
        return np.array(concat_list)

    concat_train=concate_numpyarray(train1,train2)
    concat_valid=concate_numpyarray(valid1,valid2)
    concat_test=concate_numpyarray(test1,test2)
    logging.info('shape:{}{}{}'.format(concat_train.shape,concat_valid.shape,concat_test.shape))
    np.savez_compressed(os.path.join(droot,name),train=concat_train,valid=concat_valid,test=concat_test)
    logging.info('merging finished')
    merged_dataset=np.load(os.path.join(droot,name)+'.npz')
    return merged_dataset

def merge_main(droot,namelist,targetname):
    #for 3 datasetname
    dataset_list=[]
    for name in namelist:
        datasetpath=droot+name
        dataset=np.load(datasetpath)
        dataset_list.append(dataset)
        logging.info('type:{}'.format(type(dataset)))
    for item in dataset_list[0]:
        print item
        print type(item)
        print type(dataset_list[0][item])
    logging.info('Loading {} dataset done'.format(len(dataset_list)))

    if len(dataset_list)==1:
        logging.info('no more dataset needs merging')
    elif len(dataset_list)==2:
        merge(dataset_list[0], dataset_list[1], droot, targetname)
    else:
        temp_merge=merge(dataset_list[0],dataset_list[1],droot,'temp_merge')
        count=1
        for item in dataset_list[2:]:
            count+=1
            if count==len(dataset_list):
                temp_merge=merge(temp_merge,item,droot,targetname)
            else:
                temp_merge = merge(temp_merge, item, droot, targetname)
    return 0

if __name__ == '__main__':
    droot='/home/hsy/work/hsy/repertory/data/sketch-rnn-datasets/'
    namelist=('cat/cat.npz','elephant/elephant.npz','owl/owl.npz','pig/pig.npz')
    targetname='./merge/cat_elephant_owl_pig'
    merge_main(droot=droot,namelist=namelist,targetname=targetname)


    # consoleHandler=logging.StreamHandler()
    # consoleHandler.setFormatter(logFormat)
    # rootLogger.addHandler(consoleHandler)
    logging.info('test')
    logging.info('d')

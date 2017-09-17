from sketch_rnn_train import *
from model import *
from utils import *
from rnn import *

data_dir='/home/hsy/work/hsy/repertory/data/sketch-rnn-datasets'
models_root_dir = '/home/hsy/work/hsy/repertory//tmp/sketch_rnn/models'
model_dir = '/home/hsy/work/hsy/repertory//tmp/sketch_rnn/models/resume'



[train_set, valid_set, test_set, hps_model, eval_hps_model, sample_hps_model] = load_env(data_dir, model_dir)

# construct the sketch-rnn model here:
reset_graph()
model = Model(hps_model)
eval_model = Model(eval_hps_model, reuse=True)
sample_model = Model(sample_hps_model, reuse=True)

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

# loads the weights from checkpoint into our model
load_checkpoint(sess, model_dir)
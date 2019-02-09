
import os
import commands

# Some file names
# name of the file which stores all experience
exp_file_path = "data/features.csv"
exp_target_file_path = "data/features_all.csv"
exp_log_data_file = os.path.abspath(exp_target_file_path)
exp_log_data_file_without_header = '{}.withoutheader'.format(exp_file_path)
exp_log_data_file_shuf = '{}.shuf'.format(exp_file_path)
exp_log_data_file_train = '{}.train'.format(exp_file_path)
exp_log_data_file_eval = '{}.eval'.format(exp_file_path)
exp_log_data_file_train_shard = '{}.shard'.format(exp_log_data_file_train)
exp_log_data_file_eval_shard = '{}.shard'.format(exp_log_data_file_eval)
# shards and tfrecords
train_tfrecord_fname_out = '{}.train.tfrecord'.format(exp_file_path)
eval_tfrecord_fname_out = '{}.eval.tfrecord'.format(exp_file_path)


# Config for preprocessing
SHUF_MEM = 1  # the shuf command memory usage Gi

TRAIN_SPLIT_RATIO = 0.8 # the ratio for split train and eval data set

# Split the train and eval sets into `DATASET_NUM_SHARDS` shards. Allows for parallel
# preprocessing and is used for shuffling the dataset.
DATASET_NUM_SHARDS = 2

# the dir stores the files,models generated by engine
TARGET_DIR = "gen"
SERVING_DIR = "gen/serving_model"
ANALYSIS_DIR = "gen/analysis_model"

# Config for training
# when testing, I use a small value
TRAIN_BATCH_SIZE = 16
EVAL_BATCH_SIZE = 16

# Eval train subsampling factor
EVAL_TRAIN_SUBSAMPLE_FACTOR = 1

# Train for `TRAIN_INC_STEPS` steps before evaluating the model.
TRAIN_INC_STEPS = 1 * 1000 * 1000
# Train for `TRAIN_MAX_STEPS` steps max, then stop.
TRAIN_MAX_STEPS = 1 * 1000 * 1000
# Early stopping criterium, even if `TRAIN_MAX_STEPS` is not reached.
STOP_AFTER_WORSE_EVALS_NUM = 5

# Shuffle uses a running buffer of `shuffle_buffer_size`, so only items within each buffer
# of `shuffle_buffer_size` are shuffled. Best to make sure the dataset is shuffled beforehand.
SHUFFLE_BUFFER_SIZE = 100

# Scaling param for number of model units.
MODEL_NUM_UNIT_SCALE = 32
# Dropout probability
DROPOUT_PROB = 0.5

FIX_LEARNING_RATE = 0.001

LOG_FREQ_STEP = 100

# Select top `TOP_SEEDS_K` seeds and randomize
TOP_SEEDS_K = 20
# Recommend top `TOP_SEEDS_K` seeds.
SEEDS_K_FINAL = 5

## Variable
if os.path.isfile(exp_log_data_file_train):
    num_train_samples = int(commands.getoutput("wc -l < {}".format(exp_log_data_file_train)).strip())
if os.path.isfile(exp_log_data_file_eval):
    num_eval_samples = int(commands.getoutput("wc -l < {}".format(exp_log_data_file_eval)).strip())

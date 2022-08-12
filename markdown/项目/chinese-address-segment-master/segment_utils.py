import os
import pickle
import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
from gevent import monkey
monkey.patch_all()

from model import Model
from utils import get_logger,load_config,create_model
from data_utils import load_word2vec, input_from_line

def get_model():
    '''获取地址分词模型'''

    '''模型参数'''
    flags = tf.app.flags
    # configurations for training
    flags.DEFINE_string("ckpt_path", "ckpt", "Path to save model")
    flags.DEFINE_string("log_file", "train.log", "File for log")
    flags.DEFINE_string("map_file", "maps.pkl", "file for maps")  # （词与词频，标签与整数）文件
    flags.DEFINE_string("config_file", "config_file", "File for config")
    FLAGS = tf.app.flags.FLAGS

    '''加载配置文件与日志文件'''
    with open(FLAGS.map_file, "rb") as f:
        char_to_id, id_to_char, tag_to_id, id_to_tag = pickle.load(f)
    if os.path.isfile(FLAGS.config_file):
        config = load_config(FLAGS.config_file)
    log_path = os.path.join("log", FLAGS.log_file)
    if not os.path.isdir("log"):
        os.makedirs("log")
    if not os.path.isdir(log_path):
        os.makedirs(log_path)
    logger = get_logger(log_path)

    '''加载模型'''
    tf_config = tf.ConfigProto()
    sess = tf.Session(config=tf_config)
    sess.run(tf.global_variables_initializer())
    model = create_model(sess, Model, FLAGS.ckpt_path, load_word2vec, config, id_to_char, logger)

    return model, sess, char_to_id, id_to_tag


def address_segment(self, address):
    # print(address, type(address))  # <class 'str'>
    model, sess, char_to_id, id_to_tag = get_model()
    address_segment_result = model.evaluate_line(sess, input_from_line(address,char_to_id), id_to_tag)
    # print(address_segment_result, type(address_segment_result))  # <class 'dict'>
    return address_segment_result
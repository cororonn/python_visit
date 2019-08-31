import numpy as np
import tensorflow as tf
import sys


def read_csv(csvfile):
    cat_queue = tf.train.string_input_producer([csvfile])
    reader = tf.TextLineReader()
    key, val = reader.read(cat_queue)
    cat, label = tf.decode_csv(val, [["aa"], [1]])
    return read_img(cat)

def read_img(fname):
    img_r = tf.read_file(cat)
    return tf.image.decode_image(img_r, channels=3)

def main():
    argv = sys.argv
    argc = len(argv)
    if (argc < 2):
        print('Usage: python %s csvfile' %argv[0])
        quit()

    image = read_csv(argv[1])

    sess = tf.Session()
    init = tf.initialize_all_variables()
    sess.run(init)
    tf.train.start_queue_runners(sess)
    x = sess.run(image)

    print(x)

if __name__ == '__main__':
    main()


x = tf.placeholder(tf.float32,[None,input_size],name="input_data")
 
#画像読込
jpg = tf.read_file("cat/100. milesf3john-1200x1095.jpg")
image = tf.image.decode_jpeg(jpg, channels=1)
 
with tf.Session() as sess:
 
  input_image = sess.run(image)
  sess.run(train_grad, feed_dict={x:input_image})

"""


NUM_CLASSES = 2
IMAGE_SIZE = 28
TRAIN_SECTION = 2


flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('cat', 'python_visit\air.csv', 'File name of train data')

if __name__ == '__main__':
    test = np.loadtxt('python_visit\air.csv', delimiter=",", dtype=str)
    raw_input = np.loadtxt(open(FLAGS.train), delimiter=",", dtype=str)
    [trains, tests] = np.vsplit(raw_input, [TRAIN_SECTION])

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        train_image, train_label = get_image_and_label(sess, trains)
        test_image, test_label = get_image_and_label(sess, tests)

def get_image_and_label(sess, csv_lines):
    images = []
    labels = []
    for train in csv_lines:
        val = tf.cast(train[0], dtype=tf.string)
        jpeg_r = tf.read_file(val)
        image = tf.image.decode_jpeg(jpeg_r, channels=3)
        image = tf.image.resize_images(image, IMAGE_SIZE, IMAGE_SIZE)
        image = tf.reshape(image, [-1])
        image_val = sess.run(image).astype(np.float32) / 255.0
        images.append(image_val)
        tmp = np.zeros(NUM_CLASSES)
        tmp[int(train[1])] = 1
        labels.append(tmp)

    return np.asarray(images, dtype=np.float32), np.asarray(labels, dtype=np.float32)
"""
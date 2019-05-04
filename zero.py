import sys
import tensorflow as tf

def read_csv(csvfile):
    fname_queue = tf.train.string_input_producer([csvfile])
    reader = tf.TextLineReader()
    key, val = reader.read(fname_queue)
    fname, label = tf.decode_csv(val, [["aa"], [1]])
    return read_img(fname)

def read_img(fname):
    img_r = tf.read_file(fname)
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
"""
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


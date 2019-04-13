NUM_TRAIN =  2_000
# 学習中の出力頻度
OUTPUT_BY = 2

# 標準化
train_mean = train_dataset.mean()
train_std = train_dataset.std()
standardized_train_dataset = train_dataset.standardize()

# 損失関数の出力をトレース対象とする
loss_summary = tf.summary.scalar('MAE', loss)

# 損失関数の出力をトレース対象とする
tf.summary.scalar('MAE', loss)
# ……中略（他にもたくさんのログを対象とする）……
# ログ対象をまとめる
merged = tf.summary.merge_all()

# logsディレクトリに出力するライターを作成して利用
with tf.summary.FileWriter('logs',sess.graph) as writer:
  # 学習の実行
  sess.run(tf.global_variables_initializer())
  for i in range(NUM_TRAIN):
    batch = standardized_train_dataset.next_batch(SERIES_LENGTH, BATCH_SIZE)
    summary, mae, _ = sess.run([loss_summary, loss, optimizer], feed_dict={ x: batch[0], y: batch[1]})
    if i % OUTPUT_BY == 0:
      print('step {:d}, error {:.2f}'.format(i, mae))
      # ログの出力
      writer.add_summary(summary, global_step=i)
  # ログの出力
  writer.add_summary(summary, global_step=NUM_TRAIN)

  with tf.name_scope('prediction'):
  # 重み
    w = tf.Variable(tf.zeros([20, FEATURE_COUNT]))
  # バイアス
    b = tf.Variable([0.1] * FEATURE_COUNT)
  # 最終出力（予測）
  prediction = tf.matmul(last_state, w) + b
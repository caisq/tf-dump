"""
A little fun project that demonstrates how to use tfdbg and TensorBoard Debugger
Plugin with autograph.

For more about autograph, see:
  https://medium.com/tensorflow/autograph-converts-python-into-tensorflow-graphs-b2a871f87ec7

For more about TensorBoard Debugger Plugin, see:
  https://github.com/tensorflow/tensorboard/tree/master/tensorboard/plugins/debugger/README.md

Requires: TensorFlow 1.9.0+

To use the TensorBoard Debugger Plugin:

1. # First start the TensorBoard binary with the --debugger_port flag, e.g.,

  ```sh
  tensorboard --logdir /tmp/logdir --debugger_port 6064
  ```

2. Then run this script:

  ```sh
  python run_autograph.py
  ```

"""

import tensorflow as tf
from tensorflow.contrib import autograph
from tensorflow.python import debug as tf_debug


@autograph.convert()
def collatz(a):
  counter = 0
  while a != 1:
    if a % 2 == 0:
      a = a // 2
    else:
      a = 3 * a + 1
    counter += 1
  return counter


with tf.Graph().as_default():
  a_tensor = tf.constant(1337)
  counter_tensor = collatz(a_tensor)

  sess = tf.Session()

  # Modify me for different debugging modes: 'tensorboard' | 'cli'
  debugging_mode = 'tensorboard'

  if debugging_mode == 'tensorboard':
    sess = tf_debug.TensorBoardDebugWrapperSession(sess, 'localhost:6064')
  elif debugging_mode == 'cli':
    sess = tf_debug.LocalCLIDebugWrapperSession(sess)

  print(sess.run(counter_tensor))

import numpy as np


def calculate(lst):
  lst = np.array(lst)
  if np.shape(lst) != (9, ):
    raise ValueError('List must contain nine numbers.')
  input = np.reshape(lst, (3, 3))
  calculations = {}
  mean_ax1 = np.mean(input, axis=0)
  mean_ax2 = np.mean(input, axis=1)
  mean_all = np.mean(input)

  calculations['mean'] = [
    mean_ax1.tolist(), mean_ax2.tolist(),
    mean_all.tolist()
  ]

  var_ax1 = np.var(input, axis=0)
  var_ax2 = np.var(input, axis=1)
  var_all = np.var(input)

  calculations['variance'] = [
    var_ax1.tolist(), var_ax2.tolist(),
    var_all.tolist()
  ]

  std_ax1 = np.std(input, axis=0)
  std_ax2 = np.std(input, axis=1)
  std_all = np.std(input)

  calculations['standard deviation'] = [
    std_ax1.tolist(), std_ax2.tolist(),
    std_all.tolist()
  ]

  max_ax1 = np.max(input, axis=0)
  max_ax2 = np.max(input, axis=1)
  max_all = np.max(input)

  calculations['max'] = [max_ax1.tolist(), max_ax2.tolist(), max_all.tolist()]

  min_ax1 = np.min(input, axis=0)
  min_ax2 = np.min(input, axis=1)
  min_all = np.min(input)

  calculations['min'] = [min_ax1.tolist(), min_ax2.tolist(), min_all.tolist()]

  sum_ax1 = np.sum(input, axis=0)
  sum_ax2 = np.sum(input, axis=1)
  sum_all = np.sum(input)

  calculations['sum'] = [sum_ax1.tolist(), sum_ax2.tolist(), sum_all.tolist()]

  return calculations

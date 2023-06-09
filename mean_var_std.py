import numpy as np


def generate_mean(arr):
    return [list(arr.mean(0)), [float(i) for i in arr.mean(1)], np.mean(arr.flatten())]


def generate_variance(arr):
    return [list(arr.var(0)), [float(i) for i in arr.var(1)], np.var(arr.flatten())]


def generate_std(arr):
    return [list(arr.std(0)), [float(i) for i in arr.std(1)], np.std(arr.flatten())]


def generate_min(arr):
    return [list(arr.min(0)), [int(i) for i in arr.min(1)], np.min(arr.flatten())]


def generate_max(arr):
    return [list(arr.max(0)), [int(i) for i in arr.max(1)], np.max(arr.flatten())]


def generate_sum(arr):
    return [list(arr.sum(0)), [int(i) for i in arr.sum(1)], np.sum(arr.flatten())]


def calculate(list):
    try:
        arr = np.array(list)
        arr_3d = arr.reshape(3, 3)
        calculations = {}
        calculations['mean'] = generate_mean(arr_3d)
        calculations['variance'] = generate_variance(arr_3d)
        calculations['standard deviation'] = generate_std(arr_3d)
        calculations['max'] = generate_max(arr_3d)
        calculations['min'] = generate_min(arr_3d)
        calculations['sum'] = generate_sum(arr_3d)
        return calculations

    except ValueError:
        raise ValueError("List must contain nine numbers.")

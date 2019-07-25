import time
from pathlib import Path


def get_path_obj(path):
    if not isinstance(path, Path):
        path = Path(path)
    return path


def timeit(func):

    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print('{}: {:.4f} sec'.format(func.__name__, end-start))
        return ret

    return inner

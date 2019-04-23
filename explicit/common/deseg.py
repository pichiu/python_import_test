from .. import utils
from ..config import config

def foo():
    print('foo in common')

def main():
    utils.message('common - deseg')
    config.read_config()

if __name__ == '__main__':
    main()
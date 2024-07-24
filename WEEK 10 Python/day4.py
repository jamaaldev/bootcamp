import logging

logging.basicConfig(level= logging.DEBUG,
filename = 'erros.log',
format= '%(levelname)s : %(asctime)s - %(message)s')

logging.critical('this is the critical')
logging.error('this is the error')
logging.warning('this is the warning')
logging.info('this is the info')
logging.debug('this is the debug')

try:
    x = 10
    y = "20"
    print(x + y)
except Exception as error:
    print('there is a error',error)

print('here we go again')
# Abstração

from pathlib import Path

LOG_FILE = Path(__file__) .parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o metodo log')
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_fomatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando...')
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_fomatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg)


if __name__== '__main__':
    lp = LogPrintMixin()
    lp._log('Teste')
    lp.log_error('qualquer coisa')

    lf = LogFileMixin() 
    lf.log_error('qualquer coisa')  


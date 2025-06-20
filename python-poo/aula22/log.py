# Abstração
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o metodo log')
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg)


if __name__== '__main__':
    l = LogPrintMixin()
    l.log_error('qualquer coisa')

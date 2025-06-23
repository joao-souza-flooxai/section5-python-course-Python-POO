#Execeptions costumizadas

class MeuError(Exception) : ...


class OutroErro(Exception) : ...

def levantar():
    exeception_ = MeuError('a','b','c')
    exeception_.add_note('Isso é uma nota para ajudar no debug se essa exeception ocorrer.')
    raise MeuError('A mensagem do meu erro' )


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    raise OutroErro('Esse é outro erro relançado.')
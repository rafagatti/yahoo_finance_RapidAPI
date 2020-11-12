

def gerador_try_except(function):
    '''
    Um decorador em python, com o intuito de capturar e printar possíveis exceções
    '''
    
    def inner(*args, **kwargs):
        
        try:
            res = function(*args, **kwargs)
            print('A função {} foi executada com sucesso'.format(function.__name__))
            return res
        
        except Exception as e:
            print('Ocorreu um erro do tipo {} na execução da função {}. O erro foi: {}'.format(type(e),function.__name__, e))
    
    return inner
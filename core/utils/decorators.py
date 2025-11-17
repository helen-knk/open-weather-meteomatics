from functools import wraps
from django.db import transaction

def transaction_atomic(func):
    """
    Decorator para executar qualquer função dentro de uma transação atômica do Django.
    Se houver exceção, tudo é revertido.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        with transaction.atomic():
            return func(*args, **kwargs)
    return wrapper

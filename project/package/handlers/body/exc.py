import builtins

class Exception(builtins.Exception): pass
class InvalidOpenException(Exception): pass
class StopException       (Exception): pass
class EOFException        (Exception): pass
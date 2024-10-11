import re
import typing

from .            import exc, state
from ...          import handlers, parsers, model, util, words
from ...batteries import *

_WORD_PATTERN                = re.compile('^\\w+$')

class Parser(parsers.entity.StackingSemiParser):

    def __init__(self, after   :typing.Callable[[model.Package, model.PackageNonSource],None]):

        super().__init__()
        self._after               = after
        self._state               = state.States.BEGIN
        self._name      :str|None = None
        self._non_source          = model.PackageNonSource()
        self._non_source_router   = {state.States.BEGIN        : self._non_source.pos1,
                                     state.States.AFTER_PACKAGE: self._non_source.pos2,
                                     state.States.AFTER_NAME   : self._non_source.pos3}

    @typing.override
    def _default_handle_line     (self, line: str): pass

    @typing.override
    def _default_handle_part     (self, part:str): 
        
        line = self._line
        if   self._state is state.States.END: raise exc.StopException()

        elif self._state is state.States.BEGIN:

            if part != words.PACKAGE: raise exc.Exception(line)
            self._state = state.States.AFTER_PACKAGE

        elif self._state is state.States.AFTER_PACKAGE:

            self._name = part
            self._state = state.States.AFTER_NAME

        elif self._state is state.States.AFTER_NAME:

            if part == words.SEMICOLON:

                self._stop()

            elif part == words.DOT          or \
                 part == words.ASTERISK     or \
                 not words.is_reserved(part):

                self._name += part

            else: raise exc.Exception(line)

        else: raise AssertionError(f'{self._state=}')

    @typing.override
    def _default_handle_comment  (self, text:str): 

        self._non_source_router[self._state].append(model.Comment(text))

    @typing.override
    def _default_handle_spacing  (self, spacing:str): 

        self._non_source_router[self._state].append(spacing)

    @typing.override
    def _default_handle_newline  (self): self._default_handle_spacing('\n')

    @typing.override
    def _default_handle_eof      (self): raise exc.EOFException(self._line) # there should not be a EOF at all, before semi-colon

    def _stop(self): 
        
        self._state = state.States.END
        self._after(model.Package(name=self._name), self._non_source)

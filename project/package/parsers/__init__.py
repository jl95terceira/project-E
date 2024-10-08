import typing

from .   import body, callargs, generics, signature, type, annotation, part, entity
from ..  import model, handlers

class StreamPrinter(handlers.entity.EntityHandler):

    @typing.override
    def handle_package           (self, package:model.Package):

        print(f'Handling package:               {package}')

    @typing.override
    def handle_import            (self, import_:model.Import):

        print(f'Handling import:                {import_}')

    @typing.override
    def handle_annotation        (self, annot:model.Annotation):

        print(f'Handling annotation:            {annot}')

    @typing.override
    def handle_class             (self, class_:model.Class):

        print(f'Handling class:                 {class_}')

    @typing.override
    def handle_class_end         (self, class_end:model.ClassEnd=model.ClassEnd()):

        print(f'Handling end of class')

    @typing.override
    def handle_static_constructor(self, sconstr:model.StaticConstructor):

        print(F'Handling static constructor:    {sconstr}')

    @typing.override
    def handle_constructor       (self, constr:model.Constructor):

        print(f'Handling constructor:           {constr}')

    @typing.override
    def handle_attr              (self, attr:model.Attribute):

        print(f'Handling attribute:             {attr}')

    @typing.override
    def handle_method            (self, method:model.Method):

        print(f'Handling method:                {method}')

    @typing.override
    def handle_enum_value        (self, enum:model.EnumValue):

        print(f'Handling enum value:            {enum}')

    @typing.override
    def handle_comment           (self, comment:model.Comment):

        print(f'Handling comment:               {comment}')

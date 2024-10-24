from ... import model

import abc

class Handler(abc.ABC):

    @abc.abstractmethod
    def handle_package      (self, package:model.Package):  ...
    @abc.abstractmethod
    def handle_import       (self, import_:model.Import):  ...
    @abc.abstractmethod
    def handle_class        (self, class_:model.ClassHeader):  ...
    @abc.abstractmethod
    def handle_class_end    (self):  ...
    @abc.abstractmethod
    def handle_initializer  (self, initializer:model.Initializer):  ...
    @abc.abstractmethod
    def handle_constructor  (self, constr:model.Constructor):  ...
    @abc.abstractmethod
    def handle_attr         (self, attr:model.Attribute):  ...
    @abc.abstractmethod
    def handle_method       (self, method:model.Method):  ...
    @abc.abstractmethod
    def handle_enum_value   (self, enum:model.EnumValue):  ...
    @abc.abstractmethod
    def handle_ainterface   (self, ainterface:model.AInterface): ...
    @abc.abstractmethod
    def handle_comment      (self, comment:model.Comment): ...
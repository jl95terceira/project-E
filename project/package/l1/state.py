from .. import util

class State(util.Named): pass
class States:

    DEFAULT                     = State('')
    PACKAGE                     = State('Package')
    IMPORT                      = State('Import')
    ANNOTATION                  = State('Annotation')
    CLASS_BEGIN                 = State('Class')
    CLASS_AFTER_NAME            = State('Class After-Name')
    CLASS_EXTENDS               = State('Class Ext.')
    CLASS_IMPLEMENTS            = State('Class Impl.')
    CLASS_IMPLEMENTS_NAMED      = State('Class Impl. Named')
    CLASS_IMPLEMENTS_AFTER      = State('Class Impl. After')
    ENUM                        = State('Enum')
    ENUM_NAMED                  = State('Enum Named')
    ENUM_DEFINED                = State('Enum Defined')
    CONSTRUCTOR_SIGNATURE       = State('Constr. Sign.')
    CONSTRUCTOR_DECLARED        = State('Constr. Declared')
    CONSTRUCTOR_BODY            = State('Constr. Body')
    STATIC_CONSTRUCTOR_BODY     = State('Static Constr. Body')
    ATTR_BEGIN                  = State('Attr')
    ATTR_TYPED                  = State('Attr Typed')
    ATTR_NAMED                  = State('Attr Named')
    ATTR_INITIALIZE             = State('Attr Initialize')
    METHOD_SIGNATURE            = State('Method Signature')
    METHOD_DECLARED             = State('Method Declared')
    METHOD_BODY                 = State('Method Body')

class TypeState(util.Named): pass
class TypeStates:

    BEGIN    = TypeState('Begin')
    DEFAULT  = TypeState('')
    AFTERDOT = TypeState('After-Dot')

class SignatureState(util.Named): pass
class SignatureStates:

    BEGIN        = SignatureState('Begin')
    DEFAULT      = SignatureState('')
    ARG_TYPED    = SignatureState('Arg Typed')
    ARG_NAMED    = SignatureState('Arg Named')
    ARG_SEPARATE = SignatureState('Arg Sep.')

class BodyState(util.Named): pass
class BodyStates:

    BEGIN   = BodyState('')
    ONGOING = BodyState('Ongoing')

class ParArgsState(util.Named): pass
class ParArgsStates:

    BEGIN    = ParArgsState('Begin')
    DEFAULT  = ParArgsState('')
    SEPARATE = ParArgsState('Sep.')
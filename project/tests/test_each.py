import itertools
import unittest

from . import *

class GeneralTests              (unittest.TestCase): 

    def setUp(self):

        self.tr,self.th = gett(self)

    def test_01(self): self.th.test(';')
    def test_02(self): self.th.test(';;;;;;;;;;;;;;;;;;;;;;;;')
    def test_03(self): self.th.test('')
    @to_fail
    def test_04(self): self.th.test('package hello;')
    @to_fail
    def test_05(self): self.th.test(';package hello;')

class PackageTests              (unittest.TestCase): 

    def setUp(self):

        self.tr,self.th = gett(self)
        self.tr.r_package(model.Package(name='abc.def'))

    def test(self, name='abc.def', end=';'): self.th.test(' '.join(filter(bool, ('package',name,end))))

    def test_correct    (self): self.test()
    @to_fail
    def test_wrong_nosc (self): self.test(end='')
    @to_fail
    def test_wrong_name (self): self.test(name='abc.ddf;')

class ImportTests               (unittest.TestCase): 

    def setUp(self):

        self.tr,self.th = gett(self)
        self.tr.r_import_(model.Import(name='foo.bar'))

    def test(self, static=False, name='foo.bar', end=';'): self.th.test(' '.join(filter(bool, ('import','static' if static else '',name,end))))

    def test_correct        (self): self.test()
    @to_fail
    def test_wrong_static   (self): self.test(static=True)
    @to_fail
    def test_wrong_name     (self): self.test(name='foo.baz')
    @to_fail
    def test_wrong_nosc     (self): self.test(end='')

class ImportTestsCombinations   (unittest.TestCase): 

    def setUp(self): self.tr,self.th = gett(self)

    def test(self):

        for i,static in enumerate((True,False,)):

            with self.subTest(i=i):

                self.tr.clear_registry()
                self.th.reset         ()
                self.tr.r_import_     (model.Import(name='hello.world', static=static))
                self.th.test          (' '.join(filter(bool, (f'import','static ' if static else '', 'hello.world;'))))

class AnnotationTests           (unittest.TestCase): 

    def setUp(self):

        self.tr,self.th = gett(self)
        self.tr.r_annotation(model.Annotation(name='Log'))

    def test_01(self): self.th.test('@Log')
    def test_02(self): self.th.test('@Log;;')
    @to_fail
    def test_03(self): self.th.test('@Lag')

class ClassTests                (unittest.TestCase): 

    def setUp(self):

        self.tr,self.th = gett(self)
        self.tr.r_class_(model.Class(name      ='Foo', 
                                     access    =model.AccessModifiers.PUBLIC, 
                                     extends   ='Bar', 
                                     implements={'Tim', 'Tom'}))

    def test(self, access=model.AccessModifiers.PUBLIC, static=False, type=model.ClassTypes.CLASS, name='Foo', extends='Bar', implements=['Tim','Tom',], end='{'):

        self.th.test(' '.join(filter(bool, (access.keyword, 'static' if static else '', type.keyword, name, 'extends', extends, 'implements', ', '.join(implements), end))))

    def test_correct            (self): self.test()
    @to_fail
    def test_wrong_access       (self): self.test(access=model.AccessModifiers.DEFAULT)
    @to_fail
    def test_wrong_static       (self): self.test(static=True)
    @to_fail
    def test_wrong_type         (self): self.test(type=model.ClassTypes.INTERFACE)
    @to_fail
    def test_wrong_name         (self): self.test(name='Fuu')
    @to_fail
    def test_wrong_extends      (self): self.test(extends='Baz')
    @to_fail
    def test_wrong_implements   (self): self.test(implements={'Tim', 'Tam'})
    @to_fail
    def test_wrong_implements_2 (self): self.test(implements={'Tim'})
    @to_fail
    def test_wrong_implements_3 (self): self.test(implements={'Tom'})

class ClassTestsCombinations    (unittest.TestCase): 

    def setUp(self):

        self.tr,self.th = gett(self)

    def test(self):

        for i,(access, 
               static    ,
               finality  ,
               type      ) in enumerate(itertools.product(model.AccessModifiers.values(),
                                                          (True,False,),
                                                          model.FinalityTypes  .values(),
                                                          model.ClassTypes     .values())):

            with self.subTest(i=i):

                self.tr.clear_registry()
                self.th.reset         ()
                self.tr.r_class_      (model.Class(name='Hello', access=access, static=static, finality=finality, type=type))
                self.th.test          (' '.join(filter(bool, (access.keyword, 'static' if static else '', finality.keyword, type.keyword, 'Hello {'))))
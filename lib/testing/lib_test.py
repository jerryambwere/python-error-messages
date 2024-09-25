#!/usr/bin/env python3

import runpy

class TestNameError:
    '''
    a_name_error.py
    '''

    def test_name_error(self):
        '''
        contains defined name "hello_world"
        '''

        runpy.run_path('a_name_error.py')

class TestSyntaxError:
    '''
    a_syntax_error.py
    '''

    def test_syntax_error(self):
        '''
        multiplies two numbers
        '''
        
        runpy.run_path('a_syntax_error.py')

class TestTypeError:
    '''
    a_type_error.py
    '''

    def test_type_error(self):
        '''
        adds two numbers
        '''
        
        runpy.run_path('a_type_error.py')

class TestAssertionError:
    '''
    an_assertion_error.py
    '''

    def test_assertion_error(self):
        '''
        evaluates two equal values
        '''
        
        runpy.run_path('an_assertion_error.py')
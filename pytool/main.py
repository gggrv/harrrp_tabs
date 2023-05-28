# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------+++
#

# logging
import logging
log = logging.getLogger(__name__)

# embedded in python
import os
# pip install
# same project
    
class Paths:
    
    __CODE_ROOT = os.path.dirname( __file__ )
    __APPLICATION_ROOT = os.path.dirname( __CODE_ROOT )
    __TABS_ROOT = os.path.join( __APPLICATION_ROOT, 'tabs' )
    
    @staticmethod
    def get_code_root():
        # Returns the root folder of the main code.
        return Paths.__CODE_ROOT
    
    @staticmethod
    def get_application_root():
        # Returns the root folder of this application.
        return Paths.__APPLICATION_ROOT
    
    @staticmethod
    def get_tabs_root():
        return Paths.__TABS_ROOT

#---------------------------------------------------------------------------+++
# end 2023.05.28
# created

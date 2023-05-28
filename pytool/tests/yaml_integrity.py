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
from pytool import MainPaths
from pytool.common import readf_yaml
from pytool.common.enums.Tabs import ETabAccess

def _check_tabs( access_value ):
    
    # Tests all existing published (or not, or both)
    # tabs to make sure that they are valid .yaml files.
    # Prints any problems.
    
    # `access_value` = ETabAccess.value1...
    
    found = {}
    
    tab_dir = MainPaths.get_tabs_root()
    for root, subs, files in os.walk( tab_dir ):
        
        for file in files:
            # skip unneeded
            
            if not access_value in root:
                continue
            if not file.endswith( '.yaml' ):
                continue
            
            src = os.path.join( root, file )
            
            try:
                readf_yaml( src )
                found[ src ] = True
            except Exception as ex:
                found[ src ] = str( ex )
                
    for src, v in found.items():
        if not v is True:
            print( '-'*10, src, v )
            
def check_tabs_public():
    
    _check_tabs( ETabAccess.PUBLISHED )
            
def check_tabs_private():
    
    _check_tabs( ETabAccess.PRIVATE )

#---------------------------------------------------------------------------+++
#

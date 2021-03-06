#############################################################################
# Copyright (c) Members of the EGEE Collaboration. 2006-2010.
# See http://www.eu-egee.org/partners/ for details on the copyright holders.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors:
#     Joel Casutt     - joel.casutt@switch.ch
#############################################################################
'''
Created on 4/jan/2012

@author: joelcasutt
'''
from Probe import HydraProbe
from AbstractProbe import HydraAbstractProbe

class HydraStatusProbe( HydraProbe ):

    def __init__( self, serviceName, clientAuth ):
        super(HydraStatusProbe, self).__init__(serviceName, clientAuth)
        
    def check( self ):
        status = HydraProbe.getStatus( self )
        if status['Status'].find('And now... Some Services') != -1:
             self.nagios_ok("OK: Service is running!")
        else:
            self.nagios_critical("CRITICAL: Expected string not found!")

#!/usr/bin/env python

# On local PC (w/ Cisco AnyConnect live connection):
'ssh -R 1521:10.125.143.202:1521 allosure@cdx-cf'

# On remote server:
'export TNS_ADMIN=$ORACLE_HOME/network/admin'


dsnStr = '(DESCRIPTION =(ADDRESS = (PROTOCOL = TCP)(HOST = localhost)' \
+ '(PORT = 1521))(CONNECT_DATA =(SERVER = DEDICATED)(SERVICE_NAME = seq01)))'

Oracle_con = cx_Oracle.connect('jcollins', '####', dsnStr)

import pandas as pd 

 
#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
PyDog4Apache - 2016 - by psy (epsylon@riseup.net)

You should have received a copy of the GNU General Public License along
with PyDog4Apache; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import os
from subprocess import PIPE
from subprocess import Popen as execute
        
class Updater(object):     
    def __init__(self):
        GIT_REPOSITORY = "https://github.com/epsylon/pydog4apache"
        rootDir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../../', ''))
        if not os.path.exists(os.path.join(rootDir, ".git")):
            print "Not any .git repository found!\n"
            print "="*30
            print "\nYou should clone PyDog4Apache manually with:\n"
            print "$ git clone %s" % GIT_REPOSITORY
            print ""
        else:
            checkout = execute("git pull", shell=True, stdout=PIPE, stderr=PIPE).communicate()[0]
            if "Fast-forward" in checkout:
                print "Congratulations!! PyDog4Apache has been updated... ;-)\n"
            else:
                print "Your PyDog4Apache doesn't need to be updated... ;-)\n"

#!/usr/bin/env python

import sys
import os

sys.path.insert(1, os.path.join(os.path.dirname(__file__), 'src'))

from hello.application import Application

if __name__ == "__main__":
    try:
        app = Application(package="hello-world", 
                          version="0 (debug)",
                          pkgdatadir=os.path.join(os.path.dirname(__file__), 'data'))
    except Exception, e:
        sys.exit("Could not initialize application: %s" % str(e))
    app.run()

"""Routes"""

from os.path import dirname, basename, isfile
import glob
import sys
sys.path.append("/app/server/routes/")

modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

import sys
import unittest

sys.path.append('../tplinkroutermr600')

loader = unittest.TestLoader()
testSuite = loader.discover('test')
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(testSuite)

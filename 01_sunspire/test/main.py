from typing import *
from tests.test_solaris import TestSolaris
from tests.test_starfall import TestStarfall
from tests.test_helios import TestHelios
from tests.test_orbital import TestOrbital
import unittest

tests = [
    TestOrbital,
    # TestHelios,
    TestSolaris,
    # TestStarfall
]

if __name__ == "__main__":
    for test_class in tests:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        unittest.TextTestRunner(verbosity=2).run(suite)


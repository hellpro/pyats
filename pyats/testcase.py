from lin_test import LinuxCommonSetup, A1testcase
from cisco_test import CiscoCommonSetup, C1testcase, C2testcase, C3testcase
from pyats import aetest


class CommonSetup(CiscoCommonSetup):
    pass

'''
class LinTestcase(A1testcase):
    pass
'''

class C1CiscoTestcase(C1testcase):
    pass

class C2CiscoTestcase(C2testcase):
    pass

class C3CiscoTestcase(C3testcase):
    pass


if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest='testbed', type=loader.load)
    args, unknown = parser.parse_known_args()
    aetest.main(**vars(args))

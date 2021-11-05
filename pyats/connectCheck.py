from pyats import aetest

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology(self,
                       testbed,
                       sw1_name = 'SW1',
                       sw2_name = 'SW2',
                       sw3_name = 'SW3',
                       hq1_name = 'HQ1',
                       fw1_name = 'FW1',
                       br1_name = 'BR1'):
        sw1 = testbed.devices[sw1_name]
        sw2 = testbed.devices[sw2_name]
        sw3 = testbed.devices[sw3_name]
        hq1 = testbed.devices[hq1_name]
        fw1 = testbed.devices[fw1_name]
        br1 = testbed.devices[br1_name]

        self.parent.parameters.update(sw1 = sw1,
                                      sw2 = sw2,
                                      sw3 = sw2,
                                      hq1 = hq1,
                                      fw1 = fw1,
                                      br1 = br1)
        

    @aetest.subsection
    def establish_connections(self, steps, sw1, sw2, sw3, hq1, fw1, br1):
        with steps.start(f"Connecting to {sw1.name}"):
            sw1.connect(mit = True, log_stdout = False)

        with steps.start(f"Connecting to {sw2.name}"):
            sw2.connect(mit = True, log_stdout = False)

        with steps.start(f"Connecting to {sw3.name}"):
            sw3.connect(mit = True, log_stdout = False)

        with steps.start(f"Connecting to {hq1.name}"):
            hq1.connect(mit = True, log_stdout = False)
        
        with steps.start(f"Connecting to {fw1.name}"):
            fw1.connect(mit = True, log_stdout = False)
        
        with steps.start(f"Connecting to {br1.name}"):
            br1.connect(mit = True, log_stdout = False)

class BaseTestcase(aetest.Testcase):
    @aetest.test
    def hostname(self, steps, sw1, hq1):
        cmd = 'show running-config | section hostname'
        with steps.start(f"Check hostname {sw1.name}"):
            try:
                assert sw1.name in sw1.execute(cmd)
            except Exception as e:
                self.failed(f"Hostname {sw1.name} - {sw1.execute(cmd)}")
        
        with steps.start(f"Check hostname {hq1.name}"):
            try:
                assert hq1.name in hq1.execute(cmd)
            except Exception as e:
                self.failed(f"Hostname {hq1.name} - {hq1.execute(cmd)}")
        
    @aetest.test
    def domain_name(self, steps, sw2, fw1):
        cmd = 'show running-config | include domain-name'
        with steps.start(f"Check domain name {sw2.name}"):
            try:
                assert 'ssa.com' in sw2.execute(cmd)
            except Exception as e:
                self.failed(f"Domain name {sw2.name} - {sw2.execute(cmd)}")
        with steps.start(f"Check domain name {fw1.name}"):
            try:
                assert 'ssa.com' in fw1.execute(cmd)
            except Exception as e:
                self.failed(f"Domain name {fw1.name} - {fw1.execute(cmd)}")

if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest='testbed', type=loader.load)
    args, unknown = parser.parse_known_args()
    aetest.main(**vars(args))

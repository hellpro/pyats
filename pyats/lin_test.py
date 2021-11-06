from pyats import aetest


class LinuxCommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology_lin(self,
                           testbed,
                           l1_name='L1',
                           l2_name='L2'):
        l1 = testbed.devices[l1_name]
        l2 = testbed.devices[l2_name]

        self.parent.parameters.update(l1=l1,
                                      l2=l2)

    @aetest.subsection
    def establish_connections_lin(self, steps, l1, l2):
        with steps.start(f"Connecting to {l1.name}"):
            l1.connect(mit=True, log_stdout=False)

        with steps.start(f"Connecting to {l2.name}"):
            l2.connect(mit=True, log_stdout=False)


class A1testcase(aetest.Testcase):
    @aetest.setup
    def config_iface(self, steps, l1, l2):
        with steps.start(f"Configure ens3 on {l1.name}"):
            cmd = [
                "ip address add 192.168.1.1/24 dev ens3",
                "ip link set ens3 down",
                "ip link set ens3 up"]
            l1.execute(cmd)
        with steps.start(f"Configure ens3 on {l2.name}"):
            cmd = [
                "ip address add 192.168.1.2/24 dev ens3",
                "ip link set ens3 down",
                "ip link set ens3 up"]
            l2.execute(cmd)
    @aetest.test
    def hostname(self, steps, l1, l2):
        with steps.start(f"Check hostname of {l1.name}"):
            try:
                assert 'L1' in l1.execute('hostname')
            except Exception as e:
                self.failed(f"Hostname {l1.name} - {l1.execute('hostname')}")
        with steps.start(f"Check hostname of {l2.name}"):
            try:
                assert 'L2' in l2.execute('hostname')
            except Exception as e:
                self.failed(f"Hostname {l2.name} - {l2.execute('hostname')}")

    @aetest.test
    def ping_test(self, steps, l1, l2):
        with steps.start(f"Check ping {l1.name} to {l2.name}"):
            try:
                assert l1.ping('192.168.1.2')
            except Exception as e:
                self.failed(f"Ping {l1.name} to {l2.name} failed")
        with steps.start(f"Check ping {l2.name} to {l1.name}"):
            try:
                assert l2.ping('192.168.1.1')
            except Exception as e:
                self.failed(f"Ping {l2.name} to {l1.name} failed")

    @aetest.test
    def soft_install_test(self, steps, l1, l2):
        with steps.start(f"Check soft installation on {l1.name}"):
            try:
                assert 'openldap' in l1.execute('rpm -qa openldap')
            except Exception as e:
                self.failed(f"Soft not install on {l1.name}")
        with steps.start(f"Check soft installation on {l2.name}"):
            try:
                assert 'openldap' in l2.execute('rpm -qa openldap')
            except Exception as e:
                self.failed(f"Soft not install on {l2.name}")


if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest='testbed', type=loader.load)
    args, unknown = parser.parse_known_args()
    aetest.main(**vars(args))

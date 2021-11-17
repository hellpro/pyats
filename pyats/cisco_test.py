from pyats import aetest


class CiscoCommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology_cisco(self,
                             testbed,
                             sw1_name='SW1',
                             sw2_name='SW2',
                             sw3_name='SW3',
                             hq1_name='RTR',
                             fw1_name='FW',
                             br1_name='BRANCH'):
        sw1 = testbed.devices[sw1_name]
        sw2 = testbed.devices[sw2_name]
        sw3 = testbed.devices[sw3_name]
        hq1 = testbed.devices[hq1_name]
        fw1 = testbed.devices[fw1_name]
        br1 = testbed.devices[br1_name]

        self.parent.parameters.update(sw1=sw1,
                                      sw2=sw2,
                                      sw3=sw2,
                                      hq1=hq1,
                                      fw1=fw1,
                                      br1=br1)

    @aetest.subsection
    def establish_connections_cisco(self, steps, sw1, sw2, sw3, hq1, fw1, br1):
        with steps.start(f"Connecting to {sw1.name}"):
            try:
                sw1.connect(mit=True, log_stdout=False)
            except Exception as e:
                pass
            else:
                pass
            finally:
                pass
            sw1.connect(mit=True, log_stdout=False)

        with steps.start(f"Connecting to {sw2.name}"):
            try:
                sw2.connect(mit=True, log_stdout=False)
            except Exception as e:
                pass
            else:
                pass
            finally:
                pass
            

        with steps.start(f"Connecting to {sw3.name}"):
            try:
                sw3.connect(mit=True, log_stdout=False)
            except Exception as e:
                pass
            else:
                pass
            finally:
                pass
            sw3.connect(mit=True, log_stdout=False)

        with steps.start(f"Connecting to {hq1.name}"):
            try:
                hq1.connect(mit=True, log_stdout=False)
            except Exception as e:
                pass
            else:
                pass
            finally:
                pass
            

        with steps.start(f"Connecting to {fw1.name}"):
            try:
                fw1.connect(mit=True, log_stdout=False)
            except Exception as e:
                pass
            else:
                pass
            finally:
                pass
            

        with steps.start(f"Connecting to {br1.name}"):
            try:
                br1.connect(mit=True, log_stdout=False)
            except Exception as e:
                pass
            else:
                pass
            finally:
                pass
            


class C1testcase(aetest.Testcase):
    @aetest.test
    def hostname(self, sw1):
        cmd = 'show running-config | section hostname'
        try:
            assert "SW1" in sw1.execute(cmd)
        except Exception as e:
            self.failed(f"Hostname {sw1.name} - {sw1.execute(cmd)}")

    @aetest.test
    def local_user(self, hq1):
        cmd = 'show running-config | section username'
        try:
            assert 'privilege 15' in hq1.execute(cmd)
        except Exception as e:
            self.failed(f"User don't create on {hq1.name} - {hq1.execute(cmd)}")

    @aetest.test
    def scrypt(self, sw1):
        cmd = 'show running-config | section username'
        try:
            assert 'scrypt' in sw1.execute(cmd)
        except Exception as e:
            self.failed(f"User don't create on {sw1.name} - {sw1.execute(cmd)}")

    @aetest.test
    def banner(self, br1):
        cmd = 'show running-config | include banner'
        try:
            assert 'banner motd' in br1.execute(cmd)
        except Exception as e:
            self.failed(f"Banner don't create on {br1.name} - {br1.execute(cmd)}")

    @aetest.test
    def view(self, hq1):
        cmd = 'show running-config | include parser'
        try:
            assert 'view' in hq1.execute(cmd)
        except Exception as e:
            self.failed(f"View don't create on {hq1.name}")

    @aetest.test
    def superview(self, hq1):
        cmd = 'show running-config | include parser'
        try:
            assert 'superview' in hq1.execute(cmd)
        except Exception as e:
            self.failed(f"Superview don't create on {hq1.name}")\

    @aetest.test
    def tftp(self, hq1):
        cmd = 'show running-config | include server'
        try:
            assert 'tftp' in hq1.execute(cmd)
        except Exception as e:
            self.failed(f"TFTP don't archive on {hq1.name}")

    @aetest.test
    def password_encr(self, sw2):
        cmd = 'show running-config | include service'
        try:
            assert 'password-encryption' in sw2.execute(cmd)
        except Exception as e:
            self.failed(f"password-encryption dont use on {sw2.name} - {sw2.execute(cmd)}")


class C2testcase(aetest.Testcase):
    @aetest.test
    def vlan_table(self, sw1):
        cmd = 'show vlan brief'
        try:
            assert "CLIENT" in sw1.execute(cmd)
        except Exception as e:
            self.failed(f"VLAN don't create on {sw1.name} - {sw1.execute(cmd)}")

    @aetest.test
    def dtp(self, sw1):
        cmd = 'show interface trunk'
        try:
            assert 'desirable' in sw1.execute(cmd)
        except Exception as e:
            self.failed(f"DTP dont passed {sw1.name} - sw1.execute(cmd)")

    @aetest.test
    def trunk_portfast(self, sw2):
        cmd = 'show running-config | section interface'
        try:
            assert 'portfast trunk' in sw2.execute(cmd)
        except Exception as e:
            self.failed(f"Portfast not active on trunk {sw2.name} - {sw2.execute(cmd)}")

    @aetest.test
    def lacp(self, sw1):
        cmd = 'show etherchannel summary'
        try:
            assert 'Po1(SU)' in sw1.execute(cmd)
        except Exception as e:
            self.failed(f"LACP not create on {sw1.name} - {sw1.execute(cmd)}")

    @aetest.test
    def pagp(self, sw1):
        cmd = 'show etherchannel summary'
        try:
            assert 'Po2(SU)' in sw1.execute(cmd)
        except Exception as e:
            self.failed(f"PAgP not create on {sw1.name} - {sw1.execute(cmd)}")

    @aetest.test
    def shut_if(self, sw3):
        cmd = 'show vlan brief'
        try:
            assert 'SHUTDOWN e1/1 ' in sw3.execute(cmd)
        except Exception as e:
            self.failed(f"Interface no shutdown {sw3.name} - {sw3.execute(cmd)}")

    @aetest.test
    def dhcp_snoop(self, sw2):
        cmd = 'show running-config | include DHCP'
        try:
            assert 'snooping' in sw2.execute(cmd)
        except Exception as e:
            self.failed(f"DHCP snooping not use on {sw2.name}")

    @aetest.test
    def arp_inspect(self, sw2):
        cmd = 'show running-config | include arp'
        try:
            assert 'inspection' in sw2.execute(cmd)
        except Exception as e:
            self.failed(f"ARP inspect not use on {sw2.name}")

    @aetest.test
    def source_card(self, sw1):
        cmd = 'show running-config | include source'
        try:
            assert 'card' in sw1.execute(cmd)
        except Exception as e:
            self.failed(f"Source card not use on {sw1.name}")

    @aetest.test
    def load_bal(self, sw1):
        cmd = 'show running-config | include etherchannel'
        try:
            assert 'load' in sw1.execute(cmd)
        except Exception as e:
            self.failed(f"Load balance not use on {sw1.name}")

    @aetest.test
    def stp_mode(self, sw1):
        cmd = 'show spanning-tree summary | include mode'
        try:
            assert 'rapid' in sw1.execute(cmd)
        except Exception as e:
            self.failed(f"STP mode on {sw1.name} - {sw1.execute(cmd)}")
    
    
    @aetest.test
    def stp_prior(self, sw1):
        cmd = 'show running-config | include spanning-tree'
        try:
            assert 'primary' in sw1.execute(cmd)
        except Exception as e:
            self.failed(f"STP prior on {sw1.name} - {sw1.execute(cmd)}")

    @aetest.test
    def stp_root(self, sw2):
        cmd = 'show running-config | section interface Ethernet1/3'
        try:
            assert 'bpduguard' in sw2.execute(cmd)
        except Exception as e:
            self.failed(f"STP mode on {sw2.name} - {sw2.execute(cmd)}")
    

class C3testcase(aetest.Testcase):

    @aetest.test
    def vlan_routing(self, sw1):
        try:
            assert '!!' in sw1.ping('10.11.20.1')
        except Exception as e:
            self.failed(f"Ping to {sw1.name} - {sw1.ping('10.11.20.1')}")

    @aetest.test
    def l2vpn(self, hq1):
        cmd = 'show ip interface brief'
        try:
            assert '10.5.5.0' in hq1.execute(cmd)
        except Exception as e:
            self.failed(f"L2VPN on {hq1.name} - {hq1.execute(cmd)}")

    @aetest.test
    def ppp(self, br1):
        cmd = 'show ip interface brief'
        try:
            assert '40.15.25.66' in br1.execute(cmd)
        except Exception as e:
            self.failed(f"PPP on {br1.name} - {br1.execute(cmd)}")

    @aetest.test
    def ipoe(self, br1):
        cmd = 'show ip int bri'
        try:
            assert '10.255.61.34' in br1.execute(cmd)
        except Exception as e:
            self.failed(f"IPoE on {br1.name} - {br1.execute(cmd)}")

    @aetest.test
    def dhcp_bind(self, br1):
        cmd = 'show ip dhcp binding'
        try:
            assert '172.16.10' in br1.execute(cmd)
        except Exception as e:
            self.failed(f"DHCP on {br1.name} - {br1.execute(cmd)}")

    @aetest.test
    def nat(self, hq1):
        cmd = 'show running-config | include ip nat'
        try:
            assert 'overload' in hq1.execute(cmd)
        except Exception as e:
            self.failed(f"NAT on {hq1.name} - {hq1.execute(cmd)}")

    @aetest.test
    def bgp(self, br1):
        cmd = 'show ip route bgp'
        try:
            assert '1.1.1.1' in br1.execute(cmd)
        except Exception as e:
            self.failed(f"BGP on {br1.name} - {br1.execute(cmd)}")


    @aetest.test
    def ibgp(self, hq1):
        cmd = 'show ip route bgp'
        try:
            assert '33.33.33.192' in hq1.execute(cmd)
        except Exception as e:
            self.failed(f"iBGP on {hq1.name} - {hq1.execute(cmd)}")
    
    @aetest.test
    def br_remove(self, br1):
        cmd = 'show ip route bgp'
        try:
            assert '40.15.25.64' in br1.execute(cmd)
        except Exception as e:
            self.failed(f"Route not remove on {br1.name}")

    @aetest.test
    def branch_lb(self, br1):
        cmd = 'show running-config | include balance'
        try:
            assert 'balance' in br1.execute(cmd)
        except Exception as e:
            self.failed(f"Load balance on {br1.name} not active")


    @aetest.test
    def gre(self, hq1):
        try:
            assert '!!' in hq1.ping('10.20.20.2')
        except Exception as e:
            self.failed(f"Ping branch- {hq1.ping('10.20.20.2')}")

    @aetest.test
    def ospf(self, br1):
        cmd = 'show ip route ospf'
        try:
            assert '10.5.5.0' in br1.execute(cmd)
        except Exception as e:
            self.failed(f"OSPF on {br1.name} - {br1.execute(cmd)}")
    
    @aetest.test
    def eigrp(self, br1):
        cmd = 'show ip route eigrp'
        try:
            assert '10.11.10.0' in br1.execute(cmd)
        except Exception as e:
            self.failed(f"EIGRP on {br1.name} - {br1.execute(cmd)}")

    print('Everything - 0')


if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest='testbed', type=loader.load)
    args, unknown = parser.parse_known_args()
    aetest.main(**vars(args))

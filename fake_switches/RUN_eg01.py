from twisted.internet import reactor
from pyometry.pyprofi.fake_switches.switch_configuration import SwitchConfiguration, Port
from pyometry.pyprofi.fake_switches.transports.ssh_service import SwitchSshService
from pyometry.pyprofi.fake_switches.cisco.cisco_core import CiscoSwitchCore

class MySwitchConfiguration( SwitchConfiguration ):
    def __init__(self, *args, **kwargs):
        super( MySwitchConfiguration, self ).__init__(objects_overrides={"Port": MyPort}, *args, **kwargs)


class MyPort(Port):
    def __init__(self, name):
        self._access_vlan = None

        super(MyPort, self).__init__(name)

    @property
    def access_vlan(self):
        return self._access_vlan

    @access_vlan.setter
    def access_vlan(self, value):
        if self._access_vlan != value:
            self._access_vlan = value
            print ("This could add vlan to eth0")


if __name__ == '__main__':
    
    # weitermachen : 20200110_130752
    
    ssh_service = SwitchSshService(ip="127.0.0.1"
                                   ,port=11001
                                   ,switch_core=CiscoSwitchCore( MySwitchConfiguration("127.0.0.1", "my_switch", ports=[MyPort("FastEthernet0/1")]) ))
    ssh_service.hook_to_reactor(reactor)
    reactor.run()

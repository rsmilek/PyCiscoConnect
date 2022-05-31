from os import path
from pywinauto import Desktop, Application

CISCO_CONNECT_APP = 'C:\\Program Files (x86)\\Cisco\Cisco AnyConnect Secure Mobility Client\\vpnui.exe'

# Make Cisco app visible - not so nice, don't know about better way...
try:
    ciscoApp = Application(backend='uia').connect(path=CISCO_CONNECT_APP, timeout=3)
except:
    ciscoApp = Application(backend='uia').start(CISCO_CONNECT_APP, timeout=3)

Application(backend='uia').start(CISCO_CONNECT_APP, timeout=3)
window = ciscoApp['Cisco AnyConnect Secure Mobility Client']

window.wait('visible', timeout=10)
window['ConnectButton'].click()

ciscoApp["Cisco AnyConnect Login"].wait('visible', timeout=30)
webWindow = ciscoApp["Cisco AnyConnect Login"]
webWindow['E-mail addressEdit'].wait('ready', timeout=30)
webWindow['E-mail addressEdit'].type_keys("radim.smilek@cz.abb.com")
webWindow['PasswordEdit'].type_keys("Kolovrat73")
webWindow['Login'].click()

window.child_window(title="Cisco AnyConnect").wait('visible', timeout=60)
modal = window.child_window(title="Cisco AnyConnect")
modal.AcceptButton.wait('ready', timeout=5)
modal.AcceptButton.click()

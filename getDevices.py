import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set URL and login body
url = 'https://sandbox-sdwan-2.cisco.com/j_security_check'
login_body = {
    'j_username': 'devnetuser',
    'j_password': 'RG!_Yw919_83'
}

# Must use a session for SD-WAN
session = requests.session()

response = session.post(url, data=login_body, verify=False)
# print(response)

if not response.ok or response.text:
    print('Login failure')
    import sys
    sys.exit(1)
else:
    print('Login worked! Yay!')

# Get Devices
url = 'https://sandbox-sdwan-2.cisco.com/dataservice/device'

device_response = session.get(url, verify=False).json()['data']
# print(json.dumps(device_response, indent=2, sort_keys=True))

for device in device_response:
    print(f"Hostname: {device['host-name']}")
    print(f"IP: {device['local-system-ip']}")
    print(f"Model: {device['device-model']}")
    print('')

# Get Templates
# template_url = 'https://sandbox-sdwan-2.cisco.com/dataservice/template/device'
# template_response = session.get(template_url, verify=False).json()['data']
# print(template_response)

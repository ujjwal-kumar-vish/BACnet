from bacpypes.app import BIPSimpleApplication
from bacpypes.local.device import LocalDeviceObject
from bacpypes.core import run
from bacpypes.apdu import WhoIsRequest, IAmRequest
from bacpypes.pdu import Address

# Configuration for the local BACnet device
DEVICE_ID = 12345
DEVICE_NAME = "MyBACpypesDevice"
VENDOR_ID = 15  # Example vendor ID
IP_ADDRESS = "192.168.1.9/24" # Your device's IP address and subnet mask

class WhoIsIAmApplication(BIPSimpleApplication):
    def __init__(self, local_device, address):
        super().__init__(local_device, address)

    def do_IAmRequest(self, apdu):
        """Handle incoming I-Am requests."""
        print(f"Received I-Am from: {apdu.pduSource}")
        print(f"  Device Identifier: {apdu.iAmDeviceIdentifier}")
        print(f"  Max APDU Length Accepted: {apdu.maxAPDULengthAccepted}")
        print(f"  Segmentation Supported: {apdu.segmentationSupported}")
        print(f"  Vendor ID: {apdu.vendorID}")

def main():
    # Create a local device object
    this_device = LocalDeviceObject(
        objectIdentifier=('device', DEVICE_ID),
        objectName=DEVICE_NAME,
        vendorIdentifier=VENDOR_ID
    )

    # Create the BACnet/IP application
    app = WhoIsIAmApplication(this_device, IP_ADDRESS)

    # Create a Who-Is request (optional: specify limits or target address)
    who_is_request = WhoIsRequest()
    # To target a specific device: who_is_request = WhoIsRequest(deviceInstanceRange=(1000, 1000))
    # To send to a specific address: app.request(who_is_request, Address("192.168.1.5"))

    # Send the Who-Is request
    print("Sending Who-Is request...")
    who_is_request = WhoIsRequest()
    who_is_request.pduDestination = Address("192.168.1.255")
    app.request(who_is_request)

    # Run the BACpypes application
    print("BACpypes application running. Waiting for I-Am responses...")
    run()

if __name__ == "__main__":
    main()
import asyncio
import BAC0

async def main():
    # Start BAC0 in lite mode
    bacnet = BAC0.lite()

    # Send Who-Is broadcast
    print("Sending Who-Is request...")
    bacnet.who_is()

    # Wait a few seconds to collect responses
    await asyncio.sleep(5)

    # Display discovered devices
    print("I-Am responses received:")
    for device in bacnet.devices:
        print(f"Device ID: {device['device_id']}")
        print(f"  Address: {device['address']}")
        print(f"  Max APDU: {device['max_apdu']}")
        print(f"  Segmentation: {device['segmentation']}")
        print(f"  Vendor ID: {device['vendor_id']}")
        print("-" * 40)

    # Clean up
    bacnet.disconnect()

# Launch the async event loop
if __name__ == "__main__":
    asyncio.run(main())
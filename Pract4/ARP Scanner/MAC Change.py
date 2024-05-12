import subprocess
subprocess.run(["ifconfig", "eth0"],shell=True)

if __name__ == "__main__":
    interface = "eth0"
    new_mac = "00:11:22:23:43:24"

    print(f"Shutting down the interface : {interface.upper()}")
    subprocess.run(["ifconfig",interface,"down"])

    print((f"Changing{interface.upper()} MAC address to ----->>>> : {new_mac}"))
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])

    subprocess.run(["ifconfig", interface,"up"])
    print("Network interface turned ON !!!!!")
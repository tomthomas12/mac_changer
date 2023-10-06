import subprocess
print("\n\n\n")
print("  __  __          _____          _____ _    _          _   _  _____ ______ _____   ")
print(" |  \/  |   /\   / ____|        / ____| |  | |   /\   | \ | |/ ____|  ____|  __ \  ")
print(" | \  / |  /  \ | |            | |    | |__| |  /  \  |  \| | |  __| |__  | |__) | ")
print(" | |\/| | / /\ \| |            | |    |  __  | / /\ \ | . ` | | |_ |  __| |  _  /  ")
print(" | |  | |/ ____ \ |____        | |____| |  | |/ ____ \| |\  | |__| | |____| | \ \  ")
print(" |_|  |_/_/    \_\_____|        \_____|_|  |_/_/    \_\_| \_|\_____|______|_|  \_\ ")
print("\n\n\n")
                                                                            
if __name__ == "__main__":
    interface = "eth0"
    new_mac = input("Enter your new MAC adress : ")

    print(f"We are going to shut down the interface : {interface} ")
    subprocess.run(["ifconfig",interface,"down"])

    print(f"Changing {interface} MAC address to : {new_mac}")
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])


    subprocess.run(["ifconfig",interface,"up"])
    print("Network interface turned ON")

import os

while True:
    print("\n===== PERSONAL FIREWALL =====")
    print("1. Block IP")
    print("2. Unblock IP")
    print("3. Show Rules")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        ip = input("Enter IP to block: ")
        os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
        print(f"{ip} blocked successfully!")

    elif choice == "2":
        ip = input("Enter IP to unblock: ")
        os.system(f"sudo iptables -D INPUT -s {ip} -j DROP")
        print(f"{ip} unblocked successfully!")

    elif choice == "3":
        os.system("sudo iptables -L")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")

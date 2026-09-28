from netmiko import ConnectHandler

routeurs = [
    {
        "device_type" : "cisco_ios",
        "host" : "192.168.1.101",
        "username" : "admin",
        "password" : "cisco123",
        "disabled_algorithms": {},
    },
    {
        "device_type" : "cisco_ios",
        "host" : "192.168.1.102",
        "username" : "admin",
        "password" : "cisco123",
        "disabled_algorithms": {},
    },
    {
        "device_type" : "cisco_ios",
        "host" : "192.168.1.103",
        "username" : "admin",
        "password" : "cisco123",
        "disabled_algorithms": {},
    }]

commandes = ["banner motd # ACCES RESTREINT - SATOM IT #"]

for routeur in routeurs:
    net_connect = ConnectHandler(**routeur)
    temp = net_connect.send_config_set(commandes)
    print(temp)
    net_connect.save_config()
    net_connect.disconnect()
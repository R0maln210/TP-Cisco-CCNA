---
title: 'TP 3.3 - DHCP Snooping : mitigation d''un serveur DHCP pirate - Romain Jaquet'

---

# TP 3.3 - DHCP Snooping : mitigation d'un serveur DHCP pirate - Romain Jaquet

## Lab complet : 

<img width="1254" height="860" alt="01 - lab complet" src="https://github.com/user-attachments/assets/e3b59ab0-74d5-46f1-8eb4-309101c65699" />

## SW1 : 

```
conf t
hostname SW1
ip dhcp snooping
ip dhcp snooping vlan 1
interface eth0/0
ip dhcp snooping trust
exit

interface e0/1
ip dhcp snooping limit rate 10
exit

interface e0/2
ip dhcp snooping limit rate 10
exit

# Les serveurs DHCP Cisco rejettent ces requêtes par sécurité. On doit donc enlever cette option
no ip dhcp snooping information option
exit
```

## DHCP_Legit : 

```
conf t
hostname DHCP_Legit
interface eth0/0
no switchport
ip add 192.168.1.254 255.255.255.0
no shutdown
exit

service dhcp
ip dhcp pool LEGIT
network 192.168.1.0 255.255.255.0
default-router 192.168.1.254
```

## DHCP_Pirate : 

```
conf t
hostname DHCP_Pirate
interface eth0/0
no switchport
ip add 10.0.0.254 255.255.255.0
no shutdown
exit

service dhcp
ip dhcp pool PIRATE
network 10.0.0.0 255.255.255.0
default-router 10.0.0.254
```

## PC1 : 

```
set pcname PC1
ip dhcp
```

## Commandes pour la vérification : 

### show ip dhcp snooping
Sur SW1 : 

<img width="1232" height="1650" alt="02 - show ip dhcp snooping" src="https://github.com/user-attachments/assets/f6908db2-0183-45ae-9803-1d47e11e15f8" />

### show ip dhcp snooping binding
Sur SW1 : 

<img width="1200" height="288" alt="03 - show ip dhcp snooping binding" src="https://github.com/user-attachments/assets/e4dfebfa-3523-4280-9bfe-de487f0487ec" />

### ip dhcp : 
Sur PC1 : 

<img width="1196" height="96" alt="04 - ip dhcp" src="https://github.com/user-attachments/assets/f0c9a115-2e39-4309-9d6a-9d06e85bf470" />

---
title: 'TP 5.1 - ACL standard nommée : restriction d''accès administratif (VTY) - Romain Jaquet'

---

# TP 5.1 - ACL standard nommée : restriction d'accès administratif (VTY) - Romain Jaquet

## Lab complet : 

<img width="546" height="674" alt="01 - lab complet" src="https://github.com/user-attachments/assets/fafecabf-f8f5-4815-95e6-231668ce279d" />

## R1 : 

```
conf t
hostname R1

interface fa1/0
ip address 192.168.1.254 255.255.255.0
no shutdown
exit

interface fa2/0
ip address 192.168.2.254 255.255.255.0
no shutdown
exit

# Mise en place du SSH
ip domain-name satom.local
username ADMIN privilege 15 secret Adm1n2026
crypto key generate rsa general-keys modulus 2048
ip ssh version 2

# Création de l'access-list
ip access-list standard ADMIN-ONLY
permit host 192.168.1.10
exit

# Applique l'access-list et le SSH
line vty 0 4
transport input ssh
login local
access-class ADMIN-ONLY in
exit
```

## PC ADMIN : 

```
set pcname ADMIN
ip 192.168.1.10/24 192.168.1.254
```

## PC AUTRE POSTE : 

```
set pcname APOSTE
ip 192.168.2.20/24 192.168.2.254
```

## Commandes pour la vérification : 

### show access-lists ADMIN-ONLY
Sur R1 : 

<img width="594" height="150" alt="02 - show access-list" src="https://github.com/user-attachments/assets/c90f4cc3-487e-47dc-a9a1-d16ee2d0e542" />

### show ip interface | include line protocol
Sur R1 : 

<img width="960" height="596" alt="03 - show ip interface brief" src="https://github.com/user-attachments/assets/1e4379f4-832a-4c18-a08f-9ea38c1b0245" />

### ssh -l ADMIN 192.168.1.254
### ssh -l ADMIN 192.168.2.254

Pnetlab ne permet pas aux vPC de faire du ssh, j'ai donc décidé d'ajouter un routeur pour voir si le ssh fonctionnait.

### --> Modification à faire : 

### RADMIN : 

```
conf t
hostname RADMIN

interface eth0/0
no switchport
ip address 192.168.1.10 255.255.255.0
no shutdown
exit
ip route 0.0.0.0 0.0.0.0 192.168.1.254
```

### RAPOSTE : 

```
conf t
hostname RAPOSTE

interface eth0/0
no switchport
ip address 192.168.2.20 255.255.255.0
no shutdown
exit
ip route 0.0.0.0 0.0.0.0 192.168.2.254
```
<img width="1228" height="1684" alt="04 - ssh -l ADMIN " src="https://github.com/user-attachments/assets/84f3857d-4b9f-49ac-b734-807654757155" />

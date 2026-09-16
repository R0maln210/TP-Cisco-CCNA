---
title: 'TP 3.1 — Durcissement de l''accès administratif : AAA local + SSH - Romain Jaquet'

---

# TP 3.1 — Durcissement de l'accès administratif : AAA local + SSH - Romain Jaquet

## Lab complet : 

<img width="550" height="278" alt="01 - lab complet" src="https://github.com/user-attachments/assets/9a3c88ed-d151-4fff-b9e4-434cfa6e9df1" />

## R1 : 

```
conf t
hostname R1

# Configuration de l'interface
interface fa0/0
ip add 192.168.1.1 255.255.255.0
no shutdown
exit

# Configuration du SSH
ip domain-name satom.local
username SATOMIT privilege 15 secret Adm1n#2026
crypto key generate rsa modulus 2048
ip ssh version 2
line vty 0 4 
transport input ssh
login local
exec-timeout 5 0
exit
enable secret C1sco#Enable2026
```

## PC ADMIN : 

```
set pcname ADMIN
ip address 192.168.1.10/24 192.168.1.1
ping 192.168.1.1
```

## Commandes pour la vérification : 

### show ip ssh

<img width="1236" height="826" alt="02 - show ip ssh" src="https://github.com/user-attachments/assets/6d4c2210-3507-40e8-9bed-131bb6d875e5" />

### show users

Pnetlab ne permet pas aux vPC de faire du ssh, j'ai donc décidé d'ajouter un routeur pour voir si le ssh fonctionnait.

### --> Modification à faire : 

### R2 : 

```
conf t
hostname ADMIN

interface fa0/0
ip add 192.168.1.10 255.255.255.0
no shutdown
exit
```

<img width="1242" height="1654" alt="03 - show users" src="https://github.com/user-attachments/assets/b72e7da3-bbef-4696-b43f-e9a20d8ca354" />

### ssh -l SATOMIT 192.168.1.1

<img width="1232" height="1024" alt="04 - ssh SATOMIT" src="https://github.com/user-attachments/assets/c50b2250-0467-42ca-87ad-173c21445d36" />

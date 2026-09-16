---
title: 'TP 3.1 — Durcissement de l''accès administratif : AAA local + SSH - Romain Jaquet'

---

# TP 3.1 — Durcissement de l'accès administratif : AAA local + SSH - Romain Jaquet

## Lab complet : 

![01 - lab complet](https://hackmd.io/_uploads/BkOtu6vYGe.png)

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

![02 - show ip ssh](https://hackmd.io/_uploads/Bk9u_aDtze.png)

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

![03 - show users](https://hackmd.io/_uploads/S1cPdTPKze.png)

### ssh -l SATOMIT 192.168.1.1

![04 - ssh SATOMIT](https://hackmd.io/_uploads/rJWO_pvYzl.png)
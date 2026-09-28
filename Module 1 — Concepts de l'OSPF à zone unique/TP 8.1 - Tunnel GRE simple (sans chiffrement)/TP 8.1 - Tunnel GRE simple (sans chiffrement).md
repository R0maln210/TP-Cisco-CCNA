---
title: TP 8.1 - Tunnel GRE simple (sans chiffrement)

---

# TP 8.1 - Tunnel GRE simple (sans chiffrement)

<img width="498" height="220" alt="01 - lab complet" src="https://github.com/user-attachments/assets/6d72352e-ebe9-4ae4-bd1f-851e355098ee" />

## R1 : 

```
en
conf t
hostname R1 

interface tunnel 0
ip add 192.168.100.1 255.255.255.252
tunnel source fa0/0
tunnel destination 198.51.100.1
tunnel mode gre ip
exit

interface fa0/0
ip add 203.0.113.1 255.255.255.0
no shutdown
exit

ip route 0.0.0.0 0.0.0.0 FastEthernet0/0
exit

wr
```

## R2 : 

```
en 
conf t
hostname R2

interface tunnel 0 

ip add 192.168.100.2 255.255.255.252
tunnel source fa0/0
tunnel destination 203.0.113.1
tunnel mode gre ip 
exit

interface fa0/0
ip add 198.51.100.1 255.255.255.0
no shutdown
exit

ip route 0.0.0.0 0.0.0.0 FastEthernet0/0
exit

wr
```

## Commandes pour la vérification : 

### show interfaces tunnel 0

<img width="1232" height="1244" alt="02 - show interfaces tunnel 0" src="https://github.com/user-attachments/assets/a8a08e06-6dbe-49e8-befe-c38e56c930b6" />

### ping 

<img width="2490" height="412" alt="03 - ping" src="https://github.com/user-attachments/assets/3fe46d19-0efb-4236-9c22-41dca5243b68" />

---
title: 'TP 5.2 - ACL étendue : filtrage de services (web autorisé, tout le reste bloqué)'

---

# TP 5.2 - ACL étendue : filtrage de services (web autorisé, tout le reste bloqué)

## Lab complet : 

![01 - lab complet](https://hackmd.io/_uploads/SJiHXMuYzx.png)

## R1 : 

```
conf t
hostname R1

interface fa1/0
ip address 192.168.99.254 255.255.255.0
no shutdown
exit

interface fa2/0
ip address 8.8.8.1 255.255.255.0
no shutdown
exit

ip access-list extended INVITES-WEB-ONLY
permit tcp 192.168.99.0 0.0.0.255 any eq 80
permit tcp 192.168.99.0 0.0.0.255 any eq 443
permit udp 192.168.99.0 0.0.0.255 any eq 53
deny ip 192.168.99.0 0.0.0.255 any
exit

interface fa1/0
ip access-group INVITES-WEB-ONLY in
exit
```

## LANGIT : 

```
set pcname LANGIT
ip 192.168.99.10/24 192.168.99.254
```

## SRV-INTERNET : 

```
conf t
hostname SRV-INTERNET

interface eth0/0
no switchport
ip address 8.8.8.8 255.255.255.0
no shutdown
exit

ip route 0.0.0.0 0.0.0.0 8.8.8.1
ip http server

# Ne fonctionne pas sur ces routeurs PNETLAB
ip http secure-server
ip dns server
```

## Commandes pour la vérification : 

### show access-lists INVITES-WEB-ONLY
Sur R1 : 

![02 - show access-list](https://hackmd.io/_uploads/ByQ87fdYfg.png)

### show ip interface fa1/0 | include access list
Sur R1 : 

![03 - show ip interface](https://hackmd.io/_uploads/S1lwmzuFGe.png)

### rlogin 8.8.8.8 80 
Sur LANGIT : 

![04 - rlogin](https://hackmd.io/_uploads/HyUvQfuFzx.png)

### ping 8.8.8.8
Sur LANGIT : 

![05 - ping](https://hackmd.io/_uploads/H1sPmGOtzx.png)

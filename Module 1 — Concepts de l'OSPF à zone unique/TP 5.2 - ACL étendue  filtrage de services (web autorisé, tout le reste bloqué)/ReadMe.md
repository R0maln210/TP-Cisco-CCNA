---
title: 'TP 5.2 - ACL étendue : filtrage de services (web autorisé, tout le reste bloqué)'

---

# TP 5.2 - ACL étendue : filtrage de services (web autorisé, tout le reste bloqué)

## Lab complet : 

<img width="1026" height="262" alt="01 - lab complet" src="https://github.com/user-attachments/assets/44bdd7a7-8140-4712-94c8-4dc03132656f" />

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

<img width="820" height="194" alt="02 - show access-list" src="https://github.com/user-attachments/assets/69ea5d3f-622f-42e0-a2cf-be1785505c65" />

### show ip interface fa1/0 | include access list
Sur R1 : 

<img width="732" height="108" alt="03 - show ip interface" src="https://github.com/user-attachments/assets/0457256a-494e-4b5f-bc00-4d462ad1b603" />

### rlogin 8.8.8.8 80 
Sur LANGIT : 

<img width="926" height="190" alt="04 - rlogin" src="https://github.com/user-attachments/assets/1b68090e-b57e-4ddb-998b-4eaa2adefeec" />

### ping 8.8.8.8
Sur LANGIT : 

<img width="1210" height="394" alt="05 - ping" src="https://github.com/user-attachments/assets/0f4fe743-e71c-4e7c-a4f7-b818446b2972" />

---
title: TP 2.3 — Authentification OSPF MD5 et dépannage d'adjacence - Romain Jaquet

---

# TP 2.3 — Authentification OSPF MD5 et dépannage d'adjacence - Romain Jaquet

## Lab complet : 

![01 - lab complet](https://hackmd.io/_uploads/r1CBHcUKfl.png)

## R1 : 

```
conf t
interface fa0/0
ip ospf message-digest-key 1 md5 CCNA-Satom2026!
ip ospf authentication message-digest
exit
```

## R2 : 

```
conf t
interface fa0/0
ip ospf message-digest-key 1 md5 CCNA-Satom2026!
ip ospf authentication message-digest
exit
```

## R3: 

```
conf t
interface fa0/0
ip ospf message-digest-key 1 md5 CCNA-Satom2026!
ip ospf authentication message-digest
exit
```

## Commandes pour la vérification : 

### show ip ospf interface

R1 : 
![02 - show ip ospf interface](https://hackmd.io/_uploads/r1mYrqIFzl.png)

### debug ip ospf adj

R1 : 
![03 - debug ip ospf adj](https://hackmd.io/_uploads/H1UAH9UYzl.png)

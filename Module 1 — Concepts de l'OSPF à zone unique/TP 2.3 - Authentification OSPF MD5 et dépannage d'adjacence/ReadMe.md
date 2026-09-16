---
title: TP 2.3 — Authentification OSPF MD5 et dépannage d'adjacence - Romain Jaquet

---

# TP 2.3 — Authentification OSPF MD5 et dépannage d'adjacence - Romain Jaquet

## Lab complet : 

<img width="1798" height="980" alt="01 - lab complet" src="https://github.com/user-attachments/assets/68f77b1c-99df-4e85-874a-1ba79612c4fa" />

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
<img width="1128" height="1030" alt="02 - show ip ospf interface" src="https://github.com/user-attachments/assets/88fc76ca-ba4a-4be6-b2f4-99550990c5fc" />

### debug ip ospf adj

R1 : 
<img width="1012" height="200" alt="03 - debug ip ospf adj" src="https://github.com/user-attachments/assets/2a47b476-3718-4bb7-a346-ae24105a761f" />

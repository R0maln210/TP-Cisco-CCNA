---
title: TP 2.2 — Route par défaut et interfaces passives par défaut - Romain Jaquet

---

# TP 2.2 — Route par défaut et interfaces passives par défaut - Romain Jaquet

nom du lab : TP 1-4 Bonus_1789458517116_1789462978774
## Lab complet : 

<img width="1376" height="788" alt="01 - lab complet" src="https://github.com/user-attachments/assets/250dfefd-1626-448e-be39-83066b0f00b0" />

## R1 : 

```
conf t
interface fa1/0
ip address 203.0.113.2 255.255.255.0
no shutdown
exit
ip route 0.0.0.0 0.0.0.0 203.0.113.1
```

## Commandes pour la vérification : 

### show ip route | include ^Gateway|0.0.0.0/0

Sur R1 : 
<img width="1232" height="822" alt="02 - show ip route include Gateway" src="https://github.com/user-attachments/assets/4b2e14d8-8357-47de-8aa1-7c597c8623dc" />

### show ip ospf database external

Sur R2 : 
<img width="1228" height="818" alt="03 - show ip ospf database external" src="https://github.com/user-attachments/assets/6253d2a7-314e-49c0-85a5-206ecc5d9003" />

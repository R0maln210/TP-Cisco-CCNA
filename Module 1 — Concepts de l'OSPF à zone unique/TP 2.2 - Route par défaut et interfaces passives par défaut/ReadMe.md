---
title: TP 2.2 — Route par défaut et interfaces passives par défaut - Romain Jaquet

---

# TP 2.2 — Route par défaut et interfaces passives par défaut - Romain Jaquet

nom du lab : TP 1-4 Bonus_1789458517116_1789462978774
## Lab complet : 

![01 - lab complet](https://hackmd.io/_uploads/ryQNTt8Kfl.png)

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
![02 - show ip route include Gateway](https://hackmd.io/_uploads/Byzb6tUYMe.png)

### show ip ospf database external

Sur R2 : 
![03 - show ip ospf database external](https://hackmd.io/_uploads/r1O-pKIYMx.png)

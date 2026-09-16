---
title: TP 2.1 - Déploiement OSPF complet avec interfaces passives - Romain Jaquet

---

# TP 2.1 - Déploiement OSPF complet avec interfaces passives - Romain Jaquet

nom du lab : TP 1-4 Bonus_1789458517116
## Lab complet : 

![01 - lab complet](https://hackmd.io/_uploads/HJSIHKLKMg.png)

## R1 : 

```
conf t
router ospf 1
passive-interface fa1/0
```

## Commandes pour la vérification :

### show ip ospf interface brief 

Sur R1 : 
![02 - show ip ospf interface brief](https://hackmd.io/_uploads/Sy69VtUtGe.png)

### show ip protocols | section Passive

Sur R1 : 
![03 - show ip protocols section Passive](https://hackmd.io/_uploads/SkECEt8tGx.png)

### show ip route ospf

Sur R2 : 
![04 - show ip route ospf](https://hackmd.io/_uploads/r1aVHF8Fzg.png)

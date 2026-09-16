---
title: TP 2.1 - Déploiement OSPF complet avec interfaces passives - Romain Jaquet

---

# TP 2.1 - Déploiement OSPF complet avec interfaces passives - Romain Jaquet

nom du lab : TP 1-4 Bonus_1789458517116
## Lab complet : 

<img width="3108" height="1692" alt="01 - lab complet" src="https://github.com/user-attachments/assets/3734484a-1594-423e-bb4d-a65e87d2f60a" />

## R1 : 

```
conf t
router ospf 1
passive-interface fa1/0
```

## Commandes pour la vérification :

### show ip ospf interface brief 

Sur R1 : 
<img width="1224" height="196" alt="02 - show ip ospf interface brief" src="https://github.com/user-attachments/assets/766c5c00-feaa-4d05-83cf-ebaa26e07ad9" />

### show ip protocols | section Passive

Sur R1 : 
<img width="1232" height="170" alt="03 - show ip protocols section Passive" src="https://github.com/user-attachments/assets/3fae6dcd-b3cc-45d7-abad-64034eb6ecdc" />

### show ip route ospf

Sur R2 : 
<img width="1224" height="540" alt="04 - show ip route ospf" src="https://github.com/user-attachments/assets/22dc82e1-cd16-4878-98ab-868f27e5e214" />

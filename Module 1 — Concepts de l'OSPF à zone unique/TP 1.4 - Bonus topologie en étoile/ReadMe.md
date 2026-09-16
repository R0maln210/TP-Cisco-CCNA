---
title: TP 1.4 - Schéma en étoile (BONUS) - Romain Jaquet

---

# TP 1.4 - Schéma en étoile (BONUS) - Romain Jaquet

## Lab complet : 

## R1 : 

```
# On change l'adresse IP ainsi que le masque de sous réseau : 
conf t
interface fa0/0
ip add 192.168.1.1 255.255.255.0

# On modifie les networks : 
conf t
router ospf 1
network 192.168.1.0 0.0.0.255 area 0
network 1.1.1.1 0.0.0.0 area 0
```

## R2 : 

```
# On change l'adresse IP ainsi que le masque de sous réseau :
conf t
interface fa0/0
ip add 192.168.1.1 255.255.255.0

# On modifie les networks : 
conf t
router ospf 1
network 192.168.1.0 0.0.0.255 area 0
network 1.1.1.1 0.0.0.0 area 0
```

## R3 : 

```
# On change l'adresse IP ainsi que le masque de sous réseau :
conf t
interface fa0/0
ip add 192.168.1.1 255.255.255.0

# On modifie les networks : 
conf t
router ospf 1
network 192.168.1.0 0.0.0.255 area 0
network 1.1.1.1 0.0.0.0 area 0
```

## Commandes pour la vérification : 

### show ip interface brief : 

![show ip interface brief](https://hackmd.io/_uploads/H1RnPuIYMx.png)

### ping + show ip ospf neighbor

![ping + show ip ospf neighbor](https://hackmd.io/_uploads/r1CAP_UtMg.png)

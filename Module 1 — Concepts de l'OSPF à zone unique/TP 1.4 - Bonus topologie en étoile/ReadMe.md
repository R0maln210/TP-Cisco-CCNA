---
title: TP 1.4 - Schéma en étoile (BONUS) - Romain Jaquet

---

# TP 1.4 - Schéma en étoile (BONUS) - Romain Jaquet

## Lab complet : 

<img width="3098" height="1668" alt="01 - lab en entier" src="https://github.com/user-attachments/assets/911de3a5-6a9e-4411-a183-6713b8486737" />

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

<img width="2476" height="1658" alt="02 - show ip interface brief" src="https://github.com/user-attachments/assets/af73c5ec-61dc-491c-a888-efd2e062100d" />

### ping + show ip ospf neighbor

<img width="2480" height="1658" alt="03 - ping + show ip ospf neighbor" src="https://github.com/user-attachments/assets/1b6f7847-9a2e-4fd0-8ad0-76f5d0e5b8d2" />

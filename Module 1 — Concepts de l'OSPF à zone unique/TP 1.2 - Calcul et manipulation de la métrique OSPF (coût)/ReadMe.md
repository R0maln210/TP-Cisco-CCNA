# TP 1.2 - Calcul et manipulation de la métrique OSPF (coût) - Romain Jaquet

## Lab Complet

<img width="1448" height="678" alt="01 - Lab en entier" src="https://github.com/user-attachments/assets/9bf371a3-8eb5-4609-8640-471630589cfa" />

## R1 : 

```
en
conf t

# On change le coût de l'interface fa0/0
interface fa0/0
bandwidth 10000
exit

# On définit la métrique par défaut de l'ospf 1 du routeur
router ospf 1 
auto-cost reference-bandwidth 1000
exit
```

## Commandes pour la vérification : 

```
R1# show ip ospf interface fa0/0 | include Cost
R1# show ip route ospf
R3# traceroute 1.1.1.1
```

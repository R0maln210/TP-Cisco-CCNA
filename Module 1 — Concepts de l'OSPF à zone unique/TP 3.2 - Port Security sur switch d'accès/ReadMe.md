---
title: TP 3.2 - Port Security sur switch d'accès - Romain Jaquet

---

# TP 3.2 - Port Security sur switch d'accès - Romain Jaquet

## Lab complet : 

![01 - lab complet](https://hackmd.io/_uploads/ry-zKAPFzg.png)

## R1 : 

```
conf t
hostname R1

interface fa0/0
ip add 192.168.10.1 255.255.255.0
duplex half
no shutdown
exit
```

## SW1 : 

```
conf t
interface fa1/0
switchport mode access
switchport port-security
switchport port-security maximum 1
switchport port-security mac-address sticky
switchport port-security violation shutdown
exit
```

# PC Etudiant : 

```
set pcname PC_ETU
ip 192.168.10.10/24 192.168.10.1
```

## Commandes pour la vérification : 

### show port-security interface e0/0
### show port-security address
Sur SW1 : 

Pour pouvoir voir un chiffre dans "Total MAC Addresses", il faut que le PC ait envoyé au moins un paquet vers le switch, pour cela il suffit de faire un ping vers la passerelle.

![02 - commande pour la vérification](https://hackmd.io/_uploads/BJLGKCwYfe.png)

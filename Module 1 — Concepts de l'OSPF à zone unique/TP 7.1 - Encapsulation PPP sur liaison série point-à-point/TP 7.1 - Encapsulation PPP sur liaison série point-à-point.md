---
title: TP 7.1 - Encapsulation PPP sur liaison série point-à-point

---

# TP 7.1 - Encapsulation PPP sur liaison série point-à-point

## Lab complet : 

![01 - lab complet](https://hackmd.io/_uploads/H1x4pU0Yfe.png)

## R1-SIEGE : 

```
en
conf t
interface s5/0
encapsulation ppp
ip add 172.168.1.1 255.255.255.255.252
no shutdown
exit
do wr
```

## R2-AGENCE : 

```
en
conf t
interface s5/0
encapsulation ppp
ip add 172.168.1.2 255.255.255.252
no shutdown
exit
```

## Commandes pour la vérification : 

### show interface s5/0

![02 - show interface](https://hackmd.io/_uploads/BkaY6UAKfl.png)

### show ppp all

![03 - show ppp all](https://hackmd.io/_uploads/SJYyCICtfg.png)
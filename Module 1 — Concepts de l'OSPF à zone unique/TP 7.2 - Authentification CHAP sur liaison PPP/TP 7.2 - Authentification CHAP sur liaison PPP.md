---
title: TP 7.2 - Authentification CHAP sur liaison PPP

---

# TP 7.2 - Authentification CHAP sur liaison PPP

## Lab complet : 

![01 - lab complet](https://hackmd.io/_uploads/SyhG7D0Kfg.png)

## R1 : 

```
en
conf t
hostname R1
username R2 password Ppp-Satom-2026

interface s5/0
encapsulation ppp
ppp authentication chap
exit
do wr
```

## R2 : 

```
en
conf t
hostname R2
username R1 password Ppp-Satom-2026

interface s5/0
encapsulation ppp
ppp authentication chap
exit
do wr
```

## Commandes pour la vérification : 

### debug ppp authentication
### show ppp all

![02 - show ppp all](https://hackmd.io/_uploads/rkdEQw0Yzg.png)


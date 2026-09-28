---
title: TP 7.2 - Authentification CHAP sur liaison PPP

---

# TP 7.2 - Authentification CHAP sur liaison PPP

## Lab complet : 

<img width="578" height="214" alt="01 - lab complet" src="https://github.com/user-attachments/assets/927c890e-5156-44a8-8e78-2121bc123e0e" />

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

<img width="2468" height="284" alt="02 - show ppp all" src="https://github.com/user-attachments/assets/15fc7662-e7de-49da-b8f9-7cc7cdd3c532" />

---
title: TP 7.1 - Encapsulation PPP sur liaison série point-à-point

---

# TP 7.1 - Encapsulation PPP sur liaison série point-à-point

## Lab complet : 

<img width="596" height="238" alt="01 - lab complet" src="https://github.com/user-attachments/assets/6f2ea3d6-8ff3-4373-85bd-6e91a4c75fd7" />

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

<img width="2468" height="958" alt="02 - show interface" src="https://github.com/user-attachments/assets/bfc3e1ec-80f3-435a-b0e1-62912b8b3ac6" />

### show ppp all

<img width="2472" height="222" alt="03 - show ppp all" src="https://github.com/user-attachments/assets/d5b556b0-7cc9-4bff-93ce-6373ae4802b6" />

---
title: TP 9.2 - File d'attente prioritaire LLQ pour la voix

---

# TP 9.2 - File d'attente prioritaire LLQ pour la voix

## Lab complet : 

![01 - lab complet](https://hackmd.io/_uploads/r1tdS2k5zg.png)

## R1 : 

```
en
conf t

policy-map QOS-WAN
class VOIX-VIDEO
priority percent 30
exit

class DONNEES-CRITIQUES
bandwidth percent 40
exit

class class-default
fair-queue
exit

interface fa0/0
service-policy output QOS-WAN
```

## R2 : 

```
en
conf t
hostname R2

interface fa0/0
ip add 203.0.113.2 255.255.255.252
no shutdown
bandwidth 2000
exit

do wr
```

## Commandes pour la vérification : 

### show policy-map interface fa0/0

![02 - show policy.map interface](https://hackmd.io/_uploads/HkL5rhJcGg.png)

---
title: TP 9.2 - File d'attente prioritaire LLQ pour la voix

---

# TP 9.2 - File d'attente prioritaire LLQ pour la voix

## Lab complet : 

<img width="1848" height="1218" alt="01 - lab complet" src="https://github.com/user-attachments/assets/c52a4416-266f-49b1-b64b-bc74ea744908" />

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

<img width="1234" height="1404" alt="02 - show policy map interface" src="https://github.com/user-attachments/assets/09b08881-746f-4a6d-a688-9a34333dd732" />

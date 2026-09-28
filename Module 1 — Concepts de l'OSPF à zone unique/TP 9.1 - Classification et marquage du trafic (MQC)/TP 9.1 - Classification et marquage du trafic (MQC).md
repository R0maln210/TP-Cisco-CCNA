---
title: TP 9.1 - Classification et marquage du trafic (MQC)

---

# TP 9.1 - Classification et marquage du trafic (MQC)

## Lab complet : 

![image](https://hackmd.io/_uploads/H1DQg219fx.png)

## R1 : 

```
en
conf t
hostname R1

class-map match-any VOIX-VIDEO
match protocol rtp
exit

class-map match-any DONNEES-CRITIQUES
match protocol http
exit

policy-map MARQUAGE-CAMPUS
class VOIX-VIDEO
set dscp ef
exit

class DONNEES-CRITIQUES
set dscp af21
exit

class class-default
set dscp default
exit
exit

interface fa1/0
ip add 192.168.10.254 255.255.255.0
no shutdown
service-policy input MARQUAGE-CAMPUS
exit

interface fa2/0
ip add 192.168.20.254 255.255.255.0
no shutdown
service-policy input MARQUAGE-CAMPUS
exit

interface fa3/0
ip add 192.168.30.254 255.255.255.0
no shutdown
service-policy input MARQUAGE-CAMPUS
exit

do wr
```

## PC-FLUX :

```
set pcname PC-FLU
ip 192.168.10.1/24 192.168.10.254
save
```

## Commandes pour la vérification : 

### show policy-map interface fa1/0

![02 - show policy map interface](https://hackmd.io/_uploads/H16cl315fl.png)

### ![03 - show class-map](https://hackmd.io/_uploads/BkEox2JqMg.png)
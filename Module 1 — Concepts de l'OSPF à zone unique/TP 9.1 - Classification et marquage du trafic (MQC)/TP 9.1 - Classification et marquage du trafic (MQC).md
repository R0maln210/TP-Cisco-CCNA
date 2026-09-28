---
title: TP 9.1 - Classification et marquage du trafic (MQC)

---

# TP 9.1 - Classification et marquage du trafic (MQC)

## Lab complet : 

<img width="1878" height="1024" alt="01 - lab complet" src="https://github.com/user-attachments/assets/58af0950-9c80-4451-a9b4-b868c41eb807" />

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

<img width="1236" height="1084" alt="02 - show policy map interface" src="https://github.com/user-attachments/assets/d69b58cc-e8de-4255-b168-fbcc5548b164" />

### show class-map

<img width="1234" height="354" alt="03 - show class-map" src="https://github.com/user-attachments/assets/889657fb-dbe7-44b3-ae9f-c6f150303f3c" />

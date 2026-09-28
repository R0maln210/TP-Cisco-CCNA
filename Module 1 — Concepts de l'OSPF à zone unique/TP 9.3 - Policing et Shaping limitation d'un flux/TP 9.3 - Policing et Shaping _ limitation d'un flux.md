---
title: 'TP 9.3 - Policing et Shaping : limitation d''un flux'

---

# TP 9.3 - Policing et Shaping : limitation d'un flux

## Lab complet : 

<img width="1848" height="1218" alt="01 - lab complet" src="https://github.com/user-attachments/assets/aef53db4-80a3-40d7-a8de-0931480e5919" />

## R1 : 

```
conf t
class-map match-any SAUVEGARDE
match protocol smb
exit

policy-map LIMITATION-BACKUP
class SAUVEGARDE
police 512000 8000 exceed-action drop
exit

interface fa3/0
service-policy input LIMITATION-BACKUP
```

## Commandes pour la vérification : 

### show policy-map interface fa3/0

<img width="1232" height="1116" alt="02 - policy-map interface" src="https://github.com/user-attachments/assets/da9815dc-4da6-44cb-bf5b-d13c67371a3f" />

---
title: 'TP 9.3 - Policing et Shaping : limitation d''un flux'

---

# TP 9.3 - Policing et Shaping : limitation d'un flux

## Lab complet : 

![01 - lab complet](https://hackmd.io/_uploads/S11wth15Ge.png)

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

![02 - policy-map interface](https://hackmd.io/_uploads/Bkg_cny5fl.png)
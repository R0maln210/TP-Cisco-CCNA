---
title: TP 5.3 - Dépannage d'une ACL existante mal appliquée

---

# TP 5.3 - Dépannage d'une ACL existante mal appliquée


## Correction : 
```
interface g0/0
 no ip access-group 101 out
 ip access-group 101 in
 exit
```
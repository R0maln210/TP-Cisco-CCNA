---
title: TP 4.1 - Atelier de calcul de wildcard mask - Romain Jaquet

---

# TP 4.1 - Atelier de calcul de wildcard mask - Romain Jaquet

| Cible à filtrer | Masque réseau | Wildcard mask attendu |
| -------- | -------- | -------- |
| 192.168.10.0/24     | 255.255.255.0     | 0.0.0.255     |
| 192.168.20.0/26     | 255.255.255.192     | 0.0.0.63     |
| 10.0.0.0/16     | 255.255.0.0     | 0.0.255.255     |
| 192.168.30.5     | 255.255.255.255     | 0.0.0.0     |
| Toute adresse (any)     | -     | 255.255.255.255     |
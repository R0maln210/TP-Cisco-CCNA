---
title: TP 7.3 - Étude de cas comparative  choix d'une technologie WAN

---

# TP 7.3 - Étude de cas comparative  choix d'une technologie WAN

## Lab complet : 

## 1. Grille de comparaison

| Critère | Ligne louée dédiée | MPLS | VPN IPSec sur Internet |
| -------- | -------- | -------- | --- |
| Coût mensuel | Élevé | Moyen-élevé | Faible |
| Bande passante garantie (LSA) | Oui | Oui | Non (best-effort) |
| Sécurité intrinsèque | Élevée (lien privé) | Moyenne (opérateur) | Dépend du chiffrement configuré |
| Scabilité multi-sites | Faible (point-à-point) | Élevée (any-to-any) | Élevée |

## 2. Recommandation

Pour le campus de Renens, le choix dépend du compromis entre le budget et la criticité des accès pédagogiques en temps réel. Un MPLS est idéal pour garantir la qualité de service (QoS) des plateformes de cours, mais un VPN IPSec sur une fibre Internet redondante offre un excellent compromis coût/performance pour un déploiement rapide et sécurisé.

## 3. Justification si une solution hybride serait pertinente

Une solution hybride combinant MPLS en lien principal et VPN IPSec sur Internet en secours est fortement pertinente pour plusieurs raisons :

- Continuité pédagogique : Elle garantit une haute disponibilité (HA) transparente pour les étudiants et enseignants en cas de coupure de la ligne principale.

- Optimisation des coûts : Au lieu de payer deux lignes MPLS très onéreuses, le lien Internet de secours est nettement moins cher.

- Sécurité renforcée : Le trafic de secours bascule automatiquement sur un tunnel chiffré IPsec, maintenant un niveau de sécurité élevé même sur le réseau public.
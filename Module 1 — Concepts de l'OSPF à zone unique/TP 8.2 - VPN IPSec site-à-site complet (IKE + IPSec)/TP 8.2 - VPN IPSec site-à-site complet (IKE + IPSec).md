---
title: TP 8.2 - VPN IPSec site-à-site complet (IKE + IPSec)

---

# TP 8.2 - VPN IPSec site-à-site complet (IKE + IPSec)

## Lab complet : 

<img width="1204" height="286" alt="01 - lab complet" src="https://github.com/user-attachments/assets/51a3d0c0-b0e9-4f64-bcd6-50c42213e1f3" />

## R1 : 

```
en
conf t

interface fa1/0
ip add 192.168.10.254 255.255.255.0
no shutdown
exit

crypto isakmp policy 10
encryption aes 256
hash sha256
authentication pre-share
group 14
exit

crypto isakmp key VpnSatom2026! address 198.51.100.1

crypto ipsec transform-set TS-SATOM esp-aes 256 esp-sha256-hmac

access-list 100 permit ip 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255

crypto map CMAP-SATOM 10 ipsec-isakmp
set peer 198.51.100.1
set transform-set TS-SATOM
match address 100
exit

interface fa0/0
crypto map CMAP-SATOM
```

## R2 : 

```
en
conf t

interface fa1/0
ip add 192.168.20.254 255.255.255.0
no shutdown
exit

crypto isakmp policy 10
encryption aes 256
hash sha256
authentication pre-share
group 14
exit

crypto isakmp key VpnSatom2026! address 203.0.113.1

crypto ipsec transform-set TS-SATOM esp-aes 256 esp-sha256-hmac

access-list 100 permit ip 192.168.20.0 0.0.0.255 192.168.10.0 0.0.0.255

crypto map CMAP-SATOM 10 ipsec-isakmp
set peer 203.0.113.1
set transform-set TS-SATOM
match address 100
exit

interface fa0/0
crypto map CMAP-SATOM
```

## PC-LAN-SIEGE : 

```
set pcname PC-SGE
ip 192.168.10.10/24 192.168.10.254
```

## PC-LAN-AGENCE : 

```
set pcname PC-AGC
ip 192.168.20.20/24 192.168.20.254
```

## Commandes pour la vérification : 

### show crypto isakmp sa

<img width="1234" height="254" alt="02 - show crypto isakmp sa" src="https://github.com/user-attachments/assets/beafaf22-c556-4249-8255-146af9e62449" />

### show crypto ipsec sa

<img width="1220" height="1694" alt="03 - show crypto ipsec sa" src="https://github.com/user-attachments/assets/396d4a02-65a1-4f48-90a9-88fdb6510b43" />

### show crypto map

<img width="1236" height="584" alt="04 - show crypto map" src="https://github.com/user-attachments/assets/4f12e02f-54b5-4800-b201-f2283957385a" />

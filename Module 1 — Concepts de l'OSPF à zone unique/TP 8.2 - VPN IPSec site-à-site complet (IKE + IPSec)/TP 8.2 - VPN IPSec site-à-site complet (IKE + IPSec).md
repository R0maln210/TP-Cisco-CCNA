---
title: TP 8.2 - VPN IPSec site-à-site complet (IKE + IPSec)

---

# TP 8.2 - VPN IPSec site-à-site complet (IKE + IPSec)

## Lab complet : 

![01 - lab complet](https://hackmd.io/_uploads/H1ua7sJqMe.png)

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

![02 - show crypto isakmp sa](https://hackmd.io/_uploads/H1NdVoycze.png)

### show crypto ipsec sa

![03 - show crypto ipsec sa](https://hackmd.io/_uploads/H1ZKEjJqGg.png)

### show crypto map

![04 - show crypto map](https://hackmd.io/_uploads/HkscViJ9zx.png)
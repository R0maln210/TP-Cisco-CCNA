---
title: TP 8.1 - Tunnel GRE simple (sans chiffrement)

---

# TP 8.1 - Tunnel GRE simple (sans chiffrement)

![01 - lab complet](https://hackmd.io/_uploads/Hy7ID50tGx.png)

## R1 : 

```
en
conf t
hostname R1 

interface tunnel 0
ip add 192.168.100.1 255.255.255.252
tunnel source fa0/0
tunnel destination 198.51.100.1
tunnel mode gre ip
exit

interface fa0/0
ip add 203.0.113.1 255.255.255.0
no shutdown
exit

ip route 0.0.0.0 0.0.0.0 FastEthernet0/0
exit

wr
```

## R2 : 

```
en 
conf t
hostname R2

interface tunnel 0 

ip add 192.168.100.2 255.255.255.252
tunnel source fa0/0
tunnel destination 203.0.113.1
tunnel mode gre ip 
exit

interface fa0/0
ip add 198.51.100.1 255.255.255.0
no shutdown
exit

ip route 0.0.0.0 0.0.0.0 FastEthernet0/0
exit

wr
```

## Commandes pour la vérification : 

### show interfaces tunnel 0

![02 - show interfaces tunnel 0](https://hackmd.io/_uploads/rJ9RPcCYGl.png)

### ping 

![03 - ping](https://hackmd.io/_uploads/r1mxdcAtfe.png)
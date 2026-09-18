---
title: TP Final CCNA - Romain Jaquet

---

# TP Final CCNA - Romain Jaquet

## Lab complet : 

![01 - lab complet](https://hackmd.io/_uploads/Bk1S5wcYMl.png)

## Phase 1 : Routage dynamique OSPF

### R-EDGE : 

```
en
conf t
hostname R-EDGE

interface fa0/0
ip add 203.0.113.2 255.255.255.252
no shutdown
exit

interface fa1/0
ip add 10.0.12.1 255.255.255.252
no shutdown
exit

interface fa2/0
ip add 10.0.13.1 255.255.255.252
no shutdown
exit

interface loopback 0
ip address 1.1.1.1 255.255.255.255
exit

ip route 0.0.0.0 0.0.0.0 203.0.113.1

router ospf 1
router-id 1.1.1.1
network 10.0.12.0 0.0.0.3 area 0
network 10.0.13.0 0.0.0.3 area 0
network 1.1.1.1 0.0.0.0 area 0
default-information originate
exit

interface fa1/0
ip ospf message-digest-key 1 md5 pass123
ip ospf authentication message-digest
exit

interface fa2/0
ip ospf message-digest-key 1 md5 pass123
ip ospf authentication message-digest
exit

do wr
```

### R-FORMATION : 

```
en
conf t
hostname R-FORMATION

interface fa1/0
ip add 10.0.12.2 255.255.255.252
no shutdown
exit

interface fa0/0
no shutdown
exit

interface fa0/0.10
encapsulation dot1Q 10
ip add 192.168.10.1 255.255.255.0
no shutdown
exit

interface fa0/0.99
encapsulation dot1Q 99
ip add 192.168.99.1 255.255.255.0 
no shutdown
exit

interface loopback 0
ip address 2.2.2.2 255.255.255.255
exit

router ospf 1
router-id 2.2.2.2
network 10.0.12.0 0.0.0.3 area 0
network 192.168.10.0 0.0.0.255 area 0
network 192.168.99.0 0.0.0.255 area 0
network 2.2.2.2 0.0.0.0 area 0
passive-interface fa0/0.10
passive-interface fa0/0.99
exit

interface fa1/0
ip ospf message-digest-key 1 md5 pass123
ip ospf authentication message-digest
exit

do wr
```

### R-ADMIN : 

```
en
conf t
hostname R-ADMIN

interface fa0/0
ip add 192.168.20.1 255.255.255.0
no shutdown
exit

interface fa1/0
ip add 10.0.0.1 255.255.255.0
no shutdown
exit

interface fa2/0
ip add 10.0.13.2 255.255.255.252
no shutdown
exit

interface loopback 0
ip address 3.3.3.3 255.255.255.255
exit

router ospf 1
router-id 3.3.3.3
network 10.0.13.0 0.0.0.3 area 0
network 192.168.20.0 0.0.0.255 area 0
network 10.0.0.0 0.0.0.255 area 0
network 3.3.3.3 0.0.0.0 area 0
passive-interface fa0/0
passive-interface fa1/0
exit

interface fa2/0
ip ospf message-digest-key 1 md5 pass123
ip ospf authentication message-digest
exit

do wr
```

### SERVER-WEB-PAIE : 

```
en
conf t
hostname SERVER-WEB-PAIE

no ip routing

interface e0/0
no switchport 
ip address 10.0.0.50 255.255.255.0
no shutdown
exit

ip default-gateway 10.0.0.1

do wr
```

### SW-FORMATION : 

```
en
conf t
hostname SW-FORMATION

vlan 10
name FORMATION
exit

vlan 99
name INVITES
exit

interface e0/0
switchport trunk encapsulation dot1q
switchport mode trunk
no shutdown
exit

interface e0/1
switchport mode access
switchport access vlan 10
no shutdown
exit

interface e0/2
switchport mode access
switchport access vlan 99
no shutdown
exit

do wr
```

### PC-ADMINISTRATION : 

```
ip 192.168.20.10/24 192.168.20.1
set pcname PC-ADM
save
```

### PC-INFO : 

```
ip 192.168.10.10/24 192.168.10.1
set pcname PC-INF
save
```

### PC-INVITES : 

```
ip 192.168.99.10/24 192.168.99.1
set pcname PC-INV
save
```

---

### Commandes pour la vérification : 

### show ip ospf neighbor 
sur les 3 routeurs

![01 - show ip ospf neighbor](https://hackmd.io/_uploads/BkwTsP9YMl.png)

### show ip route ospf 
sur R-FORMATION et R-ADMIN

![02 - show ip route ospf](https://hackmd.io/_uploads/Syo1nwqYMe.png)

### show ip protocols | section Passive 
sur R-FORMATION --> fa0/0.10 et fa0/0.99, R-ADMIN --> fa0/0 et fa 1/0

![03 - show ip protocols section Passive](https://hackmd.io/_uploads/S1zehP9Kzx.png)

### show ip ospf interface fax/x | include authentication 
sur R-EDGE --> fa1/0 et fa2/0, R-FORMATION --> fa1/0, R-ADMIN --> fa2/0

![04 - show interface include authentication](https://hackmd.io/_uploads/BJPx3w5tzl.png)

### ping 
entre PC-ADM et PC-INF

![05 - ping entre admin et info](https://hackmd.io/_uploads/S1Gb3PqKGe.png)

## Phase 2 : Sécurisation des accès et de la couche 2

### R-EDGE

```
conf t 

ip domain-name satom.local
username admin-tech privilege 15 secret Admin123

crypto key generate rsa modulus 2048
ip ssh version 2

line vty 0 4 
login local 
transport input ssh
exec-timeout 5 0
exit

do wr
```

### R-FORMATION

```
conf t 

ip domain-name satom.local
username admin-tech privilege 15 secret Admin123

crypto key generate rsa modulus 2048
ip ssh version 2

line vty 0 4 
login local 
transport input ssh
exec-timeout 5 0
exit

do wr
```

### R-ADMIN

```
conf t 

ip domain-name satom.local
username admin-tech privilege 15 secret Admin123

crypto key generate rsa modulus 2048
ip ssh version 2

line vty 0 4 
login local 
transport input ssh
exec-timeout 5 0
exit

do wr
```

### SW-FORMATION : 

```
conf t

interface e0/1
switchport mode access
switchport access vlan 10
switchport port-security
switchport port-security maximum 1
switchport port-security violation shutdown
switchport port-security mac-address sticky
no shutdown
exit

ip dhcp snooping
ip dhcp snooping vlan 10
no ip dhcp snooping information option

interface e0/0
ip dhcp snooping trust
exit

do wr
```

---

### Commandes pour la vérification : 

### show ip ssh
sur les 3 routeurs

![01 - show ip ssh](https://hackmd.io/_uploads/Syl8pO9Kzl.png)

### show running-config | section line vty
sur les 3 routeurs

![02 - show running config section line vty](https://hackmd.io/_uploads/HyLUaOcKGx.png)

### show port-security interface e0/x
sur sw-formation sur les interface e0/0 et e0/1

![03 - show port security interface](https://hackmd.io/_uploads/SkoIa_qKfe.png)

### show ip dhcp snooping
sur sw-formation

![04 - show ip dhcp snooping](https://hackmd.io/_uploads/rkZD6u9KMx.png)

## Phase 3 : Filtrage réseau par ACL

### R-EDGE : 

```
conf t

ip access-list standard ADMIN-ONLY-SSH
permit host 192.168.20.10
deny any log
exit

line vty 0 4
access-class ADMIN-ONLY-SSH in
exit

do wr
```

### R-FORMATION : 

```
conf t

ip access-list standard ADMIN-ONLY-SSH
permit host 192.168.20.10
deny any log
exit

line vty 0 4
access-class ADMIN-ONLY-SSH in
exit

ip access-list extended INVITES-RESTRICTIONS
deny ip 192.168.99.0 0.0.0.255 host 10.0.0.50
permit udp 192.168.99.0 0.0.0.255 any eq domain
permit tcp 192.168.99.0 0.0.0.255 any eq domain
permit tcp 192.168.99.0 0.0.0.255 any eq www
permit tcp 192.168.99.0 0.0.0.255 any eq 443
deny ip 192.168.99.0 0.0.0.255 any log
exit

interface fa0/0.99
ip access-group INVITES-RESTRICTIONS in
exit

do wr
```

### R-ADMIN : 

```
conf t

ip access-list standard ADMIN-ONLY-SSH
permit host 192.168.20.10
deny any log
exit

line vty 0 4
access-class ADMIN-ONLY-SSH in
exit

do wr
```

---

### Commandes pour la vérification : 

### ssh -l admin-tech 192.168.10.1
sur PC-INF
--> la commande ne fonctionne pas sur les VPC de PnetLab

### ping 10.0.0.50
sur PC-INV

![01 - ping depuis pc inv](https://hackmd.io/_uploads/rywU8YqKGl.png)

### show ip access-lists
sur R-FORMATION

![02 - show ip access-lists](https://hackmd.io/_uploads/S1pU8t9Fzx.png)

### Explication écrite du diagnostic et de la correction de l'ACL RDP mal placée 

```
access-list 101 deny tcp any host 10.0.0.50 eq 3389
access-list 101 permit ip any any
! appliquée par erreur sur l'interface qui fait sortir le trafic vers le serveur, dans le mauvais sens
```

L'analyse a révélé que l'ACL étendue 101, censée bloquer le flux RDP vers le 10.0.0.50, n'était pas opérationnelle. Le compteur de correspondances restant à zéro lors des tests avec show ip access-lists, la règle était appliquée dans le mauvais sens ou sur la mauvaise interface.

Sans modifier le contenu de l'ACL, son point d'application a été corrigé en la déplaçant au plus près de la source du trafic. Les tentatives de connexion RDP ont été immédiatement bloquées, ce qui a été validé par l'incrémentation des compteurs de rejet sur le routeur.

## Phase 4 : Connectivité Internet et NAT

### R-EDGE : 

```
ip nat inside source static 10.0.0.50 203.0.113.10

ip access-list standard PAT-NETWORKS
permit 192.168.0.0 0.0.255.255
permit 10.0.0.0 0.255.255.255
exit

ip nat inside source list PAT-NETWORKS interface fa0/0 overload

interface fa1/0
ip nat inside
exit

interface fa2/0
ip nat inside
exit

interface fa0/0
ip nat outside
exit

do wr
```

### Commandes pour la vérification : 

### show ip nat translations
--> on ne voit que le static parce que tout le dynamique ne fonctionne pas depuis n'importe quel appareil

![01 - show ip nat translation](https://hackmd.io/_uploads/SyGR_s5FMl.png)

### show ip nat statistics
--> pareil que pour la commande précédente

![02 - show ip nat statistics](https://hackmd.io/_uploads/ByLJFicYze.png)

## Phase 5 : Audit final, incident imposé et documentation (transversal)

### Incident injecté au sein de ma configuration

<b>Type d'incident :</b> Perte de configuration après un redémarrage non sauvegardé

<b>Diagnostic :</b> Au redémarrage de la machine, lorsque nous avons tapé "show running-config" le routeur R-EDGE ne comportait pas les dernières règles de NAT et de sécurité des ports.

<b>Commandes de diagnostic utilisées :</b>

```
show running-config
show startup-config
```

<b>Solution :</b>Il faut remettre les commandes NAT et de sécurité des ports et ensuite bien penser à taper la commande wr.

### Sauvegarde de la configuration finale de chaque équipement et copie des configurations.

### show running-config

### R-EDGE : 

```
R-EDGE#show running-config
Building configuration...

Current configuration : 2844 bytes
!
! Last configuration change at 12:04:45 UTC Fri Sep 18 2026
upgrade fpd auto
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname R-EDGE
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
!
!
!
ip domain name satom.local
ip cef
no ipv6 cef
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
!
username admin-tech privilege 15 secret 5 $1$ScII$hw2g5JNmvN/uxtPB8PDd2/
!
redundancy
!
!
ip ssh version 2
!
!
!
!
!
!
!
!
!
!
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
!
interface FastEthernet0/0
 ip address 203.0.113.2 255.255.255.252
 ip nat outside
 ip virtual-reassembly in
 duplex half
!
interface FastEthernet1/0
 ip address 10.0.12.1 255.255.255.252
 ip nat inside
 ip virtual-reassembly in
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 pass123
 duplex half
!
interface FastEthernet2/0
 ip address 10.0.13.1 255.255.255.252
 ip nat inside
 ip virtual-reassembly in
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 pass123
 duplex half
!
interface FastEthernet3/0
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/0
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/1
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/2
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/3
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/4
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/5
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/6
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/7
 no ip address
 shutdown
 duplex half
!
interface Serial5/0
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/1
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/2
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/3
 no ip address
 shutdown
 serial restart-delay 0
!
router ospf 1
 router-id 1.1.1.1
 network 1.1.1.1 0.0.0.0 area 0
 network 10.0.12.0 0.0.0.3 area 0
 network 10.0.13.0 0.0.0.3 area 0
 default-information originate
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!
!
ip nat inside source list 1 interface FastEthernet0/0 overload
ip nat inside source list PAT-NETWORKS interface FastEthernet0/0 overload
ip nat inside source static 10.0.0.50 203.0.113.10
ip route 0.0.0.0 0.0.0.0 203.0.113.1
!
ip access-list standard ADMIN-ONLY-SSH
 permit 192.168.20.10
 deny   any log
ip access-list standard PAT-NETWORKS
 permit 192.168.0.0 0.0.255.255
 permit 10.0.0.0 0.255.255.255
!
access-list 1 permit any
!
!
!
control-plane
!
!
!
mgcp profile default
!
!
!
gatekeeper
 shutdown
!
!
line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 access-class ADMIN-ONLY-SSH in
 exec-timeout 5 0
 login local
 transport input ssh
!
!
end
```

### R-FORMATION : 

```
R-INFORMATION#show running-config
Building configuration...

Current configuration : 2814 bytes
!
! Last configuration change at 11:45:56 UTC Fri Sep 18 2026
upgrade fpd auto
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname R-INFORMATION
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
!
!
!
ip domain name satom.local
ip cef
no ipv6 cef
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
!
username admin-tech privilege 15 secret 5 $1$c4cz$jKi4tYHVn4c4jObAq.sXA.
!
redundancy
!
!
ip ssh version 2
!
!
!
!
!
!
!
!
!
!
interface FastEthernet0/0
 no ip address
 duplex half
!
interface FastEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
!
interface FastEthernet0/0.99
 encapsulation dot1Q 99
 ip address 192.168.99.1 255.255.255.0
 ip access-group INVITES-RESTRICTIONS in
!
interface FastEthernet1/0
 ip address 10.0.12.2 255.255.255.252
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 pass123
 duplex half
!
interface FastEthernet2/0
 no ip address
 shutdown
 duplex half
!
interface FastEthernet3/0
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/0
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/1
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/2
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/3
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/4
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/5
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/6
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/7
 no ip address
 shutdown
 duplex half
!
interface Serial5/0
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/1
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/2
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/3
 no ip address
 shutdown
 serial restart-delay 0
!
router ospf 1
 router-id 2.2.2.2
 passive-interface FastEthernet0/0.10
 passive-interface FastEthernet0/0.99
 network 10.0.12.0 0.0.0.3 area 0
 network 192.168.10.0 0.0.0.255 area 0
 network 192.168.99.0 0.0.0.255 area 0
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!
!
!
ip access-list standard ADMIN-ONLY-SSH
 permit 192.168.20.10
 deny   any log
!
ip access-list extended INVITES-RESTRICTIONS
 deny   ip 192.168.99.0 0.0.0.255 host 10.0.0.50
 permit udp 192.168.99.0 0.0.0.255 any eq domain
 permit tcp 192.168.99.0 0.0.0.255 any eq domain
 permit tcp 192.168.99.0 0.0.0.255 any eq www
 permit tcp 192.168.99.0 0.0.0.255 any eq 443
 deny   ip 192.168.99.0 0.0.0.255 any log
!
!
!
!
control-plane
!
!
!
mgcp profile default
!
!
!
gatekeeper
 shutdown
!
!
line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 access-class ADMIN-ONLY-SSH in
 exec-timeout 5 0
 login local
 transport input ssh
!
!
end
```

### R-ADMIN : 

```
R-ADMIN#show running-config
Building configuration...

Current configuration : 2367 bytes
!
! Last configuration change at 09:27:52 UTC Fri Sep 18 2026
upgrade fpd auto
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname R-ADMIN
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
!
!
!
ip domain name satom.local
ip cef
no ipv6 cef
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
!
username admin-tech privilege 15 secret 5 $1$Brzf$y834ri8uJR2OC.1JQN51V1
!
redundancy
!
!
ip ssh version 2
!
!
!
!
!
!
!
!
!
!
interface Loopback0
 ip address 3.3.3.3 255.255.255.255
!
interface FastEthernet0/0
 ip address 192.168.20.1 255.255.255.0
 duplex half
!
interface FastEthernet1/0
 ip address 10.0.0.1 255.255.255.252
 duplex half
!
interface FastEthernet2/0
 ip address 10.0.13.2 255.255.255.252
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 pass123
 duplex half
!
interface FastEthernet3/0
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/0
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/1
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/2
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/3
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/4
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/5
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/6
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/7
 no ip address
 shutdown
 duplex half
!
interface Serial5/0
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/1
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/2
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/3
 no ip address
 shutdown
 serial restart-delay 0
!
router ospf 1
 router-id 3.3.3.3
 passive-interface FastEthernet0/0
 passive-interface FastEthernet1/0
 network 3.3.3.3 0.0.0.0 area 0
 network 10.0.0.0 0.0.0.255 area 0
 network 10.0.13.0 0.0.0.3 area 0
 network 192.168.20.0 0.0.0.255 area 0
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!
!
!
ip access-list standard ADMIN-ONLY-SSH
 permit 192.168.20.10
 deny   any log
!
!
!
!
control-plane
!
!
!
mgcp profile default
!
!
!
gatekeeper
 shutdown
!
!
line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 access-class ADMIN-ONLY-SSH in
 exec-timeout 5 0
 login local
 transport input ssh
!
!
end
```

### SW-FORMATION : 

```
SW-FORMATION#show running-config
Building configuration...

Current configuration : 1131 bytes
!
! Last configuration change at 09:05:44 UTC Fri Sep 18 2026
!
version 15.1
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname SW-FORMATION
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
no ipv6 cef
ipv6 multicast rpf use-bgp
!
ip cef
!
!
ip dhcp snooping vlan 10
no ip dhcp snooping information option
ip dhcp snooping
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
!
!
!
vlan internal allocation policy ascending
!
!
!
!
!
!
!
!
!
!
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
 duplex auto
 ip dhcp snooping trust
!
interface Ethernet0/1
 switchport access vlan 10
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky
 switchport port-security mac-address sticky 0050.7966.681f
 duplex auto
!
interface Ethernet0/2
 switchport access vlan 99
 switchport mode access
 duplex auto
!
interface Ethernet0/3
 duplex auto
!
!
no ip http server
!
!
!
!
!
control-plane
!
!
line con 0
 logging synchronous
line aux 0
line vty 0 4
!
end
```

### SW-ADMIN : 

```
SW-ADMIN#show running-config
Building configuration...

Current configuration : 728 bytes
!
! Last configuration change at 12:30:33 UTC Fri Sep 18 2026
!
version 15.1
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname SW-ADMIN
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
no ipv6 cef
ipv6 multicast rpf use-bgp
!
ip cef
!
!
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
!
!
!
vlan internal allocation policy ascending
!
!
!
!
!
!
!
!
!
!
interface Ethernet0/0
 duplex auto
!
interface Ethernet0/1
 duplex auto
!
interface Ethernet0/2
 duplex auto
!
interface Ethernet0/3
 duplex auto
!
!
no ip http server
!
!
!
!
!
control-plane
!
!
line con 0
 logging synchronous
line aux 0
line vty 0 4
!
end
```

### SERVER-WEB-PAIE : 

```
SERVER-WEB-PAIE#show running-config
Building configuration...

Current configuration : 825 bytes
!
! Last configuration change at 06:45:55 UTC Fri Sep 18 2026
!
version 15.1
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname SERVER-WEB-PAIE
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
no ipv6 cef
ipv6 multicast rpf use-bgp
no ip routing
!
no ip cef
!
!
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
!
!
!
vlan internal allocation policy ascending
!
!
!
!
!
!
!
!
!
!
interface Ethernet0/0
 no switchport
 ip address 10.0.0.50 255.255.255.0
!
interface Ethernet0/1
 duplex auto
!
interface Ethernet0/2
 duplex auto
!
interface Ethernet0/3
 duplex auto
!
ip default-gateway 10.0.0.1
!
no ip http server
!
!
!
!
!
control-plane
!
!
line con 0
 logging synchronous
line aux 0
line vty 0 4
 login
!
end
```

### show startup-config ; 

R-EDGE : 

```
R-EDGE#show startup-config
Using 2844 out of 129016 bytes
!
! Last configuration change at 12:04:45 UTC Fri Sep 18 2026
upgrade fpd auto
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname R-EDGE
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
!
!
!
ip domain name satom.local
ip cef
no ipv6 cef
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
!
username admin-tech privilege 15 secret 5 $1$ScII$hw2g5JNmvN/uxtPB8PDd2/
!
redundancy
!
!
ip ssh version 2
!
!
!
!
!
!
!
!
!
!
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
!
interface FastEthernet0/0
 ip address 203.0.113.2 255.255.255.252
 ip nat outside
 ip virtual-reassembly in
 duplex half
!
interface FastEthernet1/0
 ip address 10.0.12.1 255.255.255.252
 ip nat inside
 ip virtual-reassembly in
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 pass123
 duplex half
!
interface FastEthernet2/0
 ip address 10.0.13.1 255.255.255.252
 ip nat inside
 ip virtual-reassembly in
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 pass123
 duplex half
!
interface FastEthernet3/0
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/0
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/1
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/2
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/3
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/4
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/5
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/6
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/7
 no ip address
 shutdown
 duplex half
!
interface Serial5/0
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/1
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/2
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/3
 no ip address
 shutdown
 serial restart-delay 0
!
router ospf 1
 router-id 1.1.1.1
 network 1.1.1.1 0.0.0.0 area 0
 network 10.0.12.0 0.0.0.3 area 0
 network 10.0.13.0 0.0.0.3 area 0
 default-information originate
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!
!
ip nat inside source list 1 interface FastEthernet0/0 overload
ip nat inside source list PAT-NETWORKS interface FastEthernet0/0 overload
ip nat inside source static 10.0.0.50 203.0.113.10
ip route 0.0.0.0 0.0.0.0 203.0.113.1
!
ip access-list standard ADMIN-ONLY-SSH
 permit 192.168.20.10
 deny   any log
ip access-list standard PAT-NETWORKS
 permit 192.168.0.0 0.0.255.255
 permit 10.0.0.0 0.255.255.255
!
access-list 1 permit any
!
!
!
control-plane
!
!
!
mgcp profile default
!
!
!
gatekeeper
 shutdown
!
!
line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 access-class ADMIN-ONLY-SSH in
 exec-timeout 5 0
 login local
 transport input ssh
!
!
end
```

### R-FORMATION : 

```
R-INFORMATION#show startup-config
Using 2814 out of 129016 bytes
!
! Last configuration change at 11:45:56 UTC Fri Sep 18 2026
upgrade fpd auto
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname R-INFORMATION
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
!
!
!
ip domain name satom.local
ip cef
no ipv6 cef
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
!
username admin-tech privilege 15 secret 5 $1$c4cz$jKi4tYHVn4c4jObAq.sXA.
!
redundancy
!
!
ip ssh version 2
!
!
!
!
!
!
!
!
!
!
interface FastEthernet0/0
 no ip address
 duplex half
!
interface FastEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
!
interface FastEthernet0/0.99
 encapsulation dot1Q 99
 ip address 192.168.99.1 255.255.255.0
 ip access-group INVITES-RESTRICTIONS in
!
interface FastEthernet1/0
 ip address 10.0.12.2 255.255.255.252
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 pass123
 duplex half
!
interface FastEthernet2/0
 no ip address
 shutdown
 duplex half
!
interface FastEthernet3/0
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/0
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/1
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/2
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/3
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/4
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/5
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/6
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/7
 no ip address
 shutdown
 duplex half
!
interface Serial5/0
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/1
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/2
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/3
 no ip address
 shutdown
 serial restart-delay 0
!
router ospf 1
 router-id 2.2.2.2
 passive-interface FastEthernet0/0.10
 passive-interface FastEthernet0/0.99
 network 10.0.12.0 0.0.0.3 area 0
 network 192.168.10.0 0.0.0.255 area 0
 network 192.168.99.0 0.0.0.255 area 0
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!
!
!
ip access-list standard ADMIN-ONLY-SSH
 permit 192.168.20.10
 deny   any log
!
ip access-list extended INVITES-RESTRICTIONS
 deny   ip 192.168.99.0 0.0.0.255 host 10.0.0.50
 permit udp 192.168.99.0 0.0.0.255 any eq domain
 permit tcp 192.168.99.0 0.0.0.255 any eq domain
 permit tcp 192.168.99.0 0.0.0.255 any eq www
 permit tcp 192.168.99.0 0.0.0.255 any eq 443
 deny   ip 192.168.99.0 0.0.0.255 any log
!
!
!
!
control-plane
!
!
!
mgcp profile default
!
!
!
gatekeeper
 shutdown
!
!
line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 access-class ADMIN-ONLY-SSH in
 exec-timeout 5 0
 login local
 transport input ssh
!
!
end
```

### R-ADMIN : 

```
R-ADMIN#show startup-config
Using 2367 out of 129016 bytes
!
! Last configuration change at 09:27:52 UTC Fri Sep 18 2026
upgrade fpd auto
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname R-ADMIN
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
!
!
!
!
!
!
ip domain name satom.local
ip cef
no ipv6 cef
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
!
username admin-tech privilege 15 secret 5 $1$Brzf$y834ri8uJR2OC.1JQN51V1
!
redundancy
!
!
ip ssh version 2
!
!
!
!
!
!
!
!
!
!
interface Loopback0
 ip address 3.3.3.3 255.255.255.255
!
interface FastEthernet0/0
 ip address 192.168.20.1 255.255.255.0
 duplex half
!
interface FastEthernet1/0
 ip address 10.0.0.1 255.255.255.252
 duplex half
!
interface FastEthernet2/0
 ip address 10.0.13.2 255.255.255.252
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 pass123
 duplex half
!
interface FastEthernet3/0
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/0
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/1
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/2
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/3
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/4
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/5
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/6
 no ip address
 shutdown
 duplex half
!
interface Ethernet4/7
 no ip address
 shutdown
 duplex half
!
interface Serial5/0
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/1
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/2
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial5/3
 no ip address
 shutdown
 serial restart-delay 0
!
router ospf 1
 router-id 3.3.3.3
 passive-interface FastEthernet0/0
 passive-interface FastEthernet1/0
 network 3.3.3.3 0.0.0.0 area 0
 network 10.0.0.0 0.0.0.255 area 0
 network 10.0.13.0 0.0.0.3 area 0
 network 192.168.20.0 0.0.0.255 area 0
!
ip forward-protocol nd
no ip http server
no ip http secure-server
!
!
!
ip access-list standard ADMIN-ONLY-SSH
 permit 192.168.20.10
 deny   any log
!
!
!
!
control-plane
!
!
!
mgcp profile default
!
!
!
gatekeeper
 shutdown
!
!
line con 0
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 access-class ADMIN-ONLY-SSH in
 exec-timeout 5 0
 login local
 transport input ssh
!
!
end
```

### SW-FORMATION : 

```
SW-FORMATION#show startup-config
Using 741 out of 524288 bytes, uncompressed size = 1131 bytes
!
! Last configuration change at 09:05:44 UTC Fri Sep 18 2026
!
version 15.1
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname SW-FORMATION
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
no ipv6 cef
ipv6 multicast rpf use-bgp
!
ip cef
!
!
ip dhcp snooping vlan 10
no ip dhcp snooping information option
ip dhcp snooping
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
!
!
!
vlan internal allocation policy ascending
!
!
!
!
!
!
!
!
!
!
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
 duplex auto
 ip dhcp snooping trust
!
interface Ethernet0/1
 switchport access vlan 10
 switchport mode access
 switchport port-security
 switchport port-security mac-address sticky
 switchport port-security mac-address sticky 0050.7966.681f
 duplex auto
!
interface Ethernet0/2
 switchport access vlan 99
 switchport mode access
 duplex auto
!
interface Ethernet0/3
 duplex auto
!
!
no ip http server
!
!
!
!
!
control-plane
!
!
line con 0
 logging synchronous
line aux 0
line vty 0 4
!
end
```

### SW-ADMIN : 

```
SW-ADMIN#show startup-config
Using 468 out of 524288 bytes, uncompressed size = 666 bytes
!
version 15.1
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname SW-ADMIN
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
no ipv6 cef
ipv6 multicast rpf use-bgp
!
ip cef
!
!
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
!
!
!
vlan internal allocation policy ascending
!
!
!
!
!
!
!
!
!
!
interface Ethernet0/0
 duplex auto
!
interface Ethernet0/1
 duplex auto
!
interface Ethernet0/2
 duplex auto
!
interface Ethernet0/3
 duplex auto
!
!
no ip http server
!
!
!
!
!
control-plane
!
!
line con 0
 logging synchronous
line aux 0
line vty 0 4
!
end
```

### SERVER-WEB-PAIE : 

```
SERVER-WEB-PAIE#show startup-config
Using 591 out of 524288 bytes, uncompressed size = 825 bytes
!
! Last configuration change at 06:45:55 UTC Fri Sep 18 2026
!
version 15.1
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname SERVER-WEB-PAIE
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
no ipv6 cef
ipv6 multicast rpf use-bgp
no ip routing
!
no ip cef
!
!
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
!
!
!
vlan internal allocation policy ascending
!
!
!
!
!
!
!
!
!
!
interface Ethernet0/0
 no switchport
 ip address 10.0.0.50 255.255.255.0
!
interface Ethernet0/1
 duplex auto
!
interface Ethernet0/2
 duplex auto
!
interface Ethernet0/3
 duplex auto
!
ip default-gateway 10.0.0.1
!
no ip http server
!
!
!
!
!
control-plane
!
!
line con 0
 logging synchronous
line aux 0
line vty 0 4
 login
!
end
```

### Tableau récapitulatif de tout ce qui a été mis en oeuvre : 

| Domaine | Élément / Fonctionnalité | Équipement concerné | Description / Détails de la mise en œuvre |
| :--- | :--- | :--- | :--- |
| **Routage** | OSPF Multi-site | R-EDGE, R-FORMATION, R-ADMIN | Routage dynamique inter-sites avec authentification MD5 (`pass123`) activée sur les interfaces de liaison. |
| **Sécurité LAN** | Port-Security | Switches d'accès | Limitation du nombre d'adresses MAC autorisées par port pour contrer les usurpations. |
| **Sécurité LAN** | DHCP Snooping | Switches d'accès | Protection contre les faux serveurs DHCP (DHCP spoofing) en discriminant les ports de confiance. |
| **Filtrage (ACL)** | Accès RDP | Routeurs / Pare-feu | Règles d'accès filtrant et sécurisant les flux Bureau à distance (RDP) entre les réseaux. |
| **NAT / PAT** | NAT Statique | R-EDGE | Traduction fixe pour le serveur web de paie (`10.0.0.50` $\leftrightarrow$ `203.0.113.10`). |
| **NAT / PAT** | PAT Dynamique (Overload) | R-EDGE | Mutualisation de l'adresse IP publique de sortie pour les réseaux internes (ACL `PAT-NETWORKS`). |


## Rapport sur le projet : 

Ce projet réseau multi-site a consisté à concevoir et sécuriser une architecture interconnectée autour des routeurs R-EDGE, R-FORMATION et R-ADMIN.
Les choix techniques se sont portés sur le protocole de routage dynamique OSPF pour assurer la communication entre les sites, renforcé par une authentification MD5.
La sécurité de niveau 2 a été traitée par la mise en place du Port-Security et du DHCP Snooping sur les commutateurs d'accès, tandis que le filtrage des flux a été géré par des listes de contrôle d'accès (ACL). Enfin, le plan d'adressage a intégré un NAT statique pour le serveur web de paie et un PAT dynamique sur le routeur de bordure R-EDGE qui n'a malheuresement pas fonctionné dans ma configuration.

Au cours de la phase de validation, un incident de type perte de configuration après un redémarrage non sauvegardé a été simulé sur R-EDGE. Le diagnostic via la commande show running-config a mis en évidence l'absence des dernières règles de NAT et de sécurité des ports, la configuration active n'ayant pas été enregistrée dans la mémoire non volatile. L'incident a été résolu en réinjectant les commandes nécessaires et en validant la manipulation par la commande wr.

En conclusion, si ce projet devait être déployé dans un environnement de production réel, plusieurs modifications seraient apportées.
Il serait mieux d'introduire de la haute disponibilité sur le routeur de bordure R-EDGE afin d'éviter tout point de défaillance unique.
De plus, la gestion des configurations et des sauvegardes ne serait plus laissée à une action manuelle mais automatisée via des scripts centralisés ou des outils dédiés, pour garantir l'intégrité du réseau face aux incidents matériels.


## Phase questions : Questions de connaissances (100 questions, QCM) 

### Catégorie A — Concepts OSPF (Module 1)

#### A1. OSPF appartient à quelle catégorie de protocole de routage ?

a) Vecteur de distance
b) État de liens
c) Hybride
d) Vecteur de chemin

#### A2. Quel algorithme utilise OSPF pour calculer le meilleur chemin ?

a) Bellman-Ford
b) Dijkstra (SPF)
c) DUAL
d) A*

#### A3. Quelle est la bande passante de référence par défaut utilisée pour calculer le coût OSPF ?

a) 10 Mbps
b) 100 Mbps
c) 1000 Mbps
d) 10000 Mbps

#### A4. Quelle commande modifie la bande passante de référence utilisée dans le calcul du coût OSPF ?

a) bandwidth reference
b) auto-cost reference-bandwidth
c) ip ospf cost
d) reference-bandwidth ospf

#### A5. Comment est déterminé le Router-ID si aucun n'est configuré manuellement ?

a) IP la plus basse de toutes les interfaces
b) IP la plus haute des interfaces actives, priorité aux loopbacks
c) Adresse MAC la plus haute
d) Toujours 0.0.0.0

#### A6. Pourquoi recommande-t-on une interface loopback pour fixer le Router-ID ?

a) Elle est toujours active, ce qui le stabilise
b) Elle est plus rapide
c) Elle consomme moins de mémoire
d) C'est obligatoire pour OSPF

#### A7. Quel est le rôle du DR (Designated Router) sur un segment multi-accès ?

a) Répartir la charge du trafic
b) Centraliser les échanges LSA pour réduire le nombre d'adjacences
c) Chiffrer le trafic OSPF
d) Remplacer le Router-ID

#### A8. Sur un lien point-à-point, l'élection DR/BDR a-t-elle lieu ?

a) Oui, systématiquement
b) Non, elle n'a pas de sens sur ce type de lien
c) Seulement si configurée manuellement
d) Seulement en IPv6
#### A9. Valeurs par défaut des timers Hello/Dead sur un réseau broadcast (Ethernet) ?

a) 5s / 20s
b) 10s / 40s
c) 30s / 120s
d) 60s / 180s

#### A10. Que se passe-t-il si les timers Hello/Dead diffèrent entre deux voisins ?

a) L'adjacence se forme quand même
b) L'adjacence ne peut pas se former
c) Seul le Hello timer compte
d) OSPF ignore cette différence

#### A11. Quel état de voisinage OSPF indique une adjacence pleinement établie ?

a) 2-Way
b) ExStart
c) Full
d) Loading

#### A12. Quel type de LSA décrit les liens directement connectés d'un routeur ?

a) Router LSA (type 1)
b) Network LSA
c) Summary LSA
d) External LSA

#### A13. Quelle commande affiche l'état des adjacences OSPF ?

a) show ip ospf database
b) show ip ospf neighbor
c) show ip route ospf
d) show ip protocols

#### A14. Lequel de ces critères N'EMPÊCHE PAS la formation d'une adjacence OSPF s'il diffère ?

a) Area ID
b) Masque de sous-réseau du lien
c) Hostname du routeur
d) Type d'authentification

#### A15. Quelle commande observe en temps réel la formation des adjacences OSPF ?

a) show ip ospf adj
b) debug ip ospf adj
c) trace ip ospf
d) monitor ospf neighbor

#### A16. Que représente l'aire 0 dans OSPF ?

a) Une zone optionnelle
b) L'aire de backbone, obligatoire en conception multi-aires
c) Une zone réservée aux liens WAN
d) Une aire désactivée par défaut

#### A17. Dans network 10.0.12.0 0.0.0.3 area 0, que représente 0.0.0.3 ?

a) Un masque de sous-réseau classique
b) Un wildcard mask
c) Une adresse de broadcast
d) Un ID de zone

### Catégorie B — Configuration OSPF (Module 2)

#### B1. Dans router ospf 1, que représente le « 1 » ?

a) L'area ID
b) Le process ID, localement significatif au routeur
c) Le Router-ID
d) Le numéro d'AS

#### B2. Le process ID OSPF doit-il être identique sur tous les routeurs du domaine ?

a) Oui, obligatoirement
b) Non, il est local à chaque routeur
c) Oui, en zone unique seulement
d) Non, seulement en IPv6

#### B3. Quel est l'effet de passive-interface g0/0 ?

a) L'interface arrête d'annoncer son réseau
b) L'interface continue d'annoncer son réseau mais n'envoie plus de Hello
c) L'interface est désactivée
d) L'interface devient une interface de secours

#### B4. Pourquoi rendre passive une interface connectée à un LAN utilisateur ?

a) Pour économiser de la bande passante uniquement
b) Pour empêcher un hôte non autorisé de former une adjacence OSPF
c) Parce que c'est obligatoire dans OSPF
d) Pour activer le DR sur ce segment

#### B5. Quelle commande rend toutes les interfaces passives par défaut ?

a) passive-interface all
b) passive-interface default
c) no active-interface
d) shutdown-interface default

#### B6. Que fait default-information originate sur un routeur OSPF ?

a) Elle génère une route par défaut même sans route locale
b) Elle injecte une route par défaut dans OSPF, à condition d'en posséder déjà une
c) Elle supprime toute route par défaut
d) Elle active OSPF automatiquement

#### B7. Quelle différence apporte le mot-clé always dans default-information originate always ?

a) Force l'injection même sans route par défaut locale active
b) Diminue le coût de la route
c) Change le type de LSA en type 1
d) Active l'authentification automatiquement

#### B8. Quel type de LSA transporte une route par défaut externe injectée ?

a) Type 1
b) Type 2
c) Type 3
d) Type 5 (External)

#### B9. Quelle commande active l'authentification MD5 sur une interface OSPF ?

a) ip ospf authentication message-digest
b) ip ospf md5-key
c) router ospf authentication
d) area 0 md5

#### B10. Avant d'activer l'authentification MD5, quelle commande faut-il configurer sur l'interface ?

a) ip ospf priority 0
b) ip ospf message-digest-key <n> md5 <clé>
c) ip ospf network point-to-point
d) ip ospf cost 10

#### B11. Que se passe-t-il si la clé MD5 diffère entre deux routeurs voisins ?

a) L'adjacence se forme avec un avertissement
b) L'adjacence échoue (mismatch authentication)
c) Le trafic passe en clair
d) OSPF désactive l'authentification automatiquement

#### B12. Quelle commande vérifie si l'authentification est active sur une interface OSPF ?

a) show ip ospf interface <if> | include Auth
b) show running-config ospf
c) show ip ospf auth-status
d) debug ip ospf auth

#### B13. Quelle commande liste les réseaux annoncés et les interfaces passives d'un processus OSPF ?

a) show ip ospf database
b) show ip protocols
c) show ip ospf neighbor
d) show ip route

#### B14. Sur quel type d'interface faut-il éviter passive-interface ?

a) Les interfaces LAN utilisateur
b) Les interfaces backbone reliant deux routeurs OSPF
c) Les interfaces loopback
d) Toutes les interfaces

#### B15. Un voisin reste bloqué à l'état EXSTART. Cause fréquente ?

a) MTU différente entre les deux interfaces
b) Adresse IP incorrecte
c) VLAN natif différent
d) Câble défectueux uniquement

#### B16. Quelle commande force le recalcul complet du processus OSPF ?

a) clear ip ospf process
b) reload ospf
c) restart ip ospf
d) Supprimer puis recréer router ospf 1 uniquement

#### B17. Pourquoi sauvegarder (write memory) après chaque modification OSPF validée ?

a) Ce n'est pas nécessaire, OSPF sauvegarde automatiquement
b) Pour éviter de perdre la configuration au prochain redémarrage
c) Uniquement requis pour les ACL
d) Cela relance automatiquement les adjacences

### Catégorie C — Sécurité réseau (Module 3)
C1. Pourquoi Telnet est-il déconseillé pour l'administration des équipements ?

a) Il est plus lent que SSH
b) Il transmet identifiants et commandes en clair
c) Il ne fonctionne pas sur IPv6
d) Il nécessite une clé RSA

#### C2. Quelle commande génère la paire de clés RSA nécessaire à SSH ?

a) crypto key generate rsa modulus 2048
b) generate ssh-key rsa
c) ip ssh key generate
d) enable ssh rsa

#### C3. Quel prérequis, avant la génération de clé RSA, sert d'identifiant à la clé (FQDN) ?

a) hostname R1 seul
b) ip domain-name <domaine>
c) ip ssh enable
d) crypto pki enable

#### C4. Que fait ip ssh version 2 ?

a) Active SSHv1 et v2 simultanément
b) Force l'utilisation exclusive de SSHv2
c) Désactive SSH
d) Configure le port SSH

#### C5. Sous line vty 0 4, quelle commande restreint l'accès au protocole SSH uniquement ?

a) access-class ssh-only
b) transport input ssh
c) login ssh
d) ssh only

#### C6. Quelle commande authentifie les connexions vty via la base de comptes locaux ?

a) login local
b) login authentication
c) aaa new-model seul
d) password local

#### C7. Entre enable secret et enable password, lequel est prioritaire si les deux existent ?

a) enable password
b) enable secret
c) Les deux s'appliquent en même temps
d) Aucun, il faut choisir explicitement

#### C8. Intérêt de exec-timeout 5 0 sur une ligne vty ?

a) Limite la bande passante disponible
b) Déconnecte une session inactive après 5 minutes
c) Force une reconnexion toutes les 5 minutes
d) Bloque les connexions après 5 tentatives

#### C9. Que fait switchport port-security mac-address sticky ?

a) Bloque toutes les adresses MAC
b) Apprend dynamiquement la première MAC et l'ajoute à la configuration
c) Change l'adresse MAC du port
d) Désactive le port

#### C10. Quel mode de violation port security place le port en état err-disabled ?

a) protect
b) restrict
c) shutdown
d) monitor

#### C11. Comment relever un port passé en err-disabled ?

a) reload du switch obligatoire
b) shutdown puis no shutdown sur l'interface
c) clear port-security
d) no switchport port-security

#### C12. Quelle commande active globalement le DHCP snooping sur un switch ?

a) ip dhcp snooping
b) dhcp snooping enable
c) ip dhcp inspect
d) switchport dhcp snooping

#### C13. Qu'est-ce qu'un port « trusted » en DHCP snooping ?

a) Un port où le filtrage MAC est désactivé
b) Le seul type de port autorisé à relayer des réponses DHCP
c) Un port avec port security activé
d) Un port du VLAN natif

#### C14. Objectif de ip dhcp snooping limit rate <n> sur un port non fiable ?

a) Limiter la bande passante totale du port
b) Limiter le nombre de paquets DHCP/seconde (anti flood/DoS)
c) Limiter le nombre d'adresses MAC apprises
d) Limiter le débit DHCP à un seul bail

#### C15. Risque principal d'un serveur DHCP non autorisé (rogue) sur le réseau ?

a) Il ralentit uniquement le Wi-Fi
b) Il peut distribuer de fausses adresses/passerelles et détourner le trafic
c) Aucun impact si le VLAN est isolé
d) Il désactive automatiquement OSPF

#### C16. Quelle fonctionnalité complète le DHCP snooping contre l'usurpation via ARP ?

a) Port security
b) Dynamic ARP Inspection (DAI)
c) OSPF authentication
d) NAT overload

#### Catégorie D — Concepts ACL (Module 4)
D1. Que fait une ACL Cisco par défaut si aucune règle ne correspond à un paquet ?

a) Elle l'autorise par défaut
b) Elle le refuse (deny any implicite)
c) Elle génère une erreur
d) Elle le redirige vers le CPU

#### D2. Rôle d'un wildcard mask dans une ACL ?

a) Identique au masque de sous-réseau
b) Indique quels bits doivent correspondre (0) et lesquels sont ignorés (1)
c) Chiffre l'adresse IP
d) Définit la durée de vie de la règle

#### D3. Wildcard mask correspondant à 192.168.10.0/24 ?

a) 255.255.255.0
b) 0.0.0.255
c) 0.0.0.0
d) 0.255.255.255

#### D4. Quel mot-clé remplace le wildcard 0.0.0.0 pour un hôte unique ?

a) any
b) all
c) host
d) single

#### D5. Quel mot-clé remplace le wildcard 255.255.255.255 pour toute adresse ?

a) any
b) all
c) host
d) none

#### D6. Plage de numéros d'une ACL IP standard numérotée ?

a) 1-99 (et 1300-1999)
b) 100-199
c) 200-299
d) 1-999

#### D7. Plage de numéros d'une ACL IP étendue numérotée ?

a) 1-99
b) 100-199 (et 2000-2699)
c) 300-399
d) 1000-1099

#### D8. Sur quel(s) critère(s) une ACL standard filtre-t-elle le trafic ?

a) Adresse source uniquement
b) Source et destination
c) Source, destination, protocole et port
d) Adresse MAC uniquement

#### D9. Sur quel(s) critère(s) une ACL étendue filtre-t-elle le trafic ?

a) Source uniquement
b) Source et destination, protocole, ports
c) Port de destination uniquement
d) Protocole uniquement

#### D10. Où placer de préférence une ACL étendue ?

a) Le plus près de la destination
b) Le plus près de la source
c) Peu importe
d) Toujours sur le routeur de bordure Internet

#### D11. Où placer de préférence une ACL standard ?

a) Le plus près de la source
b) Le plus près de la destination
c) Sur n'importe quelle interface
d) Uniquement sur les lignes VTY

#### D12. Dans quel ordre les lignes d'une ACL sont-elles évaluées ?

a) Aléatoire
b) De la dernière à la première
c) Séquentiellement, arrêt au premier match
d) Toutes en parallèle

#### D13. Une ACL standard ne contient qu'une ligne deny 192.168.20.0 0.0.0.255. Effet sur le reste du trafic ?

a) Autorisé par défaut
b) Bloqué par le deny any implicite
c) Erreur générée
d) Redirigé

#### D14. Combien d'ACL peut-on appliquer sur une même interface, pour un même protocole et un même sens ?

a) Autant que nécessaire
b) Une seule
c) Deux
d) Trois

#### D15. Pour bloquer un sous-réseau tout en laissant passer le reste, que faut-il ajouter après la ligne deny ?

a) Rien
b) Une ligne permit any explicite
c) Une seconde ligne deny any
d) Un shutdown de l'interface

#### D16. Avantage principal d'une ACL nommée par rapport à une ACL numérotée ?

a) Plus rapide à traiter par le CPU
b) Plus lisible, ajout/suppression de lignes individuelles
c) Pas de deny implicite
d) Fonctionne uniquement avec OSPF

#### Catégorie E — Configuration ACL IPv4 (Module 5)
E1. Quelle commande crée une ACL standard nommée « ADMIN-ONLY » ?

a) access-list standard ADMIN-ONLY
b) ip access-list standard ADMIN-ONLY
c) ip access-group standard ADMIN-ONLY
d) create acl standard ADMIN-ONLY

#### E2. Quelle commande applique une ACL standard aux lignes VTY en entrée ?

a) ip access-group <nom> in
b) access-class <nom> in
c) line access-list <nom>
d) vty filter <nom>

#### E3. Quelle commande applique une ACL à une interface physique, en entrée ?

a) access-class <nom> in
b) ip access-group <nom> in
c) interface access-list <nom> in
d) ip filter <nom> in

#### E4. Pourquoi access-class plutôt que access-group sur les lignes VTY ?

a) access-group est réservé aux ACL étendues
b) access-class est la commande spécifique à l'accès administratif, différente des interfaces
c) Ce sont des synonymes
d) access-class est obsolète

#### E5. Quelle commande affiche le contenu d'une ACL avec le nombre de correspondances (matches) ?

a) show running-config acl
b) show access-lists
c) show ip interface
d) show acl-counters

#### E6. Quelle commande confirme sur quelle interface et dans quel sens une ACL est appliquée ?

a) show access-lists
b) show ip interface <if> | include access list
c) show ip protocols
d) show running-config | include vty

#### E7. Les compteurs matches restent à 0 malgré du trafic. Que vérifier en priorité ?

a) La longueur du nom de l'ACL
b) Que l'ACL est appliquée sur la bonne interface et le bon sens
c) La version d'IOS
d) Le nombre de VLAN configurés

#### E8. Dans une ACL étendue, quel mot-clé précède un numéro de port unique ?

a) eq
b) at
c) is
d) port

#### E9. Quel port TCP correspond au trafic HTTPS ?

a) 80
b) 443
c) 53
d) 22

#### E10. Quel port UDP correspond au trafic DNS ?

a) 80
b) 443
c) 53
d) 67

#### E11. Quel port TCP correspond au trafic RDP ?

a) 3389
b) 22
c) 25
d) 8080

#### E12. Quelle syntaxe autorise le HTTP dans permit tcp 192.168.99.0 0.0.0.255 any ... ?

a) eq 21
b) eq 80
c) eq 443
d) eq 25

#### E13. Dans une ACL nommée, comment supprimer uniquement la ligne numéro 20 ?

a) no 20 (en mode configuration de l'ACL)
b) delete line 20
c) remove access-list 20
d) clear acl 20

#### E14. Une ACL RDP est appliquée en out sur l'interface d'entrée du trafic client, alors que le trafic ressort par une autre interface. Quel est le problème ?

a) Aucun
b) L'ACL doit être appliquée sur l'interface par laquelle le trafic sort réellement (ou en in côté client)
c) Il faut doubler l'ACL en out sur les deux interfaces
d) RDP ne peut pas être filtré par ACL

#### E15. Une ACL standard (source uniquement) suffit-elle pour bloquer un VLAN entier vers UN SEUL serveur précis, en laissant le reste accessible ?

a) Oui
b) Non, une ACL étendue est nécessaire pour cibler une destination précise
c) Cela dépend du masque
d) Oui, avec host

#### E16. Impact d'une ACL appliquée en entrée, au plus près de la source, sur la charge CPU du routeur ?

a) Aucun impact
b) Elle réduit la charge en filtrant le trafic indésirable au plus tôt
c) Elle augmente systématiquement la charge CPU
d) Elle désactive le routage

#### E17. Un poste non autorisé tente un SSH après application de l'ACL ADMIN-ONLY sur les VTY. Résultat attendu si la config est correcte ?

a) La connexion réussit normalement
b) La connexion est refusée
c) Le routeur redémarre
d) Le SSH bascule en Telnet

#### Catégorie F — NAT pour IPv4 (Module 6)
F1. Que signifie l'acronyme NAT ?

a) Network Address Translation
b) Network Access Tunneling
c) Node Address Table
d) Network Authentication Type

#### F2. Comment appelle-t-on l'adresse privée d'un hôte interne, vue depuis l'intérieur du réseau ?

a) Inside global
b) Inside local
c) Outside local
d) Outside global

#### F3. Comment appelle-t-on l'adresse publique représentant un hôte interne, vue depuis Internet ?

a) Inside local
b) Inside global
c) Outside global
d) Outside local

#### F4. Quelle commande marque une interface comme faisant face au réseau interne pour le NAT ?

a) ip nat outside
b) ip nat inside
c) ip nat local
d) ip nat private

#### F5. Quelle commande marque une interface comme faisant face au réseau externe pour le NAT ?

a) ip nat inside
b) ip nat public
c) ip nat outside
d) ip nat wan

#### F6. Quel type de NAT crée une correspondance fixe et permanente, idéale pour publier un serveur ?

a) NAT dynamique
b) NAT statique
c) PAT/overload
d) NAT64

#### F7. Quelle commande configure un NAT statique associant 10.0.0.50 à 203.0.113.10 ?

a) ip nat inside source static 10.0.0.50 203.0.113.10
b) ip nat static 10.0.0.50 to 203.0.113.10
c) ip nat inside source list 10.0.0.50 pool 203.0.113.10
d) nat static 10.0.0.50 203.0.113.10

#### F8. Quel type de NAT traduit vers une plage limitée d'adresses publiques, sur un modèle 1-pour-1 temporaire ?

a) NAT statique
b) NAT dynamique (pool)
c) PAT/overload
d) NAT66

#### F9. Toutes les adresses d'un pool NAT dynamique sont utilisées et un nouvel hôte tente une traduction. Que se passe-t-il ?

a) Le NAT utilise une adresse au hasard
b) La traduction échoue (compteur « misses »)
c) Le pool s'agrandit automatiquement
d) Le trafic passe sans traduction

#### F10. Quel mécanisme permet à de nombreux hôtes internes de partager une seule adresse publique ?

a) NAT statique
b) NAT dynamique simple
c) PAT (NAT overload), basé sur les ports
d) DHCP relay

#### F11. Quel mot-clé active le PAT dans ip nat inside source list <acl> interface <if> ... ?

a) pat
b) overload
c) share
d) multiplex

#### F12. Quelle commande affiche la table des traductions NAT actives ?

a) show ip nat pool
b) show ip nat translations
c) show nat table
d) show ip nat active

#### F13. Quelle commande affiche des statistiques globales sur le NAT, avec le compteur d'échecs ?

a) show ip nat translations
b) show ip nat statistics
c) show ip nat summary
d) show running-config nat

#### F14. Pourquoi préférer le NAT statique au PAT pour publier un serveur interne accessible depuis Internet ?

a) Le PAT ne fonctionne pas avec les serveurs
b) Le NAT statique garantit une IP:port fixe atteignable de l'extérieur ; le PAT seul ne permet pas d'initier une connexion entrante sans redirection de port
c) Le NAT statique est plus rapide en débit
d) Aucune différence pratique

#### F15. Une entreprise dispose d'une seule adresse publique pour tout son réseau interne. Quelle solution est la plus adaptée pour l'accès Internet sortant ?

a) NAT statique
b) NAT dynamique avec pool de 4 adresses
c) PAT/overload sur l'unique adresse publique
d) Aucune solution n'est possible

#### F16. Une ACL utilisée dans une règle NAT (ip nat inside source list <acl> ...) sert à :

a) Bloquer du trafic comme une ACL de sécurité classique
b) Définir quels hôtes/réseaux internes sont éligibles à la traduction
c) Chiffrer les paquets NAT
d) Limiter la bande passante NAT

#### F17. Que révèle une ligne de show ip nat translations où plusieurs entrées partagent la même adresse « Inside global » avec des ports différents ?

a) Une erreur de configuration
b) Un fonctionnement normal du PAT/overload
c) Un conflit d'adresses IP
d) Une attaque par déni de service
    
### Mes réponses : 
    
#### A1. OSPF appartient à quelle catégorie de protocole de routage ?

b) État de liens

#### A2. Quel algorithme utilise OSPF pour calculer le meilleur chemin ?

b) Dijkstra (SPF)

#### A3. Quelle est la bande passante de référence par défaut utilisée pour calculer le coût OSPF ?

d) 10000 Mbps

#### A4. Quelle commande modifie la bande passante de référence utilisée dans le calcul du coût OSPF ?

b) auto-cost reference-bandwidth

#### A5. Comment est déterminé le Router-ID si aucun n'est configuré manuellement ?

b) IP la plus haute des interfaces actives, priorité aux loopbacks

#### A6. Pourquoi recommande-t-on une interface loopback pour fixer le Router-ID ?

a) Elle est toujours active, ce qui le stabilise

#### A7. Quel est le rôle du DR (Designated Router) sur un segment multi-accès ?

b) Centraliser les échanges LSA pour réduire le nombre d'adjacences

#### A8. Sur un lien point-à-point, l'élection DR/BDR a-t-elle lieu ?

b) Non, elle n'a pas de sens sur ce type de lien

#### A9. Valeurs par défaut des timers Hello/Dead sur un réseau broadcast (Ethernet) ?

b) 10s / 40s

#### A10. Que se passe-t-il si les timers Hello/Dead diffèrent entre deux voisins ?

a) L'adjacence se forme quand même

#### A11. Quel état de voisinage OSPF indique une adjacence pleinement établie ?

c) Full

#### A12. Quel type de LSA décrit les liens directement connectés d'un routeur ?

c) Summary LSA

#### A13. Quelle commande affiche l'état des adjacences OSPF ?

b) show ip ospf neighbor

#### A14. Lequel de ces critères N'EMPÊCHE PAS la formation d'une adjacence OSPF s'il diffère ?

c) Hostname du routeur

#### A15. Quelle commande observe en temps réel la formation des adjacences OSPF ?

b) debug ip ospf adj

#### A16. Que représente l'aire 0 dans OSPF ?

b) L'aire de backbone, obligatoire en conception multi-aires

#### A17. Dans network 10.0.12.0 0.0.0.3 area 0, que représente 0.0.0.3 ?

b) Un wildcard mask

### Catégorie B — Configuration OSPF (Module 2)

#### B1. Dans router ospf 1, que représente le « 1 » ?

b) Le process ID, localement significatif au routeur

#### B2. Le process ID OSPF doit-il être identique sur tous les routeurs du domaine ?

a) Oui, obligatoirement

#### B3. Quel est l'effet de passive-interface g0/0 ?

b) L'interface continue d'annoncer son réseau mais n'envoie plus de Hello

#### B4. Pourquoi rendre passive une interface connectée à un LAN utilisateur ?

b) Pour empêcher un hôte non autorisé de former une adjacence OSPF

#### B5. Quelle commande rend toutes les interfaces passives par défaut ?

b) passive-interface default

#### B6. Que fait default-information originate sur un routeur OSPF ?

b) Elle injecte une route par défaut dans OSPF, à condition d'en posséder déjà une

#### B7. Quelle différence apporte le mot-clé always dans default-information originate always ?

a) Force l'injection même sans route par défaut locale active

#### B8. Quel type de LSA transporte une route par défaut externe injectée ?

d) Type 5 (External)

#### B9. Quelle commande active l'authentification MD5 sur une interface OSPF ?

a) ip ospf authentication message-digest

#### B10. Avant d'activer l'authentification MD5, quelle commande faut-il configurer sur l'interface ?

b) ip ospf message-digest-key <n> md5 <clé>

#### B11. Que se passe-t-il si la clé MD5 diffère entre deux routeurs voisins ?

b) L'adjacence échoue (mismatch authentication)

#### B12. Quelle commande vérifie si l'authentification est active sur une interface OSPF ?

a) show ip ospf interface <if> | include Auth

#### B13. Quelle commande liste les réseaux annoncés et les interfaces passives d'un processus OSPF ?

b) show ip protocols

#### B14. Sur quel type d'interface faut-il éviter passive-interface ?

b) Les interfaces backbone reliant deux routeurs OSPF

#### B15. Un voisin reste bloqué à l'état EXSTART. Cause fréquente ?

a) MTU différente entre les deux interfaces

#### B16. Quelle commande force le recalcul complet du processus OSPF ?

a) clear ip ospf process

#### B17. Pourquoi sauvegarder (write memory) après chaque modification OSPF validée ?

b) Pour éviter de perdre la configuration au prochain redémarrage

### Catégorie C — Sécurité réseau (Module 3)

C1. Pourquoi Telnet est-il déconseillé pour l'administration des équipements ?

b) Il transmet identifiants et commandes en clair

#### C2. Quelle commande génère la paire de clés RSA nécessaire à SSH ?

a) crypto key generate rsa modulus 2048

#### C3. Quel prérequis, avant la génération de clé RSA, sert d'identifiant à la clé (FQDN) ?

b) ip domain-name <domaine>

#### C4. Que fait ip ssh version 2 ?

b) Force l'utilisation exclusive de SSHv2

#### C5. Sous line vty 0 4, quelle commande restreint l'accès au protocole SSH uniquement ?

b) transport input ssh

#### C6. Quelle commande authentifie les connexions vty via la base de comptes locaux ?

a) login local

#### C7. Entre enable secret et enable password, lequel est prioritaire si les deux existent ?

b) enable secret

#### C8. Intérêt de exec-timeout 5 0 sur une ligne vty ?

b) Déconnecte une session inactive après 5 minutes

#### C9. Que fait switchport port-security mac-address sticky ?

b) Apprend dynamiquement la première MAC et l'ajoute à la configuration

#### C10. Quel mode de violation port security place le port en état err-disabled ?

c) shutdown

#### C11. Comment relever un port passé en err-disabled ?

b) shutdown puis no shutdown sur l'interface

#### C12. Quelle commande active globalement le DHCP snooping sur un switch ?

a) ip dhcp snooping

#### C13. Qu'est-ce qu'un port « trusted » en DHCP snooping ?

b) Le seul type de port autorisé à relayer des réponses DHCP

#### C14. Objectif de ip dhcp snooping limit rate <n> sur un port non fiable ?

b) Limiter le nombre de paquets DHCP/seconde (anti flood/DoS)

#### C15. Risque principal d'un serveur DHCP non autorisé (rogue) sur le réseau ?

b) Il peut distribuer de fausses adresses/passerelles et détourner le trafic

#### C16. Quelle fonctionnalité complète le DHCP snooping contre l'usurpation via ARP ?

b) Dynamic ARP Inspection (DAI)

#### Catégorie D — Concepts ACL (Module 4)
D1. Que fait une ACL Cisco par défaut si aucune règle ne correspond à un paquet ?

b) Elle le refuse (deny any implicite)

#### D2. Rôle d'un wildcard mask dans une ACL ?

b) Indique quels bits doivent correspondre (0) et lesquels sont ignorés (1)

#### D3. Wildcard mask correspondant à 192.168.10.0/24 ?

b) 0.0.0.255

#### D4. Quel mot-clé remplace le wildcard 0.0.0.0 pour un hôte unique ?

c) host

#### D5. Quel mot-clé remplace le wildcard 255.255.255.255 pour toute adresse ?

a) any

#### D6. Plage de numéros d'une ACL IP standard numérotée ?

a) 1-99 (et 1300-1999)

#### D7. Plage de numéros d'une ACL IP étendue numérotée ?

b) 100-199 (et 2000-2699)

#### D8. Sur quel(s) critère(s) une ACL standard filtre-t-elle le trafic ?

a) Adresse source uniquement

#### D9. Sur quel(s) critère(s) une ACL étendue filtre-t-elle le trafic ?

b) Source et destination, protocole, ports

#### D10. Où placer de préférence une ACL étendue ?

b) Le plus près de la source

#### D11. Où placer de préférence une ACL standard ?

b) Le plus près de la destination

#### D12. Dans quel ordre les lignes d'une ACL sont-elles évaluées ?

c) Séquentiellement, arrêt au premier match

#### D13. Une ACL standard ne contient qu'une ligne deny 192.168.20.0 0.0.0.255. Effet sur le reste du trafic ?

a) Autorisé par défaut

#### D14. Combien d'ACL peut-on appliquer sur une même interface, pour un même protocole et un même sens ?

b) Une seule

#### D15. Pour bloquer un sous-réseau tout en laissant passer le reste, que faut-il ajouter après la ligne deny ?

b) Une ligne permit any explicite

#### D16. Avantage principal d'une ACL nommée par rapport à une ACL numérotée ?

b) Plus lisible, ajout/suppression de lignes individuelles

#### Catégorie E — Configuration ACL IPv4 (Module 5)
E1. Quelle commande crée une ACL standard nommée « ADMIN-ONLY » ?

b) ip access-list standard ADMIN-ONLY

#### E2. Quelle commande applique une ACL standard aux lignes VTY en entrée ?

b) access-class <nom> in

#### E3. Quelle commande applique une ACL à une interface physique, en entrée ?

b) ip access-group <nom> in

#### E4. Pourquoi access-class plutôt que access-group sur les lignes VTY ?

b) access-class est la commande spécifique à l'accès administratif, différente des interfaces

#### E5. Quelle commande affiche le contenu d'une ACL avec le nombre de correspondances (matches) ?

b) show access-lists

#### E6. Quelle commande confirme sur quelle interface et dans quel sens une ACL est appliquée ?

b) show ip interface <if> | include access list

#### E7. Les compteurs matches restent à 0 malgré du trafic. Que vérifier en priorité ?

b) Que l'ACL est appliquée sur la bonne interface et le bon sens

#### E8. Dans une ACL étendue, quel mot-clé précède un numéro de port unique ?

a) eq

#### E9. Quel port TCP correspond au trafic HTTPS ?

b) 443

#### E10. Quel port UDP correspond au trafic DNS ?

c) 53

#### E11. Quel port TCP correspond au trafic RDP ?

a) 3389

#### E12. Quelle syntaxe autorise le HTTP dans permit tcp 192.168.99.0 0.0.0.255 any ... ?

b) eq 80

#### E13. Dans une ACL nommée, comment supprimer uniquement la ligne numéro 20 ?

a) no 20 (en mode configuration de l'ACL)

#### E14. Une ACL RDP est appliquée en out sur l'interface d'entrée du trafic client, alors que le trafic ressort par une autre interface. Quel est le problème ?

b) L'ACL doit être appliquée sur l'interface par laquelle le trafic sort réellement (ou en in côté client)

#### E15. Une ACL standard (source uniquement) suffit-elle pour bloquer un VLAN entier vers UN SEUL serveur précis, en laissant le reste accessible ?

b) Non, une ACL étendue est nécessaire pour cibler une destination précise

#### E16. Impact d'une ACL appliquée en entrée, au plus près de la source, sur la charge CPU du routeur ?

b) Elle réduit la charge en filtrant le trafic indésirable au plus tôt

#### E17. Un poste non autorisé tente un SSH après application de l'ACL ADMIN-ONLY sur les VTY. Résultat attendu si la config est correcte ?

b) La connexion est refusée

#### Catégorie F — NAT pour IPv4 (Module 6)
F1. Que signifie l'acronyme NAT ?

a) Network Address Translation

#### F2. Comment appelle-t-on l'adresse privée d'un hôte interne, vue depuis l'intérieur du réseau ?

b) Inside local

#### F3. Comment appelle-t-on l'adresse publique représentant un hôte interne, vue depuis Internet ?

b) Inside global

#### F4. Quelle commande marque une interface comme faisant face au réseau interne pour le NAT ?

b) ip nat inside

#### F5. Quelle commande marque une interface comme faisant face au réseau externe pour le NAT ?

c) ip nat outside

#### F6. Quel type de NAT crée une correspondance fixe et permanente, idéale pour publier un serveur ?

b) NAT statique

#### F7. Quelle commande configure un NAT statique associant 10.0.0.50 à 203.0.113.10 ?

a) ip nat inside source static 10.0.0.50 203.0.113.10

#### F8. Quel type de NAT traduit vers une plage limitée d'adresses publiques, sur un modèle 1-pour-1 temporaire ?

b) NAT dynamique (pool)

#### F9. Toutes les adresses d'un pool NAT dynamique sont utilisées et un nouvel hôte tente une traduction. Que se passe-t-il ?

b) La traduction échoue (compteur « misses »)

#### F10. Quel mécanisme permet à de nombreux hôtes internes de partager une seule adresse publique ?

c) PAT (NAT overload), basé sur les ports

#### F11. Quel mot-clé active le PAT dans ip nat inside source list <acl> interface <if> ... ?

b) overload

#### F12. Quelle commande affiche la table des traductions NAT actives ?

b) show ip nat translations

#### F13. Quelle commande affiche des statistiques globales sur le NAT, avec le compteur d'échecs ?

b) show ip nat statistics

#### F14. Pourquoi préférer le NAT statique au PAT pour publier un serveur interne accessible depuis Internet ?

b) Le NAT statique garantit une IP:port fixe atteignable de l'extérieur ; le PAT seul ne permet pas d'initier une connexion entrante sans redirection de port

#### F15. Une entreprise dispose d'une seule adresse publique pour tout son réseau interne. Quelle solution est la plus adaptée pour l'accès Internet sortant ?

c) PAT/overload sur l'unique adresse publique

#### F16. Une ACL utilisée dans une règle NAT (ip nat inside source list <acl> ...) sert à :

b) Définir quels hôtes/réseaux internes sont éligibles à la traduction

#### F17. Que révèle une ligne de show ip nat translations où plusieurs entrées partagent la même adresse « Inside global » avec des ports différents ?

b) Un fonctionnement normal du PAT/overload
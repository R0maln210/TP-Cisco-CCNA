# TP 1.1 - Découverte du voisinage OSPF et des états d'adjacence - Romain Jaquet

## Lab complet : 

![01 - Lab en entier](https://hackmd.io/_uploads/Hy3TP8SKze.png)

## R1 : 

```
# On attribue l'adresse IP aux interfaces
en
conf t
interface fa0/0
ip add 192.168.1.1 255.255.255.252
no shut
exit

interface fa1/0
ip add 192.168.3.1 255.255.255.252
no shut

# On configure l'interface de loopback
R1(config)# interface loopback 0
R1(config-if)# ip address 1.1.1.1 255.255.255.255
R1(config-if)# exit

# On configure l'OSPF avec les networks
R1(config)# router ospf 1
R1(config-router)# router-id 1.1.1.1
R1(config-router)# network 192.168.1.0 0.0.0.3 area 0
R1(config-router)# network 192.168.3.0 0.0.0.3 area 0
R1(config-router)# network 1.1.1.1 0.0.0.0 area 0
R1(config-router)# exit
R1# debug ip ospf adj
```

## R2 : 

```
# On attribue l'adresse IP aux interfaces
en
conf t
interface fa0/0
ip add 192.168.1.2 255.255.255.252
no shut
exit

interface fa2/0
ip add 192.168.2.1 255.255.255.252
no shut

# On configure l'interface de loopback
R2(config)# interface loopback 0 
R2(config-if)# ip address 2.2.2.2 255.255.255.255 
R2(config-if)# exit 

# On configure l'OSPF avec les networks
R2(config)# router ospf 1 
R2(config-router)# router-id 2.2.2.2 
R2(config-router)# network 192.168.1.0 0.0.0.3 area 0 
R2(config-router)# network 192.168.2.0 0.0.0.3 area 0 
R2(config-router)# network 2.2.2.2 0.0.0.0 area 0 
R2(config-router)# exit 
R2# debug ip ospf adj
```

## R3 : 

```
# On attribue l'adresse IP aux interfaces
en
conf t
interface fa1/0
ip add 192.168.3.2 255.255.255.252
no shut
exit

interface fa2/0
ip add 192.168.2.2 255.255.255.252
no shut

# On configure l'interface de loopback
R3(config)# interface loopback 0 
R3(config-if)# ip address 3.3.3.3 255.255.255.255 
R3(config-if)# exit 

# On configure l'OSPF avec les networks
R3(config)# router ospf 1 
R3(config-router)# router-id 3.3.3.3 
R3(config-router)# network 192.168.3.0 0.0.0.3 area 0 
R3(config-router)# network 192.168.2.0 0.0.0.3 area 0 
R3(config-router)# network 3.3.3.3 0.0.0.0 area 0 
R3(config-router)# exit 
R3# debug ip ospf adj
```

## Commandes pour la vérification : 

```
show ip ospf neighbor
show ip protocols
show ip ospf interface brief
```

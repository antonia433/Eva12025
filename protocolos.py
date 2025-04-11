OSPF = 110
RIP = 120
EIGRP = 90
BGP = 20

pregunta = str(input("De que Protoclo desea saber la Distancia Administrativa?:"))

if pregunta ==str("OSPF"):
    print("La Distancia Administrativa del Protocolo OSPF es "+ str(OSPF))
elif pregunta ==str("RIP"):
    print("Ls Distancia Administrativa del Protocolo RIP es "+ str(RIP))
elif pregunta ==str("EIGRP"):
    print("La Distanica Administrativa del Protocolo EIGRP es "+ str(EIGRP))
elif pregunta ==str("BGP"): 
    print("La Distancia Administrativa del Protocolo BGP es "+ str(BGP))   
else:
    print("Escribe un nombre valido para el protocolo /n(Por ejemplo OSPF, RIP, EIGRP O BGP) ")
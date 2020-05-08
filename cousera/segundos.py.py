segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

b = total_segs // 3600
a = b // 86400
seg_restantes = total_segs % 3600
c = seg_restantes // 60
d = seg_restantes % 60

if (b >= 24): 
	a = int(b / 24)
	b = int(b % 24)

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")

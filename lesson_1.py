Osh = int(input('температура в Ошской области... '))
JalalAbad = int(input('температура в Джалал-Абаде... '))
Chui = int(input('температура в Чуйской области... '))
IssikKul = int(input('температура в Иссик-Кульской области... '))
Naaryn = int(input('температура в Наарынской области... '))
Talas = int(input('температура в Талаской области... '))
Batken = int(input('температура в Баткенской области... '))
result = ((Osh + JalalAbad + Chui + IssikKul + Naaryn + Talas + Batken) / 7)


print(f'Средний показатель температуры воздуха по КР на сегодня {round(result,1)} °C.')

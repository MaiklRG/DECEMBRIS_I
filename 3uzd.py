# Izveidot Python programmu, kas pārbauda, vai ievadītais skaitlis ir nepāra, izmantojot if priekšrakstu.
a=int(input("Ievadi skaitli:"))
#print(bool(a))
nepara_skaitlis=[]
for skaitlis in a:
    if skaitlis%2!=0:
        nepara_skaitlis.append(skaitlis)
        print(nepara_skaitlis)
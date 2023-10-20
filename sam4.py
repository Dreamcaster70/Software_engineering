prhase=str(input('Введите предложение на английском языке: ').lower())
count=0
for i in prhase:
    if i == 'a' or i == 'e' or i == 'i' or i =='o' or i =='u':
        count+=1
new_prhase=prhase.replace("ugly", "beauty")
print(f"Длина предложения:{len(prhase)},\n предложение в нижнем регистре:{prhase.lower()},\n количество гласных:{count},"
      f"\nНовое предложение:{new_prhase},\n Начинается ли предложение с 'the' {prhase.startswith('the')}"
      f"\n Заканчивается ли предложение на 'end'{prhase.endswith('end')}")






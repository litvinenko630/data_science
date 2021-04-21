total = int(input("Введите количество секунд: "))
seconds = total % 60
minutes = int(((total - seconds) / 60) % 60)
hours = int((total - seconds - minutes * 60) / 3600)
print(f"{hours:02}:{minutes:02}:{seconds:02}")

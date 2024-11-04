import matplotlib.pyplot as plt

# Функция для загрузки данных из одного файла
def readlog (filename):
    with open(filename,'r') as file:
        a = 0
        all_time, all_memori = 0.0, 0.0
        for line in file:
            time,memori = line.strip().split(',')
            a += 1
            all_time = all_time + float(time)
            all_memori = all_memori+float(memori)
            #print(f'{time} , {memori} , {a}')
        all_time = all_time / a
        all_memori = all_memori / a
    return all_time, all_memori

as_time, as_memory = readlog('acinhio_task1.log')
mult_time, mult_memory = readlog('multiprocessing_task1.log')
tread_time, tread_memory = readlog('treading_task1.log')

# Создаем фигуру и оси
fig, ax1 = plt.subplots()

# Строим первый график (левая ось)
ax1.bar('asynh1', as_time, color='b')
ax1.bar('mult1', mult_time, color='b')
ax1.bar('tread1', tread_time, color='b')
ax1.set_ylabel('Время', color='b')
ax1.tick_params('y', colors='b')

# Создаем вторую ось
ax2 = ax1.twinx()

# Строим второй график (правая ось)
ax2.bar('asynh2', as_memory, color='r')
ax2.bar('mult2', mult_memory, color='r')
ax2.bar('tread2', tread_memory, color='r')
ax2.set_ylabel('Память', color='r')
ax2.tick_params('y', colors='r')

# Заголовки и метки
plt.xlabel('Категории')
plt.title('Сравнение подходов асинхронного програмирования\nработа с сетевыми данными')
#plt.xticks(5, ['Категория 1', 'Категория 2', 'Категория 3'])
plt.savefig('task1.jpg')
plt.show()
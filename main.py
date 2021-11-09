from kmean import *
import numpy
import matplotlib.pyplot as plt
import csv

checkData = netbook_read("data_iris.txt")
print(checkData)
mainData = []
mainDataTwoPar = []
for i in range(len(checkData)):
    mainData.append([checkData[i][0], checkData[i][1], checkData[i][2], checkData[i][3]])
    mainDataTwoPar.append([checkData[i][2], checkData[i][3]])

klasters = 3# Количество кластеров
iterators = 20# Количество итераций
eps = 0.0000001

labelsFourPar = kmeans(klasters, iterators, mainData, eps)
labelsTwoPar = kmeans(klasters, iterators, mainDataTwoPar, eps)

clustering_assessment(labelsFourPar, checkData, 4)
clustering_assessment(labelsTwoPar, checkData, 2)


'''
Data = netbook_read("data_iris.txt")# Имя файла
Data_2 = list()
for i in range(len(Data)):
    Data_2.append(Data[i].copy())
    Data[i].pop(4)
klasters = 3# Количество кластеров
iterators = 20# Количество итераций
eps = 0.0000001
S = [[0 for i in range(2)] for i in range(3)]
'''

'''
Data = []
Data_2 = []
with open("train.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        a = []
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # 0 - Id пассажира
            # 1 - Выжил ли
            # 2 - Класс пассажира !
            # 3 - Имя
            # 4 - Пол !
            # 5 - Возарст !
            # 6 - кол-во братьев, сестёр !
            # 7 - кол-во родителей, детей !
            # 8 - номер билета
            # 9 - плата за проезд !
            # 10 - каюта
            # 11 - порт посадки !
            a.append(float(row[2]) * 3)
            if row[5] == '':
                a.append(0)
            else:
                a.append(float(row[5]) / 15)
            a.append(float(row[6]))
            a.append(float(row[7]))
            a.append(float(row[9]) / 150)
            if row[4] == "female":
                a.append(0)
            else:
                a.append(5)
            if row[11] == "C":
                a.append(0)
            elif row[11] == "S":
                a.append(3)
            else:
                a.append(6)
            Data.append(a.copy())
            a.append(float(row[1]))
            Data_2.append(a)
        count += 1

print("Data:", Data)
klasters = 2# Количество кластеров
iterators = 20# Количество итераций
eps = 0.0000001

labels = kmeans(klasters, iterators, Data, eps)# Кластеризация
clustering_assessment(labels, Data_2, 7)
import random
#labels[0] = [random.randint(0, 1) for i in range(len(Data))]
Vn_clustering_assessment(labels[0], Data, labels[1], 7)

Data = numpy.nan_to_num(Data)
fig, ax = plt.subplots()
plt.scatter(Data[:, 2], Data[:, 3], c=labels[0])
plt.xlabel('Количество братьев/сестёр', fontsize=17)
plt.ylabel('Количество детей/родителей', fontsize=17)
fig.savefig('Age_Salary_3')
plt.show()

fig, ax = plt.subplots()
plt.scatter(Data[:, 1], Data[:, 4], c=labels[0])
plt.xlabel('Возраст пассажира', fontsize=17)
plt.ylabel('Стоимость билета', fontsize=17)
fig.savefig('Age_Salary_3')
plt.show()
'''
'''
#================================= 4 признака =======================================

labels = kmeans(klasters, iterators, Data, eps)# Кластеризация
clustering_assessment(labels, Data_2, 4)
Vn_clustering_assessment(labels[0], Data, labels[1], 4)
#print(labels[0])
#================================= 2 признака =======================================

for i in range(len(Data)):
    Data[i].pop(0)
    Data[i].pop(0)
    Data_2[i].pop(0)
    Data_2[i].pop(0)

labels = kmeans(klasters, iterators, Data, eps)# Кластеризация
clustering_assessment(labels, Data_2, 2)
Vn_clustering_assessment(labels[0], Data, labels[1], 2)


#График
Data = numpy.nan_to_num(Data)
fig, ax = plt.subplots()
plt.scatter(Data[:, 0], Data[:, 1], c=labels[0])
plt.xlabel('Длина стебля', fontsize=17)
plt.ylabel('Ширина стебля', fontsize=17)
fig.savefig('Age_Salary_3')
plt.show()
'''
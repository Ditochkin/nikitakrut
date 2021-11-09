import random
import numpy as np
import csv

#=============== Считывание данных блокнот ================================
def netbook_read(fname):
    Data = []
    with open(fname, "r") as f:
        A = False
        for line in f.readlines():
            if A:
                Data.append(line[0:-1].split(','))
                Data[-1][0] = float(Data[-1][0])
                Data[-1][1] = float(Data[-1][1])
                Data[-1][2] = float(Data[-1][2])
                Data[-1][3] = float(Data[-1][3])
                if Data[-1][4] == 'setosa':
                    Data[-1][4] = 0
                elif Data[-1][4] == 'versicolor':
                    Data[-1][4] = 1
                else:
                    Data[-1][4] = 2
            A = True
    return Data

#=============== Считывание данных ================================
def csv_read(fname):
    with open(fname) as f:
        reader = csv.reader(f)
        k = 0
        a = list()
        for row in reader:
            arr = row[0].split(',')
            for i in range(len(arr)):
                if k!=0 :
                    arr[i] = int(arr[i])
            if k != 0: a.append(arr[1:])
            k = 1
        return a

#======================================== Расстояние между точками =====================================================
def distance(p1, p2):
    d = 0
    for i in range(len(p1)):
        d = d + (p1[i] - p2[i]) * (p1[i] - p2[i])
    return d**0.5

def otklon(p1, p2):
    d = 0
    for i in range(len(p1)):
        d = d + (p1[i] - p2[i])
    return d**2

def approx(c1, c2):
    return (c1 + c2) / 2

def norm(p):
    d = 0
    for i in range(len(p)):
        d += p[i]**2
    return d ** (1/2)

#======================================== Кластеризация ================================================================
def kmeans(k_klaster, k_iter, data, Eps):
    Max = 0
    o = max(data)
    for i in range(len(o)):
        Max += o[i]
    Max = Max / len(o) / k_klaster
    #==================================== Список случайных центров =====================================================
    centers = []
    for i in range(k_klaster):
        centers.append(data[random.randint(0, len(data) - 1)])
        j = 0

        while(j < i):
            if distance(centers[j], centers[i]) < Max:
                j = 0
                centers.pop()
                centers.append(data[random.randint(0, len(data) - 1)])
            else:
                j += 1
    #==================================== Сдвиг центров ================================================================
    print(centers)
    for q in range(k_iter):
        dis_cen = [None for i in range(len(data))]
        S = [[0 for i in range(len(centers[0]))] for i in range(len(centers))]
        S1 = [[0 for i in range(len(centers[0]))] for i in range(len(centers))]
        centers_old = list()
        for i in range(len(data)):
            min = distance(data[i], centers[0])
            min_id = 0
            for j in range(len(centers)):
                x = distance(data[i], centers[j])
                if x < min:
                    min = x
                    min_id = j
            dis_cen[i] = min_id
            for j in range(len(S[0])):
                S[min_id][j] += data[i][j] * norm(data[i])
                S1[min_id][j] += data[i][j]

        for j in range(len(S)):
            for g in range(len(S[0])):
                centers[j][g] = S[j][g] / norm(S1[j])
    return ([dis_cen, centers])


def clustering_assessment(labels, Data, num):
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    for i in range(len(Data)):
        # Matrix[i, 4] - класстер
        # cl[Data[i][4]][1] - класс
        for j in range(len(Data) - i - 1):

            if labels[0][i] == labels[0][j + 1 + i] and Data[i][-1] == Data[j + 1 + i][-1]:
                TP += 1
            elif labels[0][i] == labels[0][j + 1 + i] and Data[i][-1] != Data[j + 1 + i][-1]:
                FP += 1
            elif labels[0][i] != labels[0][j + 1 + i] and Data[i][-1] == Data[j + 1 + i][-1]:
                FN += 1
            else:
                TN += 1
    print("Оценка качества кластеризации по ", num, "ми признакам:", sep="")
    print("TP = ", TP, "\nFP = ", FP, "\nFN = ", FN, "\nTN = ", TN, sep="")
    Rand = (TP + TN) / (TP + TN + FP + FN)
    print("Индекс Rand:", Rand)
    Jaccard = TP / (TP + FN + FP)
    print("Индекс Jaccard:", Jaccard)
    FM = ((TP / (TP + FP)) * (TP / (TP + FN))) ** (1 / 2)
    print("Индекс Fowlkes-Mallows:", FM)
    print()

def Vn_clustering_assessment(labels, data, centers, num):
    Cluster_Cohesion = 0
    Cluster_Separation = 0
    for i in range(len(labels)):
        Cluster_Cohesion += otklon(centers[labels[i]], data[i])
    print(centers)
    k = 0
    for i in range(len(centers)):
        for j in range(len(labels)):
            if labels[j] != i:
                k += 1
                Cluster_Separation += otklon(centers[i], data[j])
    print("K =", k)
    print("Внутренния оценка качества кластеризации по ", num, " признакам:", sep="")
    print("Cluster Cohesion:", Cluster_Cohesion)
    print("Cluster Separation", Cluster_Separation)


from PySide2 import QtWidgets
from PySide2.QtWidgets import QFileDialog
from ui_test import Ui_MainWindow
import sys
import sympy as sym
import math
import networkx as nx
import matplotlib.pyplot as plt
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
import pyqtgraph as pg

c = sym.symbols('c:100', real=True) # можно также использовать var


# def getfile(self):
#    fname = QFileDialog.getOpenFileName(self, 'Open file',
#                                        'c:\\', "Файлы в формате SIF (*.sif)")
#    self.le.setPixmap(QPixmap(fname))

def getfile(self):
    dlg = QFileDialog()
    dlg.setFileMode(QFileDialog.AnyFile)
    #qdir = QDir()
    #qdir.setNameFilters(["*.sif"])
    #dlg.setFilter(qdir)#"Файлы в формате SIF (*.sif)")
    filenames = []

    if dlg.exec_():
        filenames = dlg.selectedFiles()
        f = open(filenames[0], 'r')

        with f:
            data = f.readlines()
            self.fileName.setText(filenames[0])
            return data
    return [False]
def distance(i, G):    
        #global S
        n = G.number_of_nodes()
        gr = [[] for i in range(0,n+1)]
        S = [0]*n # число вершин на расстояниях 0..(n-1)
        S[0] = 1

        for e in G.edges():
            gr[e[0]].append(e[1])
            gr[e[1]].append(e[0])
        p=[-1]*(n+1)
        d=[n + 1]*(n+1)
        d[i] = 0
        fire=[]
        used=[0]*(n+1)
        fire.append(i)
        used[i]=1
        while len(fire) !=0:
            u=fire[0]
            fire=fire[1:]
            for v in gr[u]:
                if used[v]==0:
                    fire.append(v)
                    used[v]=1
                    p[v]=u
                    d[v] = min(d[v], d[u] + 1)
                    S[d[v]] = S[d[v]] + 1
        return S
    
def f(i, G): # функционал для i через кратчайшие пути, i>=1
    global c
    #S = []
    maxLength = G.number_of_nodes() - 1
    S = distance(i,G)
    #print(S)
    p = sum(c[k]*S[k] for k in range(1,maxLength + 1))
    return sym.symbols('alpha')**p
        


def entropy_S(G): # через функционал (3)
    s = 0
    temp = sum(f(i,G) for i in G.nodes())
    for i in G.nodes():
        s = s+ f(i,G)/temp*sym.log(f(i,G)/temp)
    return -s

def entropy_SC(G):  # через функционал (2)
    s = 0
    R = []
    l = []
    for item in nx.algorithms.subgraph_centrality(G).items():
        R.append(round(item[1] - 1, 2))
    temp = sum(sym.symbols('alpha') ** R[i - 1] for i in G.nodes())
    for i in G.nodes():
        s = s + sym.symbols('alpha') ** R[i - 1] / temp * sym.log(sym.symbols('alpha') ** R[i - 1] / temp)
    return -s



class Aplct(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)
        self.show()
        self.uploadNetwork.clicked.connect(self.uploadNet)
        self.visualNetwork.clicked.connect(self.visualizeNet)

    def visualizeNet(self):
        global G
        plt.close()
        plt.figure(figsize=(10, 10))
        plt.clf()
        nx.draw(G, with_labels = True)
        plt.show()

    def uploadNet(self):
        if self.formatNet.currentRow() == 1:
            self.infoNetwork.setText("Этот формат пока недоступен, выберите другой"
                                     )
            return
        data = getfile(self)
        if data[0] == False:
            return
        # y = [2,4,6,8,10,12,14,16,18,20]
       # self.infoNetwork.setText(edges[0])#edges[0][0]+edges[0][1])
        global G
        try:
            G = nx.Graph()
            G1 = nx.Graph()
            # G2=nx.Graph()
            # G1.add_edges_from([(1,2),(1,3),(2,3),(1,4),(4,5),(2,5),(4,6),(5,6)])
            edges = [(x.split()[0], x.split()[2]) for x in data]
            G.add_edges_from(edges)#[(1,5),(1,3),(2,3),(1,4),(4,2),(2,5),(4,6),(5,6)])
            self.infoNetwork.setText("Число вершин в сети =" + str(G.number_of_nodes()) + '\n' +
                                     "Число ребер в сети =" + str(G.number_of_edges())
                                     )
            self.visualNetwork.setEnabled(True)

            p = dict()
            i = 1
            for e in edges:
                if not (e[0] in p.keys()):
                    p[e[0]] = i
                    i += 1
                if not (e[1] in p.keys()):
                    p[e[1]] = i
                    i += 1
            edges_numerated = [(p[x[0]], p[x[1]]) for x in edges]

            G1.add_edges_from(edges_numerated)
            #self.infoNetwork.setText(' '.join(list(map(str, G1.nodes()))))
            S1 = entropy_S(G1)
            lat = sym.latex(S1)
            plt.clf()
            # add text
            plt.figure(figsize=(20, 3))
            plt.text(0, 0.6, r"$%s$" % lat, fontsize=20)

            # hide axes
            fig = plt.gca()
            fig.axes.get_xaxis().set_visible(False)
            fig.axes.get_yaxis().set_visible(False)
           # plt.draw()  # or savefig
            #plt.show()
            #for i in range(1, G.number_of_nodes()+1):
            #    S1= S1.subs(c[i],1)
            #S1.subs(c[1], 4).subs(c[2], 3).subs(c[3], 2)
            plt.savefig('entropy_1.png')
            plt.clf()
            plt.close()
            S2 = entropy_SC(G1)
            self.entropy_shortest.setText(str(S1))
            self.entropy_closed.setText(str(S2))
            lat = sym.latex(S2)

            # add text
            plt.figure(figsize=(20, 3))
            plt.text(0, 0.6, r"$%s$" % lat, fontsize=20)

            # hide axes
            fig = plt.gca()
            fig.axes.get_xaxis().set_visible(False)
            fig.axes.get_yaxis().set_visible(False)
           # plt.draw()  # or savefig
            #plt.show()
            plt.savefig('entropy_2.png')
            plt.clf()
            plt.close()
        # nx.draw(G2)
        except Exception:
            self.infoNetwork.setText("Неверный формат данных!")

if __name__ == '__main__':
    
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Сздание инстанса класса
    calc = Aplct()
    # Запуск
    sys.exit(app.exec_())

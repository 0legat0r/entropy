from PySide2 import QtWidgets
from ui import Ui_MainWindow
import sys
import sympy as sym
import math
import networkx as nx
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import pyqtgraph as pg

"""
G1=nx.Graph()
G2=nx.Graph()
G1.add_edges_from([(1,2),(1,3),(2,3),(1,4),(4,5),(2,5),(4,6),(5,6)])
G2.add_edges_from([(1,5),(1,3),(2,3),(1,4),(4,2),(2,5),(4,6),(5,6)])
#nx.draw(G1)
nx.draw(G2)
c = sym.symbols('c:100', real=True) # можно также использовать var
#print(c)

"""
c = sym.symbols('c:100', real=True) # можно также использовать var

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

class Aplct(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Создание формы и Ui (наш дизайн)
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.digit_pressed)
        self.textEdit.setText('0')
        



    def digit_pressed(self):
        y = [2,4,6,8,10,12,14,16,18,20]
        G1=nx.Graph()
        G2=nx.Graph()
        G1.add_edges_from([(1,2),(1,3),(2,3),(1,4),(4,5),(2,5),(4,6),(5,6)])
        G2.add_edges_from([(1,5),(1,3),(2,3),(1,4),(4,2),(2,5),(4,6),(5,6)])
        nx.draw(G1)
        S1=entropy_S(G1)
        S1.subs(c[1],4).subs(c[2],3).subs(c[3],2)
        
        self.textBrowser.setText(str(S1))
        
        #nx.draw(G2)
        plt.show()
        
    
    
        
if __name__ == '__main__':
    
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Сздание инстанса класса
    calc = Aplct()
    # Запуск
    sys.exit(app.exec_())

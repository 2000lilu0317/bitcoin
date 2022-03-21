# for plot
from django.shortcuts import render
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64

def create_graph(x_list,t_list,x_predict):
    plt.cla()
    plt.plot(t_list, x_list, label="real")
    plt.plot(t_list, x_predict, label="predict")
    plt.xlabel('date')
    plt.xticks(rotation=90)
    plt.ylabel('price(yen)')
    plt.legend()

def get_image():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_image_list(x_list,t_list):
    graph_list = []
    create_graph(x_list[-24:],t_list[-24:],x_list[-24:]*1.1)
    graph_list.append(get_image())
    create_graph(x_list[-120:],t_list[-120:],x_list[-120:]*1.1)
    graph_list.append(get_image())
    create_graph(x_list[-720:],t_list[-720:],x_list[-720:]*1.1)
    graph_list.append(get_image())
    create_graph(x_list[-4320:],t_list[-4320:],x_list[-4320:]*1.1)
    graph_list.append(get_image())
    return graph_list
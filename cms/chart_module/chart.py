# for plot
from django.shortcuts import render
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64

def create_graph(x_list,t_list):
    plt.cla()
    plt.plot(t_list, x_list, label="x")
    plt.xlabel('t')
    plt.ylabel('x')

def get_image():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
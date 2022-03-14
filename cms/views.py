# for prediction
from django.views.generic.base import TemplateView
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.models import Sequential
import numpy as np
import pandas as pd
import os

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

def create_model():
    model=Sequential()
    model.add(Dense(16,activation="relu",input_shape=(16,)))
    model.add(Dense(16,activation="relu"))
    model.add(Dense(64,activation="relu"))
    model.add(Dense(1))
    return model

def predict():
    model = create_model()
    model.load_weights('./cms/param.hdf5')
    df = pd.read_csv("./cms/price-data-re.csv")
    df = df.sort_index(axis='index',ascending=False)
    input_data = np.array([[df["終値"].iloc[-(i+1)] for i in range(16)]])
    return model.predict(input_data).flatten()

class BitcoinView(TemplateView):
    template_name = 'cms/bitcoin.html'

    def get_context_data(self,**kwargs):
        prediction = predict()

        df = pd.read_csv("./cms/price-data-re.csv")
        show_list = df["終値"]
        x_list = show_list
        t_list = range(len(show_list))
        create_graph(x_list, t_list)
        graph = get_image()

        context = super().get_context_data(**kwargs)
        context["pred"] = prediction[0]
        context["graph"] = graph
        return context
    
class EthereumView(TemplateView):
    template_name = 'cms/ethereum.html'

    def get_context_data(self,**kwargs):
        prediction = predict()

        df = pd.read_csv("./cms/price-data-re.csv")
        show_list = df["終値"]
        x_list = show_list
        t_list = range(len(show_list))
        create_graph(x_list, t_list)
        graph = get_image()

        context = super().get_context_data(**kwargs)
        context["pred"] = prediction[0]
        context["graph"] = graph
        return context

class AboutView(TemplateView):
    template_name = 'cms/about.html'

    def get_context_data(self,**kwargs):
        prediction = predict()

        df = pd.read_csv("./cms/price-data-re.csv")
        show_list = df["終値"]
        x_list = show_list
        t_list = range(len(show_list))
        create_graph(x_list, t_list)
        graph = get_image()

        context = super().get_context_data(**kwargs)
        context["lists"] = {
            "Li Lu":"https://ca.slack-edge.com/T02UJKE1DM3-U033J3LTFJ4-8cb083f5dc2c-512",
            "Kouno Kazuma":"https://avatars.slack-edge.com/2022-02-10/3084805746754_ef576612ac0ea4b73a74_512.jpg",
            "KIMURA Nanako":"https://avatars.slack-edge.com/2022-02-09/3078572785586_262bec1d6d4ea5889e45_512.png",
        }
        return context
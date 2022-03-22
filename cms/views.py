from django.views.generic.base import TemplateView
import numpy as np
import pandas as pd
import datetime

from cms.module.predict import predict

from cms.chart_module.chart import get_image_list

pre_predict = [0,0]

class BitcoinView(TemplateView):
    template_name = 'cms/btn.html'

    def get_context_data(self,**kwargs):

        prediction = predict("btn")
        diff = pre_predict[0]-prediction
        pre_predict[0] = prediction

        df = pd.read_csv("cms/module/btnjpy_hour.csv")
        show_list = df["ClosePrice"]
        x_list = show_list
        t_list = df["CloseTime"]
        x_predict = pd.read_csv("cms/module/btn_predict.csv")["price"]
        new_list = [datetime.datetime.fromtimestamp(d) for d in t_list]
        graph_list = get_image_list(x_list, x_predict, new_list)

        context = super().get_context_data(**kwargs)
        context["pred"] = prediction
        context["diff"] = diff
        context["graph_list"] = graph_list
        return context
    
class EthereumView(TemplateView):
    template_name = 'cms/eth.html'

    def get_context_data(self,**kwargs):

        prediction = predict("eth")
        diff = pre_predict[1]-prediction
        pre_predict[1] = prediction

        df = pd.read_csv("cms/module/ethjpy_hour.csv")
        show_list = df["ClosePrice"]
        x_list = show_list
        t_list = df["CloseTime"]
        x_predict = pd.read_csv("cms/module/eth_predict.csv")["price"]
        new_list = [datetime.datetime.fromtimestamp(d) for d in t_list]
        graph_list = get_image_list(x_list, x_predict, new_list)

        context = super().get_context_data(**kwargs)
        context["pred"] = prediction
        context["diff"] = diff
        context["graph_list"] = graph_list
        return context

class AboutView(TemplateView):
    template_name = 'cms/about.html'

    def get_context_data(self,**kwargs):

        context = super().get_context_data(**kwargs)
        context["lists"] = {
            "Li Lu":"https://ca.slack-edge.com/T02UJKE1DM3-U033J3LTFJ4-8cb083f5dc2c-512",
            "Kouno Kazuma":"https://avatars.slack-edge.com/2022-02-10/3084805746754_ef576612ac0ea4b73a74_512.jpg",
            "KIMURA Nanako":"https://avatars.slack-edge.com/2022-02-09/3078572785586_262bec1d6d4ea5889e45_512.png",
        }
        return context
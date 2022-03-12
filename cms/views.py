from django.views.generic.base import TemplateView
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.models import Sequential
import numpy as np
import pandas as pd
import os

def create_model():

    model=Sequential()
    model.add(Dense(16,activation="relu",input_shape=(16,)))
    model.add(Dense(16,activation="relu"))
    #色々modelの構造をいじってみて実験すると良い。下のコメントを外すだけでもまた形状が変化する。
    model.add(Dense(64,activation="relu"))
    model.add(Dense(1))

    return model

class TopView(TemplateView):
    template_name = 'cms/top.html'

    def get_context_data(self,**kwargs):
        model = create_model()
        model.load_weights('./cms/param.hdf5')
        df = pd.read_csv("./cms/price-data-re.csv")
        df = df.sort_index(axis='index',ascending=False)
        input_data = np.array([[df["終値"].iloc[-(i+1)] for i in range(16)]])
        prediction = model.predict(input_data).flatten()

        context = super().get_context_data(**kwargs)
        context["pred"] = prediction
        return context
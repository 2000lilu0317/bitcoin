from cms.module.model_edited import create_model
import pandas as pd
import numpy as np

def predict(name):

    #モデルの読み込み
    model = create_model()

    #学習した重みを読み込み
    #先にtrain.pyを実行していないと、param.hdf5が存在しないのでエラーになる
    load_path = "cms/module/{}_param.hdf5"
    model.load_weights(load_path.format(name))

    #学習したデータを使って今日の終値予測

    #予測に使うデータを準備
    path = "cms/module/{}jpy_hour.csv"
    df = pd.read_csv(path.format(name))

    #入力データ
    input_data = np.array([[df["ClosePrice"].iloc[-(i+1)] for i in range(16)]])

    #推論値
    prediction = model.predict(input_data).flatten()[0]
    return prediction
from cms.module.model_edited import create_model
import pandas as pd
import numpy as np

import lightgbm as lgb #LightGBM

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

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
    return format(prediction, '.1f')


def predict2(name,other):
    path = "cms/module/{}jpy_day.csv"
    df = pd.read_csv(path.format(name))
    df2 = pd.read_csv(path.format(other))
    for i in range(21):
        df["ClosePrice-"+str(i+1)]=df["ClosePrice"].shift(i+1)
    # for i in range(16):
    #     df["前日比%-"+str(i+1)]=df["前日比%"].shift(i+1)
    for i in range(16):
        df2["ClosePrice-"+str(i+1)]=df2["ClosePrice"].shift(i+1)

    X = pd.concat([df[["ClosePrice-"+str(i+1) for i in range(21)]],df2[["ClosePrice-"+str(i+1) for i in range(16)]]],axis=1)
    X = X.dropna(how="any").values
    y = df.dropna(how="any")['ClosePrice'].values


    model = lgb.LGBMRegressor() # モデルのインスタンスの作成
    model.fit(X, y) # モデルの学習

    input_data = np.concatenate([[df["ClosePrice"].iloc[-(i+1)] for i in range(21)],[df2["ClosePrice"].iloc[-(i+1)] for i in range(16)]]).reshape(1, -1)

    #推論値
    prediction = model.predict(input_data)[0]
    return format(prediction, '.1f')
from cms.module.model_edited import create_model
from tensorflow.keras.layers import Activation, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from csv import writer

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

def train(name):

    #モデルの作成
    model = create_model()

    #Deep Learning モデルの形状を表示
    #print(model.summary())

    #modelをコンパイル（最小化しようとする損失関数--ここでは自乗誤差--などを指定）する
    model.compile(loss='mse', optimizer=Adam(learning_rate=0.001), metrics=['mae'])

    #学習用データ
    path = "cms/module/{}jpy_hour.csv"
    df = pd.read_csv(path.format(name))

    #後のコードが書きやすいように訓練データを加工
    #よくわからない時はdfをprintで見てみると良い

    #同じ行に過去16時点の価格(予想に使う説明変数)と今の価格（目的変数）が並ぶようにする
    for i in range(16):
        df["ClosePrice-"+str(i+1)]=df["ClosePrice"].shift(i+1)

    df = df.dropna(how="any")

    #dfをnumpy配列に変換
    #訓練データ(train_x)は　過去16時点までの価格*行数　となっている
    train_x=df[["ClosePrice-"+str(i+1) for i in range(16)]].values
    train_y=df["ClosePrice"].values

    #注意）今回はコードの簡単さを重視して正規化などは無し
    #リターンの時系列などにする、といった工夫もなし

    # 学習の実行
    history = model.fit(train_x, train_y, epochs=400, validation_split=0.2, verbose=0)

    #学習結果をファイルに保存
    #成功するとディレクトリ内にparam.hdf5というファイルが生成される
    save_path = "cms/module/{}_param.hdf5"
    model.save_weights(save_path.format(name))

    input_data = np.array([[df["ClosePrice"].iloc[-(i+1)] for i in range(16)]])
    prediction = model.predict(input_data).flatten()[0]
    print("OKOKOKO")
    print(prediction)
    csv_path = "cms/module/{}_predict.csv"
    with open(csv_path.format(name), 'a') as f:
        write = writer(f)
        write.writerow([time.time(),prediction,])

# 必要なライブラリのインポート
import streamlit as st
import numpy as np
import pandas as pd

# タイトルとテキストを記入
st.title('Streamlit 基礎')
st.write('Hello World!')

# データフレームの準備
df = pd.DataFrame({
    '一列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})

# 動的なテーブル
st.dataframe(df)

# 引数を使用した動的テーブル
st.dataframe(df.style.highlight_max(axis=0), width=300, height=200)

# 静的テーブル
st.table(df)


# 【チャート表示】
# 10行3列のデータフレームをい準備
df1 = pd.DataFrame(
    np.random.rand(10, 3),
    columns = ['a', 'b', 'c']
)

# 折れ線グラフ
st.line_chart(df1)

# 面グラフ
st.area_chart(df1)

# 棒グラフ
st.bar_chart(df1)

# 【マップをプロット】
# 乱数をデータフレームで用意
df2 = pd.DataFrame(
    
    # 乱数 + 新宿の緯度と経度
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

# マップをプロット
# st.map(df2)


# 【画像の表示】
# Pillow
from PIL import Image

# 画像の読み込み
# img = Image.open('desktop.png')
# st.image(img, caption='desktop', use_column_width=True)


# 【インタラクティブなウィジェットの表示】
# チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('desktop.png')
    st.image(img, caption='desktop', use_column_width=True)

# セレクトボックス
option = st.selectbox(
    '好きな数字を入力してください。',
    list(range(1, 11))
)
'あなたの好きな数字は' , option , 'です。'

# テキスト入力による値の動的変更
text = st.text_input('あなたの好きなスポーツを教えてください。')

'あなたの好きなスポーツは', text

# スライダーによる値の動的変更
condition = st.slider('あなたの今の調子は？', 0, 1000, 500)

'コンディション : ', condition

# スライダーによる値の動的変更
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'コンディション : ', condition

# expander
expander1 = st.expander('質問１')
expander1.write('質問1の回答')

# プログレスバーの表示
import time

latest_iteration = st.empty()
bar = st.progress(0)

# バーを0.1秒ごとに進める
for i in range(100):
    latest_iteration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done'
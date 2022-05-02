#from turtle import left
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

st.write("Progress bar")
st.write("Start!!")
latest_interation = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_interation.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)
st.write("Done!!")

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("問合せ１")
expander1.write("問合せ回答１")
expander2 = st.expander("問合せ２")
expander2.write("問合せ回答２")
expander3 = st.expander("問合せ３")
expander3.write("問合せ回答３")


option = st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1, 11))
)
st.write("あなたが好きな数字は", option, "です。")

st.sidebar.write("Interactive Widgets")
text = st.sidebar.text_input("あなたの趣味を教えてください。")
st.sidebar.write("趣味：", text)

condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
st.sidebar.write("コンディション：", condition)

st.write("Display Image")
if st.button("Show Image"):
    img = Image.open("./input/sample.jpg")
    st.image(img, caption="Sample Image", use_column_width=True)

st.write("DataFrame")
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a,', 'b', 'c']
)

if st.checkbox("Show Line Chart"):
    st.line_chart(df)
    st.dataframe(df.style.highlight_max(axis=0))
    st.table(df.style.highlight_max(axis=0))

"""
# Level1
## Level2
### Level3
```python
import streamlit as st
import numpy as np
import pandas as pd
"""

df2 = pd.DataFrame(
    np.random.rand(100, 2)/[20, 20] + [35.69, 139.70],
    columns=['lat', 'lon']
)
if st.checkbox("Show Map"):
    st.map(df2)
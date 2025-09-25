
import streamlit as st
import pandas as pd
import numpy as np

# 한글 폰트 설정 (matplotlib)
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# NanumGothic 폰트 경로
FONT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fonts/NanumGothic-Regular.ttf'))
if os.path.exists(FONT_PATH):
	fontprop = fm.FontProperties(fname=FONT_PATH)
	plt.rcParams['font.family'] = fontprop.get_name()
	plt.rcParams['axes.unicode_minus'] = False
	fm.fontManager.addfont(FONT_PATH)
else:
	st.warning('한글 폰트 파일을 찾을 수 없습니다.')

st.title('간단한 데이터 시각화')

# 임의의 데이터 생성
data = {
	'카테고리': ['A', 'B', 'C', 'D'],
	'값': np.random.randint(10, 100, 4)
}
df = pd.DataFrame(data)

st.subheader('데이터프레임')
st.dataframe(df)

st.subheader('Bar Chart')
st.bar_chart(df.set_index('카테고리'))

st.subheader('Matplotlib Bar Chart (한글 폰트 적용)')
fig, ax = plt.subplots()
ax.bar(df['카테고리'], df['값'], color='skyblue')
ax.set_xlabel('카테고리', fontproperties=fontprop if os.path.exists(FONT_PATH) else None)
ax.set_ylabel('값', fontproperties=fontprop if os.path.exists(FONT_PATH) else None)
ax.set_title('카테고리별 값 (한글 폰트)', fontproperties=fontprop if os.path.exists(FONT_PATH) else None)
if os.path.exists(FONT_PATH):
	for label in (ax.get_xticklabels() + ax.get_yticklabels()):
		label.set_fontproperties(fontprop)
st.pyplot(fig)

st.subheader('Line Chart (임의의 시계열 데이터)')
chart_data = pd.DataFrame(
	np.random.randn(20, 3),
	columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

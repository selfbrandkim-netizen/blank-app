import streamlit as st

st.title("🎈 아문의 앱")
st.write(
    "아문입니다. [docs.streamlit.io](https://docs.streamlit.io/)."
)

# 정보성 메시지 박스
st.info("ℹ️ 정보 메시지입니다.")
st.warning("⚠️ 경고 메시지입니다.")
st.success("✅ 성공 메시지입니다.")
st.error("❌ 오류 메시지입니다.")


import streamlit as st
import pandas as pd

st.info("📘 누구나 볼 수 있도록 공개된 시트를 Pandas로 직접 불러오는 가장 간단한 방법입니다.\n📎 링크는 반드시 `export?format=csv` 형태로 설정하세요.")

csv_url1 = "https://docs.google.com/spreadsheets/d/1VC_q8HJfIufjGVR2zGRcJjBgkefIbp6Pv01rQ1uvoXI/export?format=csv"
df1 = pd.read_csv(csv_url1)
st.dataframe(df1)

# `choice` 항목을 카운트한 후 막대그래프로 표시합니다.
counts = df1["choice"].value_counts()
st.write("## `choice` 항목별 빈도수")
st.bar_chart(counts)

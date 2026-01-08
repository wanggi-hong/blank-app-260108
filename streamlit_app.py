"""
Streamlit 위젯 데모 페이지

이 파일은 교육용으로 제작된 단일 페이지 데모입니다.
각 위젯의 사용 예시와 함께 한국어 주석(설명)을 풍부하게 추가했습니다.
실행: streamlit run streamlit_app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from PIL import Image
import io

# ------------------------------
# 페이지 기본 메타/제목
# ------------------------------
st.set_page_config(page_title="Streamlit 위젯 데모", layout="wide")

st.title("🔧 Streamlit 위젯 데모 — 한 페이지로 보는 주요 요소들")
st.caption("각 위젯 아래의 주석을 읽으며 직접 값을 바꿔 보세요. 학습용으로 주석을 자세히 달았습니다.")

# ------------------------------
# 텍스트 및 마크다운 블록
# ------------------------------
st.header("1) 텍스트와 마크다운")
# st.write는 다양한 타입을 자동으로 렌더링합니다 (텍스트, 수치, 데이터프레임 등)
st.write("간단한 `st.write` 사용 예시: 문자열, 숫자, 리스트, 딕셔너리를 바로 렌더링합니다.")

# markdown, code, latex 등 교육용으로 보여주기
st.markdown("**굵은 텍스트**, *기울임*, `인라인 코드` 예시")
st.code("for i in range(5):\n    print(i)", language="python")
st.latex(r"E = mc^2")

# ------------------------------
# 정보/경고/에러 박스, metric
# ------------------------------
st.header("2) 상태 박스와 메트릭")
st.info("정보 메시지: 사용 안내나 상태를 보여줄 때 사용")
st.warning("경고 메시지: 사용자에게 주의를 요청할 때 사용")
st.error("에러 메시지: 오류를 표시할 때 사용")
st.metric(label="오늘의 온도", value="18°C", delta="+2°C")

# ------------------------------
# 입력 위젯 (인터랙티브)
# ------------------------------
st.header("3) 입력 위젯들 (버튼, 체크박스, 라디오, 셀렉트 등)")

st.subheader("버튼과 콜백")
# 버튼은 클릭 시 True를 반환합니다. on_click 콜백도 가능.
if st.button("클릭해 보세요 (st.button)"):
    st.success("버튼을 눌렀습니다 👏 — 버튼은 클릭 이벤트를 처리합니다.")

st.subheader("체크박스")
# 체크박스는 boolean 값을 반환합니다
if st.checkbox("체크박스 예시 (체크하면 보이는 텍스트)"):
    st.write("체크되어 있습니다 — 체크박스는 토글에 적합합니다.")

st.subheader("라디오, 셀렉트박스, 멀티셀렉트")
# 라디오는 단일 선택
radio_choice = st.radio("라디오 예시 (단일 선택)", ("옵션 A", "옵션 B", "옵션 C"))
st.write("선택한 항목:", radio_choice)

# selectbox는 드롭다운 단일 선택
selectbox_choice = st.selectbox("selectbox (드롭다운)", ["사과", "바나나", "체리"])
st.write("선택한 과일:", selectbox_choice)

# multiselect은 다중 선택
multi_choice = st.multiselect("multiselect (여러 개 선택)", ["파이썬", "자바스크립트", "루비"], default=["파이썬"])
st.write("선택한 언어:", multi_choice)

st.subheader("슬라이더와 숫자 입력")
# slider는 범위나 단일 값 선택
age = st.slider("나이 선택", min_value=0, max_value=120, value=30)
st.write("나이:", age)

# number_input은 정밀한 숫자 입력에 유용
num = st.number_input("숫자 입력 (정수)", min_value=0, max_value=100, value=10)
st.write("입력한 숫자:", num)

st.subheader("텍스트 입력과 텍스트 영역")
# text_input은 한 줄 입력, text_area는 여러 줄 입력
name = st.text_input("이름을 입력하세요", value="홍길동")
comment = st.text_area("코멘트를 입력하세요", value="여기에 작성하세요...")
st.write(f"안녕하세요, {name}님! 코멘트 길이: {len(comment)}")

# ------------------------------
# 날짜/시간/파일/이미지 입력 등
# ------------------------------
st.header("4) 날짜/시간/파일/미디어 입력")
col1, col2, col3 = st.columns(3)
with col1:
    date = st.date_input("날짜 선택")
    st.write("선택한 날짜:", date)
with col2:
    time = st.time_input("시간 선택")
    st.write("선택한 시간:", time)
with col3:
    uploaded_file = st.file_uploader("파일 업로드 (예: CSV)")
    if uploaded_file is not None:
        # 업로드된 CSV를 DataFrame으로 읽어 보여주기
        try:
            df = pd.read_csv(uploaded_file)
            st.write("업로드된 CSV 미리보기:")
            st.dataframe(df.head())
        except Exception as e:
            st.error("CSV 로드에 실패했습니다: " + str(e))

st.subheader("이미지/오디오/비디오 표시")
# 이미지 예시 (PIL을 사용해 메모리에서 생성)
img = Image.new('RGB', (200, 100), color=(73, 109, 137))
# `use_column_width`는 deprecated 되었으므로 `width`로 대체합니다. 이미지는 픽셀 너비(예: 200)를 지정합니다.
st.image(img, caption="PIL로 생성한 예시 이미지", width=200)

# 오디오/비디오 표시 (로컬 파일이 없으므로 샘플 바이트는 생략)
st.info("오디오/비디오는 업로드하거나 URL을 사용해 테스트할 수 있습니다.")

# ------------------------------
# 레이아웃: 컬럼, 익스팬더, 탭, 사이드바
# ------------------------------
st.header("5) 레이아웃과 컨테이너")
with st.expander("익스팬더 — 접었다가 펼치기 가능한 영역"):
    st.write("무게감 있는 도움말이나 긴 설명을 숨기고 싶을 때 사용하세요.")

left, right = st.columns([2, 1])
with left:
    st.subheader("왼쪽 컬럼")
    st.write("주 콘텐츠를 여기에 둡니다.")
with right:
    st.subheader("오른쪽 컬럼")
    st.write("보조 정보나 위젯을 배치하세요.")

st.subheader("탭 사용 예시")
tab1, tab2, tab3 = st.tabs(["탭 1", "탭 2", "탭 3"])
with tab1:
    st.write("탭 1의 내용")
with tab2:
    st.write("탭 2의 내용")
with tab3:
    st.write("탭 3의 내용")

st.sidebar.header("사이드바 예시")
sidebar_choice = st.sidebar.selectbox("사이드바 선택", ["옵션 1", "옵션 2"]) 
st.sidebar.write("사이드바에서 선택한 값:", sidebar_choice)

# ------------------------------
# 데이터 표시: table, dataframe, json, map
# ------------------------------
st.header("6) 데이터 및 차트 표시")
# 샘플 데이터 생성
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"]) 
st.line_chart(chart_data)

st.subheader("DataFrame / Table / JSON")
df = pd.DataFrame({"이름": ["Alice", "Bob", "Charlie"], "나이": [24, 30, 22]})
st.dataframe(df)  # 데이터프레임은 인터랙티브하게 정렬/검색 가능
st.table(df)      # table은 정적 표시
st.json({"key": "value", "numbers": [1, 2, 3]})

st.subheader("지도 (Map)")
# 랜덤 좌표 데이터를 만들어 지도에 표시
map_data = pd.DataFrame(np.random.randn(100, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"])
st.map(map_data.rename(columns={"lat": "lat", "lon": "lon"}))

# ------------------------------
# 차트 라이브러리 (Altair / Matplotlib)
# ------------------------------
st.header("7) 외부 차트 라이브러리 연동")

st.subheader("Altair 예시")
alt_chart = alt.Chart(chart_data.reset_index()).mark_area().encode(
    x="index", y="a"
)
st.altair_chart(alt_chart, use_container_width=True)

st.subheader("Matplotlib 예시")
fig, ax = plt.subplots()
ax.plot(chart_data.index, chart_data['b'], color='orange')
# 한글 폰트가 없을 경우 matplotlib에서 글리프 경고가 발생하므로 영어 제목으로 설정합니다.
ax.set_title('Matplotlib line chart example')
st.pyplot(fig)

# ------------------------------
# 양식(form) 및 세션 상태(session_state)
# ------------------------------
st.header("8) Form과 session_state")
with st.form("my_form"):
    st.write("폼 내부의 입력은 제출 버튼을 누를 때까지 적용되지 않습니다")
    input_text = st.text_input("폼 입력")
    input_number = st.number_input("폼 숫자 입력", min_value=0, max_value=10, value=5)
    submitted = st.form_submit_button("제출")
    if submitted:
        st.success(f"제출 완료 — 텍스트: {input_text}, 숫자: {input_number}")

st.subheader("session_state 예시: 카운터")
if 'counter' not in st.session_state:
    st.session_state.counter = 0

inc, dec = st.columns(2)
with inc:
    if st.button("증가 (+)"):
        st.session_state.counter += 1
with dec:
    if st.button("감소 (-)"):
        st.session_state.counter -= 1
st.write("현재 카운트:", st.session_state.counter)

# ------------------------------
# 동적 UI: placeholder, progress, spinner
# ------------------------------
st.header("9) 동적 UI 요소와 애니메이션")
placeholder = st.empty()  # 나중에 내용을 업데이트할 수 있는 자리 표시자
placeholder.info("여기에 동적으로 업데이트 되는 내용을 표시합니다.")

# 진행 표시기 예시
if st.button("진행 표시기 예시 실행" ):
    with st.spinner("작업 진행 중..."):
        for i in range(101):
            st.progress(i)
    st.success("작업 완료!")

# ------------------------------
# 유틸리티: cache, download 등
# ------------------------------
st.header("10) 유틸리티 및 팁")
st.write("st.cache_data/st.cache_resource를 사용하면 비용이 큰 계산을 캐시할 수 있습니다.")

# 다운로드 예시 (CSV로 변환하여 제공)
def to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = to_csv(df)
st.download_button("데이터프레임 다운로드 (CSV)", data=csv, file_name='sample.csv', mime='text/csv')

# ------------------------------
# 마무리 노트
# ------------------------------
st.markdown("---")
st.write("✅ 데모 끝 — 위젯을 직접 조작해 보시고 주석을 읽어보세요.")
st.caption("추가로 보고 싶은 위젯이나 동작(예: 웹소켓, 실시간 업데이트 등)이 있으면 알려주세요.")

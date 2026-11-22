import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 추천", page_icon="🍱", layout="centered")

# 카테고리별 점심 메뉴 데이터
MENU_DATA = {
    "한식": ["김치찌개", "된장찌개", "제육볶음", "비빔밥", "국밥", "불고기", "칼국수", "돈까스"],
    "중식": ["짜장면", "짬뽕", "탕수육 세트", "마라탕", "볶음밥", "마파두부덮밥"],
    "일식": ["초밥", "라멘", "우동", "규동", "카레라이스", "메밀소바", "가츠동"],
    "양식/기타": ["파스타", "수제버거", "피자", "샌드위치", "쌀국수", "타코", "샐러드"]
}

# 앱 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("무엇을 먹을지 고민될 때 버튼을 눌러보세요!")
st.divider()

# 카테고리 선택 (다중 선택 가능)
selected_categories = st.multiselect(
    "원하는 음식 종류를 선택하세요 (비워두면 전체에서 추천):",
    options=list(MENU_DATA.keys()),
    default=list(MENU_DATA.keys())
)

# 선택된 카테고리의 메뉴들을 하나의 리스트로 합치기
candidate_menus = []
if selected_categories:
    for category in selected_categories:
        candidate_menus.extend(MENU_DATA[category])
else:
    # 아무것도 선택하지 않았을 경우 전체 메뉴를 후보로 설정
    for menus in MENU_DATA.values():
        candidate_menus.extend(menus)

# 추천 버튼
if st.button("🎲 오늘의 메뉴 추천받기", type="primary", use_container_width=True):
    chosen_menu = random.choice(candidate_menus)
    
    st.balloons() # 축하 풍선 효과
    st.success(f"### 🎉 오늘의 추천 메뉴는 **'{chosen_menu}'** 입니다!")

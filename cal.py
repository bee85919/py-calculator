import streamlit as st

# 계산기 함수: 사용자로부터 입력된 수식을 계산
def calculator(expression):
    try:
        result = eval(expression)
        if len(str(result)) > 10:  # 결과가 10자리를 초과하면 오류 메시지 반환
            return '자리수 초과'
        return result
    except ZeroDivisionError:  # 0으로 나누는 경우 처리
        return '숫자 아님'
    except:  # 그 외의 오류 처리
        return '오류'

# 앱의 전체 스타일을 지정하는 CSS 추가
st.markdown(
    """
    <style>
        .stTextInput input {
            border-radius: 15px;
            font-size: 25px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 7.5px;
            background-color: #967bb6;
            color: white;
            font-size: 25px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 앱 제목 설정
st.title("세뱃돈 계산기")
st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가

# 세션 상태에서 expression 값을 가져오거나 초기화
expression = st.session_state.get("expression", "")

# 계산기 버튼 레이아웃 설정
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '&ast;'],
    ['1', '2', '3', '&minus;'],
    ['0', '.', 'C', '&plus;'],
    ['=',]
]

# 버튼 생성 및 기능 구현
for row in buttons:
    cols = st.columns(4)
    for col, button_text in zip(cols, row):
        if col.button(f"{button_text}", use_container_width=True):
            if button_text == 'C':  # 'C' 버튼을 누르면 마지막 문자 삭제
                expression = expression[:-1]
            elif button_text == '=':  # '=' 버튼을 누르면 수식 계산
                result = calculator(expression)
                expression = str(result)
            else:  # 그 외의 버튼을 누르면 해당 문자 추가
                expression += button_text.replace('&plus;', '+').replace('&ast;', '*').replace('&minus;', '-')
            # 버튼 클릭 후 업데이트된 expression 값을 세션 상태에 저장
            st.session_state.expression = expression

# 업데이트된 expression 값을 사용하여 텍스트 입력 위젯 표시
expression = st.text_input("", expression, max_chars=None)

# 계산 결과 표시
st.markdown("<br>", unsafe_allow_html=True)  # 줄바꿈 추가
st.write("결과:", calculator(expression))

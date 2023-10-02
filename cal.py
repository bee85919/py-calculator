import streamlit as st

def calculator(expression):
    try:
        # 연산 수행
        result = eval(expression)
        # 10자리 숫자를 초과하면 'Infinity' 표시
        if len(str(result)) > 10:
            return 'Infinity'
        return result
    except ZeroDivisionError:  # 0으로 나누는 경우
        return '숫자 아님'
    except:
        return '오류'

st.title("세뱃돈 계산기")

expression = st.session_state.get("expression", "")

# 버튼 구현
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '\*'],
    ['1', '2', '3', '\-'],
    ['0', 'C', '=', '\+']
]

for row in buttons:
    cols = st.columns(4)
    for col, button_text in zip(cols, row):
        if col.button(button_text):
            if button_text == 'C':
                expression = expression[:-1]
            elif button_text == '=':
                result = calculator(expression)
                expression = str(result)
            else:
                expression += button_text

st.session_state.expression = expression
st.text_input("입력창", expression)

if st.button("AC"):
    expression = ""
    st.session_state.expression = ""

st.write("결과:", calculator(expression))

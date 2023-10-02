import streamlit as st

def calculator(expression):
    try:
        result = eval(expression)
        if len(str(result)) > 10:
            return '자리수 초과'
        return result
    except ZeroDivisionError:
        return '숫자 아님'
    except:
        return '오류'

# CSS 스타일 추가
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

st.title("세뱃돈 계산기")

expression = st.session_state.get("expression", "")
expression = st.text_input("", expression, max_chars=None)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '\*'],
    ['1', '2', '3', '\-'],
    ['0', '.', 'C', '\+'],
    ['=',]
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

st.write("결과:", calculator(expression))

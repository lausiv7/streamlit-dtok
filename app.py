import streamlit as st
import pandas as pd

# 엑셀 파일 로드
csv_file = './test.csv'
df = pd.read_csv(csv_file)

# 로그인 함수
def login(username, password):

    # 첫 번째 행 출력
    row1 = df.iloc[0]
    print('Row 1:', row1)
    
    # 비밀번호를 문자열로 변환 숫자로 입력시 문자열로 인식안되어 처리안되는 문제 해결
    df['pw'] = df['pw'].astype(str)
    
    user = df[(df['id'] == username) & (df['pw'] == password)]
    
    print('User:', user)  # 입력한 id와 pw를 터미널에 출력
    if len(user) > 0:
        return user.iloc[0]['status']
    else:
        return 'Invalid credentials'

# 로그인 페이지 렌더링
def render_login_page():
    st.header('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        status = login(username, password)
        st.write('Status:', status)

# 메인 앱
def main():
    render_login_page()

if __name__ == '__main__':
    main()

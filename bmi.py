import streamlit as st 

def BMI(w, h):
    return w/(h*h)
    
#w = float(input('請輸入體重(KG)？'))
w = st.number_input('請輸入體重(KG)？')
#h = st.number_input('請輸入身高(M)？')
h = st.text_input('請輸入身高(M)？', '168')
h = float(h)

count=0
while(True):
    confirm_input=0
    confirm_input = st.button('輸入確認', key = count)
    if confirm_input:    
        h = st.text_input('請輸入身高(M)？', '168')
        st.write('體重肥胖')
    count += 1    

'''
confirm_input = st.button('輸入確認')
if confirm_input:
    bmi = BMI(w, h)
    #print('BMI為', bmi)
    st.write('BMI為', bmi)
    if (bmi < 18):
        st.write('體重過輕')
    elif (bmi < 24):
        st.write('體重正常')
    elif (bmi < 27):
        st.write('體重過重')
    else:
        st.write('體重肥胖')
'''

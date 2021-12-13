import streamlit as st

x = st.slider('Select a value')

car_simulation = {'gas_warning':2, 'speed_limit':100, 'temp_warning':30, '轉速':12000}
#gas = int(input('油量的資料收集:油箱滿是10格 =>'))
gas = st.slider('油量的資料收集:油箱滿是10格 =>', 0, 10, 8)

if gas <= car_simulation.get('gas_warning'):
  st.write('油箱只剩', gas, '格! 準備加油!!')
else:
  st.write('油箱還剩', gas, '格。')

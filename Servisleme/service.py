import streamlit as st
import pandas as pd
import pickle

#en iyi modeli yükle
model_path = r"C:\Users\baran\OneDrive\Masaüstü\Zeynep Baran\Algoritmalar\best_model_lightgbm.pkl"
with open(model_path, 'rb') as file:
    loaded_model = pickle.load(file)

# tabloları yükle
df = pd.read_excel(r"C:\Users\baran\OneDrive\Masaüstü\Zeynep Baran\Veri Toplama\SUN CREAM-ENCODED.xlsx")
df_brands = pd.read_excel(r"C:\Users\baran\OneDrive\Masaüstü\Zeynep Baran\Veri Toplama\brand.xlsx")
df_colors = pd.read_excel(r"C:\Users\baran\OneDrive\Masaüstü\Zeynep Baran\Veri Toplama\colors.xlsx")
df_types = pd.read_excel(r"C:\Users\baran\OneDrive\Masaüstü\Zeynep Baran\Veri Toplama\types.xlsx")
#spf = st.number_input('SPF', min_value=df['SPF'].unique().min(), max_value=df['SPF'].unique().max(), step=1)
#volume = st.number_input('Hacim (ml)', min_value=df['PRODUCT QUANTITY'].unique().min(), max_value=df['PRODUCT QUANTITY'].unique().max(), step=1)

st.title("Güneş Kremi Fiyat Tahmini")

#veri grişleri
brand = st.selectbox('Marka Seçin', df_brands["BRAND"].unique())
color = st.selectbox('Renk Seçin', df_colors["COLOR"].unique())
type_1 = st.selectbox('Tip Seçin', df_types["TYPE"].unique())
spf=st.selectbox('SPF değeri seçin',df["SPF"].unique())
volume=st.selectbox('Ürün miktarı seçiniz',df["PRODUCT QUANTITY"].unique())

#alınan verilerin encodedlananmış hallerinin indexlerini bul ve değerleri al 
encoding_index_brand = df_brands[df_brands["BRAND"] == brand].index[0]
brand_encoded=df_brands["BRAND_ENCODED"][encoding_index_brand]


encoding_index_color=df_colors[df_colors["COLOR"]==color].index[0]
color_encoded=df_colors["COLOR_ENCODED"][encoding_index_color]


encoding_index_type=df_types[df_types["TYPE"]==type_1].index[0]
type_1_encoded=df_types["TYPE_ENCODED"][encoding_index_type]


#alınan verilerle ynei bir df oluştur ve modele gönder
input_data = pd.DataFrame({'brand': [brand_encoded], 'color': [color_encoded], 'type': [type_1_encoded], 'SPF': [spf], 'volume_ml': [volume]})
input_df = pd.DataFrame(input_data)



# en iyi performanslı modeli kullanarak tahmin yap
prediction = loaded_model.predict(input_df)[0]

st.success(f'Olası fiyat: {prediction} TL')
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

def run():

    # membuat judul
    st.title('Premiere League Result Prediction')

    # membuat subheader
    st.subheader('Analisa Dataset English Premier League')

    #image
    image = Image.open('cc1.jpg')
    st.image(image, caption = 'Premiere League Result Prediction')

    # deskripsi
    st.write('Page ini dibuat oleh : Heru')
    st.write('Batch : HCK - 018')
    st.write('Bertujuan untuk melakukan prediksi hasil pertandingan Premiere league dan Odds pertandingan')

    # # bold
    st.write('## Exploratory Data Analysis (EDA)')

    # buat garis
    st.markdown('---')

    # show dataframe
    df1 = pd.read_csv('P1M2_Heru.csv',encoding='windows-1254')
    st.dataframe(df1)

    # buat garis
    st.markdown('---')

    # EDA 1
    st.write('#### Bagaimana Distribusi Hasil Pertandingan?')
    proportion = df1['FTR'].value_counts().reset_index()
    fig = px.pie(proportion, names="FTR", 
                values="count", 
                title="Dataset proportion",
                hover_data=["count"], 
                )
    st.plotly_chart(fig)
    # Deskripsi
    st.write('- Home win sebanyak 45% pada data')
    st.write('- Away win sebanyak 28.4% pada data')
    st.write('- Draw sebanyak 25.8% pada data')
    st.write('- Terjadi slightly imbalanced pada data')

    # buat garis
    st.markdown('---')

    # EDA 2
    st.write('#### Berapa Jumlah Pertandingan per Musim?')
    # Menghitung jumlah row per season
    totalMatch = df1['Season'].value_counts().reset_index()
    # visualisasi 
    fig2 = px.bar(totalMatch, x='Season', y='count', orientation='v',text_auto='.2s')
    fig2.update_layout(xaxis= dict(type='category', categoryorder = "category ascending"))
    st.plotly_chart(fig2)
     # Deskripsi
    st.write('- Jumlah match pada musim 1993-94 dan 1994-95 berjumlah 460, memiliki 80 match lebih banyak dibandingkan musim setelahnya')
    st.write('- Jumlah match stabil di 380 match permusim')
    st.write('- Hanya terdapat 310 match pada 2021 dikarenakan musim masih berjalan ketika data ini diambil')
    
     # EDA 3
    st.write('#### Bagaimana Distribusi kartu kuning Berdasasrkan Hasil Pertandingan?')
    # Menghitung jumlah kartu kuning dan kartu merah berdasarkan hasil pertandingan
    totalCard = df1.groupby('FTR').sum().reset_index()

    # Membuat plot untuk kartu kuning
    fig_yellow = px.bar(totalCard, x='FTR', y=['HY', 'AY'], barmode='group', 
                        labels={'FTR': 'Hasil Pertandingan', 'value': 'Jumlah Kartu Kuning', 'variable': 'Tim'})

    # Menampilkan plot
    st.plotly_chart(fig_yellow)
    # Deskripsi
    st.write('- Distribusi Kartu Kuning jika hasil Away Win relatif tidak jauh berbeda')
    st.write('- Distribusi Kartu Kuning lebih banyak dilakukan oleh team away ketika hasil pertandingan dimenangkan oleh tim home atau tuan rumah')

    # EDA 4
    st.write('#### Bagaimana Distribusi kartu Merah Berdasasrkan Hasil Pertandingan?')
    # Membuat plot untuk kartu merah
    fig_red = px.bar(totalCard, x='FTR', y=['HR', 'AR'], barmode='group', 
                    title='Distribusi Kartu Merah Berdasarkan Hasil Pertandingan',
                    labels={'FTR': 'Hasil Pertandingan', 'value': 'Jumlah Kartu Merah', 'variable': 'Tim'})
    # Menampilkan plot
    st.plotly_chart(fig_red)
    # Deskripsi
    st.write('- Distribusi Kartu Merah akan lebih banyak terjadi di team yang mengalami kekalahan')
    st.write('- Distribusi Kartu Merah paling tinggi terjadi pada hasil Home win dimana team Away memiliki jumlah kartu merah lebih banyak 3 kali lipat')

    # EDA 5
    st.write('#### Bagaimana Distribusi Hasil Pertandingan Berdasarkan Skor Babak Pertama?')
    # Menggabungkan skor babak pertama menjadi satu kolom
    df1['HT_Score'] = df1['HTHG'].astype(str) + '-' + df1['HTAG'].astype(str)

    # Menghitung distribusi hasil pertandingan berdasarkan skor babak pertama
    ht_distribution = df1.groupby(['HT_Score', 'FTR']).size().reset_index(name='Count')

    # Membuat plot menggunakan Plotly
    fig3 = px.bar(ht_distribution, x='HT_Score', y='Count', color='FTR', barmode='group',
                title='Distribusi Hasil Pertandingan Berdasarkan Skor Babak Pertama',
                labels={'HT_Score': 'Skor Babak Pertama', 'Count': 'Jumlah Pertandingan', 'FTR': 'Hasil Pertandingan'})

    # Menampilkan plot
    st.plotly_chart(fig3)
    # Deskripsi
    st.write('- Banyak pertandingan yang memiliki hasil draw pada half-time')
    st.write('- Tim Home memiliki keunggulan walaupun relatif kecil ')
    st.write('- Tim Away Jarang memimpin pertandingan saat half time ')

    # EDA 6
    st.write('#### Siapakah tim yang paling sering mengikuti EPL?')
    # Menghitung jumlah row per season
    totalTeam = df1['HomeTeam'].value_counts().reset_index()

    # top 5
    b = totalTeam.head(5)

    # visualisasi 

    fig4 = px.bar(b, x='HomeTeam', y='count', orientation='v')
    st.plotly_chart(fig4)
    # Deskripsi
    st.write('- 5 tim yang konsisten di EPL menandakan bahwa tim berikut dapat mempengaruhi hasil pertandingan')
    st.write('- Arsenal dan ManUnited sebagai tim yang paling konsisten semenjak season 1993 dimulai')







if __name__ == '__main__':
    run()
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# daftar pertanyaan dan kesimpulan
questions = [
    'Bagaimana perbedaan total transaksi peminjaman sepeda antara hari kerja dan hari libur?',
    'Apakah faktor cuaca berpengaruh terhadap peminjaman sepeda antara pelanggan casual dan registered?',
    'Apakah faktor musim berpengaruh terhadap peminjaman sepeda antara pelanggan casual dan registered?',
]
conclusions = [
    'Berdasarkan data dua tahun di atas, total transaksi peminjaman sepeda paling banyak dilakukan pada hari kerja, yaitu sebesar 69.62% diikuti dengan hari libur, yaitu sebesar 30.38%.',
    'Berdasarkan data dua tahun di atas, rata-rata pengguna casual dan pengguna registered cenderung melakukan transaksi peminjaman sepeda ketika cuaca sedang cerah, kemudian diikuti dengan cuaca berkabut/berawan, dan salju ringan/hujan ringan. Tidak pernah ada transaksi peminjaman sepeda ketika cuaca sedang hujan lebat/badai.',
    'Berdasarkan data dua tahun di atas, rata-rata pengguna registered melakukan transaksi peminjaman sepeda terbanyak ketika musim gugur, diikuti dengan musim dingin, musim panas, dan musim semi. Sedangkan pengguna casual terdapat sedikit perbedaan, yaitu transaksi peminjaman sepeda terbanyak ketika musim gugur, musim panas, musim dingin, dan musim semi.'
]

# index pertanyaan
questionIndex: int = 0

# data harian
day_df = pd.read_csv('day.csv')
day_df['workingday_group'] = day_df['workingday'].map({
    0: 'Hari Libur',
    1: 'Hari Kerja',
})
day_df['weathersit_group'] = day_df['weathersit'].map({
    1: 'Cerah',
    2: 'Berkabut/berawan',
    3: 'Salju ringan/hujan ringan',
    4: 'Hujan lebat/badai',
})
day_df['season_group'] = day_df['season'].map({
    1: 'Musim Semi',
    2: 'Musim Panas',
    3: 'Musim Gugur',
    4: 'Musim Dingin',
})

# sidebar
with st.sidebar:
    st.header('Bike Sharing Analysis Test')
    questionIndex = questions.index(st.selectbox(
        'Pertanyaan',
        options=questions,
        index=questionIndex,
    ))
    st.divider()
    st.caption('Nama  : Rizal Dwi Anggoro')
    st.caption('Email : gnoogler4@gmail.com')

# main
st.header('Bike Sharing Analysis')
st.write('')
st.subheader(questions[questionIndex])
st.write('')

if questionIndex == 0:
    day_analysis = day_df.groupby('workingday_group')['cnt'].sum()

    day_analysis.plot(kind='pie', autopct='%1.2f%%', startangle=90)
    plt.title('Persentase Transaksi Berdasarkan Hari')
    plt.ylabel('')
    plt.axis('equal')
    st.pyplot(plt)
elif questionIndex == 1:
    weather_analysis = day_df.groupby('weathersit_group')[['casual', 'registered']].mean()

    weather_analysis.plot(kind='bar')
    plt.title('Rata-rata Transaksi Berdasarkan Cuaca')
    plt.xlabel('Cuaca')
    plt.xticks(rotation=0)
    plt.ylabel('Rata-rata transaksi')
    st.pyplot(plt)
else:
    season_analysis = day_df.groupby('season_group')[['casual', 'registered']].mean()

    season_analysis.plot(kind='line')
    plt.title('Rata-rata Transaksi Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.xticks(rotation=0)
    plt.ylabel('Rata-rata transaksi')
    st.pyplot(plt)

st.write(conclusions[questionIndex])

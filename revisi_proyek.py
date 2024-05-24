import streamlit as st
from PIL import Image

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Menu",("Home","Teori", "Nilai Ar unsur", "Kalkulator Massa Atom Relatif","Kalkulator Normalitas","Contoh Soal"))
if add_selectbox=="Home":
    st.title('_Calcustry_')
    image=Image.open('calcustry.jpg')
    st.image(image, width=350)
    st.write("Calcustry adalah singkatan dari Calculator Chemistry. Jika diartikan ke dalam Bahasa Indonesia adalah Kalkulator Kimia dimana web ini memliki fungsi untuk melakukan perhitungan Normalitas Titrasi. Tetapi, didalam web juga ada alat untuk menghitung massa atom relatif dan memunculkan nilai massa atom relatif.")
    st.caption("created by :") 
    st.caption("KELOMPOK 11 (1D - ANKIM)")
    st.caption (''' the member of the team :
          
1. R.A. Nailha Ilham (2360226)
2. Fadhil Januar (2360118)
3. Patimah Azzahra (2360223)
4. Yuliansyah Faizin Akbar (2360293)
5. Zahrani Faradisa (2360298)
''') 
    
    
    
elif add_selectbox == "Teori" :
    st.title("Dasar Teori")
    st.subheader(':blue[_1. Konsentrasi Larutan_]')
    st.write("Sebagai seorang analis tentunya nama konsentrasi larutan bukan hal yang baru untuk didengar, biasanya kalimat ini sering dijumpai ketika sedang membuat larutan. Larutan dalam ilmu kimia merupakan campuran yang bersifat homogen dengan perbandingan komposisi sesuai dengan komponen penyusunnya. Pada umumnya, suatu larutan terdiri dari satu jenis zat terlarut (Solut) dan satu pelarut (Solvent). Meskipun larutan berupa campuran homogen, komposisi yang ada pada setiap larutan bisa berbeda-beda. Misalnya, ada dua buah larutan yang dimana masing-masing pelarutnya berisi satu liter, tetapi jumlah garam yang terlarut berbeda. Dari dua larutan garam tadi, orang lain tidak bisa mengetahui berapa banyak garam yang terkandung didalamnya. Oleh karena itu, untuk mengetahui informasi mengenai jumlah relatif Solut dan Solvent yang ada pada larutan digunakan istilah konsentrasi larutan.")
    st.write("Konsentrasi larutan adalah jumlah zat yang terlarut dalam setiap satuan larutan atau pelarut. Konsentrasi larutan yang biasa dipakai pada laboratorium, yaitu Molaritas, Molalitas, Normalitas, Fraksi Mol, Konsentrasi dalam Persen, Parts per Million (ppm) dan Parts per Billion (ppb), dan Keformalan. Namun, dalam web aplikasi ini yang menjadi titik acuan yaitu konsentrasi dalam satuan Normalitas. ")
    st.subheader(':blue[_2. Normalitas_]')
    st.write("Normalitas adalah ukuran yang menunjukkan besaran konsentrasi pada berat ekuivalen setara dalam gram per larutan. Adapun rumus normalitas yang digunakan untuk mencari padatan yang dilarutkan dalam air yaitu : ")
    image=Image.open('Rumus normalitas.jpg')
    st.image(image, width=450)
    st.subheader(':blue[_3. Massa Atom Relatif_]')
    st.write("Massa atom relatif adalah massa suatu atom yang ditentukan dengan cara membandingkan massa atom standar. Massa atom relatif ini disimbolkan dengan Ar dan tidak memiliki satuan.")
    st.write("Dalam teori atom Bohr, disebutkan bahwa atom-atom dari unsur tertentu di alam dapat memiliki massa yang berbeda-beda. Oleh karena itu, massa atom relatif dari suatu unsur dihitung berdasarkan massa atom rata-rata dari keseluruhan isotop stabil yang terdapat di alam dibandingkan dengan massa atom standar. Adapun rumus menghitung Massa Atom Relatif yaitu : ")
    image=Image.open('rumus Ar.jpg')
    st.image(image, width=450) 

elif add_selectbox == "Nilai Ar unsur" :
    st.title("Mengetahui Nilai Ar Unsur") 
    unsur = st.text_input("Masukkan lambang/symbol unsur kimia ex;Fe")
    st.warning('Perhatikan penulisan saat memasukkan unsur, masukkan sesuai simbol atom ', icon="⚠️")
    tombol = st.button("Tampilkan nilai Massa Atom Relatif")


#Percabangan lebih dari dua kasus
    if unsur == "H" :
        st.success ("1")
    elif unsur == "Li" :
        st.success ("7")
    elif unsur == "Na" :
        st.success ("23")
    elif unsur == "K" :
        st.success ("39")
    elif unsur == "Rb" :
        st.success ("85,5")
    elif unsur == "Cs" :
        st.success ("133")
    elif unsur == "Fr" :
        st.success ("223")
    elif unsur == "Be" :
        st.success ("9")
    elif unsur == "Mg" :
        st.success ("24,3")
    elif unsur == "Ca" :
        st.success ("40")
    elif unsur == "Sr" :
        st.success ("88")
    elif unsur == "Ba" :
        st.success ("137")
    elif unsur == "Ra" :
        st.success ("226")
    elif unsur == "Ra" :
        st.success ("226")
    elif unsur == "Sc" :
        st.success ("45")
    elif unsur == "Y" :
        st.success ("89")
    elif unsur == "Ti" :
        st.success ("48")
    elif unsur == "Zr" :
        st.success ("91,2")
    elif unsur == "Hf" :
        st.success ("178,5")
    elif unsur == "Rf" :
        st.success ("267,1")
    elif unsur == "B" :
        st.success ("11")
    elif unsur == "Al" :
        st.success ("27")
    elif unsur == "Ga" :
        st.success ("70")
    elif unsur == "In" :
        st.success ("115")
    elif unsur == "Tl" :
        st.success ("204,4")
    elif unsur == "Uut" :
        st.success ("289")
    elif unsur == "C" :
        st.success ("12")
    elif unsur == "Si" :
        st.success ("28,1")
    elif unsur == "Ge" :
        st.success ("73")
    elif unsur == "Sn" :
        st.success ("119")
    elif unsur == "Pb" :
        st.success ("207,2")
    elif unsur == "Fl" :
        st.success ("289,2")
    elif unsur == "Nh" :
        st.success ("286,2")
    elif unsur == "Lu" :
        st.success ("175")
    elif unsur == "Lr" :
        st.success ("262,1")
    elif unsur == "V" :
        st.success ("51")
    elif unsur == "Nb" :
        st.success ("93")
    elif unsur == "Ta" :
        st.success ("181")
    elif unsur == "Db" :
        st.success ("262")
    elif unsur == "Cr" :
        st.success ("52")
    elif unsur == "Mo" :
        st.success ("96")
    elif unsur == "W" :
        st.success ("184")
    elif unsur == "Sg" :
        st.success ("266")
    elif unsur == "N" :
        st.success ("14")
    elif unsur == "P" :
        st.success ("31")
    elif unsur == "As" :
        st.success ("75")
    elif unsur == "Sb" :
        st.success ("122")
    elif unsur == "Bi" :
        st.success ("209")
    elif unsur == "Uup" :
        st.success ("288")
    elif unsur == "Mc" :
        st.success ("289,2")
    elif unsur == "O" :
        st.success ("16")
    elif unsur == "S" :
        st.success ("32")
    elif unsur == "Se" :
        st.success ("79")
    elif unsur == "Te" :
        st.success ("128")
    elif unsur == "Po" :
        st.success ("209")
    elif unsur == "Lv" :
        st.success ("293.2")
    elif unsur == "Mn" :
        st.success ("55")
    elif unsur == "Tc" :
        st.success ("99")
    elif unsur == "Re" :
        st.success ("186,2")
    elif unsur == "Bh" :
        st.success ("264")
    elif unsur == "Fe" :
        st.success ("56")
    elif unsur == "Ru" :
        st.success ("101")
    elif unsur == "Os" :
        st.success ("190,2")
    elif unsur == "Hs" :
        st.success ("269")
    elif unsur == "Co" :
        st.success ("59")
    elif unsur == "Rh" :
        st.success ("103")
    elif unsur == "Ir" :
        st.success ("192,2")
    elif unsur == "Mt" :
        st.success ("268")
    elif unsur == "Ni" :
        st.success ("59")
    elif unsur == "Pd" :
        st.success ("106,4")
    elif unsur == "Pt" :
        st.success ("195")
    elif unsur == "Ds" :
        st.success ("269")
    elif unsur == "F" :
        st.success ("19")
    elif unsur == "Cl" :
        st.success ("35,5")
    elif unsur == "Br" :
        st.success ("80")
    elif unsur == "I" :
        st.success ("127")
    elif unsur == "At" :
        st.success ("210")
    elif unsur == "Uus" :
        st.success ("292")
    elif unsur == "He" :
        st.success ("4")
    elif unsur == "Ne" :
        st.success ("20,2")
    elif unsur == "Ar" :
        st.success ("40")
    elif unsur == "Kr" :
        st.success ("85")
    elif unsur == "Xe" :
        st.success ("131,3")
    elif unsur == "Rn" :
        st.success ("222")
    elif unsur == "Uuo" :
        st.success ("293")
    elif unsur == "La" :
        st.success ("139")
    elif unsur == "Ce" :
        st.success ("140")
    elif unsur == "Pr" :
        st.success ("141")
    elif unsur == "Nd" :
        st.success ("144")
    elif unsur == "Pm" :
        st.success ("145")
    elif unsur == "Sm" :
        st.success ("150")
    elif unsur == "Eu" :
        st.success ("152")
    elif unsur == "Gd" :
        st.success ("157")
    elif unsur == "Td" :
        st.success ("159")
    elif unsur == "Dy" :
        st.success ("162")
    elif unsur == "Ho" :
        st.success ("165")
    elif unsur == "Er" :
        st.success ("167")
    elif unsur == "Tm" :
        st.success ("169")
    elif unsur == "Yb" :
        st.success ("173")
    elif unsur == "Lu" :
        st.success ("175")
    elif unsur == "Ac" :
        st.success ("227")
    elif unsur == "Th" :
        st.success ("232")
    elif unsur == "Pa" :
        st.success ("231")
    elif unsur == "U" :
        st.success ("238")
    elif unsur == "Np" :
        st.success ("237")
    elif unsur == "Pu" :
        st.success ("244")
    elif unsur == "Am" :
        st.success ("243")
    elif unsur == "Cm" :
        st.success ("247")
    elif unsur == "Bk" :
        st.success ("247")
    elif unsur == "Cf" :
        st.success ("251")
    elif unsur == "Es" :
        st.success ("254")
    elif unsur == "Fm" :
        st.success ("257")
    elif unsur == "Md" :
        st.success ("258")
    elif unsur == "No" :
        st.success ("259")
    elif unsur == "Lr" :
        st.success ("262")
    else :
        st.success (" ")


        
elif add_selectbox=="Kalkulator Massa Atom Relatif" :
    st.title('Kalkulator Massa Atom Relatif')
    
    massa_rata_rata_1_atom_x= st.number_input('Masukkan Massa Rata-Rata 1 Atom (x 10^-23)')
    massa_atom_C_12= st.number_input('Masukkan Massa Atom C-12 (x 10^-23)')
    tombol = st.button('Hitung Massa Atom Relatif')
    if tombol :
        Massa_Ar = massa_rata_rata_1_atom_x*10*(-23)/(1/12*massa_atom_C_12*10*(-23))
        st.success(f'Massa Atom Relatif adalah {Massa_Ar:.2f}')
        
elif add_selectbox == "Kalkulator Normalitas":
    st.title('Kalkulator Normalitas')
    massa= st.number_input('Masukkan Massa (mgram)')
    BE= st.number_input('Masukkan BE/BM')
    Volume=st.number_input ('Masukkan Volume (mL)')
    FP=st.number_input ('Masukkan FP (jika tidak ada FP masukkan angka 1 sebagai FP )')
    tombol = st.button('Hitung Normalitas')
    if tombol :
        Normalitas = massa/(FP*Volume*BE)
        st.success(f'Normalitas adalah {Normalitas:.4f}')

     


elif add_selectbox == "Contoh Soal" :
    st.title("Contoh Soal")
    st.write ("1. Seorang analis ingin melakukan standardisasi HCl 0,1N , prosedur sebagai berikut : ditimbang 1,5 g boraks (Na2BrO7.10H2O) dimasukan ke dalam labu takar 100 mL dan ditepatkan sampai tanda tera lalu di homogen. Larutan di pipet 25mL dan di Titar dengan HCl menggunakan indikator metil merah (MM) 2 tetes, didapatkan volume titik akhir sebanyak 24,40 mL. Tentukan berapa Normalitas HCl setelah di standardisasi ( Be boraks = 190,6 mg/mg rek )")
    st.write ("2. Tentukan Ar O")
    st.write ("3. Diketahui massa rata-rata 1 atom oksigen = 2,657 x 10^-23 gram dan massa 1 atom C-12 = 1,99 x 10^-23 gram. Tentukanlah massa atom relatif oksigen !")



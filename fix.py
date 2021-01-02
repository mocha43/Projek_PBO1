import sqlite3

class Database:
    def __init__(self, database):
        self.conn = sqlite3.connect(database) #mengkoneksikan ke database
        self.cursor = self.conn.cursor() 
        #cursor digunakan untuk memfasilitasi pemrosesan selanjutnya seperti delete,insert,dll
    def queryData(self, query):
        self.cursor.execute(query)
        #cotohnya ini untuk bisa execute harus ada cursor terlebih dahulu dan execute digunakan untuk mengeksekusi query
        self.conn.commit()
        #digunakan untuk menyimpan perubahan
    def selectAllData(self, query):
        self.queryData(query)
        return self.cursor.fetchall()
        #fungsi ini untuk menampilkan semua isi data

class App(Database):
    def menu(self):
        print("1.Registrasi")
        print("2.Login")
        print("3.Keluar")

    def quit(self):
        exit()
        #menu wes ngerti lah ya dhan

class registrasi(Database):
    def Registrasi(self):
        self.id_pengguna = input("masukkan id")
        self.nama = input("masukkan nama")
        self.email = input("email")
        self.password = input("pass")
        self.query = ("INSERT INTO Pengguna (id_pengguna,nama,email,password)Values(?,?,?,?);")
        #disini kita menulis query biasanya kan sql ada new query nah query ini fungsinya seperti itu
        self.cursor.execute(self.query, (self.id_pengguna, self.nama, self.email, self.password))
        #disini kita mengeksekusi query tersebut nah setelah self.query ada self.id_pengguna, dst
        #supaya data yang diinputkan mencocokkan pada nama kolom pada tabel sql
        self.conn.commit()
        #setelah itu kita simpan perubahan

class Order(Database):
    def Login(self):
        self.nama = input("masukkan username anda :")
        self.password = input("masukkan password anda :")
        self.conn = sqlite3.connect('dbnew.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Pengguna where nama=? and password=?;", (self.nama, self.password))
        #iki intine podo ya dhan
        self.data_user = self.cursor.fetchone()
        #disini kita buat variabel baru yaitu data user dimana isi dari data user adalah setiap data per baris dari tabel pengguna 
        if self.data_user != None:
            #disini jika pada variabel data user tidak sama dengan kosong atau artinya ada yang sama username dan password maka benar dan print ("brhasil")
            print("anda berhasil masuk")
            print("List Product/Servis")
            self.Shop()
        else :
            print("data yang anda masukkan salah")

    def Shop(self):
        self.cursor.execute("SELECT * FROM Shop")
        #menggunakan row supaya data yang ditampilkan kebawah kalau tidak nanti datanya kesamping
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        self.id_pengguna = self.data_user[0]
        self.id_product  = input("masukkan id produk/servis yang ingin dibeli : ")
        self.qty = int(input("jumlah barang yang ingin dibeli/jika servis bisa ditulis : "))
        self.query = ("INSERT INTO [Order] (id_pengguna, id_product, qty) Values(?, ?,?);")
        self.cursor.execute(self.query, (self.id_pengguna, self.id_product, self.qty))
        self.conn.commit()
        self.Total()
        #Di shop intinya sama dan untuk menampilkan harga udah buat view dulu di database sqlitenya
        #maka dari itu untuk total nya tinggal select * from total untuk isi view lak ditakoni iso duduhne ae dhan
        
    def Total(self):
        print("TOTAL HARGA")
        self.cursor.execute("SELECT * FROM total")
        print(self.cursor.fetchone())



app = App('dbnew.db')
reg = registrasi('dbnew.db')
ord = Order('dbnew.db')
appRun = True
while appRun:
    app.menu()
    try:
        pilihan = int(input("Pilih menu dengan angka: "))
    except ValueError:
        app.menu()
    if pilihan == 1:
        reg.Registrasi()
    elif pilihan == 2:
        ord.Login()
    elif pilihan == 3:
        app.quit()
    else:
        print("Menu yang dipilih tidak tersedia")
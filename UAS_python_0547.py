#modul yang diimport dari pip install request, mysql-connector, dan tabulate
import requests
from tabulate import tabulate
from mysql import connector

###################################################################################################################
#Database dengan nama db_akademik_0547 dan tabel bernama tbl_students_0547


#connecting ke database 
db = connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'db_akademik_0547'
    )

if db.is_connected():
    print()
    print('Database is opened successfully!!!')
    print()


####################################################################################################################


#mendapatkan data dari API
API_URL = 'https://api.abcfdab.cfd/students'
response_API = requests.get(API_URL)
# print(response_API.status_code)--> 200 connected
json_data = response_API.json()

data_list = [] # untuk hasil dari dict dengan key data di mana values berupa list

# mengambil values dari key bernama data
for item,val in json_data.items():
    if item == "data":
        data_list.extend(val) # menggabungkan values ke data_list

# print(data_list) ##mengecek hasil list data gabungan, dapat di-uncomment


##################################################################################################################


##Memasukkan data ke dalam database

""""Dapat di-uncomment mulai dari sini"""

# database_sql = "INSERT INTO tbl_students_0547 (nim, nama, jk, jurusan, alamat) VALUES (%s, %s, %s, %s, %s)"

# for i in data_list:
#     database_val = (i["nim"], i["nama"], i["jk"], i["jurusan"], i["alamat"])
#     cursor = db.cursor()
#     cursor.execute(database_sql,database_val)
#     db.commit()
# print("Saved!!!!")

""""sampai sini"""


#################################################################################################################


if __name__ == "__main__":

    while True:

        option = input("""
1. Tampilkan semua data
2. Tampilkan data berdasarkan limit
3. Cari data berdasarkan NIM
0. Keluar
Pilihh menu >> """)

        print()

        cursor = db.cursor()

        if option == '1':
            # #menampilkan semua data menggunakan tabulate
            
            cursor.execute("SELECT * FROM tbl_students_0547")
            result = cursor.fetchall()

            list_data = [["ID","NIM","NAMA","JK","JURUSAN","ALAMAT"]]

            for x in result:
                new_data = list(x)
                list_data.append(new_data)

            print(tabulate(list_data, headers="firstrow",tablefmt='grid'))

        elif option == '2':
            #menampilkan data berdasarkan limit dan menggunakan tabulate

            limit = input("Masukkan limit : ")
            cursor.execute(f"SELECT * FROM tbl_students_0547 LIMIT {limit}")
            result = cursor.fetchall()

            list_data = [["ID","NIM","NAMA","JK","JURUSAN","ALAMAT"]]

            for x in result:
                new_data = list(x)
                list_data.append(new_data)

            print(tabulate(list_data, headers="firstrow",tablefmt='grid'))

        elif option == '3':
            #mencari data berdasarkan NIM dan menggunakan tabulate
            search_data = input("Masukkan NIM : ",)
            cursor.execute("SELECT * FROM tbl_students_0547 WHERE nim = %s",(search_data,))

            # Jika data ditemukan akan muncul data is found!!!
            if cursor.fetchone():
                print(f"{search_data} is found!!!")
                cursor.execute("SELECT * FROM tbl_students_0547 WHERE nim = %s",(search_data,))
                list_data = [["ID","NIM","NAMA","JK","JURUSAN","ALAMAT"]]
                result = cursor.fetchall()
                for x in result:
                    new_data = list(x)
                    list_data.append(new_data)

            # Jika data tidak ditemukan akan muncul data is not found!!!
            else:
                print(f"{search_data} is not found!!!")
                list_data = [["ID","NIM","NAMA","JK","JURUSAN","ALAMAT"],["N/A","N/A","N/A","N/A","N/A","N/A"]]

            print(tabulate(list_data, headers="firstrow",tablefmt='grid'))
        
        elif option == '0':
            break

        else:
            print("Please choose carefully!!!")
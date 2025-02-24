import time

database = {
    "users": [
        {
            "userid": "user123",
            "password": "Password@1",
            "email": "user123@example.com",
            "name": "John Doe",
            "gender": "Male",
            "age": "25",
            "phone": "081234567890"
        },
        {
            "userid": "jane456",
            "password": "JaneDoe@2",
            "email": "jane.doe@example.com",
            "name": "Jane Doe",
            "gender": "Female",
            "age": "30",
            "phone": "081298765432"
        },
        {
            "userid": "alex789",
            "password": "Alex@789",
            "email": "alex@example.com",
            "name": "Alex Smith",
            "gender": "Male",
            "age": "40",
            "phone": "081355544433"
        }
    ]
}

def is_valid_userid(userid):
    """Validasi User ID"""
#     UserId ==> .....
#    - Harus Kombinasi Huruf dan Angka
#    - Tidak boleh ada karakter lain
#    - Minimal 6 karakter
#    - Maksimal 20 Karakter
#    - Lakukan Pengecekan Duplikasi, Tidak boleh ada UserId yg sama
#    - Jika ada duplikat atau tidak sesuai kriteria ada Notifikasi
#    - Ketika ada masalah, User diminta masukkan lagi UserId sampai Benar
    # TODO start
    
    # TODO end
    return True

def is_valid_password(password):
    """Validasi Password"""
    if len(password) < 8:
        return False
    has_upper = has_lower = has_digit = has_special = False
#   - Harus Kombinasi Huruf Kapital, Huruf Kecil, Angka dan Karakter Khusus => /.,@#$%
#   - Minimal 8 Karakter
    # TODO start
    
    # TODO end
    return has_upper and has_lower and has_digit and has_special

def is_valid_email(email):
    """Validasi Email"""
    # - Lakukan Validasi, ketentuan validasi seperti tugas sebelumnya
    # TODO start
    
    # TODO end
    return True

def is_valid_name(name):
    """Validasi Nama"""
    # (Hanya alfabet)
    # TODO start
    
    # TODO end
    return all(c.isalpha() or c == ' ' for c in name)

def is_valid_gender(gender):
    """Validasi Gender"""
    # (Hanya bisa Female atau Male ... Pria atau Wanita)
    # TODO start
    
    # TODO end
    return True

def is_valid_age(age):
    """Validasi Usia"""
    # (Harus Integer, Minimal 17tahun, maksimal 80 tahun)
    # TODO start
    
    # TODO end
    return True

def is_valid_phone(phone):
    """Validasi Nomor HP"""
    # (Harus Integer, Jumlah karakter 11 - 13)
    # TODO start
    
    # TODO end
    return True

def register():
    """Proses Registrasi"""
    print("\n----------- Register ---------")
    while True:
        userid = input("UserId ==> ")
        if is_valid_userid(userid):
            break
        print("UserId tidak valid atau sudah terdaftar!")
    
    while True:
        password = input("Password ==> ")
        if is_valid_password(password):
            break
        print("Password tidak valid! Harus ada huruf besar, kecil, angka, dan karakter spesial.")
    
    while True:
        email = input("Email ==> ")
        if is_valid_email(email):
            break
        print("Email tidak valid!")
    
    while True:
        name = input("Nama ==> ")
        if is_valid_name(name):
            break
        print("Nama hanya boleh mengandung alfabet dan spasi!")
    
    while True:
        gender = input("Gender (Male/Female/Pria/Wanita) ==> ")
        if is_valid_gender(gender):
            break
        print("Gender harus Male, Female, Pria, atau Wanita!")
    
    while True:
        age = input("Usia ==> ")
        if is_valid_age(age):
            break
        print("Usia harus antara 17-80 tahun!")
    
    while True:
        phone = input("No Hp ==> ")
        if is_valid_phone(phone):
            break
        print("No Hp harus 11-13 digit!")
    
    data = {
        "userid": userid,
        "password": password,
        "email": email,
        "name": name,
        "gender": gender.capitalize(),
        "age": age,
        "phone": phone,
    }
    
    database["users"].append(data)
    print("Registrasi berhasil!")

def login():
    """Proses Login"""
    print("\n----------- Login ---------")
    for _ in range(5):
        userid = input("Masukkan ID: ")
        password = input("Masukkan Password: ")
        
        user = next((user for user in database["users"] if user["userid"] == userid), None)
        
        if user:
            if user["password"] == password:
                print("Anda Berhasil Login!")
                user_profile(user)
                return
            else:
                print("Password Salah!")
        else:
            print("ID Tidak Terdaftar!")
        
        time.sleep(1)
    
    print("Gagal Login 5 kali! Kembali ke menu utama.")

def user_profile(user):
    """Tampilkan Profil Pengguna"""
    print("\n--- User Profile ---")
    print(f"Nama: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Gender: {user['gender']}")
    print(f"Usia: {user['age']}")
    print(f"No Hp: {user['phone']}")

def main():
    """Menu Utama"""
    while True:
        print("\n### Selamat datang di XXYY Apps ###")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Pilih Menu: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()

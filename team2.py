database = {
    "users": []
}

def is_valid_userid(userid):
    """Validasi User ID"""
    if not (6 <= len(userid) <= 20 and userid.isalnum()):
        return False
    for user in database["users"]:
        if user["userid"] == userid:
            return False  # Duplicate User ID
    return True

def is_valid_password(password):
    """Validasi Password"""
    if len(password) < 8:
        return False
    has_upper = has_lower = has_digit = has_special = False
    special_chars = "/.,@#$%"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
            
    return has_upper and has_lower and has_digit and has_special

def is_valid_email(email):
    """Validasi Email"""
    return "@" in email and "." in email and len(email) > 5

def is_valid_name(name):
    """Validasi Nama"""
    return name.replace(" ", "").isalpha()

def is_valid_gender(gender):
    """Validasi Gender"""
    return gender.lower() in ["male", "female", "pria", "wanita"]

def is_valid_age(age):
    """Validasi Usia"""
    return age.isdigit() and 17 <= int(age) <= 80

def is_valid_phone(phone):
    """Validasi Nomor HP"""
    return phone.isdigit() and 11 <= len(phone) <= 13

def is_valid_job(job):
    """Validasi Pekerjaan"""
    return job.replace(" ", "").isalpha()

def is_valid_hobby(hobby):
    """Validasi Hobi (Harus lebih dari satu, hanya alfabet)"""
    hobbies = hobby.split(", ")
    return all(h.replace(" ", "").isalpha() for h in hobbies) and len(hobbies) > 1

def is_valid_city(city):
    """Validasi Nama Kota"""
    return city.replace(" ", "").isalpha()

def is_valid_rt_rw(value):
    """Validasi RT/RW (Harus Integer)"""
    return value.isdigit()

def is_valid_zip(zip_code):
    """Validasi Zip Code (Harus 5 digit)"""
    return zip_code.isdigit() and len(zip_code) == 5

def is_valid_geo(value):
    """Validasi Latitude / Longitude (Harus Float)"""
    try:
        float(value)
        return True
    except ValueError:
        return False

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
        job = input("Pekerjaan ==> ")
        if is_valid_job(job):
            break
        print("Pekerjaan hanya boleh alfabet!")
    
    while True:
        hobby = input("Hobi (Pisahkan dengan koma) ==> ")
        if is_valid_hobby(hobby):
            break
        print("Hobi hanya boleh alfabet dan minimal 2 hobi!")
    
    while True:
        city = input("Nama Kota ==> ")
        if is_valid_city(city):
            break
        print("Nama Kota hanya boleh alfabet!")

    while True:
        rt = input("RT ==> ")
        if is_valid_rt_rw(rt):
            break
        print("RT harus angka!")

    while True:
        rw = input("RW ==> ")
        if is_valid_rt_rw(rw):
            break
        print("RW harus angka!")

    while True:
        zip_code = input("Zip Code ==> ")
        if is_valid_zip(zip_code):
            break
        print("Zip Code harus 5 digit angka!")

    while True:
        lat = input("Latitude ==> ")
        if is_valid_geo(lat):
            break
        print("Latitude harus berupa angka!")

    while True:
        lon = input("Longitude ==> ")
        if is_valid_geo(lon):
            break
        print("Longitude harus berupa angka!")

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
        "job": job,
        "hobby": hobby,
        "address": {
            "city": city,
            "rt": rt,
            "rw": rw,
            "zip_code": zip_code,
            "geo": {"lat": lat, "lon": lon}
        },
        "phone": phone,
    }

    database["users"].append(data)
    print("Registrasi berhasil!")

def login():
    """Proses Login"""
    print("\n----------- Login ---------")
    attempts = 0

    while attempts < 5:
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

        attempts += 1
        print(f"Percobaan {attempts}/5\n")

    print("Gagal Login 5 kali! Kembali ke menu utama.")

def user_profile(user):
    """Tampilkan Profil Pengguna"""
    print("\n--- User Profile ---")
    print(f"Nama: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Gender: {user['gender']}")
    print(f"Usia: {user['age']}")
    print(f"Pekerjaan: {user['job']}")
    print(f"Hobi: {user['hobby']}")
    print("\nAlamat:")
    print(f"Nama Kota: {user['address']['city']}")
    print(f"RT: {user['address']['rt']}")
    print(f"RW: {user['address']['rw']}")
    print(f"Zip Code: {user['address']['zip_code']}")
    print(f"Latitude: {user['address']['geo']['lat']}")
    print(f"Longitude: {user['address']['geo']['lon']}")
    print(f"No Hp: {user['phone']}")

def main():
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

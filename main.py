from modules.json import readJson, writeJson, updateJson, deleteJson

pilihanUtama = True
while(pilihanUtama):
    menu = ["create", "read", "update", "delete"]
    pilihan = input("Masukkan menu: Ex(create, read, update, delete): ").lower()

    while(pilihan not in menu):
        print("Menu tidak tersedia!")
        pilihan = input("Masukkan menu: Ex(create, read, update, delete): ").lower()
        
    match pilihan:
        case "create":
            nama = input("Masukkan nama anda: ")
            nomor = input("Masukkan nomor anda: ")
            data = { "nama": nama, "nomor": nomor }
            response = writeJson(data, "data.json")
            print(response)
        case "update":
            id = int(input("Masukkan id: "))
            nama = input("Masukkan nama anda: ")
            nomor = input("Masukkan nomor anda: ")
            data = { "nama": nama, "nomor": nomor }
            response = updateJson(id, data, "data.json")
            print(response)
        case "delete":
            id = int(input("Masukkan id: "))
            response = deleteJson(id, "data.json")
            print(response)
        case "read":
            response = readJson("data.json")
            template = "{id} - {nama} - {nomor}"
            print("=== Data Mahasiswa ===")
            for item in response:
                print(template.format(id = item["id"], nama = item["nama"], nomor = item["nomor"]))
    
    pilihan = input("Apakah anda ingin melanjutkan? (Y/N): ").lower()
    if(pilihan == "n"): pilihanUtama = False
    
     
        
    
    
    



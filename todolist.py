class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tugas '{task}' telah ditambahkan.")

    def view_tasks(self):
        if not self.tasks:
            print("Daftar tugas kosong.")
        else:
            print("Daftar Tugas:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Tugas '{removed_task}' telah dihapus.")
        else:
            print("Indeks tugas tidak valid.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\n=== Aplikasi To-Do List ===")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        choice = input("Pilih menu (1-4): ")
        
        if choice == '1':
            task = input("Masukkan tugas baru: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            index = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            todo_list.remove_task(index)
        elif choice == '4':
            print("Terima kasih telah menggunakan aplikasi To-Do List. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
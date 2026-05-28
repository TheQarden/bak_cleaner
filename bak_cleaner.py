import os
import sys


def delete_bak_files(directory):
    deleted = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.bak'):
                path = os.path.join(root, file)
                try:
                    os.remove(path)
                    print(f'Удалён: {path}')
                    deleted += 1
                except Exception as e:
                    print(f'Ошибка: {path} — {e}')
    return deleted

def main():
    print("🗑️ Удаление всех .bak файлов (tool)\nAuthor: TheQarden\n")
    if len(sys.argv) > 1:
        path = sys.argv[1].strip()
    else:
        path = input("Введите путь к папке: ").strip()

    if not path:
        print("Путь не введён.")
        input("Нажмите Enter...")
        return

    if not os.path.exists(path):
        print(f"Ошибка: папка '{path}' не существует")
        input("Нажмите Enter...")
        return

    if not os.path.isdir(path):
        print(f"Ошибка: '{path}' — это не папка")
        input("Нажмите Enter...")
        return
        
    total = 0
    for root, _, files in os.walk(path):
        total += sum(1 for f in files if f.endswith('.bak'))
    if total == 0:
        print(f"В папке '{path}' нет .bak файлов.")
    else:
        print(f"Найдено {total} .bak файлов")
        confirm = input("Удалить все? (да/нет): ").strip().lower()
        if confirm in ('да', 'yes', 'д', 'y'):
            deleted = delete_bak_files(path)
            print(f"\nУдалено файлов: {deleted}")
        else:
            print("Отменено.")
if __name__ == "__main__":
    main()
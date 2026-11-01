from operator import itemgetter


class File:
    """Файл."""

    def __init__(self, file_id, name, size, catalog_id):
        self.id = file_id
        self.name = name
        self.size = size              # размер файла, КБ (количественный признак)
        self.catalog_id = catalog_id  # связь один-ко-многим


class Catalog:
    """Каталог файлов."""

    def __init__(self, catalog_id, name):
        self.id = catalog_id
        self.name = name


class FileCatalog:
    """Файлы каталога (связь многие-ко-многим)."""

    def __init__(self, file_id, catalog_id):
        self.file_id = file_id
        self.catalog_id = catalog_id


# Тестовые данные
catalogs = [
    Catalog(1, "Каталог документов"),
    Catalog(2, "Каталог изображений"),
    Catalog(3, "Архив проектов"),
    Catalog(4, "Музыкальный каталог"),
    Catalog(5, "Системные файлы"),
]

files = [
    File(1, "report.docx", 250, 1),
    File(2, "contract.pdf", 1200, 1),
    File(3, "photo.jpg", 3500, 2),
    File(4, "logo.png", 120, 2),
    File(5, "project.zip", 20480, 3),
    File(6, "song.mp3", 5400, 4),
    File(7, "kernel.sys", 800, 5),
    File(8, "notes.txt", 15, 1),
]

# Связь многие-ко-многим (файл может лежать в нескольких каталогах)
files_catalogs = [
    FileCatalog(1, 1), FileCatalog(2, 1), FileCatalog(8, 1),
    FileCatalog(3, 2), FileCatalog(4, 2),
    FileCatalog(5, 3), FileCatalog(6, 4), FileCatalog(7, 5),
    # дополнительные связи
    FileCatalog(1, 3), FileCatalog(2, 3),
    FileCatalog(4, 1), FileCatalog(6, 2), FileCatalog(8, 5),
]


def main():
    # Соединение один-ко-многим
    one_to_many = [(f.name, f.size, c.name)
                   for c in catalogs
                   for f in files
                   if f.catalog_id == c.id]

    # Соединение многие-ко-многим
    many_to_many_temp = [(c.name, fc.catalog_id, fc.file_id)
                         for c in catalogs
                         for fc in files_catalogs
                         if c.id == fc.catalog_id]
    many_to_many = [(f.name, f.size, cat_name)
                    for cat_name, cat_id, file_id in many_to_many_temp
                    for f in files if f.id == file_id]

    print("Запрос А1")
    print("Список всех связанных файлов и каталогов, отсортированный по каталогам:")
    res_1 = sorted(one_to_many, key=itemgetter(2))
    for name, size, cat in res_1:
        print(f"  {cat}: {name} ({size} КБ)")

    print("\nЗапрос А2")
    print("Список каталогов с суммарным размером файлов, отсортированный по суммарному размеру:")
    res_2_unsorted = []
    for c in catalogs:
        c_files = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(c_files) > 0:
            total = sum(size for _, size, _ in c_files)
            res_2_unsorted.append((c.name, total))
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    for cat, total in res_2:
        print(f"  {cat}: {total} КБ")

    print("\nЗапрос А3")
    print("Каталоги со словом «каталог» в названии и список файлов в них:")
    res_3 = {}
    for c in filter(lambda c: "каталог" in c.name.lower(), catalogs):
        c_files = list(filter(lambda i: i[2] == c.name, many_to_many))
        res_3[c.name] = [name for name, _, _ in c_files]
    for cat, names in res_3.items():
        print(f"  {cat}: {', '.join(names)}")


if __name__ == "__main__":
    main()

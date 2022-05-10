from pathlib import Path
from zipfile import ZipFile

with ZipFile("file.zip", "w") as zipFile:
    for path in Path("ecommerce").rglob("*.*"):
        print(path)
        zipFile.write(path)


# with ZipFile("file.zip") as zipName:
#     print(zipName.namelist())

    # p1 = path.exists()
    # p2 = path.is_file()
    # p3 = path.is_dir()

    # print(p1)
    # print(p2)
    # print(p3)

    # print(path.name)
    # print(path.stem)
    # print(path.suffix)
    # print(path.paretn)

    # path = path.with_suffix(".txt")

    # path.unlink()

    # print(path.stat)

    # print(path.read_bytes())

from os import listdir, mkdir, path


def creat(title: str, kyu: str) -> str:
    if kyu not in [i[0] for i in listdir() if "kyu" in i]:
        mkdir(f"{kyu} kyu")

    if path.exists(f"{kyu} kyu/{title}.py"):
        return "This kata already exists"

    open(f"{kyu} kyu/{title}.py", "w")
    return "Successfully created file"


title = input("Insert title of kata: ").replace(" ", "_").replace(":", "-").replace("?", "")
kyu = input("Insert kyu: ")
print(creat(title, kyu))

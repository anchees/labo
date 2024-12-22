import packages
import typer

app = typer.Typer()

@app.command()
def lab7(i: int, recursion_1_no_0: int):
    if recursion_1_no_0==1:
        print("решение с рекурсией:")
        packages.lab7.recursion(i)
    else:
        print("решение без рекурсии:")
        packages.lab7.norecursion(i)

@app.command()
def lab8(znak: str, start_chislo: int, chislo_deystvia: int, kol_povtorov: int):
    packages.lab8.lab10(znak, start_chislo, chislo_deystvia, kol_povtorov)

@app.command()
def lab9(posledovatelnost_1: str, posledovatelnost_2: str):
    otvet=packages.lab9.generator(posledovatelnost_1,posledovatelnost_2)
    for i in otvet:
        print(i)

app()
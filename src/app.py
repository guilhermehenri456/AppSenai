from enum import IntFlag
from numbers import Number

import flet
from flet import ThemeMode, Text, TextField, OutlinedIconButton, OutlinedButton, Column, CrossAxisAlignment
from flet.controls import page
from flet.controls.border_radius import horizontal


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.LIGHT   # ou Dark
    page.window.width = 400
    page.window.height = 700
    # Funções
    def salvar_nome():
        text.value = f"Bom dia {input_nome.value} {input_sobrenome.value}"
        page.update()


    # Componentes
    text = Text("Olá mundo")
    input_nome = TextField(label="Digite seu nome")
    input_sobrenome = TextField(label="Digite seu sobrenome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)


    # Construção da tela
    page.add(
        Column(
            [
                input_nome,
                input_sobrenome,
                btn_salvar,
                text
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )
    def verificar():
        try:
            n1 = int(input_n1.value)
            if n1 % 2 == 0:
                text.value = f'{n1} seu número é par'
            else:
                text.value = f'{n1} seu número é impar'
        except ValueError:
            text.value = f'Erro'

    text = Text("")
    input_n1 = TextField(label="Digite o seu primeiro numero")
    btn_verificar = OutlinedButton("Verificar", on_click=verificar)

    page.add(
        Column(
            [
                input_n1,
                btn_verificar,
                text
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )
    def nascimento():
        idade = int(input_nascimento.value)
        resultado_idade = 2026 - idade
        if resultado_idade >= 18:
            text.value = f"Ele tem {resultado_idade} anos. Ele é maior de idade, "
            page.update()
        else:
            text.value = f"Ele tem {resultado_idade} anos. Ele é menor de idade, "
            page.update()

    # componentes
    input_nascimento = TextField(label="Digite o ano de nascimento")

    btn_salvar_tres = OutlinedButton("Salvar", on_click=nascimento)

    # Contrução da tela
    page.add(
        Column(
            [
                input_nascimento,
                btn_salvar_tres,
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )


flet.app(main)
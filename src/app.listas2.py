import asyncio

import flet

from flet import ThemeMode, View, AppBar, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Text, Card, \
    Column, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, Dropdown, DropdownOption, FontWeight, Container, \
    CrossAxisAlignment


class Lampada():
    def __init__(self, material, cor, marca, preco,voltagem):
        self.material = material
        self.cor = cor
        self.marca = marca
        self.preco = preco
        self.voltagem = voltagem

def main(page: flet.Page):
    # Configurações
    page.title = "Exemplos de listas"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Funções
    # Função de navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_texto():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                Text(item)
            )



    def montar_lista_card():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                Card(
                    height=50,
                    content=Row([
                            Icon(Icons.PERSON),
                            Text(item)
                        ],
                        margin=8
                    ),

                )
            )



    def montar_lista_padrao():
        list_view.controls.clear()

        # Item é uma pessoa com nome, profissão e sexo
        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.HIGHLIGHT),
                    title=(f"A marca é {item.marca}"),
                    subtitle=(f"A voltagem é {item.voltagem}V"),
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver detalhes", icon=Icons.REMOVE_RED_EYE, on_click=lambda _, pessoa=item: ver_detalhes(pessoa)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda:excluir(item)),
                        ]
                    ),
                )
            )
    def ver_detalhes(pessoa):
        text_marca.value = pessoa.marca
        text_material.value = pessoa.material
        text_cor.value = pessoa.cor
        text_preco.value = pessoa.preco
        text_voltagem.value = pessoa.voltagem

        navegar("/detalhes")
    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        marca = input_marca.value.strip()
        voltagem = input_voltagem.value.strip()
        material = input_material.value.strip()
        cor = input_cor.value.strip()
        preco = input_preco.value.strip()


        tem_erro = False
        if marca:
            input_marca.error = None
        else:
            input_marca.error = "Campo obrigatório"

        if material:
            input_material.error = None
        else:
            input_material.error = "Campo obrigatório"

        if preco:
            input_preco.error = None
        else:
            input_preco.error = "Campo obrigatório"

        if cor:
            input_cor.error = None
        else:
            input_cor.error = "Campo obrigatório"

        if voltagem:
            input_voltagem.error = None
        else:
            input_voltagem.error = "Campo obrigatório"

        if not tem_erro:
            # Montar o objeto
            lampada = Lampada(
                marca = marca,
                material = material,
                cor = cor,
                voltagem = voltagem,
                preco = preco
            )

            # add objeto na lista
            lista_dados.append(lampada)

            input_marca.value = ""
            input_voltagem.value = ""
            input_cor.value = ""
            input_material.value = ""
            input_preco.value = ""
            navegar("lista_padrao")


        montar_lista_padrao()

    # Função de gerenciar as telas (routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/lista_padrao",
                controls=[
                    flet.AppBar(
                        title="Lista das Lâmpadas",
                        bgcolor=Colors.BLUE_200
                    ),
                    list_view,
                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro"),
                )
            )
        )
        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro da LÂMPADA",
                            bgcolor=Colors.BLUE_200
                        ),
                        input_marca,
                        input_voltagem,
                        input_cor,
                        input_preco,
                        input_material,
                        btn_salvar,
                    ]
                )
            )
        elif page.route == "/detalhes":
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                            title="Detalhes",
                        ),
                        Container(
                            Column([
                                text_marca,
                                Row([
                                    Icon(Icons.EURO_SYMBOL_OUTLINED, color=Colors.PRIMARY, size=20),
                                    text_marca
                                ]),
                                Row([
                                    Icon(Icons.COLOR_LENS_ROUNDED, color=Colors.PRIMARY, size=20),
                                    text_cor
                                ]),
                                Row([
                                    Icon(Icons.SUBJECT, color=Colors.PRIMARY, size=20),
                                    text_material
                                ]),
                                Row([
                                    Icon(Icons.ATTACH_MONEY, color=Colors.PRIMARY, size=20),
                                    text_preco
                                ]),
                                Row([
                                    Icon(Icons.ELECTRIC_BOLT_ROUNDED, color=Colors.PRIMARY, size=20),
                                    text_voltagem
                                ]),
                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER
                            ),
                            bgcolor=Colors.BLUE_700,
                            padding=15,
                            border_radius=10,
                            width=400
                        )
                    ]
                )
            )
    # Função de voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    input_marca = TextField(label="Marca", hint_text="Digite a marca")
    input_voltagem = TextField(label="Voltagem", hint_text="Digite a voltagem")
    input_material = TextField(label="Material", hint_text="Digite o material")
    input_cor = TextField(label="Cor", hint_text="Digite a cor")
    input_preco = TextField(label="Preço", hint_text="R$")
    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())
    text_marca = Text(weight=FontWeight.BOLD, size=24)
    text_material = Text()
    text_preco = Text()
    text_voltagem = Text()
    text_cor = Text()

    list_view = ListView(height=500)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    route_change()

flet.run(main)

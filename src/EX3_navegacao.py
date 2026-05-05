import asyncio
from os import remove

import flet
from flet import ThemeMode, View, control, AppBar, Colors, Button, TextField, Text, Container, Icon, CrossAxisAlignment, \
    Row, Column, Icons
from flet.controls.border_radius import horizontal


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.LIGHT  # ou Dark
    page.window.width = 400
    page.window.height = 700

    tem_erro = False

    # Funções
    def p_o_o():
        text_material.value = f"Material: {input_material.value}"
        text_tamanho.value = f"Tamanho: {input_tamanho.value}"
        text_cor.value = f"Cor: {input_cor.value}"
        text_marca.value = f"Marca: {input_marca.value}"
        text_preco.value = f"Preço :R$ {input_preco.value}"

        tem_erro = False
        if input_material.value:
            input_material.error = None
        else:
            tem_erro = True
            input_material.error = "Campo obrigatorio"

        if input_tamanho.value:
            input_tamanho.error = None
        else:
            tem_erro = True
            input_tamanho.error = "Campo obrigatorio"

        if input_cor.value:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatorio"

        if input_marca.value:
            input_marca.error = None
        else:
            tem_erro = True
            input_marca.error = "Campo obrigatorio"

        if input_preco.value:
            input_preco.error = None
        else:
            tem_erro = True
            input_preco.error = "Campo obrigatorio"

        if not tem_erro:
            input_material.value = ""
            input_tamanho.value = ""
            input_cor.value = ""
            input_marca.value = ""
            input_preco.value = ""
            navegar("/tela_msg")

    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="Cadastro da Lâmpada",
                        bgcolor=Colors.AMBER_200

                    ),
                    Text("Os Dados da Lâmpada!"),
                    input_material,
                    input_tamanho,
                    input_cor,
                    input_marca,
                    input_preco,
                    btn_salvar
                ]

            )
        )
        if page.route == "/tela_msg":
            page.views.append(
                View(
                    route="/tela_msg",
                    controls=[
                        AppBar(
                            title="Dados da Lâmpada",
                            bgcolor=Colors.AMBER_200
                        ),
                        Container(
                            Column([
                                text_material,
                                Row([
                                    Icon(Icons.SETTINGS_INPUT_COMPONENT, size=40),
                                    text_material, text_material
                                ]),
                                Row([
                                    Icon(Icons.BORDER_COLOR, size=40),
                                    text_cor, text_cor
                                ]),
                                Row([
                                    Icon(Icons.BOOKMARK, size=40),
                                    text_marca, text_marca
                                ]),
                                Row([
                                    Icon(Icons.ATTACH_MONEY, size=40),
                                    text_preco, text_preco
                                ]),
                            ]),
                            horizontal_alignment=CrossAxisAlignment.CENTER
                        ),
                    ]
                )
            )




            # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    input_material = TextField(label="Material:")
    input_tamanho = TextField(label="Tamanho:")
    input_cor = TextField(label="Cor:")
    input_marca = TextField(label="Marca:")
    input_preco = TextField(label="Preço:")
    text_material = Text()
    text_cor = Text()
    text_marca = Text()
    text_preco = Text()
    btn_salvar = Button("Salvar", on_click=p_o_o)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)

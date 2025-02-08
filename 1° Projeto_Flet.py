# Este é o primeiro projeto desenvolvido em Flet. 
# O objetivo é criar uma aplicação de frequência e gerenciamento de usuários, com recursos como login, navegação entre páginas, e modais interativos.

import flet as ft

def main(page: ft.Page):
    page.title = "Meu Aplicativo Profissional"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.adaptive = True

    # Função de navegação entre as páginas da aplicação
    def navegar_pagina(pagina_numero):
        page.clean()  # Limpa o conteúdo da página antes de adicionar o novo
        if pagina_numero == 1:
            page.add(main_content)
        elif pagina_numero == 2:
            page.add(pagina_2)
        elif pagina_numero == 3:
            page.add(pagina_3)

    # Função para criar um ícone para as páginas
    def icone_pagina(icon, label, on_click):
        return ft.Container(
            bgcolor=ft.colors.WHITE,
            height=100,
            width=250,
            border_radius=10,
            expand=True,
            padding=10,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.IconButton(on_click=on_click, icon=icon, icon_size=50),
                    ft.Text(
                        label,
                        weight=ft.FontWeight.W_900,
                        size=12,
                        color="#014a8e",
                        style=ft.TextStyle(decoration=ft.TextDecoration.NONE)
                    ),
                ],
            ),
        )

    # Função para criar ícones em uma fila
    def icones(icon, label):
        return ft.Container(
            bgcolor="TRANSPARENT",
            expand=True,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(name=icon, color=ft.colors.BLACK87, size=40),
                    ft.Text(
                        label,
                        size=10,
                        color="#014a8e",
                        style=ft.TextStyle(decoration=ft.TextDecoration.NONE),
                        weight=ft.FontWeight.W_900,
                    ),
                ]
            )
        )

    # Função para fechar o modal
    def fechar_modal(e):
        nonlocal dlg_modal
        page.close(dlg_modal)

    # Modal que exibe um código para a aplicação
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Insira o Código"),
        content=ft.Text("000", size=35),
        actions=[
            ft.ElevatedButton("Confirmar", bgcolor="#014a8e", color="WHITE", on_click=fechar_modal),
            ft.ElevatedButton("Fechar", bgcolor="#f6941d", color="WHITE", on_click=fechar_modal),
        ],
    )

    # Função para abrir o modal
    def abrir_modal(e):
        dlg_modal.open = True
        page.update()

    # Conteúdo da página 3 (Frequência)
    pagina_3 = ft.Container(
        alignment=ft.alignment.center,
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                # Cabeçalho
                ft.Container(
                    bgcolor="#014a8e",
                    alignment=ft.alignment.center,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.IconButton(on_click=lambda e: navegar_pagina(2), icon=ft.icons.ARROW_BACK, icon_color="WHITE"),
                            ft.Text("Frequência", color="WHITE", weight=ft.FontWeight.W_700, size=20),
                            ft.Icon(name=ft.icons.MENU_ROUNDED, color="WHITE"),
                        ],
                    ),
                ),

                # Card com informações de frequência
                ft.Container(
                    width=400,
                    padding=15,
                    border=ft.border.all(2, "BLACK"),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(text, color="BLACK", size=14) for text in [
                                "Curso: Técnico em informática",
                                "Data: 24/07/2024",
                                "Professor: Cosme",
                                "Código da Turma: cr7",
                                "Qtd de Aulas: 1",
                                "Horário: 13:30 às 14:30",
                                "UC/Disciplinas: Projeto Integrador Assistente de Desenvolvimento de Aplicativos Computacionais"
                            ]
                        ] + [ft.ElevatedButton("Marcar Frequência", bgcolor="#014a8e", color="WHITE", on_click=abrir_modal)]
                    ),
                ),
            ],
        ),
    )

    # Conteúdo da página 2 (Informações do Usuário)
    pagina_2 = ft.Container(
        padding=20,
        alignment=ft.alignment.center,
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # Cabeçalho
                ft.Container(
                    bgcolor="#014a8e",
                    padding=22,
                    width=250,
                    border_radius=10,
                    content=ft.Row(
                        width=150,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                "Olá, Aluno",
                                color="WHITE",
                                weight=ft.FontWeight.W_500,
                                size=16,
                                style=ft.TextStyle(decoration=ft.TextDecoration.NONE)
                            ),
                            ft.Icon(
                                name=ft.icons.MENU_ROUNDED,
                                color=ft.colors.BLACK
                            ),
                        ]
                    ),
                ),
                # Opções de serviços
                ft.Container(
                    width=200,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            ft.Text(
                                "Serviços",
                                color="#014a8e",
                                weight=ft.FontWeight.W_900,
                                size=12,
                                style=ft.TextStyle(decoration=ft.TextDecoration.NONE)
                            )
                        ]
                    ),
                ),
                # Botões de navegação para diferentes páginas
                icone_pagina(ft.icons.VERIFIED_USER, "Frequência", lambda e: navegar_pagina(3)),
                ft.Container(
                    bgcolor="#f2f2f2",
                    height=100,
                    width=250,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            ft.Text(
                                "Redes Sociais",
                                weight=ft.FontWeight.W_900,
                                color="#014a8e",
                                size=12,
                                style=ft.TextStyle(decoration=ft.TextDecoration.NONE)
                            ),
                            ft.Container(
                                bgcolor="#f2f2f2",
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        icones(ft.icons.FACEBOOK_SHARP, "Facebook"),
                                        icones(ft.icons.TIKTOK, "Tik Tok"),
                                        icones(ft.icons.APPLE, "Apple"),
                                        icones(ft.icons.CLOUD_DOWNLOAD, "Download"),
                                    ]
                                )
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )

    # Conteúdo da página principal (Login)
    main_content = ft.Container(
        padding=20,
        expand=True,
        content=ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                controls=[
                    # Logo ou imagem do aplicativo
                    ft.Image(
                        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgF-VtfcBgA_kvCsPkoBRHK7L7OteLnZ-5gw&s",
                        height=100,
                        width=100
                    ),
                    # Campos de login
                    ft.Container(
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextField(
                                    label="Usuário",
                                    height=40,
                                    width=200,
                                    suffix_icon="VERIFIED_USER_ROUNDED"
                                )
                            ]
                        ),
                    ),
                    ft.TextField(
                        label="Senha",
                        password=True,
                        can_reveal_password=True,
                        height=40,
                        width=200
                    ),
                    # Switch para seleção de usuário
                    ft.Container(
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Aluno"),
                                ft.Switch(
                                    height=30,
                                    focus_color='#014a8e'
                                ),
                                ft.Text("Docente")
                            ]
                        ),
                    ),
                    # Botões de login e navegação
                    ft.Container(
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                ft.ElevatedButton(f"Entrar", bgcolor='#014a8e', elevation=1, color="WHITE", width=200, on_click=lambda e: navegar_pagina(2)),
                                ft.TextButton(text="Esqueci minha senha"),
                                ft.Text("Versão: 1.0.4", size=16, weight=ft.FontWeight.W_600, selectable=True),
                                ft.Text(
                                    "Termos de Uso",
                                    size=16,
                                    style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)
                                )
                            ]
                        ),
                    )
                ],
            ),
        ),
    )

    # Adiciona o conteúdo principal na página inicial
    page.add(main_content)

ft.app(target=main)
# Este é o primeiro projeto desenvolvido em Flet. 
# O objetivo é criar uma aplicação de frequência e gerenciamento de usuários, com recursos como login, navegação entre páginas, e modais interativos.

import flet as ft

def main(page: ft.Page):
    page.title = "Meu Aplicativo Profissional"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.adaptive = True

    # Função de navegação entre as páginas da aplicação
    def navegar_pagina(pagina_numero):
        page.clean()  # Limpa o conteúdo da página antes de adicionar o novo
        if pagina_numero == 1:
            page.add(main_content)
        elif pagina_numero == 2:
            page.add(pagina_2)
        elif pagina_numero == 3:
            page.add(pagina_3)

    # Função para criar um ícone para as páginas
    def icone_pagina(icon, label, on_click):
        return ft.Container(
            bgcolor=ft.colors.WHITE,
            height=100,
            width=250,
            border_radius=10,
            expand=True,
            padding=10,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.IconButton(on_click=on_click, icon=icon, icon_size=50),
                    ft.Text(
                        label,
                        weight=ft.FontWeight.W_900,
                        size=12,
                        color="#014a8e",
                        style=ft.TextStyle(decoration=ft.TextDecoration.NONE)
                    ),
                ],
            ),
        )

    # Função para criar ícones em uma fila
    def icones(icon, label):
        return ft.Container(
            bgcolor="TRANSPARENT",
            expand=True,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Icon(name=icon, color=ft.colors.BLACK87, size=40),
                    ft.Text(
                        label,
                        size=10,
                        color="#014a8e",
                        style=ft.TextStyle(decoration=ft.TextDecoration.NONE),
                        weight=ft.FontWeight.W_900,
                    ),
                ]
            )
        )

    # Função para fechar o modal
    def fechar_modal(e):
        nonlocal dlg_modal
        page.close(dlg_modal)

    # Modal que exibe um código para a aplicação
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Insira o Código"),
        content=ft.Text("000", size=35),
        actions=[
            ft.ElevatedButton("Confirmar", bgcolor="#014a8e", color="WHITE", on_click=fechar_modal),
            ft.ElevatedButton("Fechar", bgcolor="#f6941d", color="WHITE", on_click=fechar_modal),
        ],
    )

    # Função para abrir o modal
    def abrir_modal(e):
        dlg_modal.open = True
        page.update()

    # Conteúdo da página 3 (Frequência)
    pagina_3 = ft.Container(
        alignment=ft.alignment.center,
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                # Cabeçalho
                ft.Container(
                    bgcolor="#014a8e",
                    alignment=ft.alignment.center,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.IconButton(on_click=lambda e: navegar_pagina(2), icon=ft.icons.ARROW_BACK, icon_color="WHITE"),
                            ft.Text("Frequência", color="WHITE", weight=ft.FontWeight.W_700, size=20),
                            ft.Icon(name=ft.icons.MENU_ROUNDED, color="WHITE"),
                        ],
                    ),
                ),

                # Card com informações de frequência
                ft.Container(
                    width=400,
                    padding=15,
                    border=ft.border.all(2, "BLACK"),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(text, color="BLACK", size=14) for text in [
                                "Curso: Técnico em informática",
                                "Data: 24/07/2024",
                                "Professor: Cosme",
                                "Código da Turma: cr7",
                                "Qtd de Aulas: 1",
                                "Horário: 13:30 às 14:30",
                                "UC/Disciplinas: Projeto Integrador Assistente de Desenvolvimento de Aplicativos Computacionais"
                            ]
                        ] + [ft.ElevatedButton("Marcar Frequência", bgcolor="#014a8e", color="WHITE", on_click=abrir_modal)]
                    ),
                ),
            ],
        ),
    )

    # Conteúdo da página 2 (Informações do Usuário)
    pagina_2 = ft.Container(
        padding=20,
        alignment=ft.alignment.center,
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # Cabeçalho
                ft.Container(
                    bgcolor="#014a8e",
                    padding=22,
                    width=250,
                    border_radius=10,
                    content=ft.Row(
                        width=150,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                "Olá, Aluno",
                                color="WHITE",
                                weight=ft.FontWeight.W_500,
                                size=16,
                                style=ft.TextStyle(decoration=ft.TextDecoration.NONE)
                            ),
                            ft.Icon(
                                name=ft.icons.MENU_ROUNDED,
                                color=ft.colors.BLACK
                            ),
                        ]
                    ),
                ),
                # Opções de serviços
                ft.Container(
                    width=200,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            ft.Text(
                                "Serviços",
                                color="#014a8e",
                                weight=ft.FontWeight.W_900,
                                size=12,
                                style=ft.TextStyle(decoration=ft.TextDecoration.NONE)
                            )
                        ]
                    ),
                ),
                # Botões de navegação para diferentes páginas
                icone_pagina(ft.icons.VERIFIED_USER, "Frequência", lambda e: navegar_pagina(3)),
                ft.Container(
                    bgcolor="#f2f2f2",
                    height=100,
                    width=250,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            ft.Text(
                                "Redes Sociais",
                                weight=ft.FontWeight.W_900,
                                color="#014a8e",
                                size=12,
                                style=ft.TextStyle(decoration=ft.TextDecoration.NONE)
                            ),
                            ft.Container(
                                bgcolor="#f2f2f2",
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        icones(ft.icons.FACEBOOK_SHARP, "Facebook"),
                                        icones(ft.icons.TIKTOK, "Tik Tok"),
                                        icones(ft.icons.APPLE, "Apple"),
                                        icones(ft.icons.CLOUD_DOWNLOAD, "Download"),
                                    ]
                                )
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )

    # Conteúdo da página principal (Login)
    main_content = ft.Container(
        padding=20,
        expand=True,
        content=ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                controls=[
                    # Logo ou imagem do aplicativo
                    ft.Image(
                        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgF-VtfcBgA_kvCsPkoBRHK7L7OteLnZ-5gw&s",
                        height=100,
                        width=100
                    ),
                    # Campos de login
                    ft.Container(
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextField(
                                    label="Usuário",
                                    height=40,
                                    width=200,
                                    suffix_icon="VERIFIED_USER_ROUNDED"
                                )
                            ]
                        ),
                    ),
                    ft.TextField(
                        label="Senha",
                        password=True,
                        can_reveal_password=True,
                        height=40,
                        width=200
                    ),
                    # Switch para seleção de usuário
                    ft.Container(
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Aluno"),
                                ft.Switch(
                                    height=30,
                                    focus_color='#014a8e'
                                ),
                                ft.Text("Docente")
                            ]
                        ),
                    ),
                    # Botões de login e navegação
                    ft.Container(
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                ft.ElevatedButton(f"Entrar", bgcolor='#014a8e', elevation=1, color="WHITE", width=200, on_click=lambda e: navegar_pagina(2)),
                                ft.TextButton(text="Esqueci minha senha"),
                                ft.Text("Versão: 1.0.4", size=16, weight=ft.FontWeight.W_600, selectable=True),
                                ft.Text(
                                    "Termos de Uso",
                                    size=16,
                                    style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)
                                )
                            ]
                        ),
                    )
                ],
            ),
        ),
    )

    # Adiciona o conteúdo principal na página inicial
    page.add(main_content)

ft.app(target=main)

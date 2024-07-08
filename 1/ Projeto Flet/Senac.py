import flet as ft
 
def main(page: ft.Page):
    page.title = "Meu Aplicativo Profissional"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.adaptive = True
 
    def navegar_pagina(pagina_numero):
        page.clean()
        
        if pagina_numero == 1:
            page.add(main_content)
        elif pagina_numero == 2:
            page.clean()
            page.add(pagina_2)
        elif pagina_numero == 3:
            page.add(pagina_3)
 
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
 
    def fechar_modal(e):
        nonlocal dlg_modal
        page.close(dlg_modal)
 
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Insira o Código"),
        content=ft.Text("000", size=35),
        actions=[
            ft.ElevatedButton("Confirmar", bgcolor="#014a8e", color="WHITE", on_click=fechar_modal),
            ft.ElevatedButton("Fechar", bgcolor="#f6941d", color="WHITE", on_click=fechar_modal),
        ],
 
    )
 
    def abrir_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
 
    pagina_3 = ft.Container(
        alignment=ft.alignment.center,
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                ft.Container(
                    bgcolor="#014a8e",
                    alignment=ft.alignment.center,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.IconButton(on_click=lambda e: navegar_pagina(2), icon=ft.icons.ARROW_BACK, icon_color="WHITE"),
                            ft.Text(
                                "Frequência",
                                color="WHITE",
                                weight=ft.FontWeight.W_700,
                                size=20,
                            ),
                            ft.Icon(
                                name=ft.icons.MENU_ROUNDED, color="WHITE"
                            ),
                        ],
                    )
                ),
                ft.Container(
                    width=400,
                    padding=15,
                    border=ft.border.all(2, "BLACK"),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Curso: Técnico em informática",
                                color="BLACK",
                                size=14,
                            ),
                            ft.Text(
                                "Data: 24/07/2024",
                                color="BLACK",
                                size=14,
                            ),
                            ft.Text(
                                "Professor: Cosme",
                                color="BLACK",
                                size=14,
                            ),
                            ft.Text(
                                "Código da Turma: cr7",
                                color="BLACK",
                                size=14,
                            ),
                            ft.Text(
                                "Qtd de Aulas: 1",
                                color="BLACK",
                                size=14,
                            ),
                            ft.Text(
                                "Horário:13:30 às 14:30",
                                color="BLACK",
                                size=14,
                            ),
                            ft.Text(
                                "UC/Disciplinas: Projeto Integrador Assistente de Desenvolvimento de Aplicativos Computacionais",
                                color="BLACK",
                                size=14,
                            ),
                            ft.ElevatedButton("Marcar Frequência", bgcolor="#014a8e", color="WHITE", on_click=abrir_modal),
                        ],
                    ),
                ),
                ft.Container(
                    padding=15,
                    width=400,
                    border=ft.border.all(2, "BLACK"),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Curso: Técnico em informática",
                                color="BLACK",
                                size=14,
                            ),
                            ft.Text(
                                "Data: 24/07/2024",
                                color="BLACK",
                                size=14,
                            ),
                            ft.Text(
                                "Professor: Cosme",
                                color="BLACK",
                                size=14,
                            ),
                            ft.Text(
                                "Código da Turma: cr7",
                                color="BLACK",
                                size=14,
                            ),
                            ft.Text(
                                "Qtd de Aulas: 1",
                                color="BLACK",
                                size=14,
                            ),
                            ft.Text(
                                "Horário:13:30 às 14:30",
                                color="BLACK",
                                size=14,
                            ),
                            ft.Text(
                                "UC/Disciplinas: Projeto Integrador Assistente de Desenvolvimento de Aplicativos Computacionais",
                                color="BLACK",
                                size=14,
                            ),
                            ft.ElevatedButton("Marcar Frequência", bgcolor="#014a8e", color="WHITE", on_click=abrir_modal),
                        ]
                    ),
                ),
            ],
        ),
    )
 
    pagina_2 = ft.Container(
        padding=20,
        alignment=ft.alignment.center,
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
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
                                        icones(ft.icons.FACEBOOK_SHARP, "Facebook",),
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
 
   
  
        
    
 
    main_content = ft.Container(
        padding=20,
        expand=True,
        content=ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
                controls=[
                    ft.Image(
                        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgF-VtfcBgA_kvCsPkoBRHK7L7OteLnZ-5gw&s",
                        height=100,
                        width=100
                    ),
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
 
    page.add(main_content)
 
ft.app(target=main)

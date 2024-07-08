import flet as ft

class State:
    toggle = True
    data_series = {
        "Maria": [],
        "João": [],
        "José": []
    }

s = State()

def main(page: ft.Page):

    def adicionar_pontos(e):
        nome = nome_dropdown.content.value
        dia = dias_dropdown.content.value
        vendas = max(0, int(numero_vendas.content.value))  
        
        updated = False
        for i, ponto in enumerate(s.data_series[nome]):
            if ponto.x == dias_semana[dia]:
                s.data_series[nome][i] = ft.LineChartDataPoint(dias_semana[dia], vendas)
                updated = True
                break
        if not updated:
            s.data_series[nome].append(ft.LineChartDataPoint(dias_semana[dia], vendas))

        chart.data_series = [
            ft.LineChartData(
                data_points=s.data_series["Maria"],
                stroke_width=2,
                color=ft.colors.BLUE,
                curved=True,
                stroke_cap_round=True,
                below_line_gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[
                        ft.colors.with_opacity(0.25, ft.colors.BLUE),
                        "transparent",
                    ],
                ),
            ),
            ft.LineChartData(
                data_points=s.data_series["João"],
                stroke_width=2,
                color=ft.colors.RED,
                curved=True,
                stroke_cap_round=True,
                below_line_gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[
                        ft.colors.with_opacity(0.25, ft.colors.RED),
                        "transparent",
                    ],
                ),
            ),
            ft.LineChartData(
                data_points=s.data_series["José"],
                stroke_width=2,
                color=ft.colors.GREEN,
                curved=True,
                stroke_cap_round=True,
                below_line_gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[
                        ft.colors.with_opacity(0.25, ft.colors.GREEN),
                        "transparent",
                    ],
                ),
            ),
        ]
        chart.update()

    dias_semana = {
        "Segunda": 0,
        "Terça": 10,
        "Quarta": 20,
        "Quinta": 30,
        "Sexta": 40,
    }

    
    nome_dropdown = ft.Container(
    ft.Dropdown(
        prefix_icon=ft.icons.PERM_IDENTITY,
        options=[
            ft.dropdown.Option("Maria"),
            ft.dropdown.Option("João"),
            ft.dropdown.Option("José"),
            
            
        ],
        
        label="Nome",
        border_color=ft.colors.GREY,
        filled=True,
        fill_color=ft.colors.with_opacity(0.1, ft.colors.BLUE),
        border_radius=ft.border_radius.all(15),
    ),
        border=ft.border.all(2, ft.colors.with_opacity(0.2, ft.colors.BLUE)),
        border_radius=ft.border_radius.all(15),
        shadow=ft.BoxShadow(
            color=ft.colors.with_opacity(0.5, ft.colors.BLACK),
            blur_radius=10,
            spread_radius=1,
            offset=ft.Offset(2, 2),
        ),
    )
    dias_dropdown = ft.Container(
        ft.Dropdown(
            prefix_icon=ft.icons.CALENDAR_TODAY,
            options=[
                ft.dropdown.Option("Segunda"),
                ft.dropdown.Option("Terça"),
                ft.dropdown.Option("Quarta"),
                ft.dropdown.Option("Quinta"),
                ft.dropdown.Option("Sexta")
            ],
            label="Dias da Semana",
            border_color=ft.colors.GREY,
            filled=True,
            fill_color=ft.colors.with_opacity(0.1, ft.colors.GREEN),
            border_radius=ft.border_radius.all(15),
        ),
        border=ft.border.all(2, ft.colors.with_opacity(0.2, ft.colors.GREEN)),
        border_radius=ft.border_radius.all(15),
        shadow=ft.BoxShadow(
            color=ft.colors.with_opacity(0.5, ft.colors.BLACK),
            blur_radius=10,
            spread_radius=1,
            offset=ft.Offset(2, 2),
        ),
    )

    numero_vendas = ft.Container(
        ft.TextField(
            label="Número de Vendas",
            input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
            prefix_icon=ft.icons.ATTACH_MONEY,
            border_color=ft.colors.GREY,
            filled=True,
            fill_color=ft.colors.with_opacity(0.1, ft.colors.YELLOW),
            border_radius=ft.border_radius.all(15),
        ),
        border=ft.border.all(2, ft.colors.with_opacity(0.2, ft.colors.YELLOW)),
        border_radius=ft.border_radius.all(15),
        shadow=ft.BoxShadow(
            color=ft.colors.with_opacity(0.5, ft.colors.BLACK),
            blur_radius=10,
            spread_radius=1,
            offset=ft.Offset(2, 2),
        ),
    )

    botao_adicionar = ft.Container(
        ft.CupertinoButton(
            content=ft.Text("Adicionar", color=ft.colors.WHITE, size=16, weight=ft.FontWeight.BOLD),
            bgcolor=ft.colors.GREY,
            alignment=ft.alignment.center,
            opacity_on_click=0.7,
            on_click=lambda e: adicionar_pontos(e),
        ),
        border=ft.border.all(2, ft.colors.with_opacity(0.2, ft.colors.BLACK)),
        border_radius=ft.border_radius.all(25),
        shadow=ft.BoxShadow(
            color=ft.colors.with_opacity(0.5, ft.colors.GREY),
            blur_radius=10,
            spread_radius=1,
            offset=ft.Offset(2, 2),
        ),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.colors.GREY, ft.colors.GREY]
        ),
    )

    chart = ft.LineChart(
        data_series=[],
        border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
        horizontal_grid_lines=ft.ChartGridLines(
            interval=1000, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        vertical_grid_lines=ft.ChartGridLines(
            interval=10, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0,
                    label=ft.Text("R$ 0,00", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=2000,
                    label=ft.Text("R$ 2000,00", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=4000,
                    label=ft.Text("R$ 4000,00", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=6000,
                    label=ft.Text("R$ 6000,00", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=8000,
                    label=ft.Text("R$ 8000,00", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=10000,
                    label=ft.Text("R$ 10000,00", size=14, weight=ft.FontWeight.BOLD),
                ),
            ],
            labels_size=120,
        ),
        right_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=10000,
                    label=ft.Text("", weight=ft.FontWeight.BOLD),
                ),
            ],
            labels_size=50,
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0,
                    label=ft.Text(
                        "Segunda",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=10,
                    label=ft.Text(
                        "Terça",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=20,
                    label=ft.Text(
                        "Quarta",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=30,
                    label=ft.Text(
                        "Quinta",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=40,
                    label=ft.Text(
                        "Sexta",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                    ),
                ),
            ],
            labels_size=40,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=0,
        max_y=10000,
        min_x=0,
        max_x=40,
        animate=1000,
        expand=True,
    )

    page.add(
        ft.Column(
            expand=True,
            controls=[
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[nome_dropdown, dias_dropdown, numero_vendas, botao_adicionar]
                    ),
                    padding=ft.padding.all(25)
                ),
                chart,
                ft.Column(
                    [
                        ft.Container(ft.Text("- João", size=15, color=ft.colors.RED), padding=5),
                        ft.Container(ft.Text("- Maria", size=15, color=ft.colors.BLUE), padding=5),
                        ft.Container(ft.Text("- José", size=15, color=ft.colors.GREEN), padding=5)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                )
            ]
        )
    )

ft.app(target=main)

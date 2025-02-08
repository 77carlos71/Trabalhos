import flet as ft
import openpyxl
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from collections import Counter

# Este código implementa uma aplicação Flet para exibição e impressão de detalhes de funcionários.
# Ele permite selecionar um funcionário, visualizar seus detalhes em dois contêineres (branco e cinza)
# e gerar um relatório em PDF com um layout profissional, incluindo título, separador e rodapé com data/hora.
# A interface inclui um botão para imprimir os detalhes selecionados.

def main(page: ft.Page):
    page.title = "Funcionário"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 0
    page.spacing = 0
    page.window.width = 1500
    page.window.height = 900
    page.window.center()
    
    nome_column_index = None  # Defina a variável globalmente
    selected_employee = None  # Armazena os detalhes do funcionário selecionado
    
    def generate_pdf(e):
        """Gera um PDF profissional com os detalhes do funcionário selecionado."""
        if selected_employee is None:
            print("Nenhum funcionário selecionado.")
            return
        
        pdf_filename = "Funcionario_Detalhes.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        width, height = letter
        
        # Adicionando título com destaque
        c.setFont("Helvetica-Bold", 20)
        c.drawString(100, height - 80, "Relatório Profissional do Funcionário")
        
        # Linha separadora
        c.line(100, height - 85, 500, height - 85)
        
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, height - 120, "Detalhes do Funcionário:")
        
        c.setFont("Helvetica", 12)
        y_position = height - 150
        for detail in selected_employee.split('\n'):
            c.drawString(100, y_position, detail)
            y_position -= 20
        
        # Adicionando rodapé com data de geração
        from datetime import datetime
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(100, 50, f"Relatório gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        
        c.save()
        os.system(f"start {pdf_filename}")  # Abre o PDF automaticamente


    def reset_app(e):
        """Reinicializa a aplicação."""
        page.clean()
        main(page)
        page.update()
        
    def apply_filter(e):
        """Aplica o filtro selecionado e atualiza a tabela."""
        if nome_column_index is not None:
            update_table(nome_column_index)  # Passa o índice da coluna "Nome"
        else:
            print("Erro: Índice da coluna 'Nome' não encontrado.")


    excel_content = []
    headers = []

    sorting_option = ft.Dropdown(
        options=[
            ft.dropdown.Option("A-Z"),
            ft.dropdown.Option("Z-A"),
        ],
        value="A-Z",
        color="white",
        bgcolor="#3a3a3a",
        width=300,
        visible=True,
        border_width=2,
        border_color="white",
        on_change=apply_filter  # Chama a função ao mudar a opção
    )

    botao_filtrar = ft.ElevatedButton(
        "Aplicar Filtro",
        on_click=lambda e: update_table(),
        style=ft.ButtonStyle(
            color={ft.ControlState.DEFAULT: "white"},
            bgcolor={ft.ControlState.DEFAULT: "#1e1e1e"},
            elevation={"pressed": 0, "": 2},
            shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=4)}
        ),
        width=300,
        height=50,
    )

    def update_table(nome_column_index):
        """Atualiza a exibição da tabela com base no filtro selecionado."""
        if not excel_content:
            return

        if sorting_option.value == "A-Z":
            sorted_content = sorted(excel_content, key=lambda x: x[nome_column_index])  # Ordenar pela coluna "Nome"
        else:
            sorted_content = sorted(excel_content, key=lambda x: x[nome_column_index], reverse=True)

        rows = []   
        for i in range(0, len(sorted_content), 2):
            col1 = sorted_content[i] if i < len(sorted_content) else None
            col2 = sorted_content[i + 1] if i + 1 < len(sorted_content) else None

            def on_show_details(row_data):
                """Exibe detalhes ao clicar no botão."""
                nonlocal selected_employee
                details = "\n".join([f"{headers[i]}: {row_data[i]}" for i in range(len(row_data))])
                selected_employee = details
                square_grey.content = ft.Text(details, size=20, color=ft.Colors.BLACK)
                page.update()

            row_controls = []
            for col in [col1, col2]:
                if col:
                    col = [item if item is not None else "Não informado" for item in col]
                    row_controls.append(
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(col[0], size=18, color=ft.Colors.BLACK),
                                    ft.FilledButton(
                                        text="Ver Detalhes",
                                        width=180,
                                        bgcolor=ft.Colors.GREY_600,
                                        color=ft.Colors.WHITE,
                                        on_click=lambda e, data=col: on_show_details(data),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            bgcolor=ft.Colors.WHITE,
                            border=ft.Border(
                                top=ft.BorderSide(2, ft.Colors.BLACK),
                                bottom=ft.BorderSide(2, ft.Colors.BLACK),
                                left=ft.BorderSide(2, ft.Colors.BLACK),
                                right=ft.BorderSide(2, ft.Colors.BLACK),
                            ),
                            padding=10,
                            width=300
                        )
                    )

            if len(row_controls) == 1:
                row_controls.append(
                    ft.Container(
                        width=300,
                    )
                )

            rows.append(ft.Row(controls=row_controls, alignment=ft.MainAxisAlignment.SPACE_AROUND))

        square_white.content = ft.Column(
            controls=[ 
                ft.Row(
                    controls=[sorting_option, botao_filtrar],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    width=770,
                ),
                *rows
            ],
            spacing=10,
            scroll=ft.ScrollMode.AUTO
        )
        page.update()

    def on_file_pick(e):
        """Lê o arquivo Excel e carrega os dados na aplicação."""
        global nome_column_index  # Use a variável global
        nonlocal excel_content, headers
        if e.files:
            file_path = e.files[0].path
            try:
                wb = openpyxl.load_workbook(file_path)
                sheet = wb.active  

                excel_content = []
                headers = []

                nome_column_index = None  # Variável para armazenar o índice da coluna "Nome"

                # Ler o cabeçalho para encontrar o índice da coluna "Nome"
                for idx, cell in enumerate(sheet[1]):  # sheet[1] acessa a primeira linha (cabeçalho)
                    cell_value = str(cell.value).strip().lower()  # Certifique-se de que está tratando como string
                    print(f"Verificando célula {idx}: '{cell_value}'")  # Adicionando debug para ver o valor da célula
                    
                    if "nome" in cell_value:  # Usando .strip() e .lower()
                        nome_column_index = idx
                        print(f"Coluna 'Nome' encontrada na posição {idx}")
                        break  # Encontrei a coluna, posso parar a busca

                if nome_column_index is None:
                    print("Coluna 'Nome' não encontrada no arquivo.")
                    return

                # Ler os dados, substituindo valores faltantes por "Não informado"
                for idx, row in enumerate(sheet.iter_rows(values_only=True)):
                    if idx == 0:
                        headers = row
                    elif len(row) > 0:
                        row = [item if item is not None else "Não informado" for item in row]
                        excel_content.append(row)

                # Exibir o filtro após carregar os dados
                sorting_option.visible = True
                botao_filtrar.visible = True

                # Chama a função para atualizar a tabela e passa o índice da coluna "Nome"
                if nome_column_index is not None:
                    update_table(nome_column_index)  # Passa o índice da coluna "Nome" para a função de atualização
                else:
                    print("Índice da coluna 'Nome' é inválido.")

            except Exception as e:
                print(f"Erro ao ler o arquivo: {str(e)}")
                square_white.content = ft.Text(f"Erro ao ler o arquivo: {str(e)}")
                page.update()

    file_picker = ft.FilePicker(on_result=on_file_pick)

    button_add = ft.ElevatedButton(
        "Adicionar",
        style=ft.ButtonStyle(
            color={ft.ControlState.DEFAULT: ft.Colors.WHITE},
            elevation={"pressed": 0, "": 2},
            animation_duration=500,
            side={ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.GREY_600)},
            shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=4)}
        ),
        width=770,
        height=150,
        on_click=lambda e: file_picker.pick_files(),
    )

    square_white = ft.Container(
        width=770,
        height=780,
        bgcolor=ft.Colors.WHITE,
        content=ft.Column(
            controls=[ft.Row(controls=[button_add], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.START
        )
    )

    square_blue = ft.Container(
        width=400,
        height=300,
        bgcolor=ft.Colors.BLUE_GREY_800,
        content=ft.Column(
            controls=[
                ft.ElevatedButton(
                    "Tela Inicial",
                    on_click=reset_app,
                    style=ft.ButtonStyle(
                        color={ft.ControlState.DEFAULT: "white"},
                        bgcolor={ft.ControlState.DEFAULT: "#1e1e1e"},
                        elevation={"pressed": 0, "": 2},
                        shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=4)}
                    ),
                    width=200,
                    height=50,
                ),
                    ft.ElevatedButton(
                    "Imprimir dados",
                    on_click=generate_pdf,
                    style=ft.ButtonStyle(
                        color={ft.ControlState.DEFAULT: "white"},
                        bgcolor={ft.ControlState.DEFAULT: "#1e1e1e"},
                        elevation={"pressed": 0, "": 2},
                        shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=4)}
                    ),
                    width=200,
                    height=50,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    square_grey = ft.Container(
        width=400,
        height=470,
        bgcolor=ft.Colors.GREY_100,
    )

    square_main = ft.Container(
        width=1200,
        height=800,
        bgcolor=ft.Colors.GREY_800,
        alignment=ft.alignment.center,
        content=ft.Stack(
            controls=[
                ft.Container(content=square_blue, right=10, top=10),
                ft.Container(content=square_grey, right=10, bottom=10),
                ft.Container(content=square_white, left=10, top=10),
            ]
        )
    )

    page.add(square_main)
    page.add(file_picker)

ft.app(target=main)

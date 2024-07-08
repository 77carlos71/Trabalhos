import flet as ft
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.graphics.shapes import *
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from PyPDF2 import PdfWriter,PdfReader
import io

from datetime import datetime 

from flet import Page, TextField, Row, Text, Container,ListView, Column, Checkbox, IconButton, CupertinoButton, Tabs, Tab, alignment, colors, border_radius, FontWeight, TextCapitalization, Card, Divider, FilePicker

class App:
    def __init__(self, page: Page):
        """
        Classe principal que gerencia a aplicação de agenda.
        """
        self.page = page  
        self.page.window_width = 600 
        self.page.window_height = 800  
        self.page.theme_mode = ft.ThemeMode.DARK  
        self.page.window_always_on_top = True  
        self.page.title = "Agenda App"  
        self.task = '' 
        self.view = 'all' 
        self.db_execute('CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY, nome TEXT, email TEXT, telefone TEXT, status TEXT)')
        self.all() 
        self.main_page()  
        self.page.update()  

    def db_execute(self, query, params=[]):
        with sqlite3.connect('banco.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall()

    def set_value(self, e, field):
        setattr(self, field, e.control.value)
        print(f"{field}: {getattr(self, field)}")

    def add(self, e, input_nome, input_email, input_telefone):
        nome = input_nome.value
        email = input_email.value
        telefone = input_telefone.value
        status = "incompleta"
        if nome and email and telefone:
            self.db_execute('INSERT INTO tarefas (nome, email, telefone, status) VALUES(?,?,?,?)', [nome, email, telefone, status])
            input_nome.value = ""
            input_email.value = ""
            input_telefone.value = ""
            self.all()
            self.page.update()
            self.atualizaTela()

    def update(self, e, input_nome, input_email, input_telefone, task_id):
        nome = input_nome.value
        email = input_email.value
        telefone = input_telefone.value
        status = "incompleta"
        if nome and email or telefone:
            self.db_execute('UPDATE tarefas SET nome=?, email=?, telefone=?, status=? WHERE id=?', [nome, email, telefone, status, task_id])
            input_nome.value = ""
            input_email.value = ""
            input_telefone.value = ""
            self.all()
            self.page.update()
            self.atualizaTela()
            self.add_button.content.value = "Adicionar"
            self.add_button.icon = ft.icons.ADD
            self.add_button.on_click = lambda e: self.add(e, self.input_nome, self.input_email, self.input_telefone)
            self.page.update()

    def all(self):
        self.results = self.db_execute('SELECT * FROM tarefas ORDER BY status DESC')
        return self.results

    def atualizaTela(self):
        if self.view == 'all':
            self.results = self.db_execute('SELECT * FROM tarefas ORDER BY status DESC')
        else:
            self.results = self.db_execute('SELECT * FROM tarefas WHERE status = ?', [self.view])
        self.update_tasks_list()
        return self.results

    def tabs_changed(self, e):
        if e.control.selected_index == 0:
            self.view = 'all'
        elif e.control.selected_index == 1:
            self.view = "incompleta"
        elif e.control.selected_index == 2:
            self.view = 'feita'
        self.atualizaTela()
        self.page.update()

    def update_tasks_list(self):
        self.page.controls.clear()
        self.main_page()
        self.page.update()

    def checked(self, e):
        is_checked = e.control.value
        task_id = e.control.data
        if is_checked:
            self.db_execute('UPDATE tarefas SET status = "feita" WHERE id = ?', [task_id])
        else:
            self.db_execute('UPDATE tarefas SET status = "incompleta" WHERE id = ?', [task_id])
        self.update_tasks_list()
        self.atualizaTela()
        self.page.update()

    def delete_task(self, e, email):
        self.db_execute('DELETE FROM tarefas WHERE email = ?', [email])
        self.atualizaTela()
        self.page.update()

    def edit_task(self, e, task_id):
        task = self.db_execute('SELECT * FROM tarefas WHERE id = ?', [task_id])
        if task:
            task = task[0]
            self.input_nome.value = task[1]
            self.input_email.value = task[2]
            self.input_telefone.value = task[3]
            self.page.update()
            self.add_button.content.value = "Atualizar"
            self.add_button.icon = ft.icons.UPDATE
            self.add_button.on_click = lambda e: self.update(e, self.input_nome, self.input_email, self.input_telefone, task_id)
            self.page.update()

    def tasks_container(self):

        return Container(
            height=self.page.height * 0.5,
            content=ListView(
                controls=[
                    Column(
                        controls=[
                    ft.Row(
            
                                controls=[
                                    Checkbox(
                                        value=res[4] == "feita",
                                        on_change=self.checked,
                                        data=res[0],
                                        col={"sm": 6, "md": 4, "xl": 2},
                                    ),
                                
                                    Column(
                                        controls=[
                                            Text(f"Nome: {res[1]}", size=16, color=colors.WHITE, text_align="center"),
                                            Text(f"Email: {res[2]}", size=16, color=colors.WHITE, text_align="center"),
                                            Text(f"Telefone: {res[3]}", size=16, color=colors.WHITE, text_align="center"),
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 2},
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                
                                ft.Row(
                                        controls=[
                                            IconButton(
                                                icon=ft.icons.DELETE,
                                                icon_color=colors.RED,
                                                on_click=lambda e, email=res[2]: self.delete_task(e, email),
                                                col={"sm": 6, "md": 4, "xl": 2},
                                            ),
                                            IconButton(
                                                icon=ft.icons.EDIT,
                                                icon_color=colors.GREEN,
                                                on_click=lambda e, task_id=res[0]: self.edit_task(e, task_id),
                                                col={"sm": 6, "md": 4, "xl": 2},        
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.END
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),
                            Divider(color=colors.GREY)
                        ]
                    ) for res in self.results if res
                ],
                spacing=10,
                padding=10
            ),
            bgcolor=colors.BLACK45,
            border_radius=border_radius.all(10),
            padding=10
        )

    def gerar_pdf(self, e=None):
        buffer = io.BytesIO()
        
        c = canvas.Canvas(buffer, pagesize=letter)
        largura, altura = letter 
        
        c.setStrokeColor(colors.BLACK)
        c.setLineWidth(1)
        c.rect(10, 10, largura - 20, altura - 20)
        
        c.setLineWidth(1)
        c.rect(10, 10, largura - 20, altura - 70)
        
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(largura / 2, altura - 40, "Meus Contatos")
        
        data_hora = datetime.now().strftime("%d/%m/%Y às %H:%M")
        c.setFont("Helvetica-Bold", 12)
        c.drawRightString(largura - 20, altura - 40, f"Emitido em {data_hora}")
        
        data = [["Nome", "Email", "Telefone"]]
        for contato in self.results:
            data.append([contato[1], contato[2], contato[3]])
        
        tabela = Table(data, colWidths=[2 * inch, 2 * inch, 2 * inch])
        
        estilo = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.GREY),  
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.WHITE),   
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),          
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),         
            ('BACKGROUND', (0, 1), (-1, -1), colors.GREY), 
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.WHITE),  
            ('GRID', (0, 0), (-1, -1), 1, colors.BLACK),   
            ('BOX', (0, 0), (-1, -1), 2, colors.BLACK)      
        ])
        tabela.setStyle(estilo)
        
        tabela.wrapOn(c, largura, altura)
        tabela.drawOn(c, 90, altura - 160)
        
        c.save()
        buffer.seek(0)
        
        pdf_writer = PdfWriter()
        pdf_reader = PdfReader(buffer)
        for pagina in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[pagina])
        
        with open("contatos.pdf", "wb") as f:
            pdf_writer.write(f)
        
        print("PDF gerado com sucesso!")
        
        

    def main_page(self):

        self.input_nome = TextField(
            hint_text="Digite o Nome...",
            border_color=colors.WHITE,
            border_radius=border_radius.all(5),
            color=colors.WHITE,
            cursor_color=colors.WHITE,
            multiline=True,
            content_padding=20,
            prefix_icon=ft.icons.DRIVE_FILE_RENAME_OUTLINE,
            capitalization=TextCapitalization.CHARACTERS,
            counter_text="0/20",
            on_change=lambda e: self.set_value(e, 'nome')
        )
        self.input_email = TextField(
            hint_text="Digite o Email...",
            border_color=colors.WHITE,
            border_radius=border_radius.all(5),
            color=colors.WHITE,
            cursor_color=colors.WHITE,
            multiline=True,
            content_padding=20,
            prefix_icon=ft.icons.ALTERNATE_EMAIL,
            capitalization=TextCapitalization.CHARACTERS,
            counter_text="0/25",
            on_change=lambda e: self.set_value(e, 'email')
        )
        self.input_telefone = TextField(
            hint_text="Digite o Telefone...",
            border_color=colors.WHITE,
            input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
            border_radius=border_radius.all(5),
            color=colors.WHITE,
            cursor_color=colors.WHITE,
            multiline=True,
            content_padding=20,
            capitalization=TextCapitalization.CHARACTERS,
            prefix_icon=ft.icons.LOCAL_PHONE_ROUNDED,
            counter_text="0/11",
            on_change=lambda e: self.set_value(e, 'telefone')
        )

        self.add_button = CupertinoButton(
            content=Text("Adicionar", color=colors.BLACK),
            bgcolor=colors.GREY,
            icon=ft.icons.ADD,
            alignment=alignment.top_left,
            border_radius=border_radius.all(15),
            opacity_on_click=0.5,
            on_click=lambda e: self.add(e, self.input_nome, self.input_email, self.input_telefone)
        )
        self.print_button = CupertinoButton(
            content=Text("Imprimir", color=colors.BLACK),
            bgcolor=colors.GREY,
            icon=ft.icons.PRINT,
            alignment=alignment.top_left,
            border_radius=border_radius.all(15),
            opacity_on_click=0.5,
            on_click=self.gerar_pdf
        )

        title = Text(
            value="Agenda de Contatos",
            size=24,
            weight=FontWeight.BOLD,
            color=colors.PRIMARY,
        )

        self.tabs = Tabs(
            selected_index=0 if self.view == 'all' else 1 if self.view == "incompleta" else 2,
            on_change=self.tabs_changed,
            tabs=[
                Tab(text='Todas'),
                Tab(text='Incompletas'),
                Tab(text='Feitas'),
            ]
        )

        tasks = self.tasks_container()

        input_bar = Column(
            controls=[
                self.input_nome,
                self.input_email,
                self.input_telefone,
                Row(
                    controls=[
                        self.add_button,
                        self.print_button,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.START
        )

        self.page.add(
            ft.ResponsiveRow(
                [
                    title, input_bar, Divider(), self.tabs, tasks
                ]
            ),
            
        ),

ft.app(target=App)

import flet as ft
import main as m
import datetime as dt


def main(page: ft.Page):
    page.title = 'Cordyceps®'
    page.window.width = m.WINDOW_WIDTH
    page.window.height = m.WINDOW_HEIGHT
    page.window.resizable = False
    page.update()

    def voltar(e):
        page.clean()
        m.main(page)
    
    # Coluna principal
    _main_column_ = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(
                        'Calendário', 
                        size=m.TEXT_SIZE, 
                        weight='bold'
                    ),
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK_IOS_NEW,
                        icon_size = 15,
                        on_click=voltar,
                    ),
                ]
            ),
            ft.Divider(
                height=2, 
                color='white24'
            ),
            ft.ListView(
                height=m.WINDOW_HEIGHT -180,
                width=m.WINDOW_WIDTH - 100,
                spacing=10,
                controls=[],
                expand=True,
            )
        ]
    )


    meses = [
        'Janeiro',
        'Fevereiro',
        'Março',
        'Abril',
        'Maio',
        'Junho',
        'Julho',
        'Agosto',
        'Setembro',
        'Outubro',
        'Novembro',
        'Dezembro',
    ]
    
    dia_semana = [
        'S',
        'T',
        'Q',
        'Q',
        'S',
        'S',
        'D',
    ]
    
    _row_dia_semana = ft.Row(
        spacing=2,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    

    # Adicionar o conteúdo à página
    page.add(
        ft.Container(
            height=m.WINDOW_HEIGHT - 80,
            bgcolor='bluegrey900',
            border_radius=20,
            alignment=ft.alignment.center,
            content=ft.Stack(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                height=600,
                                width=320,
                                bgcolor=ft.colors.with_opacity(0.6, '#161716'),
                                border=ft.border.all(0.5, 'white'),
                                border_radius=30,
                                padding=ft.padding.only(
                                    top=20, left=25, right=25, bottom=20),
                                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    expand=True,
                                    controls=[_main_column_],
                                )
                            )
                        ],
                    )
                ]
            )
        ),
    )

if __name__ == "__main__":
    ft.app(target=main)
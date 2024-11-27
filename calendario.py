import flet as ft
import main as m
import datetime as dt
import calendar

obj = calendar.Calendar()


def main(page: ft.Page):
    page.title = 'Cordyceps®'
    page.window.width = m.WINDOW_WIDTH
    page.window.height = m.WINDOW_HEIGHT
    page.window.resizable = False
    page.update()
    
    dicionario = {}
    
    ano_atual = int(dt.date.today().strftime('%Y'))
    mes_atual = dt.date.today().strftime('%m')
    dia_atual = int(dt.date.today().strftime('%d'))
    
    
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
    
    for dia in dia_semana:
        _row_dia_semana.controls.append(
            ft.Container(
                width=25,
                height=25,
                border_radius=5,
                alignment=ft.alignment.center,
                content=ft.Text(
                    dia,
                    size=9,
                    color='white',
                )
            )
        )

    # loop para criar o intervalo de anos
    for ano in range(ano_atual - 1, ano_atual + 1):
        dicionario[ano] = {}
        for mes in range(1 , 12):
            coluna_mes = ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            )
            interior = ft.Container(
                visible=True,
                content=coluna_mes,
                
            )
            
            _main_column_.controls.append(
                interior
            )

            _row_ano = ft.Row(
                spacing=2,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        f'{meses[mes - 1]} {ano}',
                        size=12,
                        # text_align=ft.TextAlign.CENTER,
                    )
                ]
            )
            
            coluna_mes.controls.append(
                _row_ano
            )
            coluna_mes.controls.append(
                _row_dia_semana
            )
            
            # # loop para criar o intervalo de dias
            # for chave in dicionario:
            #     dicionario[chave][mes] = {}
            #     for dia in range(1 - 31):
            #         dicionario[chave][mes][dia] = ft.Container(
            #             width=25,
            #             height=25,
            #             border_radius=5,
            #             alignment=ft.alignment.center,
            #             content=ft.Text(
            #                 dia,
            #                 size=9,
            #                 color='white',
            #             )
            #         )

            #         coluna_mes.controls.append(
            #             dicionario[chave][mes][dia]
            #         )
    
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
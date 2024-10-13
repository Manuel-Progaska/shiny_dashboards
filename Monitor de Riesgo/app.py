from shiny.express import ui
from shiny.ui import page_navbar
from functools import partial
import shinyswatch

ui.page_opts(title='MONITOR DE INVERSIONES')#, theme=shinyswatch.theme.pulse)


with ui.sidebar(open='desktop'):
    
    ui.input_dark_mode(mode='light')

    with ui.card():              
        ui.input_select(  
        "fondos",  
        "Fondos:",  
        {"1A": "Choice 1A", "1B": "Choice 1B", "1C": "Choice 1C"},  
        ) 
    

with ui.nav_panel('Riesgo'):
    
    with ui.navset_card_pill(id='metrics'):
        
        with ui.nav_panel("Relativo"):
            
            with ui.layout_columns():
                
                with ui.card():
                    ui.input_date_range("daterange", "Rango de Fechas", start="2020-01-01")
                    ui.input_action_button("range_dates_button", "Actualizar") 
                
                with ui.card():
                    ui.input_radio_buttons(  
                        "bmk",  
                        "Benchmark Tracking Error:",  
                        {"peer": "Peer Group", "categ": "Categoría"},  
                        )   
                    ui.input_action_button("bmk_button", "Actualizar")  
                    
                with ui.card():
                    ui.input_radio_buttons(  
                        "ir_config",  
                        "Escla de Tiempo Informatio Ratio:",  
                        {"anual": "Anual", "mes": "Mensual"},  
                        )    
                    ui.input_action_button("ir_scale_button", "Actualizar")          

                

        with ui.nav_panel("Abosluto"):
            
            'abosluto'
        
    
with ui.nav_panel('Performance'):
    'Performance'





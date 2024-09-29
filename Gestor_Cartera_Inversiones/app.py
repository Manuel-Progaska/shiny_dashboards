from shiny import reactive, render
from shiny.express import input, ui
from shinywidgets import render_plotly
import shinyswatch

## Application settings
 #lumen lux pulse slate zephyr

# Add page title and sidebar
ui.page_opts(title="Gestor de Carteras de Inversiones", fillable=True)

with ui.sidebar(open="desktop"):
    
    ui.input_dark_mode()
    
    # date selector
    ui.input_date(id="date", label="Fecha")
    
    # pais
    ui.input_select(  
        "pais",  
        "País:",  
        {"cl": "Chile", "ec": "Ecuador", "br": "Brasil"},  
    )
    
    # asset class
    ui.input_select(  
        "class",  
        "Clase activo:",  
        {"rv": "Renta Variable", "rf": "Renta Fija"},  
    )
    
    ui.input_action_button("reset", "Cargar data")

# Tabs
with ui.navset_card_pill(id="tab"):  
    with ui.nav_panel("Carteras"):
                
        with ui.navset_card_tab(id="tab_carteras"):  
            
            with ui.nav_panel("Composición"):
                "Composición"

            with ui.nav_panel("Performance"):
                "Performance"
            
            with ui.nav_panel("Benchmark"):
                "Benchmark"
     

    with ui.nav_panel("Límites"):
        
        with ui.navset_card_tab(id="tab_limites"):  
            
            with ui.nav_panel("Resumen"):
                "Resumen"

            with ui.nav_panel("Detalle"):
                "Detalle"


    with ui.nav_panel("Métricas de Riesgo"):
        
        with ui.navset_card_tab(id="tab_metricas"):  
            
            with ui.nav_panel("VaR"):
                "Resumen"

            with ui.nav_panel("Tracking Error"):
                "Detalle"
            
            with ui.nav_panel("Information Ratio"):
                "Detalle"
            
            with ui.nav_panel("Drawdown"):
                "Detalle"
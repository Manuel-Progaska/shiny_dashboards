from shiny import reactive, render
from shiny.express import input, ui
from shinywidgets import render_plotly
import shinyswatch

## Application styling


# Add page title and sidebar
ui.page_opts(title="Gestor de Carteras de Inversiones", fillable=True)

with ui.sidebar(open="desktop", class_='sidebar'):
    
    ui.input_dark_mode()
    
    # date selector
    ui.input_date(id="date", label="Fecha")
    
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
            
            with ui.nav_panel("Benchmark"):
                "Benchmark"
 
    with ui.nav_panel("Métricas de Riesgo"):
        
        with ui.navset_card_tab(id="tab_metricas"):  
            
            with ui.nav_panel("VaR"):
                "VaR"

            with ui.nav_panel("Tracking Error"):
                "Tracking Error"
            
            with ui.nav_panel("Information Ratio"):
                "Information Ratio"
            
            with ui.nav_panel("Drawdown"):
                "Drawdown" 
 
    with ui.nav_panel("Performance"):
         
        "Performance" 

    with ui.nav_panel("Límites"):
        
        with ui.navset_card_tab(id="tab_limites"):  
            
            with ui.nav_panel("Resumen"):
                "Resumen"

            with ui.nav_panel("Detalle"):
                "Detalle"



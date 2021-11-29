
library(shiny)


shinyUI(fluidPage(


    titlePanel("Tarea Shiny Plots"),
    
    tabsetPanel(
      # tabPanel('Tablas en DT',
      #          h1('Vista Basica'),
      #          fluidRow(column(12, DT::dataTableOutput('tabla_1')))
      #          ),
      tabPanel('Clicks plots',
               fluidRow(
                 column(6,
                        plotOutput('plot_click_options',
                                   click = 'clk',
                                   dblclick = 'dclk',
                                   hover = 'mouse_hover',
                                   brush = 'mouse_brush'
                                   ),
                        verbatimTextOutput('click_data')
                        ),
                 column(6,
                        tableOutput('mtcars_tbl')
                        )
               )
      )
    )

    
))

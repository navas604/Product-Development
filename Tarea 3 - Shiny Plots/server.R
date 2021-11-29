
library(shiny)
library(ggplot2)


shinyServer(function(input, output) {
  
  selected <- reactiveVal(rep(FALSE, nrow(mtcars)))
  
  observeEvent(input$clk, {
    clk_point <- nearPoints(mtcars, input$clk, allRows = TRUE)$selected_
    selected(clk_point | selected())
  })
  
##################################  
  observeEvent(input$dclk, {
    #mtcars$Selected <- FALSE
    dclk_action <- nearPoints(mtcars, input$dclk)$selected_
    if(dclk_action == TRUE){
      dclk_action = FALSE
    }
    selected(dclk_action | selected())
  })
##################################  
  # observeEvent(input$mouse_brush, {
  #   brushed_point <- brushedPoints(mtcars, input$mouse_brush, xvar = 'wt', yvar = 'mpg', allRows = TRUE)$selected_
  #   selected(brushed_point | selected())
  # })

  
  output$plot_click_options <- renderPlot({
    mtcars$Selected <- selected()
    ggplot(mtcars, aes(wt, mpg)) +
      geom_point(aes(colour = Selected)) +
      scale_colour_discrete(limits = c("TRUE", "FALSE")) +
      scale_colour_manual(values=c("red", "green"))
  })
  
  output$mtcars_tbl <- renderTable({
    #selected()
    mtcars$Selected <- selected()
    mtcars %>%
      filter(Selected == TRUE)
  })
  
  
  
  
  
  
  
  
  
  
  # selected <- reactiveVal(rep(FALSE, nrow(mtcars)))
  # 
  # observeEvent(input$clk, {
  #   #brushed <- brushedPoints(mtcars, input$plot_brush, allRows = TRUE)$selected_
  #   clk_point <- nearPoints(mtcars, input$clk, xvar = 'wt', yvar = 'mpg')$selected_
  #   selected(clk_point | selected())
  # })
  
  # output$plot_click_options <- renderPlot({
  #   # mtcars$sel <- selected()
  #   # ggplot(mtcars, aes(wt, mpg)) + 
  #   #   geom_point(aes(colour = sel)) +
  #   #   scale_colour_discrete(limits = c("TRUE", "FALSE"))
  #   ggplot(mtcars, aes(wt, mpg)) +
  #     geom_point(alpha = 0.5,
  #                size = 5,
  #                color = "blue",
  #                stroke = 0) +
  #     geom_point(data = nearPoints(mtcars, input$clk, xvar = 'wt', yvar = 'mpg'),
  #                color = 'green',
  #                alpha = 1,
  #                size = 5)
  # })
  
  #output$plot_click_options <- renderPlot({
    #plot <- plot(mtcars$wt, mtcars$mpg, xlab = 'wt', ylab = 'mpg')
    #clk_point_prev <<- mtcars[1,]
    ###clk_point <- nearPoints(mtcars, input$clk, xvar = 'wt', yvar = 'mpg')
    # if (length(clk_point$x_var) > 0) {
    #   clk_point_prev <<- clk_point
    # }
    
    
    # ggplot(mtcars, aes(wt, mpg)) +
    #   geom_point(alpha = 0.5,
    #              size = 5,
    #              color = "blue",
    #              stroke = 0) +
    #   geom_point(data = clk_point,
    #              color = 'green',
    #              alpha = 1,
    #              size = 5)
    
    
    #clk_point <- nearPoints(mtcars, input$clk)#, xvar = 'wt', yvar = 'mpg')
    #clk_point <- nearPoints(mtcars, input$clk)#, threshold = 10, maxpoints = 1)
    
    # plot <- plot +
    #   geom_point(data = clk_point,
    #              color = 'green',
    #              alpha = 1,
    #              size = 5)
    
    #plot
  # })
  
  # output$click_data <- renderPrint({
  #   rbind(c(input$clk$x, input$clk$y),
  #         c(input$dclk$x, input$dclk$y),
  #         c(input$mouse_hover$x, input$mouse_hover$y),
  #         c(input$mouse_brush$xmin, input$mouse_brush$ymin),
  #         c(input$mouse_brush$xmax, input$mouse_brush$ymax)
  #         )
  # })
  
  
  # output$mtcars_tbl <- renderTable({
  #   nearPoints(mtcars, input$clk, xvar = 'wt', yvar = 'mpg')
  #   #df <- brushedPoints(mtcars, input$mouse_brush, xvar = 'wt', yvar = 'mpg')
  #   
  # })
  
  # click = 'clk',
  # dblclick = 'dclk',
  # hover = 'mouse_hover',
  # brush = 'mouse_brush'
  

})

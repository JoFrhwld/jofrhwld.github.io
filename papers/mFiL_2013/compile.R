options(rstudio.markdownToHTML = 
          function(inputFile, outputFile) {      
            system(paste("pandoc","-s --mathjax -H css_and_js.html -t dzslides", shQuote(inputFile), "-o", shQuote(outputFile)))
          }
)  
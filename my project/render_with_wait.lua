function main(splash)
    splash:go("ncar.gov.sa/archive-guide/6")
    splash:wait(0.5)
    return {html=splash:html()}
end
    
import webbrowser
import os

class Html:

    def build_html_table(self, product, machine, instructions):
        
        tiempo = str(instructions.get(instructions.size() - 1).get(0))
        report = ''
        report += '<div class="col-12">\n'
        report += '<table class="table">\n'
        report += '<thead>\n'
        report += "<tr>\n"
        report += "<td scope='col'>Tiempo (s)</td>\n"
        for i in range(0, machine.production_lines_list.size()):
            report += "<td scope='col'>Linea " + str(machine.production_lines_list.get(position = i).number) + "</td>\n"
        report += "</tr>\n"
        report += '</thead>\n'
        report += '<tbody>\n'
        for i in range(0, instructions.size()):
            report += '<tr>\n'
            for index in range(0, instructions.get(i).size()):
                report += "<td>" + str(instructions.get(i).get(position = index)) + "</td>\n"
            report += '</tr>\n'
        report += '</tbody>\n'
        report += '</table>\n'
        report += '</div>\n'

        html = '''<!doctype html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                <title>''' + product.name + '''</title>
                <style>
                    .bg-c {
                        background-color: #fff;
                    }
                    body {
                        background-color: #303E73;
                    }
                    html, body {
                        height: 100%;
                    }
                    h1, p, td {
                        color: #fff;
                    }
                </style>
            </head>
            <body>
            <br />
                <div class="container">
                    <div class="row">
                        <div class="col-8 offset-2">
                            <h1>''' + product.name + '''</h1>
                        </div>
                        <hr />
                        <div class="row">
                            ''' + report + '''
                        </div>
                        <div class="row">
                            <h3>El tiempo optimo para crear el producto llamado ''' + product.name + ''' es ''' + tiempo + ''' segundos</h3>
                        </div>
                    </div>
                </div>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
            </body>
            </html>'''

        file = open('output/' + product.name + '.html', 'w')
        file.write(html)
        file.close()
        filename = 'file://' + os.path.realpath(file.name)
        webbrowser.open_new_tab(filename)
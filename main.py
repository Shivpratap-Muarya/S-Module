# Can be used at the place of print
def p(n):
    print(n)

# For html 
def html(html):
    web = open('index.html', 'w')
    web.write(html)
    web.close()

# For Ruby
def ruby(ruby):
    rb = open('main.rb', 'w')
    rb.write(ruby)
    rb.close()
# For Java 
def java(java):
    j = open('main.java', 'w')
    j.write(java)
    j.close()

# For JavaScript 
def JavaScript(JavaScript):
    js = open('script.js', 'w')
    js.write(JavaScript)
    js.close()

# For Css
def css(css):
  css = open('style.css', 'w')
  css = css.write(css)
  css.close()
 
# For Php
def php(php):
  php = open('php', 'w')
  php = php.write(php)
  php.close()

# Can be used by the Developer make  a web page
def web(first, second, third, forth, web_name):
    file = open('index.html', "w")
    file.write("""<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

    <title>"""+ web_name +"""</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">"""+web_name+"""</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">"""+ first +"""<span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">"""+ second +"""</a>
          </li>          
          <li class="nav-item">
            <a class="nav-link" href="#">"""+ third +"""</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">"""+ forth +"""</a>
          </li>
            </div>
          </li>
        </ul>
      </div>
    </nav>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
  </body>
</html>""")
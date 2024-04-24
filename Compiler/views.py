from django.shortcuts import render
import sys


# Create your views here.

# create index function

def index(request):
    return render(request, 'index.html')


from io import StringIO


def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST.get('codearea', '')  # Get the code area data from the POST request
        output = None  # Initialize output variable

        try:
            # Save original standard output reference
            original_stdout = sys.stdout

            # Create a StringIO object to capture the output
            output_buffer = StringIO()
            sys.stdout = output_buffer

            # Execute code
            exec(codeareadata, globals(), locals())  # Execute the code safely

            # Get the output from the buffer
            output = output_buffer.getvalue()

        except Exception as e:
            # If an exception occurs, set output to the error message
            output = str(e)

        finally:
            # Reset the standard output to its original value
            sys.stdout = original_stdout

    else:
        # If the request method is not POST, set default values
        codeareadata = ''
        output = ''

    # Return and render the index page with code and output data
    return render(request, 'index.html', {"code": codeareadata, "output": output})


def Coding_section(request):
    return render(request, "coding_answers.html")


def html_questions(request):
    return render(request, "htmlindex.html")


def php_questions(request):
    return render(request, "phpindex.html")


def html_answers(request):
    return render(request, "html_answers.html")


def php_answers(request):
    return render(request, "php_answers.html")


from django.shortcuts import render
import markdown


def compile_html(request):
    html_output = None
    if request.method == 'POST':
        markdown_text = request.POST.get('markdown_text', '')
        html_output = markdown.markdown(markdown_text)
    return render(request, 'htmlindex.html', {'html_output': html_output})


import subprocess


def compile_php(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        php_executable = 'C:/Program Files/php-8.3.6/php.exe'
        result = subprocess.run([php_executable, '-r', code], capture_output=True, text=True)
        output = result.stdout
        return render(request, 'phpindex.html', {'code': code, 'output': output})
    return render(request, 'phpindex.html', {'code': '', 'output': ''})

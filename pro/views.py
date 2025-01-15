from django.shortcuts import render,HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse('Hello')
    return render(request, 'index.html')

def about(request):
    return HttpResponse(''' <h1> Tatla <h1> <a href=https://www.youtube.com/shorts/NIKrPkhB6CE> Djanjo codewith Harry</a>''')   

def removepunc(request):
    return HttpResponse('remove punc')

def create(request):
    return HttpResponse("Create <a href='/'>back</a>")


def analyzed(request):
    # Get the form data
    djtext = request.POST.get('text', 'default')  # Get the text from the form
    removepunc = request.POST.get('removepunc', 'off')  # Get the option for removing punctuation
    fullcaps = request.POST.get('fullcaps', 'off')  # Get the option for converting to uppercase
    analyzed = djtext  # Start with original text

    # Create the context dictionary for rendering
    context = {'analyzed_text': analyzed}

    # Punctuation string for removal
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_'''

    # Remove punctuation if the user chose that option
    if removepunc == "on":
        analyzed = ""  # Reset analyzed text
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        context['purpose'] = 'Remove Punctuations'  # Set the purpose for the operation
        context['analyzed_text'] = analyzed  # Update analyzed text in context

    # Change to uppercase if the user chose that option
    if fullcaps == "on":
        analyzed = ""  # Reset analyzed text
        for char in djtext:
            analyzed += char.upper()
        # Append to the purpose if already set, or set it for the first time
        if 'purpose' in context:
            context['purpose'] += ' & Change to UPPER CASE'
        else:
            context['purpose'] = 'Change to UPPER CASE'
        context['analyzed_text'] = analyzed  # Update analyzed text in context

    # If neither option is selected, you can return a default response, like an error message
    if removepunc != "on" and fullcaps != "on":
        context['purpose'] = 'Error'
        context['analyzed_text'] = 'Please select an operation'

    # Finally, return the rendered response
    return render(request, 'analyzed.html', context)

def ex1(request):
    s = ''' <h2> Navigationn Bar <br></h2>
                <a href= "https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0w_9;II9ah7DDtYtflgwMwpT3XY9">Tatla</a>
                <br>
                <a href="https://www.facebook.com/">facebook</a><br>
                <a href="https://www.flipkart.com/">flipkart</a><br>
                <a href="https://www.google.com/">google</a> '''
    return HttpResponse(s)

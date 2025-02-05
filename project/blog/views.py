from django.shortcuts import render

Programming_Language = {
    "python": {
        "id": 1,
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    },
    "java": {
        "id": 2,
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    },
}


def language_list(request):
    return render(request, "index.html")
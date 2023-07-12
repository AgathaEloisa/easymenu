def total_productos(request):
    if request.session['listaProductos'].items():
        return print('nosewn')
class ListaProductos:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        listaProducto = self.session['listaProducto']
        if not listaProducto:
            self.session['listaProducto'] = []
            self.listaProducto = self.session['listaProducto']
        else:
            self.listaProducto = listaProducto

    
    def agregar(self, producto):
        id = producto.id
        if id not in self.listaProducto.keys():
            self.listaProducto[id]=[
                producto.id
            ]
        self.guardarMenu()

    def guardarMenu(self):
        self.session['listaProducto'] = self.listaProducto
        self.session.modified = True

    def eliminar(self, producto):
        id = producto.id
        if id in self.listaProducto:
            del self.listaProducto[id]
            self.guardarMenu()

    def limpiar(self):
        self.session['listaProducto'] = []
        self.session.modified = True
from django.views.generic import View, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import carta, productos
from .forms import ProductoForm
from django.urls import reverse_lazy

@login_required
def AdminView(request):
    products = productos.objects.all()
    context = {
        'products': products
    }
    return render(request, 'admin/admin.html', context)

def NuevoProductoView(request):
    form = ProductoForm()
    context = {
        'form': form
    }
    return render(request, 'admin/nuevo_producto.html', context)

def EditarProductoView(request, codigo):
    codigo = get_object_or_404(productos, pk=codigo)
    context = {
        'form': ProductoForm(),
        'codigo': codigo
    }
    if request.method == 'POST':
        prodForm = ProductoForm(data=request.POST)
        if prodForm.is_valid():
            Parent_obj = None
            try:
                Parent_id = int(request.POST.get('Parent_id'))
            except:
                Parent_id = None
                
            if Parent_id:
                Parent_obj = productos.objects.get(id=Parent_id)
                if Parent_obj:
                    reply_product = prodForm.save(commit=False)
                    reply_product.Parent = Parent_obj
            new_product = prodForm.save(commit=False)
            new_product.Post = codigo
            new_product.save()
            return redirect('admin/admin.html')
    # if request.method == 'post':
    #     prodForm = ProductoForm(request.POST)
    #     if prodForm.is_valid():
    #        categoria = prodForm.cleaned_data.get('categoria')
    #        codigo = prodForm.cleaned_data.get('codigo')
    #        nombre = prodForm.cleaned_data.get('nombre')
    #        precio = prodForm.cleaned_data.get('precio')
    #        descripcion = prodForm.cleaned_data.get('descripcion')

    #         p, created = productos.objects.get_or_create(categoria=categoria,codigo=codigo,nombre=nombre,precio=precio,descripcion=descripcion)
    #         p.save()
    #         return redirect('admin/admin.html')
        
    return render(request, 'admin/editar_producto.html', context)

def detalleProductoView(request, codigo):
    prod = get_object_or_404(productos, codigo = codigo)
    context = {
        'prod': prod
    }
    return render(request, 'admin/detalle_producto.html', context)

# class EditarProductoView(UpdateView):
#     model = productos
#     field=["categoria","codigo","nombre","precio","descripcion"]
#     template_name = 'admin/editar_producto.html'

#     def get_succes_url(self) -> str:
#         pk = self.kwargs['pk']
#         return reverse_lazy('administracion:home', kargs={'pk':pk})
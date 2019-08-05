from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):
    titulo      = forms.CharField(label='', widget=forms.TextInput(
                        attrs={"placeholder": "Título del Producto"}))
    
    descripcion = forms.CharField(
                    required=False,
                    widget=forms.Textarea(
                        attrs={
                            "class": "class-name-two",
                            "id": "descripcion-text-area",
                            "rows": 20,
                            'cols': 120
                        }
                    )
    )
    
    precio      = forms.DecimalField(initial=199.99)
    
    class Meta:
        model = Producto
        fields = [
            'titulo',
            'descripcion',
            'precio'
        ]
    
    def clean_titulo(self, *args, **kwargs):       
        titulo = self.cleaned_data.get("titulo")
        print(titulo)
        if "CFE" in titulo:
            print("ok")
            return titulo        
        else:
            print("error")
            #raise forms.ValidationError("No es un título válido")
        

class RawProductoForm(forms.Form):
    titulo      = forms.CharField(
                    label='', 
                    widget=forms.TextInput(
                        attrs={
                            "placeholder": "Título del Producto",
                            
                        }
                    ) 
    )
    descripcion = forms.CharField(
                    required=False,
                    widget=forms.Textarea(
                        attrs={
                            "class": "class-name-two",
                            "id": "descripcion-text-area",
                            "rows": 20,
                            'cols': 120
                        }
                    )
    )
    precio      = forms.DecimalField()
        
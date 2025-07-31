from django import forms

TIPO_CHOICES = [
        ('Amigos', 'Amigos'),
        ('Familiar', 'Familiar'),
        ('Cumpleaños', 'Cumpleaños'),
    ]

CANTIDAD_CHOICES = [
        ('5-10', '5 a 10 personas'),
        ('11-15', '11 a 15 personas'),
        ('15+', 'Más de 15 personas'),
    ]

DISEÑO_CHOICES = [
        ('libre', 'Libre'),
        ('botanico', 'Con dibujo botánico para pintar'),
        ('mix', 'Mix'),
    ]   

class WorkshopPresupuestoForm(forms.Form):
        tipo = forms.ChoiceField(choices=TIPO_CHOICES, label='Tipo de taller')
        cantidad = forms.ChoiceField(choices=CANTIDAD_CHOICES, label='Cantidad de personas')
        diseño = forms.ChoiceField(choices=DISEÑO_CHOICES, label='Diseño')
        catering = forms.BooleanField(required=False, label='¿Incluye catering?')

        email = forms.EmailField(label='Tu email')
        telefono = forms.CharField(label='Tu teléfono')
        
    
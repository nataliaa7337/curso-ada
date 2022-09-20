def puede_graduarse(asistencia, materiasAprobadas, TesisAprobada):
    if asistencia == 75 and materiasAprobadas >= 50 and TesisAprobada == 'Si': 
        return True
    else:
        return False
puede_graduarse(75, 80, 'Si')
    
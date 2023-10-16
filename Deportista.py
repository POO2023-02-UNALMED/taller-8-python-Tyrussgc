class Deportista():
    def __init__(self,añosPracticando):
        self._deporte = "Futbol"
        self._añosPracticando = añosPracticando

    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self,Deporte):
        self._deporte = Deporte

    def getAñosPracticando(self):
        return self._añosPracticando
    
    def setAñosPracticando(self,AñosPracticando):
        self._añosPracticando = AñosPracticando
class FechaHora:
    __dia = 0
    __mes = 0
    __año = 0
    __hora = 0
    __minuto = 0
    __segundo = 0
    
    def __init__(self,d=1,m=1,a=2020,h=0,minu=0,seg=0):
        self.__dia = d
        self.__mes = m
        self.__año = a
        self.__hora = h
        self.__minuto = minu
        self.__segundo = seg
    
    def Mostrar(self):
        print('%.2d/%.2d/%.2d\t -\t %.2d:%.2d:%.2d' % (self.__dia, self.__mes, self.__año, self.__hora, self.__minuto, self.__segundo))
        self.Validar(self.__dia, self.__mes, self.__año, self.__hora, self.__minuto, self.__segundo)

    def Validar(self, dia, mm, aa, hs, mi, seg):
        bandera = False
        if hs in range (0, 24) and type(hs) == int:
            if mi in range (0, 60) and type(mi) == int:
                if seg in range (0, 60) and type(seg) == int:
                    if mm in [1, 3, 5, 7, 8, 10, 12]:
                        if dia in range (1, 32) and type(dia) == int:
                            bandera = True
                    elif mm in [4, 6, 9, 11]:
                        if dia in range (1, 31) and type(dia) == int:
                            bandera = True
                    elif mm == 2:
                        if (self.Bisiesto(aa)):
                            if dia in range (1, 30) and type(dia) == int:
                                bandera = True
                        else: 
                            if dia in range (1, 29) and type(dia) == int:
                                bandera = True
        if bandera:
            print('\nFecha y Hora ingresada es valida\n')
        else:
            print('\nFecha Y hora incorrectas\n')
                        
    def Bisiesto(self, aa):
        bisiesto = False
        if aa % 4 == 0 and (aa % 100 != 0 or aa % 400 == 0):
            bisiesto = True
        return bisiesto
    
    def PonerEnHora(self,hs=0, minu=0, seg=0):
        self.__hora = hs
        self.__minuto = minu
        self.__segundo = seg
        
    def AdelantarHora(self,hs=0, minu=0, seg=0):
        self.__hora += hs
        self.__minuto += minu
        self.__segundo += seg
        if seg >= 60:
            self.__segundo = seg % 60
            self.__minuto += seg // 60
        if minu >= 60:
            self.__minuto = minu % 60
            self.__hora += minu // 60
        if hs >= 24:
            self.__hora = hs % 24
            self.__dia += hs // 24
        if self.__mes in [1,3,5,7,8,10,12]:
            if self.__dia >= 31:
                if self.__mes >= 12:
                    self.__año += 1
                    self.__mes = 1
                    self.__dia = (self.__dia % 31) + 1
        elif self.__mes in [4,6,9,11]:
            if self.__dia >= 30:
                self.__mes += self.__dia // 30
                self.__dia = (self.__dia % 30) + 1
        elif self.__mes==2: #  Controlar si el año es bisiesto
            Bisiesto = self.Bisiesto(self.__año)

            if Bisiesto == True: #  Cambio para los meses de 29 dias
                if self.__dia >= 29:
                    self.__mes += self.__dia // 29  #  suma el resultado de la division.
                    self.__dia = (self.__dia % 29)  #  si la division no da exacta sumo el resto
            else:
                if self.__dia >= 28: #  Cambio para los meses de 28 dias
                    self.__mes += self.__dia // 28
                    self.__dia = (self.__dia % 28)

         #  Actualizacion de meses y años en quinto lugar y ultimo lugar.
        if self.__mes > 12:
            self.__año += self.__mes // 24
            self.__mes = self.__mes % 24
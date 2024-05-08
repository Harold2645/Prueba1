from conexion import *

class hojasvida:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()

    def consultarTractor(self, idObjeto):
        sql = f"SELECT * FROM tractores WHERE idobjeto='{idObjeto}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregarA(self, AgregarA):
        agre = f"UPDATE tractores SET nodstractor='{AgregarA[1]}',nosmotor='{AgregarA[2]}',potenciadmotor='{AgregarA[3]}',pasodtractor='{AgregarA[4]}',numerodcilindro='{AgregarA[5]}',tipodmotorlv='{AgregarA[6]}',numerodcha='{AgregarA[7]}',numerodcer='{AgregarA[8]}' WHERE idobjeto='{AgregarA[0]}"
        self.cursor.execute(agre)
        self.mysql.commit()
    
    def agregarB(self, AgregarB):
        agre = f"UPDATE tractores SET tipodtraccion='{AgregarB[1]}',distanciaeejes='{AgregarB[2]}',alturadpacded='{AgregarB[3]}',alturatotal='{AgregarB[4]}',alturadetatdlc='{AgregarB[5]}',alturamlb='{AgregarB[6]}',longitudtilbdt='{AgregarB[7]}',anchototalf='{AgregarB[8]}',anchototalg='{AgregarB[9]}',alturadpaddl='{AgregarB[10]}',alturadpadtn='{AgregarB[11]}',distanciadpato='{AgregarB[12]}',tomafnde='{AgregarB[13]}',tomafrtrm='{AgregarB[14]}' WHERE idobjeto='{AgregarB[0]}"
        self.cursor.execute(agre)
        self.mysql.commit()

    def agregarC(self, AgregarC):
        agre = f"UPDATE tractores SET tipodidcncr='{AgregarC[1]}',marcadlbdi='{AgregarC[2]}',referenciadlbdin='{AgregarC[3]}',tensionesdlltsr='{AgregarC[4]}',tencionmdllt='{AgregarC[5]}',cargampslrt='{AgregarC[6]}',desgastedlrt='{AgregarC[7]}',dimesionesdlldsr='{AgregarC[8]}',presionmdlld='{AgregarC[9]}',cargampslrd='{AgregarC[10]}',desgastesdlrd='{AgregarC[11]}' WHERE idobjeto='{AgregarC[0]}"
        self.cursor.execute(agre)
        self.mysql.commit()   

    def agregarD(self, AgregarD):
        agre = f"UPDATE tractores SET aceitemotor='{AgregarD[1]}',aceitehidraulico='{AgregarD[2]}',aceitetransmision='{AgregarD[3]}',aceiteddd='{AgregarD[4]}',aceiteldf='{AgregarD[5]}',filtrodammr='{AgregarD[6]}',filtrodcmr='{AgregarD[7]}',filtrodahmr='{AgregarD[8]}',filtrodapmr='{AgregarD[9]}',filtrodasmr='{AgregarD[10]}',bateriamr='{AgregarD[11]}',numerodpelrta='{AgregarD[12]}',numerodpelrt='{AgregarD[13]}' WHERE idobjeto='{AgregarD[0]}"
        self.cursor.execute(agre)
        self.mysql.commit()

    def agregarE(self, AgregarE):
        agre = f"UPDATE tractores SET ftdrenaje='{AgregarE[1]}',ftbateria='{AgregarE[2]}',ftfiltroac='{AgregarE[3]}',ftfiltroar='{AgregarE[4]}',ftfiltroachid='{AgregarE[5]}',ftfiltrocomb='{AgregarE[6]}',ftcabeza='{AgregarE[7]}' WHERE idobjeto='{AgregarE[0]}"
        self.cursor.execute(agre)
        self.mysql.commit()


misFichas = hojasvida(conexion) 

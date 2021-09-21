#CSVcreator

from Cancion import Cancion
import  os, csv
import time 


class CSVcreator():
    def __init__(self, sDirectory):
        self.songsDirectory = sDirectory
        self.cancionPool = {}
        self.CVSName = "FeaturesObtain.csv"
        self.createCanciones()
        self.storeCSV()
        print("[--INFO--] ¡¡FIN!!")

    

    def createCanciones(self):
        print("[--INFO--] Leyendo directorios y obteniendo características de las canciones...")
        
        carpetasMusic = os.listdir(self.songsDirectory)
        for dir in carpetasMusic:
            listNameCanciones = [arch.name for arch in os.scandir(self.songsDirectory+"/"+dir) if arch.is_file()]
            for c in listNameCanciones:
                try:
                    can = Cancion(self.songsDirectory + "/" + dir + "/" + c)
                    can.setGenero(dir)
                    self.cancionPool[c] = can
                    print("[--INFO--] OK -- OK ", c)
                except:
                    print("[--INFO--] No fue posible obtener características de: ", c)
        print("[--INFO--] Características obtenidas.")
        
            
    

    def storeCSV(self):
        print("[--INFO--] Creando archivo CSV...")
        with open(self.CVSName, 'w', newline='') as  featuresCSV:
            writer = csv.writer(featuresCSV)
            writer.writerow(["Name", "zcr", "flt", "lds", "alds", "strpk", "nrg", "cntr", "flu", "rof", "entr", "danc", "bpm", "tufre", "ptch", "tmpo", "edmk", "edm", "mfcc1", "mfcc2", "mfcc3", "mfcc4", "mfcc5, gen"])
            for c in self.cancionPool:
                writer.writerow([c, str(self.cancionPool[c].zcr), str(self.cancionPool[c].flatness), str(self.cancionPool[c].loudness), str(self.cancionPool[c].average_loudness), str(self.cancionPool[c].s_strongpeak), str(self.cancionPool[c].s_energy), str(self.cancionPool[c].s_centroid), str(self.cancionPool[c].s_flux), str(self.cancionPool[c].s_rolloff), str(self.cancionPool[c].s_entropy), str(self.cancionPool[c].danceability), str(self.cancionPool[c].rythm_bpm), str(self.cancionPool[c].tunning_freq), str(self.cancionPool[c].pitch_salience), str(self.cancionPool[c].tempo), self.cancionPool[c].edmaKey, self.cancionPool[c].edmaScale, str(self.cancionPool[c].mfcc[0]), str(self.cancionPool[c].mfcc[1]), str(self.cancionPool[c].mfcc[2]), str(self.cancionPool[c].mfcc[3]), str(self.cancionPool[c].mfcc[4]), self.cancionPool[c].genero])
        


initialTime = time.time()

c = CSVcreator("../../../g/LuisOviedoPDG/music") 
# Carpeta donde se encuentran las canciones organizadas por genero en 
# directorios diferentes 
# Ejemplo de directorios usado: 
#/mnt/g/LuisOviedoPDG/music/Salsa
#/mnt/g/LuisOviedoPDG/music/Merengue
#/mnt/g/LuisOviedoPDG/music/Reggae
#/mnt/g/LuisOviedoPDG/music/Bachata
#/mnt/g/LuisOviedoPDG/music/Vallenato


finalTime = time.time()

print("[--INFO--] El tiempo total de ejecución fue: ", finalTime-initialTime)

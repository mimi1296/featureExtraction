#CSVcreator

from Cancion import Cancion, os
import  csv
import time 


class CSVcreator():
    def __init__(self, sDirectory):
        self.songsDirectory = sDirectory
        self.cancionPool = {}
        self.CVSName = "FeaturesObtain.csv"
        self.createCanciones()
        
        print("[--INFO--] ¡¡FIN!!")

    

    def createCanciones(self):
        print("[--INFO--] Leyendo directorios y obteniendo características de las canciones...")
        
        carpetasMusic = os.listdir(self.songsDirectory)
        #print(carpetasMusic)
        
        with open(self.CVSName, 'w', newline='') as  featuresCSV:
            writer = csv.writer(featuresCSV)
            writer.writerow(["Name", "zcr", "flt", "lds", "alds", "strpk", "nrg", "cntr", "flu", "rof", "entr", "danc", "bpm", "tufre", "ptch", "tmpo", "edmk", "edm", "mfcc1", "mfcc2", "mfcc3", "mfcc4", "mfcc5", "gen"])
            for dir in carpetasMusic:
                listNameCanciones = [arch.name for arch in os.scandir(self.songsDirectory+"/"+dir) if arch.is_file()]
                for c in listNameCanciones:
                    try:
                        can = Cancion(self.songsDirectory + "/" + dir + "/" + c)
                        print("Se crea canción")
                        can.setGenero(dir)
                        writer.writerow([c, str(can.zcr), str(can.flatness), str(can.loudness), str(can.average_loudness), str(can.s_strongpeak), str(can.s_energy), str(can.s_centroid), str(can.s_flux), str(can.s_rolloff), str(can.s_entropy), str(can.danceability), str(can.rythm_bpm), str(can.tunning_freq), str(can.pitch_salience), str(can.tempo), can.edmaKey, can.edmaScale, str(can.mfcc[0]), str(can.mfcc[1]), str(can.mfcc[2]), str(can.mfcc[3]), str(can.mfcc[4]), can.genero])
                        print("[--INFO--] OK -- OK ", c)
                    except:
                        print("[--INFO--] No fue posible obtener características de: ", c)
        print("[--INFO--] Características obtenidas.")
        
            
    

    def storeCSV(self):
        print("[--INFO--] Creando archivo CSV...")
        with open(self.CVSName, 'w', newline='') as  featuresCSV:
            writer = csv.writer(featuresCSV)
            writer.writerow(["Name", "zcr", "flt", "lds", "alds", "strpk", "nrg", "cntr", "flu", "rof", "entr", "danc", "bpm", "tufre", "ptch", "tmpo", "edmk", "edm", "mfcc1", "mfcc2", "mfcc3", "mfcc4", "mfcc5", "gen"])
            for c in self.cancionPool:
                writer.writerow([c, str(can.zcr), str(can.flatness), str(can.loudness), str(can.average_loudness), str(can.s_strongpeak), str(can.s_energy), str(can.s_centroid), str(can.s_flux), str(can.s_rolloff), str(can.s_entropy), str(can.danceability), str(can.rythm_bpm), str(can.tunning_freq), str(can.pitch_salience), str(can.tempo), can.edmaKey, can.edmaScale, str(can.mfcc[0]), str(can.mfcc[1]), str(can.mfcc[2]), str(can.mfcc[3]), str(can.mfcc[4]), can.genero])
        


initialTime = time.time()

c = CSVcreator("../../../Music/WAV") 
# Carpeta donde se encuentran las canciones organizadas por genero en 
# directorios diferentes 
# Ejemplo de directorios usado: 
#/mnt/g/LuisOviedoPDG/music/Salsa
#/mnt/g/LuisOviedoPDG/music/Merengue
#/mnt/g/LuisOviedoPDG/music/Reggae
#https://www.youtube.com/watch?v=K6oYyG0KcvQ&list=PLwY9l4M25GOJqIx-Dn-PmYs1KjPd80-1N YAA
#https://www.youtube.com/watch?v=lWKaMeJRiik&list=PLOzQFWHEFankpJykvzRJ6W5mF81ojL9I5 YAA
#/mnt/g/LuisOviedoPDG/music/Bachata
#https://www.youtube.com/watch?v=sH1i5p7xNZg&list=PLfFMDPanvFzQoOkW_jLXjfFuxKmXqtMug YAA
#https://www.youtube.com/watch?v=5wirI7FlO-Q&list=PLOX39_IQMj5dHd_HkBeUcsdmXc3RQ1Cm7 FALTA
#/mnt/g/LuisOviedoPDG/music/Vallenato
#/mnt/g/LuisOviedoPDG/music/Rock
#https://www.youtube.com/watch?v=WRcCBI5rFfM&list=PL_86NZWyc0FsJF98CRytnzItb5EXMQOne YAA
#/mnt/g/LuisOviedoPDG/music/Pop
# https://www.youtube.com/playlist?list=PLNxOe-buLm6cz8UQ-hyG1nm3RTNBUBv3K
#/mnt/g/LuisOviedoPDG/music/Jazz
#https://www.youtube.com/watch?v=vmDDOFXSgAs&list=PL-Ib9oOPR7OHKLBFVkiq0F0rppCZ7YFLp YAA
#https://www.youtube.com/watch?v=ZZcuSBouhVA&list=PL8F6B0753B2CCA128
#https://www.youtube.com/watch?v=qfIiYBMIgJs&list=PLiy0XOfUv4hFHmPs0a8RqkDzfT-2nw7WV
finalTime = time.time()

print("[--INFO--] El tiempo total de ejecución fue: ", finalTime-initialTime)

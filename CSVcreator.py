#CSVcreator

from Cancion import Cancion
import  os, csv


class CSVcreator():
    def __init__(self, sDirectory):
        self.songsDirectory = sDirectory
        self.cancionPool = {}
        self.CVSName = "FeaturesObtain.csv"
        self.createCanciones()
        self.storeCSV()

    

    def createCanciones(self):
        carpetasMusic = os.listdir(self.songsDirectory)
        for dir in carpetasMusic:
            listNameCanciones = [arch.name for arch in os.scandir(self.songsDirectory+"/"+dir) if arch.is_file()]
            for c in listNameCanciones:
                print(c)
                can = Cancion(self.songsDirectory + "/" + dir + "/" + c)
                can.setGenero(dir)
                self.cancionPool[c] = can

    

    def storeCSV(self):
        print("[--Info--] Creando archivo CSV...")
        with open(self.CVSName, 'w', newline='') as  featuresCSV:
            writer = csv.writer(featuresCSV)
            writer.writerow(["Name", "zcr", "flt", "lds", "alds", "strpk", "nrg", "cntr", "flu", "rof", "entr", "danc", "bpm", "tufre", "ptch", "tmpo", "edmk", "edm", "mfcc1", "mfcc2", "mfcc3", "mfcc4", "mfcc5, gen"])
            for c in self.cancionPool:
                writer.writerow([c, str(self.cancionPool[c].zcr), str(self.cancionPool[c].flatness), str(self.cancionPool[c].loudness), str(self.cancionPool[c].average_loudness), str(self.cancionPool[c].s_strongpeak), str(self.cancionPool[c].s_energy), str(self.cancionPool[c].s_centroid), str(self.cancionPool[c].s_flux), str(self.cancionPool[c].s_rolloff), str(self.cancionPool[c].s_entropy), str(self.cancionPool[c].danceability), str(self.cancionPool[c].rythm_bpm), str(self.cancionPool[c].tunning_freq), str(self.cancionPool[c].pitch_salience), str(self.cancionPool[c].tempo), self.cancionPool[c].edmaKey, self.cancionPool[c].edmaScale, str(self.cancionPool[c].mfcc[0]), str(self.cancionPool[c].mfcc[1]), str(self.cancionPool[c].mfcc[2]), str(self.cancionPool[c].mfcc[3]), str(self.cancionPool[c].mfcc[4]), self.cancionPool[c].genero])
        print("[--Info--] ¡¡FIN!!")



c = CSVcreator("../youtubeMusicDownloader/music")
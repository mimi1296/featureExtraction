# Cancion.py
from numpy import mean
import numpy as np
import librosa, os, json
if os.name != 'nt':

    import essentia.standard as es

# Clase Cancion contiene las características de la canción. Cuando se crea, se obtienen
class Cancion(): 
    def __init__(self, nam) :
        self.name = nam
        self.directory = os.path.dirname(nam)
        self.sr =  48000.0
        self.y, self.sr = librosa.load(self.name, sr=self.sr)
        self.frameSize = 2048
        self.hopSize = 1024
        self.n_fft = 2048
        # Features/características que se calculan al con el llamado a la función setFeatures()
        self.zcr = 0.0
        self.flatness = 0.0
        self.loudness = 0.0
        self.average_loudness = 0.0
        self.s_strongpeak = 0.0
        self.s_energy = 0.0
        self.s_centroid = 0.0
        self.s_flux = 0.0
        self.s_rolloff = 0.0
        self.s_entropy = 0.0
        self.danceability = 0.0
        self.rythm_bpm = 0.0
        self.tunning_freq = 0.0
        self.pitch_salience = 0.0
        self.tempo = 0.0
        self.edmaKey = ""
        self.edmaScale = ""
        self.mfcc = []
        self.genero = ""
        self.setFeatures()
        print("[--Info--] Se ha creado correctamente: ", self.name)

    def setFeatures(self):
        if os.name =='nt':
            resultFileName = "TempCancion.txt"
            print("windows")
            os.system(r'essentia_streaming_extractor_music.exe "' + self.name + '" "'+ resultFileName +'"') #r'essentia_streaming_extractor_music.exe "'
            data = ""
            
            with open(resultFileName, 'r') as file:
                data = file.read().replace('\n', ' ')
            json_data = json.loads(data)
            
            self.zcr = json_data["lowlevel"]["zerocrossingrate"]["mean"]
            self.flatness = json_data["lowlevel"]["barkbands_flatness_db"]["mean"]
            self.loudness = json_data["lowlevel"]["loudness_ebu128"]["integrated"]
            self.average_loudness = json_data["lowlevel"]["average_loudness"]
            self.s_strongpeak = json_data["lowlevel"]["spectral_strongpeak"]["mean"]
            self.s_energy = json_data["lowlevel"]["spectral_energy"]["mean"]
            self.s_centroid = json_data["lowlevel"]["spectral_centroid"]["mean"]
            self.s_flux = json_data["lowlevel"]["spectral_flux"]["mean"]
            self.s_rolloff = json_data["lowlevel"]["spectral_rolloff"]["mean"]
            self.s_entropy = json_data["lowlevel"]["spectral_entropy"]["mean"]
            self.danceability = json_data["rhythm"]["danceability"]
            self.rythm_bpm = json_data["rhythm"]["bpm"]
            self.tunning_freq = json_data["tonal"]["tuning_frequency"]
            self.pitch_salience = json_data["lowlevel"]["pitch_salience"]["mean"]
            self.mfcc = json_data["lowlevel"]["mfcc"]["mean"]
            self.edmaKey = json_data["tonal"]["key_edma"]["key"]
            self.edmaScale = json_data["tonal"]["key_edma"]["scale"]
            print(json_data["lowlevel"]["spectral_centroid"]["mean"])
            os.remove(resultFileName)

            
            print(json_data["lowlevel"]["zerocrossingrate"]["mean"])
        else: 
            print("linux")

            features, features_frames = es.MusicExtractor(analysisSampleRate=self.sr, lowlevelFrameSize=self.frameSize, lowlevelHopSize=self.hopSize, 
                                                    lowlevelStats=['mean', 'stdev'],
                                                    rhythmStats=['mean', 'stdev'],    
                                                    tonalStats=['mean', 'stdev'])(self.name)

            self.zcr = features['lowlevel.zerocrossingrate.mean']
            self.flatness = features['lowlevel.barkbands_flatness_db.mean']
            self.loudness = features['lowlevel.loudness_ebu128.integrated']
            self.average_loudness = features['lowlevel.average_loudness']
            self.s_strongpeak = features['lowlevel.spectral_strongpeak.mean']
            self.s_energy = features['lowlevel.spectral_energy.mean']
            self.s_centroid = features['lowlevel.spectral_centroid.mean']
            self.s_flux = features['lowlevel.spectral_flux.mean']
            self.s_rolloff = features['lowlevel.spectral_rolloff.mean']
            self.s_entropy = features['lowlevel.spectral_entropy.mean']
            self.danceability =  features['rhythm.danceability']
            self.rythm_bpm = features['rhythm.bpm']
            self.tunning_freq = features['tonal.tuning_frequency']
            self.pitch_salience = features['lowlevel.pitch_salience.mean']
            
            self.mfcc = features['lowlevel.mfcc.mean']
            self.edmaKey = features['tonal.key_edma.key']
            self.edmaScale = features['tonal.key_edma.scale']
        
        self.tempo, beat_frames = librosa.beat.beat_track(y=self.y, sr=self.sr)

    def setGenero(self, gen):
        self.genero = gen

#prueba
#c = Cancion('../youtubeMusicDownloader/music/Fabricando Fantasias - Tito Nieves (video oficial) HD [1080p]-GhciBgYbA74-recortado.wav')


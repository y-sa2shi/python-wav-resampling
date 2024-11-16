import glob
import os
import librosa
import soundfile as sf

#--------------- パラメータ設定 ---------------
target_sr=22050
resampling_dir ="../Resampling"
resampling_dir_path = resampling_dir+"/"+ str(target_sr)+"Hz"+"/"+"wav"   #リサンプリング後のwavファイルを格納するフォルダ名

wav_name = "arctic_a0001.wav"                                             #読み込むwavファイル名

#---------------------------------------------

wav_path = resampling_dir_path +"/"+ wav_name
y, sr = librosa.load(wav_path) #yは波形 srはサンプリング周波数

print(sr)
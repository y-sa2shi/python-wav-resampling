import glob
import os
import librosa
import soundfile as sf
import pathlib 

#--------------- パラメータ設定 ---------------

wav_path  = "jvs_male"                  #リサンプリングするwavファイルが格納されたフォルダ

target_sr=16000                                      #リサンプリング後のサンプリング周波数
resampling_dir ="../Resampling"                       #リサンプリング後のwavファイルを格納するフォルダ名

#---------------------------------------------

def cast(ParentalClass, child_object):
    child_object.__class__ = ParentalClass

def main():
    
    # number_wav_files = glob.glob(wav_path+'/*.wav')      #wav_path(フォルダ内に)にあるwavファイル数
    wav_list  = []                                       #wav_path(フォルダ内に)にあるwavファイル名をlistに格納

    # get_file_list = list(pathlib.Path(wav_path).glob('**/*.wav')) 

    get_file_list = pathlib.Path(wav_path)  
    for file_path in get_file_list.glob('**/*.wav'):
        wav_list.append(file_path)

    print(wav_list)

    if type(wav_list[0]) == 'pathlib.WindowsPath':
        p= str(wav_list[0])+"\wwwtxt"
        print(p)

    
    #リサンプリング後に格納するフォルダを作成
    # os.makedirs(resampling_dir+"/"+ str(target_sr)+"Hz"+"/"+wav_path)
    # resampling_dir_path = resampling_dir+"/"+ str(target_sr)+"Hz"

    # for n_wav in range (len(wav_list)):
        # befor_wav_path = wav_list[n_wav]
        # y, orig_sr = librosa.load(befor_wav_path) #yは波形 orig_srは元のサンプリング周波数

        # target_y = librosa.resample(y, orig_sr, target_sr) #リサンプリング
        # resampling_wav_path =  resampling_dir_path  + "/" + wav_list[n_wav]
        # librosa.audio.sf.write(resampling_wav_path , target_y, target_sr) #リサンプリング用のフォルダにwavファイル作成

if __name__ == "__main__":
    main()
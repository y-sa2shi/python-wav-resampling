import glob
import os
import librosa
import soundfile as sf
import argparse

#--------------- パラメータ設定 ---------------

target_sr=16000                                      #リサンプリング後のサンプリング周波数
resampling_dir ="Resampling"                       #リサンプリング後のwavファイルを格納するフォルダ名

#---------------------------------------------

def main(wav_path):
    
    number_wav_files = glob.glob(wav_path+'/*.wav')      #wav_path(フォルダ内に)にあるwavファイル数
    wav_list  = []                                       #wav_path(フォルダ内に)にあるwavファイル名をlistに格納

    #wav_listにwavファイル名を格納
    for n_wavfile in number_wav_files:
        wav_list.append(os.path.basename(n_wavfile))
    
    #リサンプリング後に格納するフォルダを作成
    os.makedirs(resampling_dir+"/"+ str(target_sr)+"Hz"+"/"+wav_path)
    resampling_dir_path = resampling_dir+"/"+ str(target_sr)+"Hz"+"/"+wav_path

    for n_wav in range (len(wav_list)):
        befor_wav_path = wav_path +"/"+ wav_list[n_wav]
        y, orig_sr = librosa.load(befor_wav_path) #yは波形 orig_srは元のサンプリング周波数

        target_y = librosa.resample(y, orig_sr, target_sr) #リサンプリング
        resampling_wav_path =  resampling_dir_path  + "/" + wav_list[n_wav]
        librosa.audio.sf.write(resampling_wav_path , target_y, target_sr) #リサンプリング用のフォルダにwavファイル作成

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    # path setting
    parser.add_argument("--wave_path", required=True,
                        type=str, help="path of wav files")
    args = parser.parse_args()

    main(args.wave_path)
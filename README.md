# python-wav-resampling

### リサンプリングプログラムの実行方法

1) 1つのフォルダに格納されているwavファイルを読み込む場合 >>　resampling_run.py
   1つのフォルダ内のwavファイル全てを読み込み、リサンプリング後のwavファイルを作成する。
   resampling_run.pyのwav_pathに読み込むフォルダのパスを記載する。
   実行方法：
   　　python resampling_run.py

2) 複数のフォルダに格納されているwavファイルを読み込む場合 >> resampling_run_arg.py
   wav_list.shにリサンプリングを行うwavファイルが格納されているフォルダを　--wavpthの後ろに記載。
   wav_list.shの上の行からパスを読み込みresampling_run_arg.pyで実行している。
   実行方法：./run.sh

import numpy as np
import sys,os,cv2,time

class ImageSizeChange():
    # 入力値設定
    def __init__(self,Inputlen,InputFilePath,OutputFilePath,InputVal1,InputVal2=None):
        args = sys.argv
        self.InputFilePath = InputFilePath
        self.OutputFilePath = OutputFilePath

        self.inputlen = Inputlen
        self.gamma = 1.5

        # コマンドライン引数によって動作を変更する
        if self.inputlen == 4:
            self.Bunkatsu = int(InputVal1)
        elif self.inputlen >= 5:
            self.y = int(InputVal1)
            self.x = int(InputVal2)
        else:
            self.Bunkatsu = 4
        
    
    # 画像加工保存
    def ImageToGrayAndSizeChange(self,filename,filepath,InputFilePath,OutputFilePath):
            print("処理対象　　　　：" + InputFilePath + "\\" + filename)
            lookUpTable = np.zeros((256,1), dtype=np.uint8)
            for i in range(256):
                lookUpTable[i][0] = 256 * (float(i)/255) ** (1.0 / self.gamma)
            gryimg = cv2.imread(filepath, 0)
            gryimg = cv2.LUT(gryimg, lookUpTable)
            
            # コマンドライン引数によって動作変更
            if self.inputlen == 5:
                img = cv2.resize(gryimg,(self.y, self.x))
            else:
                img = cv2.resize(gryimg,(int(gryimg.shape[1] / self.Bunkatsu), int(gryimg.shape[0] / self.Bunkatsu) ))
            
            # 正規化
            cv2.imwrite(OutputFilePath + "\\" + "Gray_" + filename, img)
    
    # フォルダー判定
    def FolderCheck(self,f,filepath,InputFilePath,OutputFilePath):
        if os.path.isdir(InputFilePath + "\\" + f):
            try:
                os.mkdir(OutputFilePath + "\\" + f)
                print("次のフォルダーを作成します：" + OutputFilePath + "\\" + f)
            except:
                pass
            #フォルダが存在していた場合には新しいフォルダを出力フォルダに作成してその中身を参照する
            files = os.listdir(InputFilePath + "\\" + f)
            self.FolderForLoop(files,InputFilePath + "\\" + f ,OutputFilePath + "\\" + f)
        else:
            self.ImageToGrayAndSizeChange(f,filepath,InputFilePath,OutputFilePath)

    # フォルダ内繰り返し
    def FolderForLoop(self,files,InputFilePath,OutputFilePath):
        for f in files:
            filepath = InputFilePath + "\\" + f
            self.FolderCheck(f,filepath,InputFilePath,OutputFilePath)

    # メイン処理
    def main(self):
        print("処理開始")
        print("対象フォルダ　　：" + self.InputFilePath)
        print("出力フォルダ　　：" + self.OutputFilePath)
        starttime = time.time()
        files = os.listdir(self.InputFilePath)
        self.FolderForLoop(files,self.InputFilePath,self.OutputFilePath)
        print("処理完了")
        endtime = time.time() - starttime
        print("処理時間：" + str(endtime))

# 直接起動された際に実行（テスト用）
if __name__ == "__main__":
    args = sys.argv
    inputlen = len(args)
    if inputlen >= 5:
        env = ImageSizeChange(inputlen,args[1],args[2],args[3],args[4])
    else:
        env = ImageSizeChange(inputlen,args[1],args[2],args[3])
    env.main()



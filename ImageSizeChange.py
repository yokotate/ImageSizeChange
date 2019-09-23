import sys,os,cv2,time

class ImageSizeChange():
    # 入力値設定
    def __init__(self):
        args = sys.argv
        self.InputFilePath = args[1]
        self.OutputFilePath = args[2]

        if len(args) == 4:
            self.Bunkatsu = int(args[3])
        else:
            self.Bunkatsu = 4
    
    # 画像加工保存
    def ImageToGrayAndSizeChange(self,filename,filepath,InputFilePath,OutputFilePath):
            print("処理対象　　　　：" + InputFilePath + "\\" + filename)
            gryimg = cv2.imread(filepath, 0)
            img = cv2.resize(gryimg,(int(gryimg.shape[1] / self.Bunkatsu), int(gryimg.shape[0] / self.Bunkatsu) ))
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
    env = ImageSizeChange()
    env.main()


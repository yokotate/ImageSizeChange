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
    
    # メイン処理
    def main(self):
        print("処理開始")
        print("対象フォルダ　　：" + self.InputFilePath)
        print("出力フォルダ　　：" + self.OutputFilePath)
        starttime = time.time()
        files = os.listdir(self.InputFilePath)
        for f in files:
            filename = self.InputFilePath + "\\" + f
            print("処理ファイル名　：" + f)
            # 画像加工
            gryimg = cv2.imread(filename, 0)
            img = cv2.resize(gryimg,(int(gryimg.shape[1] / self.Bunkatsu), int(gryimg.shape[0] / self.Bunkatsu) ))
            # 保存
            cv2.imwrite(self.OutputFilePath + "\\" + "Gray_" + f, img)
        print("処理完了")
        endtime = time.time() - starttime
        print("処理時間：" + str(endtime))

# 直接起動された際に実行（テスト用）
if __name__ == "__main__":
    env = ImageSizeChange()
    env.main()


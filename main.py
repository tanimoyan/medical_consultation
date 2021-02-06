import tkinter, tkinter.messagebox
import sys
from roboter import conversation

# Tkクラス生成
tki = tkinter.Tk()
# 画面サイズ
tki.geometry('600x400')
# 画面タイトル
tki.title('問診アプリ')

# ラジオボタンのラベルをリスト化する
rdo_txt = ['嘔吐', '下痢', '咳', 'その他']
# ラジオボタンの状態
rdo_var = tkinter.IntVar()

# ラジオボタンを動的に作成して配置
for i in range(len(rdo_txt)):
    rdo = tkinter.Radiobutton(tki, value=i, variable=rdo_var, text=rdo_txt[i])
    rdo.place(x=50, y=30 + (i * 24))

# ボタンクリックイベント
def btn_click():
    num = rdo_var.get()
    conversation.talk_about_medicalconsultation(rdo_txt[num])
    print(rdo_txt[num])
    # tkinter.messagebox.showinfo('チェックされた項目', rdo_txt[num])
    ret = tkinter.messagebox.askyesno('確認', 'ウィンドウを閉じますか？')
    if ret == True:
        sys.exit()

# ボタン作成
btn = tkinter.Button(tki, text='提出', command=btn_click)
btn.place(x=100, y=170)

# 画面をそのまま表示
tki.mainloop()
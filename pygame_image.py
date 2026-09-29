import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png") #練習3：こうかとん画像Surfaceの作成
    bg_img2 = pg.transform.flip(bg_img, True, False)  #練習8：2枚目の背景画像を反転
    kk_img = pg.transform.flip(kk_img, True, False) #練習3：こうかとん画像反転
    kk_rct = kk_img.get_rect() #練習10-1：Rectの取得
    kk_rct.center = 300, 200 #練習10-2：Rectのcenter属性に初期座標を設定
    
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() #練習10-3：キーの押下状態の取得
        print(key_lst[pg.K_UP], key_lst[pg.K_DOWN], key_lst[pg.K_LEFT], key_lst[pg.K_RIGHT])
        if key_lst[pg.K_UP]: #練習10-4：上に移動する
            kk_rct.move_ip((0, -1))
        if key_lst[pg.K_DOWN]: #練習10-4：下に移動する
            kk_rct.move_ip((0, 1))
        if key_lst[pg.K_LEFT]: #練習10-4：左に移動する
            kk_rct.move_ip((-1, 0))
        if key_lst[pg.K_RIGHT]: #練習10-4：右に移動する
            kk_rct.move_ip((2, 0)) #演習1-2：右を押す場合はこうかとんが右に移動する
 
            
        x = tmr%3200 #練習9：背景のループ
        kk_rct.move_ip((-1,0)) #演習1-1：こうかとんが風に流される
        screen.blit(bg_img, [-x, 0]) #練習5：背景画像を右から左に
        screen.blit(bg_img2, [-x +1600, 0])  #練習7：背景画像をもう一度
        screen.blit(bg_img2, [-x +3200, 0])  #練習9：背景のループ
        screen.blit(kk_img, kk_rct) #練習4：こうかとんSurfaceを貼り付け
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習6：FPS変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
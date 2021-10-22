"""
よく書けています！
機能ごとに改行を入れたほうがさらに〇
コメントをどんどん入れていこう

※31-３５行目を追加しました！　
"""

import pygame
from pygame.locals import *
pygame.init()

# 画面の設定
# 画面の大きさの設定
screen = pygame.display.set_mode((800, 600))
# 背景色の設定
screen.fill((0, 0, 0))
# タイトルの設定
pygame.display.set_caption("シューティングゲーム")
# 各画像のロード（表示のための準備）プレイヤー・エネミー（敵）・bullet（弾）
player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")
bullet = pygame.image.load("bullet.png")

# プレイヤーの初期位置
playerX = 400 - player.get_width() / 2
playerY = 500
# 敵の初期位置
enemyX = 200
enemyY = 200
# 弾の初期位置（プレイヤーの真上の中心）
bulletX = playerX+ player.get_width() / 2 - bullet.get_width()/2
bulletY = playerY - bullet.get_height()

running = True
while running:
    screen.fill((0, 0, 0,))
    # プレイヤーの表示・敵の表示
    screen.blit(player, (playerX, playerY))
    screen.blit(enemy, (enemyX, enemyY))
    # screen.blit(bullet,(bulletX, bulletY))

    # キーが押された時の処理
    key_press = pygame.key.get_pressed()
    # 右キーだったら
    if key_press[K_RIGHT]:
        # 画面の端っこにいった時の処理
        if playerX < 800-player.get_width():
            playerX += 0.1
    # 左キーだったら
    if key_press[K_LEFT]:
        if playerX > 0:
            playerX -= 0.1

    # イベント処理
    for event in pygame.event.get():
        # バツボタンが押されたときに終了する処理
        if event.type == QUIT:
            running = False
        # スペースが押されたときの処理
        if event.type == K_SPACE:
            screen.blit(bullet, (bulletX, bulletY))



    pygame.display.update()
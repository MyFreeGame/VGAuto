score = 0
 
# 游戏结束标志
game_over = False
 
# 游戏时钟
clock = pygame.time.Clock()
 
# 游戏循环
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            elif event.key == pygame.K_UP:
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'
 
    if direction == 'LEFT':
        snake_x -= snake_speed
    elif direction == 'RIGHT':
        snake_x += snake_speed
    elif direction == 'UP':
        snake_y -= snake_speed
    elif direction == 'DOWN':
        snake_y += snake_speed

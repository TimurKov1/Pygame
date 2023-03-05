import pygame
from tile import Tile, StaticTile
from settings import tile_size, screen_height, screen_width
from support import import_csv_layout, import_cut_graphics, import_cut_graphics_coins
from Classes.Coin import Coin


class Level:
    def __init__(self, level_data, surface, coins):
        # general setup
        self.coins = coins
        self.display_surface = surface
        self.world_shift = 3
        self.player = 0
        # Это берётся начало и конец карты, в эдиторе они добавлялись
        # player
        # player_layout = import_csv_layout(level_data['player'])
        #         self.player = pygame.sprite.GroupSingle()
        #         self.goal = pygame.sprite.GroupSingle()
        #         self.player_setup(player_layout)


        # пыль при ходьбе как я понял, нам не нужна
        # dust
        # self.dust_sprite = pygame.sprite.GroupSingle()
        #         self.player_on_ground = False


        # terrain setup
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

        # grass setup
        grass_layout = import_csv_layout(level_data['grass'])
        self.grass_sprites = self.create_tile_group(grass_layout, 'grass')

        # trees setup
        trees_layout = import_csv_layout(level_data['trees'])
        self.trees_sprites = self.create_tile_group(trees_layout, 'trees')

        # flying terrain setup
        flying_terrain_layout = import_csv_layout(level_data['flying_terrain'])
        self.flying_terrain_sprites = self.create_tile_group(flying_terrain_layout, 'flying_terrain')

        # flying terrain tileset4 setup
        flying_terrain_tileset4_layout = import_csv_layout(level_data['flying_terrain_tileset4'])
        self.flying_terrain_tileset4_sprites = self.create_tile_group(flying_terrain_tileset4_layout,
                                                                      'flying_terrain_tileset4')

        # coins setup
        coins_layout = import_csv_layout(level_data['coins'])
        self.coins_sprites = self.create_tile_group(coins_layout, 'coins')

        #sky setup
        sky_layout = import_csv_layout(level_data['sky'])
        self.sky_sprites = self.create_tile_group(sky_layout, 'sky')

        #clouds setup
        clouds_layout = import_csv_layout(level_data['clouds'])
        self.clouds_sprites = self.create_tile_group(clouds_layout, 'clouds')

        #sea setup
        sea_layout = import_csv_layout(level_data['sea'])
        self.sea_sprites = self.create_tile_group(sea_layout, 'sea')

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('./Sprites/Graphics/terrain.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'flying_terrain':
                        flying_terrain_tile_list = import_cut_graphics('./Sprites/Graphics/tileset1.png')
                        tile_surface = flying_terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'flying_terrain_tileset4':
                        flying_terrain_tileset4_tile_list = import_cut_graphics('./Sprites/Graphics/tileset4.png')
                        tile_surface = flying_terrain_tileset4_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'grass':
                        grass_tile_list = import_cut_graphics('./Sprites/Graphics/tileset1.png')
                        tile_surface = grass_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'trees':
                        trees_tile_list = import_cut_graphics('./Sprites/Graphics/tileset1.png')
                        tile_surface = trees_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'coins':
                        coins_tile_list = import_cut_graphics_coins('./Sprites/Graphics/coin.png')
                        tile_surface = coins_tile_list[int(val)]
                        sprite = Coin(x, y)
                        self.coins.append(sprite)

                    if type == 'sky':
                        sky_tile_list = import_cut_graphics('./Sprites/Graphics/sky.png')
                        tile_surface = sky_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'clouds':
                        clouds_tile_list = import_cut_graphics('./Sprites/Graphics/clouds.png')
                        tile_surface = clouds_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'sea':
                        sea_tile_list = import_cut_graphics('./Sprites/Graphics/sea.png')
                        tile_surface = sea_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    sprite_group.add(sprite)

        return sprite_group

    # Хз что это, не разобрался до конца
    # def player_setup(self, layout):
    #         for row_index, row in enumerate(layout):
    #             for col_index, val in enumerate(row):
    #                 x = col_index * tile_size
    #                 y = row_index * tile_size
    #                 if val == '0':
    #                     sprite = Player((x, y), self.display_surface, self.create_jump_particles)
    #                     self.player.add(sprite)
    #                 if val == '1':
    #                     hat_surface = pygame.image.load('../Sprites/Graphics/character/hat.png').convert_alpha()
    #                     sprite = StaticTile(tile_size, x, y, hat_surface)
    #                     self.goal.add(sprite)

    # Опять партиклы не нужные
    # def create_jump_particles(self, pos):
    #         if self.player.sprite.facing_right:
    #             pos -= pygame.math.Vector2(10, 5)
    #         else:
    #             pos += pygame.math.Vector2(10, -5)
    #         jump_particle_sprite = ParticleEffect(pos, 'jump')
    #         self.dust_sprite.add(jump_particle_sprite)

    # Колизия как я понял
    # def horizontal_movement_collision(self):
    #         player = self.player.sprite
    #         player.rect.x += player.direction.x * player.speed
    #         collidable_sprites = self.terrain_sprites.sprites() + self.crate_sprites.sprites() + self.fg_palm_sprites.sprites()
    #         for sprite in collidable_sprites:
    #             if sprite.rect.colliderect(player.rect):
    #                 if player.direction.x < 0:
    #                     player.rect.left = sprite.rect.right
    #                     player.on_left = True
    #                     self.current_x = player.rect.left
    #                 elif player.direction.x > 0:
    #                     player.rect.right = sprite.rect.left
    #                     player.on_right = True
    #                     self.current_x = player.rect.right
    #
    #         if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
    #             player.on_left = False
    #         if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
    #             player.on_right = False

    # опять колизия
    # def vertical_movement_collision(self):
    #         player = self.player.sprite
    #         player.apply_gravity()
    #         collidable_sprites = self.terrain_sprites.sprites() + self.crate_sprites.sprites() + self.fg_palm_sprites.sprites()
    #
    #         for sprite in collidable_sprites:
    #             if sprite.rect.colliderect(player.rect):
    #                 if player.direction.y > 0:
    #                     player.rect.bottom = sprite.rect.top
    #                     player.direction.y = 0
    #                     player.on_ground = True
    #                 elif player.direction.y < 0:
    #                     player.rect.top = sprite.rect.bottom
    #                     player.direction.y = 0
    #                     player.on_ceiling = True
    #
    #         if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
    #             player.on_ground = False
    #         if player.on_ceiling and player.direction.y > 0.1:
    #             player.on_ceiling = False

    # хз что это
    #     def scroll_x(self):
    #         player = self.player.sprite
    #         player_x = player.rect.centerx
    #         direction_x = player.direction.x
    #
    #         if player_x < screen_width / 4 and direction_x < 0:
    #             self.world_shift = 8
    #             player.speed = 0
    #         elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
    #             self.world_shift = -8
    #             player.speed = 0
    #         else:
    #             self.world_shift = 0
    #             player.speed = 8

    # Хз что это
    #     def get_player_on_ground(self):
    #         if self.player.sprite.on_ground:
    #             self.player_on_ground = True
    #         else:
    #             self.player_on_ground = False

    # Хз что это, что то с пылью, наверно не нужно
    #     def create_landing_dust(self):
    #         if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
    #             if self.player.sprite.facing_right:
    #                 offset = pygame.math.Vector2(10, 15)
    #             else:
    #                 offset = pygame.math.Vector2(-10, 15)
    #             fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset, 'land')
    #             self.dust_sprite.add(fall_dust_particle)

    def check(self):
        if self.player.type == 'idle':
            self.world_shift = 0
        elif self.player.type == 'run_right':
            self.world_shift = self.player.speed * -1
        elif self.player.type == 'run_left':
            self.world_shift = self.player.speed

    def run(self, move=False, loop=False):
        self.check()
        if move:
            self.world_shift = 200
        if loop:
            self.world_shift = 0
        # sky
        self.sky_sprites.draw(self.display_surface)
        self.sky_sprites.update(self.world_shift)

        #clouds
        self.clouds_sprites.draw(self.display_surface)
        self.clouds_sprites.update(self.world_shift)

        #sea
        self.sea_sprites.draw(self.display_surface)
        self.sea_sprites.update(self.world_shift)

        # terrain
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)

        # flying_terrain
        self.flying_terrain_sprites.draw(self.display_surface)
        self.flying_terrain_sprites.update(self.world_shift)

        # flying_terrain_tileset4
        self.flying_terrain_tileset4_sprites.draw(self.display_surface)
        self.flying_terrain_tileset4_sprites.update(self.world_shift)

        # grass
        self.grass_sprites.draw(self.display_surface)
        self.grass_sprites.update(self.world_shift)

        # trees
        self.trees_sprites.draw(self.display_surface)
        self.trees_sprites.update(self.world_shift)

        self.coins_sprites.draw(self.display_surface)
        self.coins_sprites.update(self.world_shift)

        # партиклы пыли получается
        # dust particles
        # self.dust_sprite.update(self.world_shift)
        # self.dust_sprite.draw(self.display_surface)

        # рисование всего этого на карте
        # player sprites
        # self.player.update()
        #         self.horizontal_movement_collision()
        #
        #         self.get_player_on_ground()
        #         self.vertical_movement_collision()
        #         self.create_landing_dust()
        #
        #         self.scroll_x()
        #         self.player.draw(self.display_surface)
        #         self.goal.update(self.world_shift)
        #         self.goal.draw(self.display_surface)




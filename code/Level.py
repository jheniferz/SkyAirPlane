import sys
from msilib.schema import Font

import pygame
from pygame import Surface, Rect

from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.score = 0
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.show_score_screen()
                        return
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Ring1'))

            self.window.fill((0, 0, 0))

            for entity in self.entity_list:
                entity.move()
                self.window.blit(entity.surf, entity.rect)

            player = next((e for e in self.entity_list if e.name == 'Player1'), None)

            if player:
                for ring in [e for e in self.entity_list if e.name == 'Ring1']:
                    if player.rect.colliderect(ring.rect):
                        self.score += 1
                        self.entity_list.remove(ring)

            self.level_text(14, f'Score: {self.score}', COLOR_WHITE, (10, 25))

            pygame.display.flip()
            clock.tick(60)

    def show_score_screen(self):
        bg = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        bg_rect = bg.get_rect(topleft=(0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return  # volta para o menu

            self.window.blit(bg, bg_rect)

            self.level_text(30, "Fim de jogo!", COLOR_WHITE, (WIN_WIDTH // 2 - 100, WIN_HEIGHT // 2 - 60))
            self.level_text(20, f"Sua pontuação: {self.score}", COLOR_WHITE,
                            (WIN_WIDTH // 2 - 100, WIN_HEIGHT // 2 - 20))
            self.level_text(16, "Pressione ENTER para voltar ao menu", COLOR_WHITE,
                            (WIN_WIDTH // 2 - 150, WIN_HEIGHT // 2 + 20))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

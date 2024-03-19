import pygame

pygame.init()
pygame.mixer.init()

def play_next_song():
    global current_song_index, songs
    current_song_index = (current_song_index + 1) % len(songs)
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

def play_previous_song():
    global current_song_index, songs
    current_song_index = (current_song_index - 1) % len(songs)
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

def play_pause_music():
    global music_started
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        if not music_started:
            music_started = True
            pygame.mixer.music.load(songs[current_song_index])
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.unpause()

window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Load button images
button_play_pause_img = pygame.image.load('lab 7/buttons/play_button.png')
button_previous_img = pygame.image.load('lab 7/buttons/previous_button.png')
button_next_img = pygame.image.load('lab 7/buttons/next_button.png')

# Resize button images
button_play_pause_img = pygame.transform.scale(button_play_pause_img, (50, 50))
button_previous_img = pygame.transform.scale(button_previous_img, (50, 50))
button_next_img = pygame.transform.scale(button_next_img, (50, 50))

# List of songs
songs = ['lab 7/music/Artic Monkeys - 505.mp3', 'lab 7/music/muzapporangespace_Mac_Demarco_For_The_First_Time_634043751.mp3','3.mp3']
current_song_index = 0

music_started = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if play_pause_rect.collidepoint(pos):
                    play_pause_music()
                elif previous_rect.collidepoint(pos):
                    play_previous_song()
                elif next_rect.collidepoint(pos):
                    play_next_song()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_pause_music()
            elif event.key == pygame.K_n:
                play_next_song()
            elif event.key == pygame.K_p:
                play_previous_song()

    window.fill((255, 255, 255))

    # Draw buttons
    previous_rect = window.blit(button_previous_img, (window_width // 2 - 150, window_height // 2 - 25))
    play_pause_rect = window.blit(button_play_pause_img, (window_width // 2 - 25, window_height // 2 - 25))
    next_rect = window.blit(button_next_img, (window_width // 2 + 100, window_height // 2 - 25))

    pygame.display.flip()

pygame.quit()

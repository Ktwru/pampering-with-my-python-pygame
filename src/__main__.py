from entities.game.game import Game


def main():
    game = Game()

    while True:
        game.handle_tic()


if __name__ == '__main__':
    main()

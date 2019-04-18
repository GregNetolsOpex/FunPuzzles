import random

class Player(object):
    """A Player in the game of darts."""

    def __init__(self, name, results=[]):
        super(Player, self).__init__()
        self.name = name
        self.results = results
        self.score = sum(self.results)

    def score_player(self):
        self.score = sum(self.results)

    def get_score(self):
        return self.score

class Darts(object):
    """A game of darts"""

    def __init__(self, participants, throws):
        super(Darts, self).__init__()
        self.participants = participants
        self.throws = throws
        self.scores = []

    def score_game(self):
        for p in self.participants:
            p.score = sum(p.results)
            self.scores.append(p.score)


    def all_scores_equal(self, n):
        return all(score == n for score in self.scores)

    def play_darts(self):
        # Not adding in any smart logic. Random throwing.
        random.shuffle(self.throws)
        for p in self.participants:
            while (len(p.results) < 6):
                p.results.append(self.throws.pop())


def main():

    # avail_throws = [1,1,1,2,3,5,5,10,10,10,20,20,25,25,50]
    # Each player will have 6 throws
    # Each player will have a odd number of odd throws
    ## There are 8 odd throws left
    ## Raj must have 3, 5 or 7 odd throws
    ## Emily must have 1, 3, 5, or 7 odd throws
    ## Bernardo must have 1, 3, 5, or 7 odd throws
    # There is only 1 way to score a 22 with 2 throws, 20 + 2
    ## This also means that emily did not get the bullseye

    # If Raj gets the bullseye on the second throw he must score 19 points in 5 throws
    ## Is this possible yes 10+5+2+1+1

    # If Bernardo gets the bullesye on the first throw he must score 21 points in 6 throws
    ## Is this possible 10+5+3+1+1+1

    # Alright it's not that simple and i don't want to think too much harder. lets start searching.



    solution_found = False
    i = 0

    while(not solution_found):
        Raj = Player("Raj", [3])
        Emily = Player("Emily", [20,2])
        Bernardo =  Player("Bernardo", [])

        avail_throws = [1,1,1,2,3,5,5,10,10,10,20,20,25,25,50]

        DartsGame = Darts([Raj, Emily, Bernardo], avail_throws)
        DartsGame.play_darts()
        DartsGame.score_game()

        solution_found = DartsGame.all_scores_equal(71)

        if (solution_found):
            print(Raj.score)
            print(Raj.results)
            print(Emily.score)
            print(Emily.results)
            print(Bernardo.score)
            print(Bernardo.results)

        i+=1
        if( i % 1000 == 0 ):
            print(i)
            print(DartsGame.scores)

if __name__ == '__main__':
    main()

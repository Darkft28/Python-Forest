import random
from copy import deepcopy

class Arbre:
    def __init__(self, etat):
        self.__etat = etat

    def getEtat(self):
        return self.__etat

    def setEtat(self, new_etat):
        self.__etat = new_etat

    def getLetter(self):
        if self.__etat == '0':
            return '⛰️'
        elif self.__etat == '1':
            return '🌳'
        elif self.__etat == '2':
            return '🔥'
        elif self.__etat == '3':
            return '🕸️'

    def fire_neighbors(self, is_neighbor_on_fire):
        if self.__etat == '1':
            if is_neighbor_on_fire:
                self.__etat = '2'
        elif self.__etat == '2':
            self.__etat = '3'

class Foret:
    def __init__(self, taille, proba):
        self.__taille = taille
        self.__foret = []
        for i in range(taille):
            self.__foret.append([])
            for j in range(taille):
                if random.random() < proba:
                    self.__foret[i].append(Arbre('1'))
                else:
                    self.__foret[i].append(Arbre('0'))
        while True:
            random_i = random.randint(0, taille - 1)
            random_j = random.randint(0, taille - 1)
            if self.__foret[random_i][random_j].getEtat() == '1':
                self.__foret[random_i][random_j].setEtat('2')
                break

    def afficher(self, etape):
        print(f"Étape {etape}:")
        for i in range(self.__taille):
            for j in range(self.__taille):
                print(self.__foret[i][j].getLetter(), end=' ')
            print('')
        print('')

    def is_neighbors_on_fire(self, i, j):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            ni = i + di
            nj = j + dj
            if 0 <= ni < self.__taille and 0 <= nj < self.__taille:
                if self.__foret[ni][nj].getEtat() == '2':
                    return True
        return False

    def propager(self):
        new_foret = deepcopy(self.__foret)
        for i in range(self.__taille):
            for j in range(self.__taille):
                if self.__foret[i][j].getEtat() == '1':
                    if self.is_neighbors_on_fire(i, j):
                        new_foret[i][j].setEtat('2')
                elif self.__foret[i][j].getEtat() == '2':
                    new_foret[i][j].setEtat('3')
        self.__foret = new_foret

    def simulate_until_burned(self):
        iteration = 0
        self.afficher(iteration)
        while any(arbre.getEtat() == '2' for row in self.__foret for arbre in row):
            iteration += 1
            self.propager()
            self.afficher(iteration)
        print(f"La forêt a brûlé en {iteration} itérations.")


if __name__ == "__main__":
    taille = int(input("Entrez la taille de la forêt: "))
    proba = float(input("Entrez la probabilité de présence d'un arbre (entre 0 et 1): "))

    foret = Foret(taille, proba)
    foret.simulate_until_burned()
    print(input('Cliquer sur Enter pour quitter'))
    
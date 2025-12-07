def ajouter_note(L, n):
    L.append(n)


def moyenne(L):
    return sum(L) / len(L)


def note_max(L):
    return max(L)


def est_reussi(n):
    return True if n >= 10 else False

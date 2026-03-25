from collections.abc import Iterable, Iterator
"""
Gestion des notes d'étudiants par matière.
Affiche les étudiants classés de la meilleure à la plus mauvaise note
pour chaque matière, ainsi que la moyenne générale de chaque étudiant.
"""

class Note:
    """Représente une note obtenue dans une matière."""

    def __init__(self, matiere: str, valeur: float):
        if not (0 <= valeur <= 20):
            raise ValueError(f"La note doit être comprise entre 0 et 20, reçu : {valeur}")
        self.matiere = matiere
        self.valeur = valeur

    def __repr__(self):
        return f"Note({self.matiere}: {self.valeur}/20)"


class Etudiant:
    """Représente un étudiant avec ses notes dans différentes matières."""

    def __init__(self, nom: str, prenom: str):
        self.nom = nom
        self.prenom = prenom
        self.notes: list[Note] = []

    def ajouter_note(self, note: Note):
        """Ajoute une note à l'étudiant."""
        self.notes.append(note)

    def get_note_par_matiere(self, matiere: str) -> float | None:
        """Retourne la note de l'étudiant dans une matière donnée."""
        for note in self.notes:
            if note.matiere == matiere:
                return note.valeur
        return None

    def moyenne(self) -> float:
        """Calcule la moyenne générale de l'étudiant."""
        if not self.notes:
            return 0.0
        return sum(n.valeur for n in self.notes) / len(self.notes)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def __repr__(self):
        return f"Etudiant({self.prenom} {self.nom}, moyenne={self.moyenne():.2f})"


class Classe:
    """Représente une classe regroupant plusieurs étudiants et matières."""

    def __init__(self, nom: str):
        self.nom = nom
        self.etudiants: list[Etudiant] = []
        self.matieres: list[str] = []

    def ajouter_etudiant(self, etudiant: Etudiant):
        """Ajoute un étudiant à la classe."""
        self.etudiants.append(etudiant)

    def ajouter_matiere(self, matiere: str):
        """Enregistre une matière dans la classe."""
        if matiere not in self.matieres:
            self.matieres.append(matiere)

    def classement_par_matiere(self, matiere: str) -> list[tuple[Etudiant, float]]:
        """
        Retourne la liste des étudiants classés du meilleur au moins bon
        pour une matière donnée.
        """
        resultats = []
        for etudiant in self.etudiants:
            note = etudiant.get_note_par_matiere(matiere)
            if note is not None:
                resultats.append((etudiant, note))
        return sorted(resultats, key=lambda x: x[1], reverse=True)

    def afficher_classements(self):
        """Affiche le classement des étudiants pour chaque matière et leur moyenne."""
        print(f"\n{'='*50}")
        print(f"  CLASSE : {self.nom}")
        print(f"{'='*50}")

        for matiere in self.matieres:
            print(f"\n📚 Matière : {matiere}")
            print(f"  {'Rang':<6} {'Étudiant':<25} {'Note':>6}")
            print(f"  {'-'*40}")
            classement = self.classement_par_matiere(matiere)
            for rang, (etudiant, note) in enumerate(classement, start=1):
                print(f"  {rang:<6} {str(etudiant):<25} {note:>5.2f}/20")

        print(f"\n📊 Moyennes générales")
        print(f"  {'Rang':<6} {'Étudiant':<25} {'Moyenne':>8}")
        print(f"  {'-'*42}")
        classes_par_moyenne = sorted(
            self.etudiants, key=lambda e: e.moyenne(), reverse=True
        )
        for rang, etudiant in enumerate(classes_par_moyenne, start=1):
            print(f"  {rang:<6} {str(etudiant):<25} {etudiant.moyenne():>7.2f}/20")

        print(f"\n{'='*50}\n")


# ── Démonstration ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    MATHS = "Mathématiques"
    PHYSIQUE = "Physique"
    INFO = "Informatique"

    terminale = Classe("Terminale S1")
    for m in (MATHS, PHYSIQUE, INFO):
        terminale.ajouter_matiere(m)

    donnees = [
        ("Alice",   "Martin",  17.5, 15.0, 19.0),
        ("Bob",     "Dupont",  12.0, 14.5, 11.0),
        ("Camille", "Durand",  15.0, 18.0, 16.5),
        ("David",   "Leroy",    9.5, 11.0, 13.0),
        ("Emma",    "Petit",   14.0, 16.5, 17.0),
    ]

    for prenom, nom, n_maths, n_phys, n_info in donnees:
        e = Etudiant(nom, prenom)
        e.ajouter_note(Note(MATHS, n_maths))
        e.ajouter_note(Note(PHYSIQUE, n_phys))
        e.ajouter_note(Note(INFO, n_info))
        terminale.ajouter_etudiant(e)

    terminale.afficher_classements()

   class StudentIterator(Iterator):
    """Itérateur qui parcourt les étudiants du meilleur au plus mauvais pour la matière 1."""

    def __init__(self, students):
        self._students = sorted(students, key=lambda s: s.notes[0], reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student

    def __iter__(self):
        return self 
class SchoolClass:
    """Alias anglais de Classe."""
    def __iter__(self):
        return StudentIterator(self.students)

    def __init__(self):
        self.students = []

    def add_student(self, student):
        def __iter__(self):
        return StudentIterator(self.students)
        self.students.append(student)

    def display_rankings(self):
        matieres = ["subject1", "subject2", "subject3"]
        for i, matiere in enumerate(matieres):
            print(f"\nRanking for {matiere}:")
            ranked = sorted(self.students, key=lambda s: s.notes[i], reverse=True)
            for rang, s in enumerate(ranked, 1):
                print(f"  {rang}. {s.name} : {s.notes[i]}/20")

        print(f"\nGeneral average ranking:")
        ranked = sorted(self.students, key=lambda s: s.average(), reverse=True)
        for rang, s in enumerate(ranked, 1):
            print(f"  {rang}. {s.name} : {s.average():.2f}/20")


class Student:
    """Alias anglais de Etudiant."""

    def __init__(self, name: str, note1: float, note2: float, note3: float):
        self.name = name
        self.notes = [note1, note2, note3]

    def average(self) -> float:
        return sum(self.notes) / len(self.notes)


# Test
school_class = SchoolClass()
def rank_matter_1(self):
        """Affiche les étudiants classés par ordre décroissant de la matière 1."""
        print("\nRanking for matter 1:")
        ranked = sorted(self.students, key=lambda s: s.notes[0], reverse=True)
        for rang, s in enumerate(ranked, 1):
            print(f"  {rang}. {s.name} : {s.notes[0]}/20")
            
            def rank_matter_2(self):
        """Affiche les étudiants classés par ordre décroissant de la matière 2."""
        print("\nRanking for matter 2:")
        ranked = sorted(self.students, key=lambda s: s.notes[1], reverse=True)
        for rang, s in enumerate(ranked, 1):
            print(f"  {rang}. {s.name} : {s.notes[1]}/20")

    def rank_matter_3(self):
        """Affiche les étudiants classés par ordre décroissant de la matière 3."""
        print("\nRanking for matter 3:")
        ranked = sorted(self.students, key=lambda s: s.notes[2], reverse=True)
        for rang, s in enumerate(ranked, 1):
            print(f"  {rang}. {s.name} : {s.notes[2]}/20")
print("\nIteration sur les étudiants (matière 1) :")
for student in school_class:
    print(f"  {student.name} : {student.notes[0]}/20")
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

school_class.display_rankings()
school_class.rank_matter_1()
school_class.rank_matter_2()
school_class.rank_matter_3()


      

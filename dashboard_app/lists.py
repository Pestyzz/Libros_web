STATUS = [
    ("EP", "EN PROCESO"),
    ("E", "ENVIADO"),
    ("EN", "ENTREGADO"),
    ("D", "DEVUELTO"),
    ("C", "CANCELADO"),
]

STATUS_CLASS_MAPPING = {
    "EP": "process",
    "E": "sent",
    "EN": "delivered",
    "D": "returned",
    "C": "canceled",
}

BOOK_LANGUAGES = [
    ("ES", "Español"),
    ("EN", "Inglés")
]

CATEGORIES = [
    ("1", "Ficción"),
    ("2", "No Ficción"),
    ("3", "Aventura"),
    ("4", "Ciencia Ficción"),
    ("5", "Fantasía"),
    ("6", "Misterio"),
    ("7", "Thriller"),
    ("8", "Romance"),
    ("9", "Terror"),
    ("10", "Biografía"),
    ("11", "Autobiografía"),
    ("12", "Historia"),
    ("13", "Filosofía"),
    ("14", "Ciencia"),
    ("15", "Tecnología"),
    ("16", "Matemáticas"),
    ("17", "Salud"),
    ("18", "Autoayuda"),
    ("19", "Negocios"),
    ("20", "Economía"),
    ("21", "Política"),
    ("22", "Sociología"),
    ("23", "Psicología"),
    ("24", "Educación"),
    ("25", "Arte"),
    ("26", "Música"),
    ("27", "Teatro"),
    ("28", "Cine"),
    ("29", "Cocina"),
    ("30", "Viajes"),
    ("31", "Deportes"),
    ("32", "Juegos"),
    ("33", "Cómics"),
    ("34", "Poesía"),
    ("35", "Ensayo"),
    ("36", "Crítica Literaria"),
    ("37", "Religión"),
    ("38", "Espiritualidad"),
    ("39", "Juvenil"),
    ("40", "Infantil"),
    ("41", "Novela"),
    ("42", "Suspenso")
]

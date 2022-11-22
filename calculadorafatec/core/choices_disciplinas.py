from django.db.models import TextChoices

class ChoicesDisciplinas(TextChoices):
    BIOLOGIA = "BIO", "BIOLOGIA"
    CONHECIMENTO_GERAIS = "CONG", "CONHECIMENTO GERAIS"
    FISICA = "FIS", "FÍSICA"
    GEOGRAFIA = "GEO", "GEOGRAFIA"
    HISTORIA = "HIST", "HISTÓRIA"    
    INGLES = "ING", "INGLÊS"        
    MATEMATICA = "MAT", "MATEMÁTICA"
    PORTUGUES = "PORT", "PORTUGUÊS"
    RACIOCINIO_LOGICO = "RLOG", "RACIOCÍNIO LÓGICO"
    QUIMICA = "QUI", "QUÍMICA"

    
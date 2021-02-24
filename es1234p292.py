class Atleta():
    def __init__(self, nome_squadra, visita_medica=False):
        self.nome_squadra = nome_squadra
        self.visita_medica = visita_medica
    def squadra(self):
        print("L'atleta gioca nella squadra:", self.nome_squadra)
    def svolgimento_visita(self):
        print("L'atleta sta facendo una visita medica... Terminata!")
        self.visita_medica = True
    def visualizza_dati(self):
        if self.visita_medica:
            print("L'atleta gioca nella squadra:", self.nome_squadra, "e ha fatto la visita medica.")
        else:
            print("L'atleta gioca nella squadra:", self.nome_squadra, "ma non ha ancora fatto la visita medica.")

def main():
    squadra = input("Inserire squadra atleta: ")
    atleta_1 = Atleta(squadra)
    while True:
        print("Premere A, per far effettuare la visita all'atleta. Premere B, per visualizzare i dati dell'atleta. Premere qualsiasi altro tasto per chiudere il programma.")
        visiona = input()
        visiona = visiona.upper()
        if visiona == "A":
            atleta_1.svolgimento_visita()
        elif visiona == "B":
            atleta_1.visualizza_dati()
        else:
            break

main()
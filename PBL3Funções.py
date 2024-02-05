import PBL3Classes

# funções
def criarlinha():
    print('-'*56)

def verificarPacienteEmConsulta(nome):
    if nome == 0:
        print('nenhum paciente chamado para consulta.')
    else:
        return nome
    
def popularSistema():
    
    pessoas = [
    {"nome": "Ana Silva", "id": 28, "cpf": "123.456.789-00"},
    {"nome": "Lucas Oliveira", "id": 35, "cpf": "234.567.890-11"},
    {"nome": "Mariana Santos", "id": 22, "cpf": "345.678.901-22"},
    {"nome": "Rafael Pereira", "id": 30, "cpf": "456.789.012-33"},
    {"nome": "Camila Costa", "id": 25, "cpf": "567.890.123-44"},
    {"nome": "Fernando Lima", "id": 32, "cpf": "678.901.234-55"},
    {"nome": "Isabela Almeida", "id": 29, "cpf": "789.012.345-66"},
    {"nome": "Pedro Rocha", "id": 27, "cpf": "890.123.456-77"},
    {"nome": "Juliana Santos", "id": 31, "cpf": "901.234.567-88"},
    {"nome": "Gustavo Oliveira", "id": 26, "cpf": "012.345.678-99"},
    {"nome": "Amanda Lima", "id": 33, "cpf": "123.456.789-01"},
    {"nome": "Marcos Silva", "id": 24, "cpf": "234.567.890-12"},
    {"nome": "Carolina Almeida", "id": 18, "cpf": "345.678.901-23"},
    {"nome": "Henrique Pereira", "id": 36, "cpf": "456.789.012-34"},
    {"nome": "Larissa Costa", "id": 23, "cpf": "567.890.123-45"},
    {"nome": "Roberto Rocha", "id": 19, "cpf": "678.901.234-56"},
    {"nome": "Bianca Santos", "id": 34, "cpf": "789.012.345-67"},
    {"nome": "Diego Oliveira", "id": 47, "cpf": "890.123.456-78"},
    {"nome": "Aline Lima", "id": 50, "cpf": "901.234.567-89"},
    {"nome": "Rodrigo Pereira", "id": 55, "cpf": "012.345.678-90"},
]

    r = PBL3Classes.Recepção()
    for j in pessoas:
        p = PBL3Classes.Paciente(j["nome"], j["cpf"], j["id"])
        r.adicionarPaciente(p)
            
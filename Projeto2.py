tamanho_tab = 15

#2.1.1 TAD casa
'''Para este TAD vamos utilizar tuplos, que são imutáveis, de modo a que,
através da definição das operações básicas associadas à TAD casa, seja possível definir funções de alto nível.'''

# Tabelas de letras e pontos

letras_validas = ('A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X','Z')

pontos = {
'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1,
'F': 4, 'G': 4, 'H': 4, 'I': 1, 'J': 5, 'L': 2,
'M': 1, 'N': 3, 'O': 1, 'P': 2, 'Q': 6, 'R': 1,
'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Z': 8 }


# Construtor

def cria_casa(lin, col):
    if type(lin) != int or type(col) != int or lin <= 0 or col <= 0: # aqui tmb é preciso pôr se lin> 15 ou col>15? ou fazemos tamanho_tab?
        raise ValueError('cria_casa: argumentos inválidos')
    casa = (lin, col)
    return casa

# Seletores

def obtem_col(casa):
    linha, coluna = casa
    return coluna

def obtem_lin(casa):
    linha, coluna = casa
    return linha

# Reconhecedor

def eh_casa(arg):
    if type(arg) != tuple or len(arg) != 2:
        return False
    for i in arg:
        if type(i) != int or i < 0 or i > tamanho_tab:
            return False
    return True
        
# Teste

def casas_iguais(c1, c2):
    if eh_casa(c1) == True and eh_casa(c2) == True and c1 == c2:
        return True
    else: return False

# Transformador

def casa_para_str(c):
    linha, coluna = c
    s = '(' + str(linha) + ',' + str(coluna) + ')'
    return s

def str_para_casa(s):
    sem_p = s[1:-1]
    nums = sem_p.split(',')
    linha = int(nums[0])
    coluna = int(nums[1])
    casa = cria_casa(linha, coluna)
    return casa

# Funções de alto nível

def incrementa_casa(c, d, s):
    linha, coluna = c
    c_original = c
    if d == 'H':
        c = (linha, coluna + s)
        if coluna + s > tamanho_tab:
            return c_original
        else: 
            return c
    elif d == 'V':
        c = (linha + s, coluna)
        if linha + s > tamanho_tab:
            return c_original
        else:
            return c

# 2.1.2 TAD jogador
'''O TAD jogador é usado para representar um jogador do jogo Scrabble, a sua pontuação
e letras. Os jogadores podem ser humanos ou agentes.'''

# Construtor

def cria_humano(nome):
    if nome == '' or type(nome) != str:
        raise ValueError('cria_humano: argumento inválido')
    else: 
        jogador_humano = {'tipo': 'humano', 'nome': nome, 'pontos': 0, 'letras': []}
    return jogador_humano

# Aqui, "agente" é basicamente o jogador que o computador vai ser

def cria_agente(nivel):
    if nivel != 'FACIL' and nivel != 'MEDIO' and nivel != 'DIFICIL':
        raise ValueError('cria_agente: argumento inválido')
    else:
        jogador_agente = {'tipo': 'agente', 'nivel': nivel, 'pontos': 0, 'letras': []}
        return jogador_agente
    
# Seletores

def jogador_identidade(j):
    if j['tipo'] == 'humano':
        return j['nome']
    else:
        return j['nivel']
    
def jogador_pontos(j):
    return j['pontos']

def jogador_letras(j):
    return ''.join(sorted(j['letras'])) # Não queremos a lista de letras ordenada, mas sim uma string

# Modificadores

def recebe_letra(j, l):
    j['letras'] = j['letras'] + [l]
    return j

def usa_letra(j,l):
    if l in j['letras']:
        j['letras'].remove(l)
        return j

def soma_pontos(j, p):
    j['pontos'] += p
    return j

# Reconhecedor

def eh_jogador(arg):
    if type(arg) != dict or 'letras' not in arg or 'pontos' not in arg or 'tipo' not in arg:
        return False
    if type(arg['letras']) != list or type(arg['pontos']) != int or arg['pontos'] < 0:
        return False
    for i in arg['letras']:
        if type(i) != str or len(i) != 1:
            return False
        # Caso seja humano
    if arg['tipo'] == 'humano':
        if 'nome' not in arg or type(arg['nome']) != str:
            return False
        # Caso seja agente
    elif arg['tipo'] == 'agente':
        if 'nivel' not in arg or type(arg['nivel']) != str:
            return False
    else:
        return False

    return True
    
def eh_humano(arg):
    if type(arg) != dict or 'tipo' not in arg:
        return False
    if arg['tipo'] != 'humano':
        return False
    return True 

def eh_agente(arg):
    if type(arg) != dict or 'tipo' not in arg:
        return False
    if arg['tipo'] != 'agente':
        return False
    return True

# Teste

def jogadores_iguais(j1, j2):
    if eh_jogador(j1) == True and eh_jogador(j2) == True and j1 == j2:
        return True
    else:
        return False
    
def jogador_para_str(t):
    letras_str = ' '.join(t['letras'])
    if t['tipo'] == 'humano':
        jog_str = f"{t['nome']} ({t['pontos']:3}): {letras_str}"
    else: 
        jog_str = f"BOT({t['nivel']}) ({t['pontos']:3}): {letras_str}"
    return jog_str

# Funções de alto nível

def distribui_letras(jog, saco, num):
    i = 0
    while i < num and len(saco) > 0:
        ultima_letra = saco.pop()
        jog['letras'].append(ultima_letra)
        i +=1
        jog['letras'].sort()
    return jog 

# 2.1.3 TAD vocabulario

# Construtor

def cria_vocabulario(v):
    if type(v) != tuple or len(v) < 2:
        raise ValueError('cria_vocabulario: argumento inválido')
    for palavra in v:
        if type(palavra) != str or len(palavra) < 2 or len(palavra) > 15:
            raise ValueError('cria_vocabulario: argumento inválido')
        for letra in palavra:
            if letra not in letras_validas:
                raise ValueError('cria_vocabulario: argumento inválido')
        
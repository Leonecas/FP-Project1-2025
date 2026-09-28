'''
Projeto 1 de FP
Leonor Mendonça Rodrigues
ist1118192
leonor.rodrigues@tecnico.ulisboa.pt
10/10/2025
'''

tamanho_tab = 15
# 3.1.1 função cria conjunto

'''Esta função vai criar um dicionário que representa um conjunto de letras, onde as chaves são as letras e os valores são o número de ocorrências dessas letras.
Esta função vai servir não só para criar o conjunto de letras do saco, mas também para criar o conjunto de letras de um jogador.'''

letras_validas = ('A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X','Z')
def cria_conjunto (let,occ):
    if type(let) != tuple or type(occ) != tuple:
        raise ValueError('cria_conjunto: argumentos inválidos')
    if len(let) != len(occ):        
        raise ValueError('cria_conjunto: argumentos inválidos')
    for a in let:                    
        if a not in letras_validas :
            raise ValueError('cria_conjunto: argumentos inválidos')
    for b in occ:                   
        if type(b) != int or b < 0:
            raise ValueError('cria_conjunto: argumentos inválidos')
        
    dicionario = {}
    for i in range(len(let)):
        dicionario[let[i]] = occ[i]
    return dicionario


# 3.1.2 função gera_numero_aleatorio

''' Esta função serve para gerar um número pseudo-aleatório a partir de um estado inicial. Que nos será útil para baralhar o saco de letras.'''      
 
 # Função para gerar um número aleatório, utilizando o gerador xorshift mencionado no enunciado.
def gera_numero_aleatorio(estado):    
    estado ^= ( estado << 13) & 0xFFFFFFFF
    estado ^= ( estado >> 17) & 0xFFFFFFFF
    estado ^= ( estado << 5) & 0xFFFFFFFF
    # a função vai-nos devolver um novo número pseudo-aleaatório (estado) gerado a partir do estado inicial.
    return estado                                  

# 3.1.3 função permuta_letras

'''Esta função vai permutar os elementos de uma lista de letras, utilizando um estado inicial para gerar números pseudo-aleatórios.
Esta função vai ser útil para baralhar a pilha de letras.'''

# Primeiro fazemos uma função para gerar um número aleatório do índice em vez de um pseudo-aleatório qualquer.
def gera_num_indice(estado, i):
    estado = gera_numero_aleatorio(estado)
    num_indice = estado % (i + 1)
    return num_indice, estado

# Função que permuta as letras da lista passada como argumento, utilizando a função anterior para gerar os índices.

def permuta_letras(letras_validas,estado):
   for i in range(len(letras_validas)-1, -1, -1):
        a, estado = gera_num_indice(estado,i)
        letras_validas[i], letras_validas[a] = letras_validas[a], letras_validas[i]

# 3.1.4 função baralha_conjunto

''' Esta função recebe um conjunto de letras e um inteiro que representa o estado e devolve uma lista baralhada com todas as letras contidas no conj_letras.
 É criada uma lista que recebe a chave do dicionário e adiciona-a à lista o número de vezes que estiver especificado no valor do dicionário,
 em seguida é chamada a função permuta_letras para permutar os elementos da lista criada, devolvendo uma lista de letras "baralhadas".'''

# Função que gera uma lista com as letras do conjunto
def gera_lista_letras(conj):
        lista_letras = []
        for letra, num in conj.items():
            lista_letras.extend([letra] * num )
        return lista_letras

# Função que baralha a lista de letras

def baralha_conjunto(conj, estado):
    lista_letras = gera_lista_letras(conj)
    permuta_letras(lista_letras, estado)
    return lista_letras    

# 3.1.5 função testa_palavra_padrao

'''Esta função vai receber uma cadeia de caracteres (palavra), uma cadeia de caracteres formada por letras e pelo caractér '.', e um conjunto de letras.
Esta função devolve True se, com as letras do conjunto, é possível formar a palavra fornecida através da substituição dos caracteres '.' do padrão,
 e devolverá False caso contrário.'''

def testa_palavra_padrao(palavra, padrao, conj):
    copia_temp_conj = conj.copy()
    if len(padrao) != len(palavra):
        return False
    for i in range(len(padrao)):
        if palavra[i] != padrao[i]:
            if padrao[i] == '.':
                if palavra[i] in copia_temp_conj:
                    if copia_temp_conj[palavra[i]] == 1:
                        del copia_temp_conj[palavra[i]]
                    else:
                        copia_temp_conj[palavra[i]] = copia_temp_conj[palavra[i]] - 1
                else:
                    return False
            else:
                return False
    return True

# 3.2.1 função cria_tabuleiro

'''Esta função não recebe um argumento, mas devolve um tabuleiro vazio.'''
def cria_tabuleiro():
    tabuleiro = []
    for x in range(tamanho_tab):
        linha = ['.'] * tamanho_tab
        tabuleiro.append(linha)
    return tabuleiro

# 3.2.2 função cria_casa

'''Recebe dois inteiros correspondentes a uma linha e uma coluna de um tabuleiro de Scrabble, e devolve a casa do tabuleiro.'''
def cria_casa(l, c):
    if type(l) != int or type(c) != int:
        raise ValueError('cria_casa: argumentos inválidos')
    if l < 0 or l > tamanho_tab or c < 0 or c > tamanho_tab:
        raise ValueError('cria_casa: argumentos inválidos')
    casa = (l, c)
    return casa

# 3.2.3 função obtem_valor

'''Recebe um tabuleiro e uma casa do tabuleiro, e devolve o valor
contido nessa casa.'''
def obtem_valor(tab, casa):
    linha, coluna = casa
    return tab[linha][coluna]

# 3.2.4 função insere_letra

''' recebe um tabuleiro, uma casa do tabuleiro e uma letra, e
insere a letra na casa indicada modificando o tabuleiro.'''
def insere_letra(tab, casa, letra):
    linha, coluna = casa
    tab[linha][coluna] = letra
    return tab


# 3.2.5 função obtem_sequencia

'''recebe um tabuleiro, uma casa do tabuleiro, uma direção e um inteiro positivo, e
devolve a cadeia de carateres de tamanho igual ao argumento inteiro fornecido, formada
por todos os valores nas casas do tabuleiro a partir da casa e na direção indicadas.'''
def obtem_sequencia(tab, casa, direcao, tamanho):
    s = ''
    linha, coluna = casa
    linha = linha - 1
    coluna = coluna - 1
    if direcao == 'H':
        for i in range(tamanho):
            if coluna + i < tamanho_tab:
                s += tab[linha][coluna + i]
            else: 
                s += '.'
    elif direcao == 'V':
        for j in range(tamanho):
            if linha + j < tamanho_tab:
                s += tab[linha + j][coluna]
            else: s += '.'
    return s

# 3.2.6 função insere_palavra

'''recebe um tabuleiro, uma casa do tabuleiro,uma direção e uma cadeia de carateres, e
insere a palavra fornecida na casa e direção indicada modificando destrutivamente o
tabuleiro. Esta função serve para que os jogadores possam inserir as suas palavras no tabuleiro.'''
def insere_palavra(tab, casa, direcao, palavra):
    linha, coluna = casa
    if direcao == 'H':
        for i in range(len(palavra)):
            insere_letra(tab, (linha-1, (coluna-1) + i), palavra[i])
    elif direcao == 'V':
        for j in range(len(palavra)):
            insere_letra(tab, ((linha-1) + j, coluna-1), palavra[j])
    return tab 

# 3.2.7 função tabuleiro_para_str

'''recebe um tabuleiro e devolve a cadeia de caracteres que o representa.'''

# Função cria cabeçalho para que o cabeçalho esteja formatado para qualquer tamanho de tabuleiro

def cria_cabeçalho():
    indentação = '   '
    string = '              '
    for coluna in range(1,tamanho_tab + 1):    
            if coluna < 10:
                string = string + ' ' 
            elif coluna >= 10 and coluna < 15:
                string = string + str(coluna)[0] + ' '
            else:
                string = string + str(coluna)[0] 
    string = string + '\n' + indentação + '  '
    for coluna in range(1,tamanho_tab + 1):
        if coluna < 15:
            string += str(coluna % 10) + ' '
        else:
            string += str(coluna % 10)
    string += '\n   +-' + ('--' * tamanho_tab) + '+\n'
    return string

#Função que converte o tabuleiro numa string para que o possamos ver formatado no terminal

def tabuleiro_para_str(tab):
    #indentação = ' ' * 3
    tab_str = cria_cabeçalho()
    for i in range(tamanho_tab):
        if i + 1 < 10:
            tab_str += f" {i + 1} |"
        else:
            tab_str += f"{i + 1} |"
        for j in range(tamanho_tab):
            tab_str = tab_str + f" {tab[i][j]}"
        tab_str = tab_str + ' |\n'
    tab_str = tab_str + '   +-' + ('--' * (tamanho_tab)) + '+'
    return tab_str


# 3.3.1 função cria_jogador
'''Esta função recebe dois inteiros representando respetivamente a ordem do jogador e os pontos iniciais, e um conjunto de letras representando as
letras do jogador de Scrabble, e devolve um jogador de Scrabble sob a forma de um dicionário.'''

def cria_jogador(ordem, pontos, conj_letras):
    for letra, occ in conj_letras. items():
        if letra not in letras_validas or type(occ) != int or occ < 0:
            raise ValueError('cria_jogador: argumentos inválidos')
    if ordem > 4 or ordem < 0 or type(ordem) != int:
        raise ValueError('cria_jogador: argumentos inválidos')
    if type(pontos) != int or pontos < 0:
        raise ValueError('cria_jogador: argumentos inválidos')
    if pontos < 0 or type(conj_letras) != dict: 
        raise ValueError('cria_jogador: argumentos inválidos')
    jogador = {"id": ordem, 'pontos': pontos, 'letras': conj_letras}
    return jogador

# 3.3.2 função jogador_para_str

'''Esta função recebe um jogador de Scrabble e devolve a cadeia de caracteres que o representa.'''

def jogador_para_str(jog):
    res = f"#{jog['id']} ({jog['pontos']:3}): "
    letras =  gera_lista_letras(jog['letras'])
    letras.sort(key=lambda x:letras_validas.index(x))
    return res + ' '.join(letras)

# 3.3.3 função distribui_letra

'''Esta função recebe uma lista de letras (pilha) e um jogador, e tenta distribuir uma letra da pilha para o jogador.'''

def distribui_letra(letras, jogador):
    if not letras:
        return False
    else: 
         ultima_letra = letras.pop()
         if ultima_letra in jogador['letras']:
            jogador['letras'][ultima_letra] += 1
         else:
             jogador['letras'][ultima_letra] = 1
         return True
    
# 3.4.1 função joga_palavra

'''Esta função tenta inserir uma palavra no tabuleiro de acordo com as regras do Scrabble.
Mas só o faz se a palavra couber no tabuleiro. A palavra pode ser formada com as letras que o jogador tem (ou que já estão no tabuleiro) e
a jogada é válida segundo as regras do jogo.
Se for possível jogar, coloca a palavra no tabuleiro e devolve um tuplo com as letras utilizadas (por ordem).
Se não der, devolve um tuplo vazio "()" e não muda o tabuleiro.'''

def joga_palavra(tab, palavra, casa, direcao, conj_letras, primeira):
    casa_central = (7, 7)
    tamanho_tab = len(tab)
    centro = tamanho_tab // 2
    linha, coluna = casa
    linha = linha - 1
    coluna = coluna - 1
    # Verificar se a palavra cabe no tabuleiro quer para a direção horizontal quer para a vertical
    if direcao == 'H' and (coluna + len(palavra)) > tamanho_tab:
            return ()
    if direcao == 'V' and (linha + len(palavra)) > tamanho_tab:
            return ()
    
    # Verificar se é a primeira jogada e se a palavra passa pelo centro do tabuleiro
    if primeira:
        if len(palavra) < 2:
            return ()
        cobre_casa_central = False
        for i in range(len(palavra)):
            lin, col = linha, coluna
            if direcao == 'H':
                col = col + i
            else: 
                lin = lin + i
            if (lin, col) == casa_central:
                cobre_casa_central = True
        if not cobre_casa_central:
            return ()
    if not primeira:
        toca_letra_existente = False
        usa_letra_nova = False

        for i in range(len(palavra)):
            lin, col = linha, coluna
            if direcao == 'H':
                col = col + i
            elif direcao == 'V':
                lin = lin + i

             # Se a posição no tabuleiro já estiver ocupada por uma letra
            if tab[lin][col] != '.':  
                if tab[lin][col] != palavra[i]:
                    return ()
                toca_letra_existente = True
            else:
                usa_letra_nova = True

             # Verificar se a nova letra toca em alguma letra existente no tabuleiro
                if lin > 0 and tab[lin-1][col] != '.' or \
                   lin < tamanho_tab-1 and tab[lin+1][col] != '.' or \
                   col > 0 and tab[lin][col-1] != '.' or \
                   col < tamanho_tab-1 and tab[lin][col+1] != '.':
                    toca_letra_existente = True
                
        if not (toca_letra_existente and usa_letra_nova):
            return ()
    # Verificar se a palavra pode ser formada com as letras do jogador
    letras_necessarias = {}
    for i in range(len(palavra)):
        lin, col = linha, coluna
        if direcao == 'H':
            col = col + i
        elif direcao == 'V':
            lin = lin + i
        if tab[lin][col] == '.':
            letras_necessarias[palavra[i]] = letras_necessarias.get(palavra[i], 0) + 1
    for letra, num in letras_necessarias.items():
        if conj_letras.get(letra, 0) < num:
            return ()
        #Inserir a palavra no tabuleiro, ao chamar a função insere_palavra
    insere_palavra(tab, casa, direcao, palavra)
        #Criar tuplo com as letras utilizadas por ordem
    tuplo = tuple(sorted(letras_necessarias.keys()))
    return tuplo

pontos = {
'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1,
'F': 4, 'G': 4, 'H': 4, 'I': 1, 'J': 5, 'L': 2,
'M': 1, 'N': 3, 'O': 1, 'P': 2, 'Q': 6, 'R': 1,
'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Z': 8 }

# 3.4.2 função processa_jogada

'''Esta função processa a jogada de um jogador, que pode ser jogar uma palavra, trocar letras ou passar a sua vez.'''

def processa_jogada(tab, jog, pilha, pontos, primeira):
    while True:
        valid = True
        answer = input(f'Jogada J{jog["id"]}: ')
        answer = answer.strip()
        if answer == "":
            continue
        answer = answer.split()

        # Se o jogador escolher passar a sua vez
        if answer[0] == 'P':
            return False
        # Se o jogador escolher trocar as suas letras
        if answer[0] == 'T' and len(answer) >= 2 and len(pilha) >= 7:
            contador = 0
            copia_letras = jog['letras'].copy()
            for i in answer[1:]:
                if i in copia_letras:
                    if copia_letras[i] == 1:
                        del copia_letras[i]
                    else:
                        copia_letras[i] -= 1
                    contador += 1
                else: 
                    valid = False
            if not valid:
                continue
            jog['letras'] = copia_letras
            for j in range(contador):
                distribui_letra(pilha, jog)
            return True

        # Se o jogador escolher jogar uma palavra
        if answer[0] == 'J' and len(answer) == 5:
            linha = int(answer[1])
            coluna = int(answer[2])
            if linha < 1 or linha > tamanho_tab or coluna < 1 or coluna > tamanho_tab:
                continue
            direcao = answer[3]
            if direcao not in ('H', 'V'):
                continue
            palavra = answer[4]
            casa = (linha, coluna)
            conj_letras = jog['letras']
            letras_usadas = joga_palavra(tab, palavra, casa, direcao, conj_letras, primeira)
            if letras_usadas == ():
                continue
            for letra in letras_usadas:
                if jog['letras'][letra] == 1:
                    del jog['letras'][letra]
                else:
                    jog['letras'][letra] -= 1
                distribui_letra(pilha, jog)

            for letra in palavra:
                jog['pontos'] += pontos[letra]
            return True

# 3.4.3 função scrabble

'''Esta é a função principal do jogo de Scrabble. Recebe o número de jogadores, o saco de letras, os pontos e um estado inicial para o gerador de números pseudo-aleatórios.'''

def scrabble(jogadores, saco, pontos, seed):

    # Verifição do número de jogadores
    if type(jogadores) != int or jogadores < 2 or jogadores > 4:
        raise ValueError('scrabble: argumentos inválidos')
    
    # Verificar se saco não está vazio
    if type(saco) != dict or len(saco) == 0:
        raise ValueError('scrabble: argumentos inválidos')
    
    # Verificar se todas as letras do saco têm valores positivos
    for letra, qtd in saco.items():
        if letra not in letras_validas:
            raise ValueError('scrabble: argumentos inválidos')
        if type(qtd) != int or qtd <= 0:
            raise ValueError('scrabble: argumentos inválidos')
    
    
    
    if type(pontos) != dict:
        raise ValueError('scrabble: argumentos inválidos')
    for let in pontos:
        if let not in letras_validas:
            raise ValueError('scrabble: argumentos inválidos')
        if type(pontos[let]) != int or pontos[let] < 0: 
            raise ValueError('scrabble: argumentos inválidos')
    for letra in letras_validas:
        if letra not in pontos:
            raise ValueError('scrabble: argumentos inválidos')

    # Verificar seed
    if type(seed) != int or seed <= 0:
        raise ValueError('scrabble: argumentos inválidos')
    
    print("Bem-vindo ao SCRABBLE.")
    
    tab = cria_tabuleiro()
    
    # Baralhar saco e criar lista de letras
    pilha = baralha_conjunto(saco, seed)
    
    # Criar jogadores e distribuir 7 letras iniciais
    lista_jogadores = []
    for i in range(jogadores):
        jog = cria_jogador(i + 1, 0, cria_conjunto((), ()))
        # Distribuir 7 letras
        for _ in range(7):
            if not distribui_letra(pilha, jog):
                break
        lista_jogadores.append(jog)
    
    
    primeira_jogada = True
    passadas_consecutivas = 0
    idx_jogador = 0
    
    
    while True:
        
        print(tabuleiro_para_str(tab))
        
        for jog in lista_jogadores:
            print(jogador_para_str(jog))
        
        jog_atual = lista_jogadores[idx_jogador]
        
        jogou = processa_jogada(tab, jog_atual, pilha, pontos, primeira_jogada)
        
        if jogou:
            primeira_jogada = False
            passadas_consecutivas = 0
            
            # Verificar se jogador ficou sem letras e com o saco vazio (após jogar)
            total_letras = sum(jog_atual['letras'].values())
            if total_letras == 0 and len(pilha) == 0:
            
                break
        else:
            passadas_consecutivas += 1
            
            # Se todos passaram consecutivamente, o jogo termina 
            if passadas_consecutivas >= jogadores:
                break
        
        # Próximo jogador
        idx_jogador = (idx_jogador + 1) % jogadores
    
    # Devolver pontuações finais
    return tuple(jog['pontos'] for jog in lista_jogadores)

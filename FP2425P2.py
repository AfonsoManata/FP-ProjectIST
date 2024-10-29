# ============================================================================ #
#                       2º Projeto de FP - Afonso Manata                       #                                         
# ============================================================================ #


# ==============================Constantes==================================== #

A = ord("a") #Código ASCII da letra a

colunas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


# =======================Funções auxiliares======================== #

def adversario(j):
     """
     Recebe uma pedra que representa o jogador e devolve a pedra que representa
     o jogador aversário
     
     Args:
          j : Pedra que representa o jogador
     
     Returns:
          pedra : Pedra que representa o jogador adversário

     """  
     return cria_pedra_branca() if eh_pedra_preta(j) else cria_pedra_preta()

def eh_col(col):
     """
     Recebe uma coluna e verifica se a coluna é válida
     
     Args:
          col : Coluna 
     
     Returns:
          bool : True se a coluna for válida e False caso contrário

     """  
     return type(col)==str and len(col)==1 and col in colunas

def eh_lin(lin):
     """
     Recebe uma linha e verifica se a coluna é válida
     
     Args:
          lin : Linha 
     
     Returns:
          bool : True se a linha for válida e False caso contrário

     """  
     return type(lin) == int and 1 <= lin <= 10

def n_valido(n):
     """
     Recebe um número de órbitas e verifica se é válido
     
     Args:
          n : Número de órbitas de um tabuleiro
     
     Returns:
          bool : True se o número de órbitas é válido e False caso contrário

     """  
     return type(n) == int and 2<=n<=5
     
def t_pos_verifica(n, tp, tb):
     """
     Recebe um número de órbitas, um tuplo de pedras pretas e um tuplo de posições 
     de pepretas e verifica se os tuplos são válidos relativamente às regras do jogo.
     
     Args:
          n : Inteiro que representa o número de órbitas de um tabuleiro
          tp : Tuplo com as posições do jogador que tem a pedra preta
          tb : Tuplo com as posições do jogador que tem a pedra branca
     
     Returns:
          bool : Devolve True se os argumentos forem válidos e False caso contrário  

     """  
     if not(type(tp)==tuple and type(tb)==tuple and \
            len(tb) + len(tp)<= (2*n)*(2*n)):
          return False

     for pos in tp: # Verificar se a posição pertence ao tabuleiro e se é única
          if not(eh_posicao_valida(pos,n) and pos not in tb and tp.count(pos)==1):
               return False

     for pos in tb: # Verificar se a posição pertence ao tabuleiro e se é única
          if not(eh_posicao_valida(pos,n) and pos not in tp and tb.count(pos)==1):
               return False
     
     return True    

def obtem_cordenadas(pos):
     """
     Recebe uma posição e devolve as coordenadas que correspondem a essa posição
     
     Args:
          pos : Posição
     
     Returns:
          tuple : Tuplo com as coordenadas correspondentes à posição dada

     """  
     return ord(obtem_pos_col(pos)) - A, obtem_pos_lin(pos)-1

def coor_to_pos(cord):
     """
     Recebe um tuplo com as coordenadas e devolve a posição correspodente
     
     Args:
          coord : Tuplo com as coordenadas 
     
     Returns:
          posicao : Posicao que corresponde aquelas coordenadas

     """  
     return cria_posicao(colunas[cord[0]], cord[1] + 1)

def pos_tabuleiro_ord(n):
     """
     Recebe um número de órbitas e devolve as posições do tabuleiro ordenadas 
     por ordem de leitura
     
     Args:
          n : Inteiro que representa o número de órbitas de um tabuleiro
     
     Returns:
          tuple : Tuplo com as posições do tabuleiro ordenadas por ordem de leitura

     """  
     
     orbitas = obtem_orbitas(n)
     res = []
     
     for orb in orbitas:
     
          # Ordenar as orbitas por linha
          orb_ord = sorted(orb,key= lambda \
                    pos:(obtem_pos_lin(pos),obtem_pos_col(pos)))
          res.append(orb_ord)
     
     return alisa(res)

def alisa(lst):
     """
     Recebe uma lista com possíveis listas dentro dela e devolve a lista mas 
     sem listas lá dentro ,ou seja, devolve a lista alisada.
     
     Args:
          lst : Lista
     
     Returns:
          list : Lista alisada

     """  
     if not lst: return []
     return (alisa(lst[0]) if type(lst[0])==list else [lst[0]]) + alisa(lst[1:])

def obtem_orbitas(n):
     """
     Recebe um número de órbitas e devolve uma lista com listas de posições 
     divididas por órbitas.
     
     Args:
          n : Inteiro entre 2 e 5 (inclusivé) que representa o número de órbitas
     
     Returns:
          list : Lista de listas de posições divididas por órbita

     """  
     pos_ordenadas, c, add = [], n-1, 1
    
     while c >= 0:
          orbitas =[]
          
          # Serve para cortar a linha de cima
          for el in range(2*n):
               num = coor_to_pos((el,-1+add))
               if not (num in orbitas) and not(num in alisa(pos_ordenadas)): 
                    orbitas+= (num,)
          
          
          # Serve para cortar a coluna do lado direito
          for el in range(2*n):
               num = coor_to_pos((2*n-add,el))
               if not (num in orbitas) and not(num in alisa(pos_ordenadas)): 
                    orbitas+= (num,)
          
          
          # Serve para cortar a linha de baixo
          for el in range(2*n-1,0,-1):
               num =coor_to_pos((el,2*n -add))
               if not(num in orbitas) and not(num in alisa(pos_ordenadas)): 
                    orbitas+= (num,)
          
          
          # Serve para cortar a coluna do lado esquerdo
          for el in range(2*n-1,0,-1):
               num =coor_to_pos((-1+add,el))
               if not (num in orbitas) and not (num in alisa(pos_ordenadas)): 
                    orbitas+= (num,)
          
          c -=1
          add+=1
          pos_ordenadas+= [orbitas]
     
     
     return pos_ordenadas[::-1]

def obtem_orbita_necessaria(t,pos):
     """
     Recebe um tabuleiro e uma posição e devolve uma lista de posições que tem 
     todas as posições da órbita(da posição dada) por ordem do relógio.

     Args:
          t : Tuplo de tuplos de pedras (tabuleiro)
          pos: Posição
     
     Returns:
          list : Lista de posições da órbita da posição dada por ordem do relógio

     """ 
     
     n, res = obtem_numero_orbitas(t), []
     n_orbita = find_orbita(t, pos)
     add = n - n_orbita +1

     
     # Serve para cortar a linha de cima 
     for el in range(2*n):
               num = coor_to_pos((el,-1+add))
               if not(num in res) and find_orbita(t,num) == n_orbita: 
                    res+= (num,)
          
          
     # Serve para cortar a coluna do lado direito
     for el in range(2*n):
          num = coor_to_pos((2*n-add,el))
          if not (num in res) and find_orbita(t,num) == n_orbita: 
               res+= (num,)
     
     
     # Serve para cortar a linha de baixo
     for el in range(2*n-1,0,-1):
          num =coor_to_pos((el,2*n -add))
          if not(num in res) and find_orbita(t,num) == n_orbita: 
               res+= (num,)
     
     
     # Serve para cortar a coluna do lado esquerdo
     for el in range(2*n-1,0,-1):
          num =coor_to_pos((-1+add,el))
          if not (num in res) and find_orbita(t,num) == n_orbita: 
               res+= (num,)
     

     
     return res

def find_orbita(t,pos):
     """
     Recebe um tabuleiro e uma posição e devolve a órbita onde essa posição está
     
     Args:
          t : Tuplo de tuplos de pedras (tabuleiro)
          pos: Posição
     
     Returns:
          int : Inteiro que corresponde ao número da órbita da posição

     """ 
     dim = 2*obtem_numero_orbitas(t)
     y1,x1 = obtem_cordenadas(pos)

     # Obtem coordenadas do ponto central fictício
     xc = dim//2 -0.5 
     yc = dim//2 -0.5
    
     d = max(abs(yc-y1), abs(xc-x1))

     return int(d) + 1 

def only_pos(tup):
     """
     Recebe um tuplo de tuplos e devolve um tuplo com apenas as posições
     
     Args:
          tup : Tuplo com posições e pedras

     Returns:
          tuple : Tuplo com apenas as posições

     """ 
     
     res = ()
     
     for lin in range(len(tup)):
          res+=(tup[lin][0],)
     
     return  res                 

def jogo_facil(t, j):
     """
     Recebe um tabuleiro e uma pedra que representa um jogador e devolve a 
     posição a escolher seguindo a estratégia do modo fácil
     
     Args:
          t : Tuplo de tuplos de pedras
          j: Pedra que representa o jogador
     
     Returns:
          posicao : Posicao indicada usando o modo facil

     """ 
     n = obtem_numero_orbitas(t) 
     free = ordena_posicoes(obtem_posicoes_pedra(t, cria_pedra_neutra()), n)
     t2 = roda_tabuleiro(cria_copia_tabuleiro(t))


     # Vou a cada livre e ver se no final do turno fica adjacente a uma própria
     for pos in free:
          pos_rodada = obtem_posicao_seguinte(t, pos, False)
          adjacentes = obtem_posicoes_adjacentes(pos_rodada, n, True)

          for posicao in adjacentes:
               if pedras_iguais(obtem_pedra(t2, posicao), j) :
                    return pos

     return free[0]

def jogo_normal(t, j):
     """
     Recebe um tabuleiro e uma pedra que representa um jogador e devolve a 
     posição a escolher seguindo a estratégia do modo normal
     
     Args:
          t : Tuplo de tuplos de pedras
          j: Pedra que representa o jogador
     
     Returns:
          posicao : Posicao indicada usando o modo normal

     """ 
     
     res_jogador, res_adversario, n = [], [], obtem_numero_orbitas(t)
     m = n * 2
     
     tab_rodado = roda_tabuleiro(cria_copia_tabuleiro(t))
     tab_rodado2 = roda_tabuleiro(cria_copia_tabuleiro(tab_rodado))

     pos_livres = obtem_posicoes_pedra(tab_rodado, cria_pedra_neutra())
     pos_livres_2 = obtem_posicoes_pedra(tab_rodado2, cria_pedra_neutra())

     while not res_jogador and not res_adversario: 
          
          for pos in pos_livres:
               
               t2 = cria_copia_tabuleiro(tab_rodado) # Não afetar o tabuleiro original 
               new_tab = coloca_pedra(t2, pos, j) 
               pos_anterior = obtem_posicao_seguinte(tab_rodado, pos, True)
               
               if verifica_linha_pedras(new_tab, pos, j, m): 
                    res_jogador.append(pos_anterior)

          for pos in pos_livres_2:     
               
               t3 = cria_copia_tabuleiro(tab_rodado2)
               new_tab2 = coloca_pedra(t3, pos, adversario(j))
               
               pos_ant1 = obtem_posicao_seguinte(tab_rodado, pos, True)
               pos_anterior2 = obtem_posicao_seguinte(tab_rodado,pos_ant1,True)
               
               if verifica_linha_pedras(new_tab2, pos, adversario(j), m):
                    res_adversario.append(pos_anterior2)
          m -= 1
                    
     if res_jogador:
          return ordena_posicoes(res_jogador,n)[0]
     else:
          return ordena_posicoes(res_adversario,n)[0]

          
# ==============================TAD posicao=================================== #
"""
Assinatura - TAD Posicao

- Construtor
     cria posicao: str x int --> posicao

- Seletores
     obtem pos col: posicao --> str
     obtem pos lin: posicao --> int

- Reconhecedor
    eh_posicao: universal --> bool

- Teste
    posicoes_iguais: universal x universal --> bool

- Transformadores
    posicao_para_str: posicao --> str
    str_para_posicao: str --> posicao

- Funcoes de Alto Nivel
    eh_posicao_valida: posicao x int --> bool
    obtem_posicoes_adjacentes: posicao x int x bool --> tuple
    ordena_posicoes: tuple x int --> tuple

"""

def cria_posicao(col,lin):
     """
     Recebe um caracter e um inteiro correspondentes à coluna
     e à linha e devolve a posição correspondente. 
     
     Args:
          col : String que representa a coluna
          lin : Inteiro que representa a linha
     
     Returns:
          posicao : Posicao resultante dessa coluna e dessa linha

     """ 
     if not(eh_col(col) and eh_lin(lin)):
          raise ValueError("cria_posicao: argumentos invalidos")
    
     return col, lin

def obtem_pos_col(posicao):
     """
     Recebe uma posição e devolve a sua coluna
     
     Args:
          posicao : Posicao
     
     Returns:
          str : Letra que representa a coluna dessa posição

     """ 
     return posicao[0]

def obtem_pos_lin(posicao):
     """
     Recebe uma posição e devolve a sua linha
     
     Args:
          posicao : Posicao
     
     Returns:
          int : Inteiro que representa a linha dessa posição

     """ 
     return posicao[1] 

def eh_posicao(ag):
     """
     Recebe um argumento e verifica se é um TAD posicao
     
     Args:
          ag : Universal
     
     Returns:
          bool : True se for uma posição e False caso contrário

     """ 
     return type(ag)==tuple and len(ag)==2 and eh_col(ag[0]) and eh_lin(ag[1])

def posicoes_iguais(p1, p2):
     """
     Recebe duas posições e verifica se são iguais
     
     Args:
          p1 : Posicao 1
          p2 : Posição 2
     
     Returns:
          bool : True se forem iguais e False caso contrário

     """ 
     return obtem_pos_lin(p1)==obtem_pos_lin(p2) and \
          obtem_pos_col(p1)==obtem_pos_col(p2)

def posicao_para_str(p):
     """
     Recebe uma posição e devolve uma string que a representa
     
     Args:
          posicao : Posicao
     
     Returns:
          str : Posição convertida em string

     """ 
     return f"{obtem_pos_col(p)}{obtem_pos_lin(p)}"

def str_para_posicao(s):
     """
     Recebe uma string e devolve a sua posição
     
     Args:
          string : String que define a posição
     
     Returns:
          str : String na forma de posição

     """ 
     return cria_posicao(s[0], int(s[1:]))

def eh_posicao_valida(p, n):
     """
     Recebe uma posição e um número de órbitas 
     
     Args:
          posicao : Posicao
          n : Inteiro que representa o número de órbitas
     
     Returns:
          bool : True se a posição for válida e False caso contrário

     """ 
     return eh_posicao(p) and n_valido(n) and eh_col(obtem_pos_col(p)) \
          and ord(obtem_pos_col(p)) - A < n*2\
          and obtem_pos_lin(p) <= n*2

def obtem_posicoes_adjacentes(p, n, d):
     """
     Recebe uma posição, um número de órbitas e um booleano e devolve um tuplo 
     das posições adjacentes à posição se d é True ou as posições adjacentes 
     ortogonais se d é False.
     
     Args:
          p : Posicao
          n : Inteiro que representa o número de órbitas 
          d : Booleano que indica o que iremos devolver
     
     Returns:
          tuple : Tuplo das posições adjacentes à posição se d é True ou as 
          posições adjacentes ortogonais se d é False.

     """ 
     adj = ()
     x_p, y_p = obtem_cordenadas(p)
     x_p += 1
     y_p +=1
     
     # Pensar nos vetores de forma a obtermos as posições adjacentes 
     # Ordem importante para que seja em sentido do relógio 
     vetores = ((0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1))

     for x,y in vetores:     
          # Para não devolvermos a mesma posição nem posições fora do tab
          if not 1<=x_p+x<=2*n or not 1<=y_p+y<=2*n:
               continue
          
          # Caso seja ortogonal
          if (x==0 or y==0): 
               adj += (cria_posicao(colunas[x_p+x-1], y_p +y),)
          
          # Caso sejam também as das diagonais
          else:
               if d: 
                    adj += (cria_posicao(colunas[x_p+x-1], y_p +y),)


     return adj
     
def ordena_posicoes(t, n):
     """
     Recebe um tuplo e um número de órbitas e devolve esse tuplo ordenado na 
     na ordem de leitura.
     
     Args:
          t : Tuplo de posições
          n : Inteiro que representa o número de órbitas 
     
     Returns:
          tuple : Tuplo inicial mas ordenado pela ordem de leitura do tabuleiro

     """ 
     return sorted(list(t), key=lambda x: pos_tabuleiro_ord(n).index(x))

# ================================TAD pedra=================================== #
"""
Assinatura - TAD Pedra

- Construtores 
    cria_pedra_branca: None --> pedra
    cria_pedra_preta: None --> pedra
    cria_pedra_neutra: None --> pedra

- Reconhecedores 
    eh_pedra: universal --> bool
    eh_pedra_branca: pedra --> bool
    eh_pedra_preta: pedra --> bool

- Teste 
    pedras_iguais: universal x universal --> bool

- Transformador
    pedra_para_str: pedra --> str

- Funções de Alto Nível
    eh_pedra_jogador: pedra --> bool
    pedra_para_int: pedra --> int

"""

def cria_pedra_branca():
     """
     Cria uma pedra branca que representa o jogador branco

     Returns:
          pedra: Pedra branca que representa o jogador branco
     """
     return -1

def cria_pedra_preta():
     """
     Cria uma pedra preta que representa o jogador preto

     Returns:
          pedra: Pedra preta que representa o jogador preto
     """
     return 1

def cria_pedra_neutra():
     """
     Cria uma pedra neutra que representa o vazio

     Returns:
          pedra: Pedra neutra que representa o vazio
     """
     return 0

def eh_pedra(arg):
     """
     Verifica se um certo argumento é ou não um TAD pedra

     Args:
          arg : Universal

     Returns:
          bool : True se for pedra e False caso contrário
     """
     return type(arg) == int and arg in (1, 0, -1)

def eh_pedra_branca(p):
     """
     Verifica se uma pedra é ou não uma pedra branca

     Args:
          p : Pedra

     Returns:
          bool : True se for pedra branca e False caso contrário
     """
     return p == cria_pedra_branca()

def eh_pedra_preta(p):
     """
     Verifica se uma pedra é ou não uma pedra preta

     Args:
          p : Pedra

     Returns:
          bool : True se for pedra preta e False caso contrário
     """
     return p == cria_pedra_preta()

def pedras_iguais(p1, p2):
     """
     Verifica se duas pedras são iguais

     Args:
          p1 : Pedra nº 1
          p2 : Pedra nº 2

     Returns:
          bool : True se as pedras forem iguais e False caso contrário
     """
     return p1 == p2

def pedra_para_str(p):
     """
     Recebe uma pedra e devolve uma string que representa essa pedra

     Args:
          p : Pedra

     Returns:
          str : String que representa essa pedra
     """
     if eh_pedra_branca(p):
          return "O"
     
     elif eh_pedra_preta(p):
          return "X"
     
     return " "
           
def eh_pedra_jogador(p):
     """
     Verifica se a pedra recebida é ou não uma pedra de um jogador

     Args:
          p : Pedra

     Returns:
          bool : True se for pedra branca ou pedra preta e False caso contrário
     """
     return eh_pedra(p) and (eh_pedra_branca(p) or eh_pedra_preta(p))

def pedra_para_int(p):
     """
     Recebe uma pedra e devolve um inteiro que representa essa pedra

     Args:
          p : Pedra

     Returns:
          int : Inteiro que representa essa pedra
     """
     if eh_pedra_branca(p):
          return -1
     
     elif eh_pedra_preta(p):
          return 1
     
     return 0


# ==============================TAD tabuleiro================================= #
"""
Assinatura - TAD Tabuleiro

Construtores:
    cria_tabuleiro_vazio: int --> tabuleiro
    cria_tabuleiro: int x tuplo x tuplo --> tabuleiro
    cria_copia_tabuleiro: tabuleiro --> tabuleiro

Seletores:
    obtem_numero_orbitas: tabuleiro --> int
    obtem_pedra: tabuleiro x posicao --> pedra
    obtem_linha_horizontal: tabuleiro x posicao --> tuplo
    obtem_linha_vertical: tabuleiro x posicao --> tuplo
    obtem_linhas_diagonais: tabuleiro x posicao --> tuplo , tuplo
    obtem_posicoes_pedra: tabuleiro x pedra --> tuplo

Modificadores:
    coloca_pedra: tabuleiro x posicao x pedra --> tabuleiro
    remove_pedra: tabuleiro x posicao --> tabuleiro

Reconhecedor:
    eh_tabuleiro: universal --> bool

Teste:
    tabuleiros_iguais: universal x universal --> bool

Transformador:
    tabuleiro_para_str: tabuleiro --> str

    
Funcoes de Alto Nivel:
    move_pedra: tabuleiro x posicao x posicao --> tabuleiro
    obtem_posicao_seguinte: tabuleiro x posicao x bool --> posicao
    roda_tabuleiro: tabuleiro --> tabuleiro
    verifica_linha_pedras: tabuleiro x posicao x pedra x int --> bool
"""

def cria_tabuleiro_vazio(n):
     """
     Cria um tabuleiro vazio com o número de órbitas introduzido

     Args:
          n : Inteiro que representa o número de órbitas do tab

     Returns:
          tabuleiro : Tabuleiro vazio com o número n de órbitas
     
     """

     if not n_valido(n):
          raise ValueError("cria_tabuleiro_vazio: argumento invalido")

     #Criar o tabuleiro vazio
     t_v = [[cria_pedra_neutra() for i in range(2 * n)] for i in range(2 * n)]
               
     return t_v

def cria_tabuleiro(n, tp, tb):
     """
     Cria um tabuleiro com o número de órbitas introduzido colocando as pedras
     de cada jogador no lugar

     Args:
          n : Inteiro que representa o número de órbitas do tab
          tp : Tuplo com posições de pedras pretas
          tb : Tuplo com posições de pedras brancas

     Returns:
          tabuleiro : Tabuleiro com o número n de órbitas e com todas as pedras
          no lugar certo
     
     """
     if not(n_valido(n) and t_pos_verifica(n,tp, tb)):
          raise ValueError("cria_tabuleiro: argumentos invalidos")
     
     tab = cria_tabuleiro_vazio(n) #Criar o tabuleiro vazio
     
     # Meter as posições pretas no síto certo
     for p in tp:
          y, x = obtem_cordenadas(p)
          tab[x][y] = cria_pedra_preta() 
     
     
     # Meter as posições brancas no síto certo
     for p in tb:
          y, x = obtem_cordenadas(p)
          tab[x][y] = cria_pedra_branca()

     return tab

def cria_copia_tabuleiro(t):
     """
     Cria uma cópia de um tabuleiro

     Args:
          t : Tuplo de tuplo de pedras (tabuleiro)

     Returns:
          tabuleiro : Copia do tabuleiro
     
     """
     
     m = 2* obtem_numero_orbitas(t)
     
     return [[t[lin][col] for col in range(m)] for lin in range(m)]

def obtem_numero_orbitas(t):
     """
     Recebe um tabuleiro e devolve o número de órbitas

     Args:
          t : Tuplo de tuplos de posições (tabuleiro)

     Returns:
          int : Número de órbitas do tabuleiro
     
     """
     return len(t)//2

def obtem_pedra(t, p):
     """
     Recebe um tabuleiro e uma posição e obtém a pedra nessa posição

     Args:
          t : Tuplo de tuplos de posições (tabuleiro)
          p : Posição

     Returns:
          pedra : Pedra que estava naquela posição
     
     """
     y, x = obtem_cordenadas(p)
     return t[x][y]

def obtem_linha_horizontal(t, p):
     """
     Recebe um tabuleiro e uma posição devolve o tuplo formado por tuplos de 
     dois elementos correspondentes à posicao e o valor de todas as posições da 
     linha horizontal que passa pela posição p, ordenadas.

     Args:
          t : Tuplo de tuplos de posições (tabuleiro)
          p : Posição

     Returns:
          tuple : tuplo formado por tuplos de dois elementos correspondentes à
     posicao e o valor de todas as posições da linha horizontal que passa pela 
     posição p, ordenadas.
     
     """
     linha, res, m = obtem_cordenadas(p)[1], (), 2 * obtem_numero_orbitas(t)
     
     for coluna in range(m):
               pos = coor_to_pos((coluna, linha))
               res += (((pos),(obtem_pedra(t, pos))),)

     return res     

def obtem_linha_vertical(t, p):
     """
     Recebe um tabuleiro e uma posição devolve o tuplo formado por tuplos de 
     dois elementos correspondentes à posicao e o valor de todas as posições da 
     linha vertical que passa pela posição p, ordenadas.

     Args:
          t : Tuplo de tuplos de posições (tabuleiro)
          p : Posição

     Returns:
          tuple : tuplo formado por tuplos de dois elementos correspondentes à
     posicao e o valor de todas as posições da linha vertical que passa pela 
     posição p, ordenadas.
     
     """
    
     coluna, res, m = obtem_cordenadas(p)[0], (), 2 * obtem_numero_orbitas(t) 
     for linha in range(m):
          pos = coor_to_pos((coluna, linha))
          res += (((pos),(obtem_pedra(t, pos))),)

     return res   

def obtem_linhas_diagonais(t, p):
     """
     Recebe um tabuleiro e uma posição devolve os tuplos formado por tuplos de 
     dois elementos correspondentes à posicao e o valor de todas as posições da 
     linha diagonal e antidiagonal que passa pela posição p, ordenadas.

     Args:
          t : Tuplo de tuplos de posições (tabuleiro)
          p : Posição

     Returns:
          tuple x tuple : tuplos formado por tuplos de dois elementos 
          correspondentes à posicao e o valor de todas as posições da linha 
          diagonal e antidiagonal que passa pela posição p, ordenadas.
     
     """
     m, n = 2* obtem_numero_orbitas(t), 2* obtem_numero_orbitas(t)
     diag, anti_diag = (), ()
     y, x = obtem_cordenadas(p)

     # Os elementos da mesma diagonal têm a mesma diferença entre as coordenadas 
     for linha in range(m): 
          for coluna in range(n):
               if (linha - coluna == x - y): 
                    pos = coor_to_pos((coluna, linha))
                    diag += (((pos),(obtem_pedra(t, pos))),)
                      
                                                                                                         
     
     # Os elementos da antidiagonal têm a mesma soma entre as coordenadas 
     for linha in range(m): 
          for coluna in range(n):
               if (linha + coluna == x + y): 
                    pos = coor_to_pos((coluna, linha))
                    anti_diag += (((pos),(obtem_pedra(t, pos))),)
     
     #A antidiagonal tem de ser invertida para seguir o enunciado
     return  (diag, anti_diag[::-1]) 

def obtem_posicoes_pedra(t, j):
     """
     Recebe um tabuleiro e uma pedra e determina a posições que correspondem
     à pedra pedida.

     Args:
          t : Tuplo de tuplos de posições (tabuleiro)
          j : Pedra que representa o jogador

     Returns:
          tuple : tuplo formado pelas posições dessa pedra
     
     """
     res, n, pedra = (), obtem_numero_orbitas(t), pedra_para_int(j)


     # Procurar posição a posição
     for pos in pos_tabuleiro_ord(n):
          
          if pedras_iguais(obtem_pedra(t, pos),pedra):
               res += (pos,) 

     return res  

def coloca_pedra(t, p, j):
     """
     Recebe um tabuleiro, uma pedra e uma posição e coloca a pedra no tabuleiro.

     Args:
          t : Tuplo de tuplos de posições (tabuleiro)
          p : Posição
          j : Pedra que representa o jogador

     Returns:
          tuple : tabuleiro já alterado
     
     """
     y,x = obtem_cordenadas(p)
     
     # Alterar destrutivamente o tabuleiro
     t[x][y] = j
     
     return t

def remove_pedra(t, p):
     """
     Recebe um tabuleiro e uma posição e remove a pedra no tabuleiro.

     Args:
          t : Tuplo de tuplos de posições (tabuleiro)
          p : Posição

     Returns:
          tuple : tabuleiro já com a posição removida
     
     """
     y,x = obtem_cordenadas(p)
     
     # Alterar destrutivamente o tabuleiro removendo a pedra
     t[x][y] = cria_pedra_neutra()       
     
     return t

def eh_tabuleiro(arg):
     """
     Recebe um argumento e verifica se é um tabuleiro

     Args:
          arg : Universal

     Returns:
          bool : True se for um tabuleiro e False caso contrário
     
     """
     # Lista com o tamanho das linhas
     el = []
     
     if not(type(arg) == list and 4<=len(arg)<=10 and len(arg)%2==0):
          return False
          
     m = len(arg)
     
     for linha in arg: 
          
          # Guardar o nº de elementos por linha
          if (type(arg) != list):
               return False
          el.append(len(linha)) 
          
          
          for valor in linha: 
               if not eh_pedra(valor):
                    return False
     
     
     #Verificar que o nº de elementos por linha é igual
     for i in range(len(el)): 
          if el[i] != el[0] or el[i]!= m:
               return False
     
     
     return True

def tabuleiros_iguais(t1, t2):
     """
     Recebe dois tabuleiros e verificam se são iguais

     Args:
          t1 : Tuplo de tuplos de posições (tabuleiro)
          t2 : Tuplo de tuplos de posições (tabuleiro)

     Returns:
          bool : True se forem iguais False caso contrário
     
     """
     # Assumindo que são tabuleiros verificar o tamanho
     if not(eh_tabuleiro(t1) and eh_tabuleiro(t2) and len(t1)==len(t2)):
          return False
     
     m = len(t1)
     flag = True
     
     # Ver se todos os elementos são iguais
     for lin in range(m):
          for col in range(m):
               pos = coor_to_pos((lin, col))
               if not pedras_iguais(obtem_pedra(t1, pos),obtem_pedra(t2, pos)):
                    flag = False
     
     return flag             

def tabuleiro_para_str(t):
     """
     Recebe um tabuleiro e passa o para stirng

     Args:
          t : Tuplo de tuplos de posições (tabuleiro)

     Returns:
          string : String que representa o tabuleiro
     
     """
     # A string começa com as letras das colunas
     n = obtem_numero_orbitas(t)
     lin,col = 2*n, 2*n 
     cad,sep ="    " + "   ".join(chr(A+ i) for i in range(col)) +"\n" , ""
     
     # Esta parte permite adicionar o separador que está entre as linhas
     for i in range(col):
          if i != 0:sep += "   " 
          
          if i ==0:sep+= "    |"
                
          else:sep+= "|"     
                    
     for i in range(lin):
          
          if i != 0: cad += sep + "\n"
               
          for j in range(col):  
               # Separador entre elementos
               if j != 0: cad += "-"
               
               # Adiciona o número das linhas
               if j==0: cad+= f"{i+1:02} "
               
               # Adiciona à string o elemento rodeado de "[]"
               pedra = obtem_pedra(t,coor_to_pos((j, i))) 
               cad+="["+pedra_para_str(pedra)+"]"

          # Caso não seja a última linha damos um parágrafo
          if i != lin-1:
               cad += "\n"

     return cad

def move_pedra(t, p1, p2):
     """
     Recebe um tabuleiroe e duas posições e coloca a pedra na outra posição.

     Args:
          t : Tuplo de tuplos de posições (tabuleiro)
          p1 : Posição
          p2 : Posiçãio

     Returns:
          tuple : tabuleiro já alterado
     
     """
     pedra = obtem_pedra(t, p1)
     
     #Colocamos a pedra no síto e depois removemos de onde ela estava
     return coloca_pedra(remove_pedra(t, p1), p2, pedra)       

def obtem_posicao_seguinte(t, p, s):
     """
     Recebe um tabuleiro uma posição e um bool e devolve a posicao seguinte

     Args:
          t : Tuplo de tuplos de posições (tabuleiro)
          p : Posição
          s : bool

     Returns:
          posicao : Posicao seguinte
     
     """
     orbita = obtem_orbita_necessaria(t, p)
     size, index = len(orbita), orbita.index(p)

     if s:
          # Para não sair fora da lista no limite superior
          return orbita[(index+1)%size]
     
     
     else:
          # Para não sair fora da lista no limite inferior
          return orbita[(index-1+size)%size]

def roda_tabuleiro(t):
     """
     Recebe um tabuleiro, uma pedra e uma posição e coloca a pedra no tabuleiro.

     Args:
          t : Tuplo de tuplos de posições (tabuleiro)
          p : Posição
          j : Pedra que representa o jogador

     Returns:
          tuple : tabuleiro já alterado
     
     """
     t2 = cria_copia_tabuleiro(t)
     tab_ord = pos_tabuleiro_ord(obtem_numero_orbitas(t))

     for pos in tab_ord:
          
          # Definir a nova posição
          pos_seg = obtem_posicao_seguinte(t, pos, False)
          
          # Alterar destrutivamente o tabuleiro para a posição seguinte
          t = coloca_pedra(t, pos_seg, obtem_pedra(t2, pos))

     return t

def verifica_linha_pedras(t, p, j, k):
     """
     Verifica se existe uma sequencia de posicoes que passa pela posicao e 
     que tem tamanho igual ou superior a k
     
     Args:
          t: Tabuleiro
          pos: Posicao
          p: Pedra
          k : Inteiro Numero de pedras seguidas necessarias para verificar

     Returns:
          bool: Se existe ou nao uma sequencia de pedras do jogador
               que passa pela posicao e que tem tamanho, no mi
     """
     if not j == obtem_pedra(t, p):
        return False
     
     diag = only_pos(obtem_linhas_diagonais(t, p)[0])
     antidiag = only_pos(obtem_linhas_diagonais(t, p)[1])
     
     horz = only_pos(obtem_linha_horizontal(t, p))
     ver = only_pos(obtem_linha_vertical(t,p))

     l,c = [horz,ver,diag,antidiag], 0

    # Loop para verificar k linhas
     for tup in l:
          flag = False
          
               
          for pos in tup:
               
               # Se as posições forem iguais a flag fica veradeira
               if posicoes_iguais(pos, p):
                    flag = True
               
               # Se a pedra for igual à pedra do jogador adicionamos 1 ao count
               if pedras_iguais(obtem_pedra(t, pos), j):
                    c += 1
               
               else:
                    c = 0
               
               # Caso a posição seja a pretendida e já terem passado k elementos
               if flag and c >= k:
                    return True
               
               # Caso já tenhamos passado pela posição e seja zero o count
               if c == 0 and flag:
                    break    
          c = 0
     
     return False

# ===========================Funções adicionais=============================== #
def eh_vencedor(t, j):
     '''
     Verifica se existe uma condicao de vitoria para as pedras que
     correspondam ah pedra recbida
     
     Args:
          t: Tabuleiro
          p: Pedra

     Returns:
          bool: Se se verifica a condicao de vitoria 
     '''
     k, flag = 2 * obtem_numero_orbitas(t), False

     for p in obtem_posicoes_pedra(t,j):
          
          if verifica_linha_pedras(t, p, j, k):
               flag = True
               break

     return flag          

def eh_fim_jogo(t):
     '''
     Verifica se o jogo esta terminado
     
     Args:
          t: Tabuleiro

     Returns:
          bool: Se o jogo esta terminado 
     '''
     return eh_vencedor(t, cria_pedra_branca()) or \
          eh_vencedor(t, cria_pedra_preta()) or \
               len(obtem_posicoes_pedra(t,cria_pedra_neutra())) == 0

def escolhe_movimento_manual(t):
     """
     Obtem uma posicao manualmente introduzida pelo utilizador
     
     Args:
          t: Tabuleiro

     Returns:
          posicao: Posicao escolhida pelo utilizador
     """
     n = obtem_numero_orbitas(t)
     while True:
          inp = input("Escolha uma posicao livre:")
          
          if not(len(inp)==2 or len(inp)==3) or not inp[0] in colunas:
               continue

          lin = inp[1:] 
          
          if not lin.isdigit() or int(lin)<1 or int(lin)>n*2:
               continue
          
          
          pos = str_para_posicao(inp)
          
          if pos in obtem_posicoes_pedra(t,cria_pedra_neutra()):
               return pos  

def escolhe_movimento_auto(t, j, lvl):
     """
     Obtem uma posicao automaticamente escolhida por uma estrategia
     facil ou normal
     
     Args:
          t: Tabuleiro
          p: pedra
          lvl: estrategia

     Returns:
          posicao: Posicao escolhida pela estrategia 
     """
     # Caso seja o modo fácil
     if lvl == "facil": return jogo_facil(t, j)
     
     # Caso seja o modo normal
     else: return jogo_normal(t, j)
          
def orbito(n, mod, jog):
     """
     Permite jogar um jogo completo de Orbito-n com um modo para
     2 jogadores e outro para 1 jogador contra o computador com
     dificuldade facil ou normal
     
     Args:
          n : Inteiro Numero de orbitas do tabuleiro
          modo : Strinf Modo de jogo
          jog : String Simbolo correspondete ao jogador

     Returns:
          posicao: Posicao escolhida 
     """
     if not(n_valido(n) and type(mod)==str and \
          mod in ("facil", "normal", "2jogadores") and type(jog)==str and \
          len(jog)==1 and jog in ("X", "O")):
          raise ValueError("orbito: argumentos invalidos")

     tab,jog_atual = cria_tabuleiro_vazio(n), cria_pedra_preta()
     
     print(f"Bem-vindo ao ORBITO-{n}.")

     jog = cria_pedra_preta() if jog == "X" else cria_pedra_branca()

     if mod == "2jogadores":
          print(f"Jogo para dois jogadores.")
          print(tabuleiro_para_str(tab))
          while not eh_fim_jogo(tab):
               
               print(f"Turno do jogador '{pedra_para_str(jog_atual)}'.") 
               
               p = escolhe_movimento_manual(tab)
               col, lin = obtem_pos_col(p), obtem_pos_lin(p)
               pos = cria_posicao(col, lin)

               tab = coloca_pedra(tab, pos, jog_atual)
               tab = roda_tabuleiro(tab)
               print(tabuleiro_para_str(tab))

               jog_atual = adversario(jog_atual)
               
          if eh_vencedor(tab, jog):
               print(f"VITORIA DO JOGADOR '{pedra_para_str(jog)}'")
               return pedra_para_int(jog)
          
          elif eh_vencedor(tab, adversario(jog)):
               print(f"VITORIA DO JOGADOR '{pedra_para_str(adversario(jog))}'")
               return pedra_para_int(adversario(jog))
          else:
               print("EMPATE")
               return 0
     
     
     
     
     print(f'Jogo contra o computador ({mod}).')
     print(f"O jogador joga com '{pedra_para_str(jog)}'.")
     print(tabuleiro_para_str(tab))
     
     while not eh_fim_jogo(tab):     
          
          if pedras_iguais(jog, jog_atual):
               print("Turno do jogador.")
               p = escolhe_movimento_manual(tab)
               col, lin = obtem_pos_col(p), obtem_pos_lin(p)
               pos = cria_posicao(col, lin)
          
          else:
               print(f'Turno do computador ({mod}):')
               pos = escolhe_movimento_auto(tab, jog_atual, mod)
          
          
          tab = coloca_pedra(tab, pos, jog_atual)
          tab = roda_tabuleiro(tab)
          print(tabuleiro_para_str(tab))

          jog_atual = adversario(jog_atual)

     if eh_vencedor(tab, jog) and not eh_vencedor(tab, adversario(jog)) :
          print(f"VITORIA")
          return pedra_para_int(jog)
     
     
     elif eh_vencedor(tab, adversario(jog)) and not eh_vencedor(tab, jog) :
          print(f"DERROTA")
          return pedra_para_int(adversario(jog))
     
     else:
          print("EMPATE")
          return 0
     





from os import system, name

def limpar_terminal(): 
    if name == 'nt': 
        system('cls')
        #_ = system('cls')     
    else: 
        system('clear')
        #_ = system('clear') 


class Formatacao:
    espacamento_de_exibicao = 2
    quantidade_de_tracos = 59

    @staticmethod
    def alterar_espacamento(novo_espacamento):
        Formatacao.espacamento_de_exibicao = novo_espacamento


# Criar uma metodo para adicionar/retirar produto
class Produto: #produto, colocar o tipo do produto #pensar na facilidade de reuso 
    def __init__(self, tipo_produto, codigo, modelo, cor, ano, disponivel=True, tipo_locacao=None , valor_locacao=0, email_cliente=None):
        self.tipo_produto = tipo_produto
        self.codigo = codigo
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.disponivel = disponivel # True para Disponivel para locação e False para Locado
        self.tipo_locacao = tipo_locacao # Valores inteiros para calcular 
        self.valor_locacao = valor_locacao
        self.email_cliente = email_cliente


class Cliente:
    def __init__(self, email_cliente, nome_cliente):
        self.email_cliente = email_cliente
        self.nome_cliente = nome_cliente

    # Listar produtos disponíveis no estoque para locacao do cliente
    def verProdutos(self, loja, tipo_a_ser_exibido):
        self.loja = loja
        Loja.mostrarDisponiveis(self.loja,tipo_a_ser_exibido)


    # Receber e-mailcliente, hora_inicial, hora_final, codigo_produto
    def alugarHora(self, inicial, final, produto_locado, loja):        
        self.valor_locacao = (final - inicial) * 5  # Inserir as variaveis de valor na loja e recuperar aqui *****

        for vai_encontrar in loja.lista_produtos:
            #print(vai_encontrar.disponivel)
            # Se o produto já estiver locado, deveria trazer uma mensagem de erro? Lembrando que a lista só mostra os disponiveis. *****
            if vai_encontrar.codigo == produto_locado and vai_encontrar.disponivel == True:
                vai_encontrar.disponivel = False #Bloquea o produto para locacao
                vai_encontrar.tipo_locacao = 'H'
                vai_encontrar.valor_locacao = self.valor_locacao
                vai_encontrar.email_cliente = self.email_cliente


    # Receber e-mailcliente, dia_inicial, dia_final, produto
    def alugarDia(self, inicial, final, produto_locado, loja):
        self.valor_locacao = (final - inicial) * 25
        for vai_encontrar in loja.lista_produtos:
            #print(vai_encontrar.disponivel)
            if vai_encontrar.codigo == produto_locado and vai_encontrar.disponivel == True:
                vai_encontrar.disponivel = False #Bloquea o produto para locacao
                vai_encontrar.tipo_locacao = 'D'
                vai_encontrar.valor_locacao = self.valor_locacao
                vai_encontrar.email_cliente = self.email_cliente                


    # Receber e-mail,semana_inicial,semana_final,produto
    def alugarSemana(self, inicial, final, produto_locado, loja):
        self.valor_locacao = 0
        self.valor_locacao = (final - inicial) * 100
        for vai_encontrar in loja.lista_produtos:
            #print(vai_encontrar.disponivel)
            if vai_encontrar.codigo == produto_locado and vai_encontrar.disponivel == True:
                vai_encontrar.disponivel = False #Bloquea o produto para locacao
                vai_encontrar.tipo_locacao = 'S'
                vai_encontrar.valor_locacao = self.valor_locacao
                vai_encontrar.email_cliente = self.email_cliente                

        # for x in loja.lista_produtos:
        #     #print(x.tipo_produto, x.codigo, x.modelo, x.cor, x.ano, x.disponivel, x.tipo_locacao, x.valor_locacao, x.email_cliente)
        #     print(f'{x.tipo_produto:10s} | {x.codigo} | {x.modelo:15s} | {x.cor:10s} | {x.ano} | {x.disponivel} | {x.tipo_locacao} | {x.valor_locacao} | {x.email_cliente}')


    #Caso a quantidade de bike alugadas for superior a 3 produtos, APLICAR O DESCONTO DE 30%
    # ou utiizar apenas no fechamento, caso o e-mail tenha alugado 3 ou mais
    def alugarFamilia(self):
        desconto_familia = 30
        return desconto_familia
        pass


#Gravar a hora inicial e o tipo de aluguel

class Loja:
    def __init__(self,lista_produtos=[]):
        self.lista_produtos = lista_produtos


    #Quando a bike for devolvida
    def calcularConta(self, cliente):
        print('Achou')
        print(cliente.email_cliente)

        for x in self.lista_produtos:
             print(f'{x.tipo_produto:10s} | {x.codigo} | {x.modelo:15s} | {x.cor:10s} | {x.ano} | {x.disponivel} | {x.tipo_locacao} | {x.valor_locacao} | {x.email_cliente}')

        # Criar um laço para encontrar o e-mail na lista acima
            # Criar uma variavel valor_final
            # Se o tipo H ou D ou S tiver mais de três entradas 
                # recuperar o alugarFamilia para aplicar o desconto de 30%
            # Valor final será a soma dos campos x.valor_locacao
            # Desbloquear produto
                #x.disponivel = False
                #x.tipo_locacao = None
                #x.tipo_valor = 0
                #x.email_cliente = None
        # Retornar valor_final     


    def receberPedidos(self, cliente, tipo_locacao, inicial, final, codigo_produto):
        
        if tipo_locacao == 'H':
            cliente.alugarHora(inicial,final,codigo_produto,self)

        elif tipo_locacao == 'D':
            cliente.alugarDia(inicial,final,codigo_produto,self)

        elif tipo_locacao == 'S':
            cliente.alugarSemana(inicial,final,codigo_produto,self)


    def mostrarEstoque(self, tipo_a_ser_exibido):
        Loja.mostrarDisponiveis(self,tipo_a_ser_exibido) #***** Ainda tenho dúvida quando devo usar self.tipo_a_ser_exibido
        Loja.mostrarLocados(self,tipo_a_ser_exibido)


    def mostrarDisponiveis(self, tipo_a_ser_exibido):
        contador = 0 # Contador de produtos  
        print(f'Produto selecionado: {tipo_a_ser_exibido.upper()}')

        produtos_para_exibir = []
        for produto in self.lista_produtos:
            if produto.disponivel and produto.tipo_produto == tipo_a_ser_exibido:
                produtos_para_exibir.append(produto)
                contador += 1

        self.imprimirProdutos(produtos_para_exibir)
        print(f'Quantidade disponível: {contador}\n')


    def mostrarLocados(self,tipo_a_ser_exibido):
        contador = 0 #Contador de produtos
        print(f'Produto selecionado: {tipo_a_ser_exibido.upper()}')

        produtos_para_exibir = []
        for produto in self.lista_produtos:
            if not produto.disponivel:
                produtos_para_exibir.append(produto)
                contador += 1

        self.imprimirProdutos(produtos_para_exibir)        
        print(f'Quantidade locada: {contador}\n')


    def imprimirProdutos(self, produtos):
        n = Formatacao.espacamento_de_exibicao
        x = Formatacao.quantidade_de_tracos
        print('-'*x)
        print(f'|{" "*n}CODIGO{"":5s}{" "*n}|{" "*n}MODELO{"":7s}{" "*n}|{" "*n}COR{"":7s}{" "*n}|{" "*n}ANO{"":1s}{" "*n}|')
        print('-'*x)
        for produto in produtos:
            print(f'|{" "*n}{produto.codigo}{" "*n}|{" "*n}{produto.modelo:13s}{" "*n}|{" "*n}{produto.cor:10s}{" "*n}|{" "*n}{produto.ano}{" "*n}|')
        print('-'*x)


limpar_terminal()

# Cadastrar produtos e criar a Loja Brasília
loja_brasilia = Loja([
    Produto('Bicicleta','61.10.01.01','Urbana','Azul','2019'),
    Produto('Bicicleta','61.10.02.01','Dobrável','Vermelha','2021'),
    Produto('Bicicleta','61.10.03.01','Fixa','Rosa','2022'),
    Produto('Bicicleta','61.10.04.01','Elétrica','Verde','2013'),
    Produto('Bicicleta','61.10.05.01','Speed','Amarela','2019'),
    Produto('Bicicleta','61.10.06.01','Mountain Bike','Vermelha','2018'),
    Produto('Bicicleta','61.10.03.02','Fixa','Azul','2019'),
    Produto('Bicicleta','61.10.07.01','BMX','Preta','2013'),
    Produto('Bicicleta','61.10.04.02','Elétrica','Branca','2013',False),    
    Produto('Patinete','61.20.04.01','Elétrica','Verde','2021'),
    Produto('Patinete','61.20.04.01','Elétrica','Preta','2021'),
])

loja_joaopessoa = Loja([
    Produto('Patinete','83.20.01.01','Urbana','Azul','2019'),
    Produto('Patinete','83.20.02.01','Dobrável','Vermelha','2021'),
    Produto('Patinete','83.20.03.01','Fixa','Rosa','2022',False),
    Produto('Patinete','83.20.04.01','Elétrica','Verde','2013'),
    Produto('Patinete','83.20.05.01','Speed','Amarela','2019'),
    Produto('Patinete','83.20.06.01','Mountain Bike','Vermelha','2018'),
    Produto('Patinete','83.20.03.02','Fixa','Azul','2019'),
    Produto('Patinete','83.20.07.01','BMX','Preta','2013'),
    Produto('Patinete','83.20.04.02','Elétrica','Branca','2013',False),    
    Produto('Bicicleta','83.10.04.01','Elétrica','Verde','2021'),
    Produto('Bicicleta','83.10.04.01','Elétrica','Preta','2021'),
])



# Cadastrar Cliente e testar os metodos instanciando o objeto cliente
# Washington = Cliente('w@email.com','Washington')
# Washington.verProdutos(loja_brasilia,'Bicicleta')
# Washington.alugarHora(3,5,'61.10.01.01',loja_brasilia)
# Washington.alugarHora(3,5,'61.10.02.01',loja_brasilia)
# Washington.alugarHora(3,5,'61.10.05.01',loja_brasilia)
# Washington.verProdutos(loja_brasilia,'Bicicleta')


#Receber Pedido
#loja_brasilia.mostrarEstoque('Bicicleta')
Washington = Cliente('w@email.com','Washington')
loja_brasilia.receberPedidos(Washington,'H',3,5,'61.10.01.01')
loja_brasilia.receberPedidos(Washington,'H',3,5,'61.10.02.01')
loja_brasilia.receberPedidos(Washington,'H',3,5,'61.10.05.01')

loja_brasilia.receberPedidos(Washington,'D',3,5,'61.10.03.01')
loja_brasilia.receberPedidos(Washington,'S',3,5,'61.10.07.01')

#loja_brasilia.mostrarEstoque('Bicicleta')

#Calcular Conta
Washington = Cliente('w@email.com','Washington')
loja_brasilia.calcularConta(Washington)









# Mostrar estoque da loja. (Bicicletas e Patinetes disponíveis e locadas)
# loja_brasilia.mostrarEstoque('Bicicleta') 
# loja_joaopessoa.mostrarEstoque('Patinete')



#loja_brasilia.receberPedidos() #Será que aqui cabe um tratamento de erro? *****
#loja_brasilia.receberPedidos('bicicleta')
#loja_brasilia.mostrarEstoque('bicicleta')
#loja_brasilia.mostrarLocados('bicicleta')
#Washington.alugarHora(3,5,'61.10.01.01') #Será que aqui deveria mostrar um erro?



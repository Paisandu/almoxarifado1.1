# classe que guarda os produtos do almoxarifado
class Almoxarifado:
 # cria o almoxarifado vazio
 def __init__(self, unidade):
    self.unidade = unidade
    self.produtos = []
 # coloca um produto novo na lista
 def adicionar(self, produto):
    self.produtos.append(produto)

# conta quantos produtos zeraram
    def contar_em_falta(self):
        total = 0 
        for p in self.produtos: 
            if p.situacao() == "Em falta":
                total = total + 1
        return total 

    # procura um produto pelo codigo
    def buscar(self, codigo):
        for p in self.produtos:
            if p.codigo == codigo:
                return p # se acho devolve o produto
        return None # se nao acho devolve nada

    # adiciona mais itens no estoque do produto
    def entrada(self, codigo, qtd):
        produto = self.buscar(codigo)
        if produto is None:
            return False # se nao acho o produto retorna falso
        produto.entrada(qtd)
        return True # deu bom, retorna verdadeiro

    # tira itens do estoque se tiver suficiente
    def saida(self, codigo, qtd):
        produto = self.buscar(codigo)
        if produto is None:
            return False # se o codigo nao existe da falso
        return produto.saida(qtd) # usa o metodo la do produto pra ver se consegue tirar

    # transforma todos os produtos numa lista de dicionarios
    def listar(self):
        lista = []
        for p in self.produtos:
            lista.append(p.listar_produtos())
        return lista

    # pega so os produtos que precisam comprar mais
    def solicitacao_compra(self):
        pedido = []
        for p in self.produtos:
            situacao_atual = p.situacao()
            if situacao_atual == "Repor" or situacao_atual == "Em falta":
                pedido.append({
                    "codigo": p.codigo,
                    "nome": p.nome,
                    "situacao": situacao_atual
                })
        return pedido

    # soma o valor total em dinheiro parado no estoque
    def valor_estoque(self):
        total = 0.0
        for p in self.produtos:
            total = total + (p.quantidade * p.preco)
        return total

    # monta um dicionario geral com os dados da unidade
    def para_dicionario(self):
        return {
            "unidade": self.unidade,
            "total_produtos": len(self.produtos),
            "produtos": self.listar()
        }
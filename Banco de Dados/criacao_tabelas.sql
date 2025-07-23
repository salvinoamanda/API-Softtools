-- Tabelas de Cadastro
CREATE TABLE Usuario (Id_usuario SERIAL,
					  Nome TEXT NOT NULL,
					  Email TEXT UNIQUE NOT NULL,
					  Senha TEXT NOT NULL,
					  Telefone VARCHAR(15),
					  Estado TEXT NOT NULL,
					   
					  PRIMARY KEY (Id_usuario));


CREATE TABLE Ferramenta (Id_produto SERIAL,
						 Nome TEXT NOT NULL,
						 Proprietario TEXT NOT NULL,
						 Diaria DECIMAL(10,2),
						 Descricao TEXT,
						 Status VARCHAR(10) NOT NULL CHECK (LOWER (Status) IN ('disponível', 'alugada')),
						 Categoria VARCHAR(11) CHECK (LOWER (Categoria) IN ('manuais', 'elétricas', 'pneumáticas', 'hidráulicas', 'de medição')),
						 Chave_pix TEXT NOT NULL,
						 Avaliacao INTEGER,
						 Id_propri INTEGER,

						 PRIMARY KEY (Id_produto),
						 FOREIGN KEY (Id_propri) REFERENCES Usuario(Id_usuario));

CREATE TABLE Fotos (Id_prod INTEGER,
					Id_foto SERIAL,
					Link_foto TEXT NOT NULL,
					
					PRIMARY KEY (Id_prod, Id_foto),
					FOREIGN KEY (Id_prod) REFERENCES Ferramenta(Id_produto));


-- Funcionalidades do sistema
CREATE TABLE Historico_aluguel (Id_cliente INTEGER,
								Id_prod INTEGER,
								
								PRIMARY KEY (Id_cliente, Id_prod),
								FOREIGN KEY (Id_cliente) REFERENCES Usuario(Id_usuario),
								FOREIGN KEY (Id_prod) REFERENCES Ferramenta(Id_produto));

CREATE TABLE Historico_registro (Id_propri INTEGER,
								 Id_prod INTEGER,
								
								 PRIMARY KEY (Id_propri, Id_prod),
								 FOREIGN KEY (Id_propri) REFERENCES Usuario(Id_usuario),
								 FOREIGN KEY (Id_prod) REFERENCES Ferramenta(Id_produto));

CREATE TABLE Pedido (Id_pedido SERIAL,
					 Quantidade_dias INTEGER,
					 Data_inicio DATE,
					 Data_devolucao DATE,
					 Alugada BOOLEAN NOT NULL,
					 
					 PRIMARY KEY (Id_pedido));

CREATE TABLE Ferramentas_pedido (Id_pedi INTEGER,
								 Id_ferramentas SERIAL,
								 Id_prod INTEGER,
								 
								 PRIMARY KEY (Id_pedi, Id_ferramentas),
								 FOREIGN KEY (Id_pedi) REFERENCES Pedido(Id_pedido),
								 FOREIGN KEY (Id_prod) REFERENCES Ferramenta(Id_produto));

CREATE TABLE Carrinho (Id_cliente INTEGER,
					   Id_pedi INTEGER,
					   
					   PRIMARY KEY (Id_cliente, Id_pedi),
					   FOREIGN KEY (Id_cliente) REFERENCES Usuario(Id_usuario),
					   FOREIGN KEY (Id_pedi) REFERENCES Pedido(Id_pedido));
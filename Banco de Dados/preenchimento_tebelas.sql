

-- 1) USUARIO (10+)
INSERT INTO usuario (nome, email, senha, telefone, estado) VALUES
('Ana Souza',       'ana@example.com',       'hash_senha_1',  '(67)90000-0001', 'MS'),
('Bruno Lima',      'bruno@example.com',     'hash_senha_2',  '(67)90000-0002', 'MS'),
('Carla Mendes',    'carla@example.com',     'hash_senha_3',  '(67)90000-0003', 'MS'),
('Diego Alves',     'diego@example.com',     'hash_senha_4',  '(67)90000-0004', 'MS'),
('Elisa Silva',     'elisa@example.com',     'hash_senha_5',  '(67)90000-0005', 'MS'),
('Felipe Rocha',    'felipe@example.com',    'hash_senha_6',  '(67)90000-0006', 'MS'),
('Gabriela Reis',   'gabriela@example.com',  'hash_senha_7',  '(67)90000-0007', 'MS'),
('Hugo Pereira',    'hugo@example.com',      'hash_senha_8',  '(67)90000-0008', 'MS'),
('Isabela Torres',  'isabela@example.com',   'hash_senha_9',  '(67)90000-0009', 'MS'),
('João Martins',    'joao@example.com',      'hash_senha_10', '(67)90000-0010', 'MS');

-- 2) PEDIDO (10+)
-- datas coerentes com quantidade_dias
INSERT INTO pedido (quantidade_dias, data_inicio, data_devolucao, alugada) VALUES
( 3, '2025-07-01', '2025-07-04', TRUE),
( 5, '2025-07-02', '2025-07-07', TRUE),
( 2, '2025-07-05', '2025-07-07', TRUE),
(10, '2025-07-10', '2025-07-20', TRUE),
( 7, '2025-07-12', '2025-07-19', TRUE),
( 4, '2025-07-15', '2025-07-19', TRUE),
( 1, '2025-07-20', '2025-07-21', TRUE),
(14, '2025-07-21', '2025-08-04', TRUE),
( 6, '2025-07-25', '2025-07-31', TRUE),
( 3, '2025-08-01', '2025-08-04', TRUE);

-- 3) FERRAMENTA (10+)
-- status e categoria usam os valores do Enum definidos no ORM: DISPONIVEL|ALUGADA e MANUAL|ELETRICA|PNEUMATICA|HIDRAULICA|MEDICAO
INSERT INTO ferramenta
(nome, diaria, descricao, status, categoria, chave_pix, avaliacao, quantidade_avaliacoes, id_proprietario)
VALUES
('Furadeira Impacto 600W',      25.00, 'Furadeira para alvenaria e madeira',        'DISPONIVEL', 'ELETRICA',   'chave_pix_ana',    5, 12, 1),
('Parafusadeira 12V',           20.00, 'Parafusadeira leve com bateria',            'DISPONIVEL', 'ELETRICA',   'chave_pix_bruno',  4,  8, 2),
('Marreta 1kg',                 10.00, 'Marreta manual para demolição leve',       'DISPONIVEL', 'MANUAL',     'chave_pix_carla',  4, 10, 3),
('Compressor de Ar 24L',        45.00, 'Compressor para ferramentas pneumáticas',   'ALUGADA',    'PNEUMATICA', 'chave_pix_diego',  5, 20, 4),
('Esmerilhadeira 900W',         30.00, 'Lixamento e corte de metal',               'DISPONIVEL', 'ELETRICA',   'chave_pix_elisa',  4, 14, 5),
('Chave de Torque',             18.00, 'Aperto controlado de parafusos',           'DISPONIVEL', 'MANUAL',     'chave_pix_felipe', 5,  6, 6),
('Macaco Hidráulico 2T',        22.00, 'Elevação de veículos leves',               'DISPONIVEL', 'HIDRAULICA', 'chave_pix_gabri',  4,  7, 7),
('Pregadeira Pneumática',       40.00, 'Aplicação de pregos em madeira',           'ALUGADA',    'PNEUMATICA', 'chave_pix_hugo',   5, 11, 8),
('Paquímetro 150mm',            12.00, 'Medição de precisão',                      'DISPONIVEL', 'MEDICAO',    'chave_pix_isabela',4,  9, 9),
('Serra Circular 1400W',        35.00, 'Corte em madeira com guia',                'DISPONIVEL', 'ELETRICA',   'chave_pix_joao',   5, 15, 10);

-- 4) FOTO (10+) – cada foto aponta para uma ferramenta existente
INSERT INTO "Foto" (id_ferramenta, link_foto) VALUES
(91, 'https://cdn.exemplo/ferramentas/1_a.jpg'),
(91, 'https://cdn.exemplo/ferramentas/1_b.jpg'),
(92, 'https://cdn.exemplo/ferramentas/2_a.jpg'),
(93, 'https://cdn.exemplo/ferramentas/3_a.jpg'),
(94, 'https://cdn.exemplo/ferramentas/4_a.jpg'),
(95, 'https://cdn.exemplo/ferramentas/5_a.jpg'),
(96, 'https://cdn.exemplo/ferramentas/6_a.jpg'),
(97, 'https://cdn.exemplo/ferramentas/7_a.jpg'),
(98, 'https://cdn.exemplo/ferramentas/8_a.jpg'),
(99, 'https://cdn.exemplo/ferramentas/9_a.jpg');

-- 5) HISTORICO_ALUGUEL (10+) – referencia usuario.id e ferramenta.id
INSERT INTO historico_aluguel ( id_cliente, id_produto, timestamp) VALUES
(2, 94,  '2025-07-11 10:00:00+00'),
(3, 95,  '2025-07-13 09:30:00+00'),
(1, 92,  '2025-07-03 14:20:00+00'),
(4, 98,  '2025-07-22 08:45:00+00'),
(5, 91,  '2025-07-06 16:10:00+00'),
(6, 97,  '2025-07-18 11:05:00+00'),
(7, 96,  '2025-07-19 17:50:00+00'),
(8, 100, '2025-07-28 13:15:00+00'),
(9, 99,  '2025-07-30 15:40:00+00'),
(10,93,  '2025-08-02 12:00:00+00');


-- 6) FERRAMENTAS_PEDIDO (10+) – pares (id_ferramenta, id_pedido) devem ser únicos
INSERT INTO ferramentas_pedido (id_ferramenta, id_pedido, quantidade) VALUES
(91,71,  1),
(92,71,  2),
(93,72,  1),
(94,73,  1),
(95,74,  2),
(96,75,  1),
(97,76,  1),
(98,77,  1),
(99,78,  3),
(100, 79,  1),
(91,80, 2);


-- 7) CARRINHO (10+) – associação usuario x pedido (pares únicos)
INSERT INTO carrinho (id_cliente, id_pedido) VALUES
(1,71),
(2,72),
(3,73),
(4,74),
(5,75),
(6,76),
(7,77),
(8,78),
(9,79),
(10, 80);





--
-- Banco de dados: `trabalho_sa`
--
CREATE DATABASE IF NOT EXISTS `trabalho_sa` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `trabalho_sa`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `fornecedor`
--

CREATE TABLE `fornecedor` (
  `idfornecedor` int(11) NOT NULL,
  `fornecedores` text DEFAULT NULL,
  `cpf` text DEFAULT NULL,
  `telefone` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `endereco` text DEFAULT NULL,
  `produto` text DEFAULT NULL,
  `quantidade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `fornecedor`
--

INSERT INTO `fornecedor` (`idfornecedor`, `fornecedores`, `cpf`, `telefone`, `email`, `endereco`, `produto`, `quantidade`) VALUES
(4, 'Sr. White', '123-321', '122-334', 'Srblack@gmail', 'Rua casqueiro', 'Bateria de carro verde', 100),
(5, 'Robertinho', '123-321-543', '121-33332', 'robertao@gmail', 'Rua dos tucanos', 'Bateria de onibus', 25),
(6, 'Sr Jeorge', '1444-1231', '314144-412', 'SrJeorgeBateras@gmail', 'Rua tranquilo', 'bateria de moto', 45);

-- --------------------------------------------------------

--
-- Estrutura para tabela `funcionario`
--

CREATE TABLE `funcionario` (
  `idfuncionario` int(11) NOT NULL,
  `nome` text DEFAULT NULL,
  `cpf` text NOT NULL,
  `telefone` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `dataDeContratacao` text DEFAULT NULL,
  `cargo` text DEFAULT NULL,
  `salario` text DEFAULT NULL,
  `endereco` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `funcionario`
--

INSERT INTO `funcionario` (`idfuncionario`, `nome`, `cpf`, `telefone`, `email`, `dataDeContratacao`, `cargo`, `salario`, `endereco`) VALUES
(1, 'Gustavo', '123-123-123', '123=123', 'gustavinho@gmail', '12/03/18', 'gerente', '15.400', 'RUA ALBANO SCHIMITCH'),
(2, 'Max', '123-123-123', '443-123', 'max@gmail', '30/04/', 'faxineiro', '19.020', 'RUA DOS TUCANOS'),
(3, 'Antonio', '123-123-123', '4002-8922', 'ben10reidelas@gmail.com', '10/05/99', 'carteiro', '40.000', 'MANGUE');

-- --------------------------------------------------------

--
-- Estrutura para tabela `produto`
--

CREATE TABLE `produto` (
  `idproduto` int(11) NOT NULL,
  `tipo` text DEFAULT NULL,
  `voltagem` text DEFAULT NULL,
  `marca` text DEFAULT NULL,
  `quantidade` int(11) DEFAULT NULL,
  `preco` text DEFAULT NULL,
  `data` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `produto`
--

INSERT INTO `produto` (`idproduto`, `tipo`, `voltagem`, `marca`, `quantidade`, `preco`, `data`) VALUES
(1, 'carro', '240', 'VGMPower', 100, '89', '14/06/28'),
(2, 'Moto', '100', 'VGMPower', 200, '59', '31/09/27'),
(3, 'Onibus', '400', 'VGMPower', 50, '199', '12/10/30');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `idusuario` int(11) NOT NULL,
  `usuario` text DEFAULT NULL,
  `senha` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuario`
--

INSERT INTO `usuario` (`idusuario`, `usuario`, `senha`) VALUES
(1, 'vgn', '123');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  ADD PRIMARY KEY (`idfornecedor`);

--
-- Índices de tabela `funcionario`
--
ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`idfuncionario`);

--
-- Índices de tabela `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`idproduto`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idusuario`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  MODIFY `idfornecedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `idfuncionario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `produto`
--
ALTER TABLE `produto`
  MODIFY `idproduto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idusuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;
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
  `cargo` text DEFAULT NULL,
  `salario` text DEFAULT NULL,
  `cidade` text DEFAULT NULL,
  `bairro` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  MODIFY `idfornecedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `idfuncionario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `produto`
--
ALTER TABLE `produto`
  MODIFY `idproduto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idusuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

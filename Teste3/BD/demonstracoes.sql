CREATE TABLE IF NOT EXISTS demonstracoes (
    Registro_ANS INT PRIMARY KEY NOT NULL,
    CNPJ VARCHAR(50) NOT NULL,
    Razao_Social VARCHAR(100) NOT NULL,
    Logradouro VARCHAR(100),
    Numero INT,
    Complemento VARCHAR(50),
    Bairro VARCHAR(50),
    Cidade VARCHAR(50),
    UF VARCHAR(4),
    CEP VARCHAR(10),
    DDD VARCHAR(10),
    Telefone VARCHAR(15),
    Fax VARCHAR(15),
    Endereco_eletronico VARCHAR(100),
    Representante VARCHAR(100),
    Cargo_Representante VARCHAR(50),
    Regiao_de_Comercializacao VARCHAR(50),
    Data_Registro_ANS DATE
);

LOAD DATA INFILE 'Teste3/Relatorio_cadop.csv' INTO TABLE demonstracoes FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS; 


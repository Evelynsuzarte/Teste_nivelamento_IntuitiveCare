CREATE TABLE IF NOT EXISTS operacoes_ativas (
    DATA_OP DATE 
    REG_ANS VARCHAR(10)
    CD_CONTA_CONTABIL VARCHAR(10)
    DESCRICAO VARCHAR(10)
    VL_SALDO_INICIAL VARCHAR(10)
    VL_SALDO_FINAL VARCHAR(10)
);


LOAD DATA INFILE '/caminho/para/seu/arquivo/dados.csv' INTO TABLE usuarios FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS; 

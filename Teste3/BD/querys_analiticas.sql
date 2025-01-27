SELECT REG_ANS, SUM(VL_SALDO_FINAL) AS Despesas_Trimestre FROM operacoes_ativas WHERE DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'  
AND DATA_OP >= DATE_SUB(CURRENT_DATE(), INTERVAL 3 MONTH) 
GROUP BY REG_ANS 
ORDER BY Despesas_Trimestre DESC 
LIMIT 10;

SELECT REG_ANS, SUM(VL_SALDO_FINAL) AS Despesas_Ano FROM operacoes_ativas WHERE DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR' 
AND DATA_OP >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 YEAR) 
GROUP BY REG_ANS 
ORDER BY Despesas_Ano DESC 
LIMIT 10;

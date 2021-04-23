 SELECT * FROM transactions
 LIMIT 10;

 SELECT SUM(money_in) FROM transactions;
 SELECT SUM(money_out) FROM transactions;

 SELECT COUNT(money_in) FROM transactions;

  SELECT COUNT(money_in) FROM transactions
  WHERE currency='BIT';

  SELECT MAX(money_in), MAX(money_out)
  FROM transactions;

  SELECT AVG(money_in) FROM transactions
  WHERE currency='ETH';

  SELECT date, ROUND(AVG(money_in),2) , ROUND(AVG(money_out),2)
  FROM transactions
  GROUP BY date







 
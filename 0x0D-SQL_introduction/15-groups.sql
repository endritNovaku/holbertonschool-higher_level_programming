-- list the number of records with the same score
SELECT score, COUNT(score) number FROM second_score GROUP BY score ORDER BY number DESC

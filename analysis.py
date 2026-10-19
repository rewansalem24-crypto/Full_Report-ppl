USE sales_project;
SELECT 'section','label','value1','value2'
UNION ALL
SELECT 'KPI','total_sales',
 CAST(SUM(CASE WHEN deal_stage='Won' THEN close_value END) AS CHAR), ''
FROM sales_pipeline
UNION ALL
SELECT 'KPI','win_rate_pct',
 CAST(ROUND(100*SUM(deal_stage='Won')/SUM(deal_stage IN ('Won','Lost')),1) AS CHAR), ''
FROM sales_pipeline
UNION ALL
SELECT 'KPI','avg_days_to_close',
 CAST(ROUND(AVG(CASE WHEN deal_stage='Won' THEN DATEDIFF(close_date,engage_date) END),1) AS CHAR), ''
FROM sales_pipeline
UNION ALL
SELECT 'Stage', deal_stage, CAST(COUNT(*) AS CHAR), ''
FROM sales_pipeline
GROUP BY deal_stage
UNION ALL
SELECT 'Product', product, CAST(SUM(close_value) AS CHAR), CAST(COUNT(*) AS CHAR)
FROM sales_pipeline
WHERE deal_stage='Won'
GROUP BY product
UNION ALL
SELECT 'Monthly', DATE_FORMAT(close_date,'%Y-%m'), CAST(SUM(close_value) AS CHAR), ''
FROM sales_pipeline
WHERE deal_stage='Won'
GROUP BY DATE_FORMAT(close_date,'%Y-%m')
UNION ALL
(SELECT 'TopAgent', sales_agent, CAST(SUM(close_value) AS CHAR), ''
FROM sales_pipeline
WHERE deal_stage='Won'
GROUP BY sales_agent
ORDER BY SUM(close_value) DESC
LIMIT 10)
UNION ALL
SELECT 'WinRate', sales_agent,
 CAST(ROUND(100*SUM(deal_stage='Won')/SUM(deal_stage IN ('Won','Lost')),1) AS CHAR),
 CAST(SUM(deal_stage='Won') AS CHAR)
FROM sales_pipeline
GROUP BY sales_agent
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/full_report.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';

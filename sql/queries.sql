SELECT *
FROM worldbank_data
LIMIT 10;


SELECT
    country,
    MAX(gdp_billions) AS gdp_billions
FROM worldbank_data
GROUP BY country
ORDER BY gdp_billions DESC;


SELECT
    country,
    AVG(life_expectancy) AS avg_life
FROM worldbank_data
GROUP BY country
ORDER BY avg_life DESC;

SELECT
    country,
    MAX(inflation) AS highest_inflation
FROM worldbank_data
GROUP BY country
ORDER BY highest_inflation DESC;

SELECT
    country,
    AVG(gdp_per_capita) AS avg_gdp_per_capita
FROM worldbank_data
GROUP BY country
ORDER BY avg_gdp_per_capita DESC;

SELECT
    country,
    gdp_per_capita,

    CASE
        WHEN gdp_per_capita >= 8000 THEN 'High Income'
        WHEN gdp_per_capita >= 3000 THEN 'Middle Income'
        ELSE 'Low Income'
    END AS income_group

FROM worldbank_data;

SELECT
    country,
    date,
    gdp_billions,

    ROW_NUMBER() OVER(
        PARTITION BY country
        ORDER BY date DESC
    ) AS row_num

FROM worldbank_data;

SELECT *
FROM
(
    SELECT *,
           ROW_NUMBER() OVER(
                PARTITION BY country
                ORDER BY date DESC
           ) AS row_num

    FROM worldbank_data
) t

WHERE row_num = 1;

SELECT *
FROM worldbank_data
WHERE gdp >
(
    SELECT AVG(gdp)
    FROM worldbank_data
);
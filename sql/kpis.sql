-- KPIS ventas totales
SELECT SUM(total_venta) AS ventas_totales
FROM ventas;
-- KPIS ticket promedio
SELECT ROUND(AVG(total_venta), 2) AS ticket_promedio
FROM ventas;
-- KPIS top 5 productos facturados
SELECT producto,
    SUM(total_venta) AS facturacion
FROM ventas
GROUP BY producto
ORDER BY facturacion DESC
LIMIT 5;
-- KPIS facturacion por categoria
SELECT categoria,
    SUM(total_venta) AS facturacion
FROM ventas
GROUP BY categoria
ORDER BY facturacion DESC;
-- KPIS facturacion por canal
SELECT canal,
    SUM(total_venta) AS facturacion
FROM ventas
GROUP BY canal
ORDER BY facturacion DESC;
--KPIS ventas por mes
SELECT strftime('%Y-%m', fecha) as mes,
    SUM(total_venta) AS facturacion
FROM ventas
GROUP BY mes
ORDER BY facturacion DESC;
--KPIS ventas por dia de la semana
SELECT CASE
        strftime('%w', fecha)
        WHEN '0' THEN 'Domingo'
        WHEN '1' THEN 'Lunes'
        WHEN '2' THEN 'Martes'
        WHEN '3' THEN 'Miercoles'
        WHEN '4' THEN 'Jueves'
        WHEN '5' THEN 'Viernes'
        WHEN '6' THEN 'Sábado'
    END as dia_semana,
    SUM(total_venta) AS facturacion
FROM ventas
GROUP BY dia_semana
ORDER BY facturacion DESC;
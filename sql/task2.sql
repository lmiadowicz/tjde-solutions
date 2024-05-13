WITH LatestProperties AS (
    SELECT
        pv.customer_id,
        pv.property_id,
        pv.value,
        p.project_id,
        ROW_NUMBER() OVER (PARTITION BY pv.customer_id, pv.property_id, p.project_id ORDER BY pv.create_dte DESC) AS rn
    FROM project_properties_values pv
    LEFT JOIN project_properties p ON pv.property_id = p.id
),
FilteredProperties AS (
    SELECT
        lp.customer_id,
        lp.project_id,
        p.label AS property_label,
        lp.value
    FROM LatestProperties lp
    LEFT JOIN project_properties p ON lp.property_id = p.id
    WHERE lp.rn = 1
),
PropertiesPivoted AS (
    SELECT
        fp.project_id,
        fp.customer_id,
        MAX(CASE WHEN fp.property_label = 'avg_message_volume' THEN fp.value::INT END) AS avg_message_volume,
        MAX(CASE WHEN fp.property_label = 'estimated_client_volume_usd' THEN fp.value::NUMERIC END) AS estimated_client_volume_usd,
        MAX(CASE WHEN fp.property_label = 'plan' THEN fp.value END) AS plan,
        MAX(CASE WHEN fp.property_label = 'interested_in_product' THEN fp.value END) AS interested_in_product,
        MAX(CASE WHEN fp.property_label = 'customer_email' THEN fp.value END) AS customer_email
    FROM FilteredProperties fp
    GROUP BY fp.project_id, fp.customer_id
)
SELECT
    pp.project_id,
    pp.customer_id,
    pp.customer_email,
    pp.avg_message_volume,
    pp.estimated_client_volume_usd,
    pp.plan,
    pp.interested_in_product
FROM PropertiesPivoted pp
WHERE
    pp.avg_message_volume > 5000 AND
    pp.estimated_client_volume_usd > 1000 AND
    pp.plan = 'free' AND
    pp.interested_in_product = 'yes';

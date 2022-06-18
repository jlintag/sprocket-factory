
DROP TABLE IF EXISTS seed_factory_json;
CREATE TEMP TABLE seed_factory_json (info JSONB);
\COPY seed_factory_json FROM 'src/data/seed_factory_data_no_lines.json';

DROP TABLE IF EXISTS ChartData;
CREATE TABLE ChartData(
    id SERIAL PRIMARY KEY,
    sprocket_production_actual INT[],
    sprocket_production_goal INT[],
    time INT[]
);
CREATE type factory_type AS (factory JSON);
WITH jsontable AS (
   SELECT info::json AS j FROM seed_factory_json
)
INSERT INTO ChartData (sprocket_production_actual, sprocket_production_goal, time)
SELECT 
     ARRAY(SELECT jsonb_array_elements_text(factory::jsonb->'chart_data'->'sprocket_production_actual'))::INT[],
     ARRAY(SELECT jsonb_array_elements_text(factory::jsonb->'chart_data'->'sprocket_production_goal'))::INT[],
     ARRAY(SELECT jsonb_array_elements_text(factory::jsonb->'chart_data'->'time'))::INT[]
FROM jsontable i, 
     json_populate_recordset(null::factory_type, i.j->'factories') t;
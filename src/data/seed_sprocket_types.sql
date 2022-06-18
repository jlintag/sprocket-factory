
DROP TABLE IF EXISTS seed_sprockets_json;
CREATE TEMP TABLE seed_sprockets_json (info JSONB);
\COPY seed_sprockets_json FROM 'src/data/seed_sprocket_types_no_lines.json';

DROP TABLE IF EXISTS Sprockets;
CREATE TABLE Sprockets(
    id SERIAL PRIMARY KEY,
    teeth INT,
    pitch_diameter INT,
    outside_diameter INT,
    pitch INT
);

CREATE type sprocket_type AS (factory JSON);
WITH jsontable AS (
   SELECT info::json AS j FROM seed_sprockets_json
)
INSERT INTO Sprockets (teeth, pitch_diameter, outside_diameter, pitch)
SELECT 
     teeth,
     pitch_diameter,
     outside_diameter,
     pitch
FROM jsontable i, 
     json_populate_recordset(null::Sprockets, i.j->'sprockets') t;
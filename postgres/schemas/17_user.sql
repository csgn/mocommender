CREATE TABLE IF NOT EXISTS MCUser (
	 id						SERIAL			NOT NULL
	,username				VARCHAR(32)		NOT NULL
	,is_active				BOOLEAN			NOT NULL
													DEFAULT FALSE
	
	,PRIMARY KEY (id)
);



CREATE TABLE "Designation" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_text_value TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Identifier" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_text_value TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "InformationResource" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE "Name" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_text_value TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Association" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	subject TEXT NOT NULL, 
	predicate TEXT NOT NULL, 
	object TEXT NOT NULL, 
	negated BOOLEAN, 
	primary_knowledge_source TEXT, 
	aggregator_knowledge_source TEXT, 
	timepoint TIME, 
	type TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "NamedThing" (id), 
	FOREIGN KEY(object) REFERENCES "NamedThing" (id), 
	FOREIGN KEY(primary_knowledge_source) REFERENCES "InformationResource" (id)
);

CREATE TABLE "Designation_identifies" (
	backref_id TEXT, 
	identifies TEXT, 
	PRIMARY KEY (backref_id, identifies), 
	FOREIGN KEY(backref_id) REFERENCES "Designation" (id)
);

CREATE TABLE "Identifier_identifies" (
	backref_id TEXT, 
	identifies TEXT, 
	PRIMARY KEY (backref_id, identifies), 
	FOREIGN KEY(backref_id) REFERENCES "Identifier" (id)
);

CREATE TABLE "Name_identifies" (
	backref_id TEXT, 
	identifies TEXT, 
	PRIMARY KEY (backref_id, identifies), 
	FOREIGN KEY(backref_id) REFERENCES "Name" (id)
);

CREATE TABLE "Attribute" (
	id TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	"Association_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES "NamedThing" (id), 
	FOREIGN KEY("Association_id") REFERENCES "Association" (id)
);

CREATE TABLE "EvidenceType" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	"Association_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Association_id") REFERENCES "Association" (id)
);

CREATE TABLE "Publication" (
	description TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT NOT NULL, 
	summary TEXT, 
	"Association_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Association_id") REFERENCES "Association" (id)
);

CREATE TABLE "Association_qualifiers" (
	backref_id TEXT, 
	qualifiers TEXT, 
	PRIMARY KEY (backref_id, qualifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Association" (id)
);

CREATE TABLE "Association_category" (
	backref_id TEXT, 
	category TEXT, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Association" (id)
);

CREATE TABLE "QuantityValue" (
	has_unit TEXT, 
	has_numeric_value FLOAT, 
	"Attribute_id" TEXT, 
	PRIMARY KEY (has_unit, has_numeric_value, "Attribute_id"), 
	FOREIGN KEY("Attribute_id") REFERENCES "Attribute" (id)
);

CREATE TABLE "Publication_authors" (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_pages" (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_lcsh_terms" (
	backref_id TEXT, 
	lcsh_terms TEXT, 
	PRIMARY KEY (backref_id, lcsh_terms), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

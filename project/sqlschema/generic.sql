

CREATE TABLE "Agent" (
	iri TEXT, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	address TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Article" (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT NOT NULL, 
	summary TEXT, 
	published_in TEXT NOT NULL, 
	iso_abbreviation TEXT, 
	volume TEXT, 
	issue TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE book (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	summary TEXT, 
	id TEXT NOT NULL, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE book_chapter (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT NOT NULL, 
	summary TEXT, 
	published_in TEXT NOT NULL, 
	volume TEXT, 
	chapter TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Boundary" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Component" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Dataset" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE "DatasetDistribution" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	distribution_download_url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DatasetSummary" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	source_web_page TEXT, 
	source_logo TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Designation" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	has_text_value TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Device" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Environment" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Event" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "GeographicLocation" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	latitude FLOAT, 
	longitude FLOAT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Governance" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE "Hardware" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Identifier" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	has_text_value TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "IndividualSystem" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "InformationResource" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE "Instruction" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE "Knowledge" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE "Law" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE "Message" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE "Name" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	has_text_value TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Phenomenon" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "PlanetaryEntity" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Project" (
	iri TEXT, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	address TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "QuantityValue" (
	has_unit TEXT, 
	has_numeric_value FLOAT, 
	PRIMARY KEY (has_unit, has_numeric_value)
);

CREATE TABLE "Regulation" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE "Rule" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE "Serial" (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	name TEXT, 
	summary TEXT, 
	iso_abbreviation TEXT, 
	type TEXT, 
	volume TEXT, 
	issue TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Software" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "System" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	in_taxon TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Association" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
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

CREATE TABLE "Attribute" (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES "NamedThing" (id)
);

CREATE TABLE "BiologicalSex" (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES "NamedThing" (id)
);

CREATE TABLE "ControlRole" (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES "NamedThing" (id)
);

CREATE TABLE "DatasetVersion" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	has_dataset TEXT, 
	ingest_date TEXT, 
	has_distribution TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_dataset) REFERENCES "Dataset" (id), 
	FOREIGN KEY(has_distribution) REFERENCES "DatasetDistribution" (id)
);

CREATE TABLE "SeverityValue" (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES "NamedThing" (id)
);

CREATE TABLE "SystemAttribute" (
	id TEXT NOT NULL, 
	type TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	name TEXT, 
	has_attribute_type TEXT NOT NULL, 
	has_quantitative_value TEXT, 
	has_qualitative_value TEXT, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_qualitative_value) REFERENCES "NamedThing" (id)
);

CREATE TABLE "Agent_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Agent" (id)
);

CREATE TABLE "Agent_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Agent" (id)
);

CREATE TABLE "Agent_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Agent" (id)
);

CREATE TABLE "Agent_affiliation" (
	backref_id TEXT, 
	affiliation TEXT, 
	PRIMARY KEY (backref_id, affiliation), 
	FOREIGN KEY(backref_id) REFERENCES "Agent" (id)
);

CREATE TABLE "Article_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Article" (id)
);

CREATE TABLE "Article_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Article" (id)
);

CREATE TABLE "Article_authors" (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES "Article" (id)
);

CREATE TABLE "Article_pages" (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES "Article" (id)
);

CREATE TABLE "Article_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "Article" (id)
);

CREATE TABLE "Article_lcsh_terms" (
	backref_id TEXT, 
	lcsh_terms TEXT, 
	PRIMARY KEY (backref_id, lcsh_terms), 
	FOREIGN KEY(backref_id) REFERENCES "Article" (id)
);

CREATE TABLE "Article_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Article" (id)
);

CREATE TABLE book_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_authors (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_lcsh_terms (
	backref_id TEXT, 
	lcsh_terms TEXT, 
	PRIMARY KEY (backref_id, lcsh_terms), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES book (id)
);

CREATE TABLE book_chapter_provided_by (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_category (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_authors (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_pages (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_keywords (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_lcsh_terms (
	backref_id TEXT, 
	lcsh_terms TEXT, 
	PRIMARY KEY (backref_id, lcsh_terms), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE book_chapter_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES book_chapter (id)
);

CREATE TABLE "Boundary_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Boundary" (id)
);

CREATE TABLE "Boundary_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Boundary" (id)
);

CREATE TABLE "Boundary_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Boundary" (id)
);

CREATE TABLE "Component_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Component" (id)
);

CREATE TABLE "Component_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Component" (id)
);

CREATE TABLE "Component_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Component" (id)
);

CREATE TABLE "Dataset_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Dataset" (id)
);

CREATE TABLE "Dataset_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Dataset" (id)
);

CREATE TABLE "Dataset_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Dataset" (id)
);

CREATE TABLE "DatasetDistribution_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "DatasetDistribution" (id)
);

CREATE TABLE "DatasetDistribution_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "DatasetDistribution" (id)
);

CREATE TABLE "DatasetDistribution_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "DatasetDistribution" (id)
);

CREATE TABLE "DatasetSummary_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "DatasetSummary" (id)
);

CREATE TABLE "DatasetSummary_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "DatasetSummary" (id)
);

CREATE TABLE "DatasetSummary_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "DatasetSummary" (id)
);

CREATE TABLE "Designation_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Designation" (id)
);

CREATE TABLE "Designation_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Designation" (id)
);

CREATE TABLE "Designation_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Designation" (id)
);

CREATE TABLE "Designation_identifies" (
	backref_id TEXT, 
	identifies TEXT, 
	PRIMARY KEY (backref_id, identifies), 
	FOREIGN KEY(backref_id) REFERENCES "Designation" (id)
);

CREATE TABLE "Device_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Device" (id)
);

CREATE TABLE "Device_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Device" (id)
);

CREATE TABLE "Device_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Device" (id)
);

CREATE TABLE "Environment_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Environment" (id)
);

CREATE TABLE "Environment_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Environment" (id)
);

CREATE TABLE "Environment_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Environment" (id)
);

CREATE TABLE "Event_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Event" (id)
);

CREATE TABLE "Event_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Event" (id)
);

CREATE TABLE "Event_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Event" (id)
);

CREATE TABLE "GeographicLocation_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "GeographicLocation" (id)
);

CREATE TABLE "GeographicLocation_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "GeographicLocation" (id)
);

CREATE TABLE "GeographicLocation_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "GeographicLocation" (id)
);

CREATE TABLE "Governance_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Governance" (id)
);

CREATE TABLE "Governance_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Governance" (id)
);

CREATE TABLE "Governance_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Governance" (id)
);

CREATE TABLE "Hardware_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Hardware" (id)
);

CREATE TABLE "Hardware_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Hardware" (id)
);

CREATE TABLE "Hardware_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Hardware" (id)
);

CREATE TABLE "Identifier_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Identifier" (id)
);

CREATE TABLE "Identifier_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Identifier" (id)
);

CREATE TABLE "Identifier_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Identifier" (id)
);

CREATE TABLE "Identifier_identifies" (
	backref_id TEXT, 
	identifies TEXT, 
	PRIMARY KEY (backref_id, identifies), 
	FOREIGN KEY(backref_id) REFERENCES "Identifier" (id)
);

CREATE TABLE "IndividualSystem_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "IndividualSystem" (id)
);

CREATE TABLE "IndividualSystem_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "IndividualSystem" (id)
);

CREATE TABLE "IndividualSystem_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "IndividualSystem" (id)
);

CREATE TABLE "InformationResource_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "InformationResource" (id)
);

CREATE TABLE "InformationResource_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "InformationResource" (id)
);

CREATE TABLE "InformationResource_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "InformationResource" (id)
);

CREATE TABLE "Instruction_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Instruction" (id)
);

CREATE TABLE "Instruction_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Instruction" (id)
);

CREATE TABLE "Instruction_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Instruction" (id)
);

CREATE TABLE "Knowledge_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Knowledge" (id)
);

CREATE TABLE "Knowledge_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Knowledge" (id)
);

CREATE TABLE "Knowledge_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Knowledge" (id)
);

CREATE TABLE "Law_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Law" (id)
);

CREATE TABLE "Law_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Law" (id)
);

CREATE TABLE "Law_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Law" (id)
);

CREATE TABLE "Message_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Message" (id)
);

CREATE TABLE "Message_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Message" (id)
);

CREATE TABLE "Message_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Message" (id)
);

CREATE TABLE "Name_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Name" (id)
);

CREATE TABLE "Name_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Name" (id)
);

CREATE TABLE "Name_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Name" (id)
);

CREATE TABLE "Name_identifies" (
	backref_id TEXT, 
	identifies TEXT, 
	PRIMARY KEY (backref_id, identifies), 
	FOREIGN KEY(backref_id) REFERENCES "Name" (id)
);

CREATE TABLE "NamedThing_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "NamedThing" (id)
);

CREATE TABLE "NamedThing_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "NamedThing" (id)
);

CREATE TABLE "NamedThing_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "NamedThing" (id)
);

CREATE TABLE "Phenomenon_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Phenomenon" (id)
);

CREATE TABLE "Phenomenon_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Phenomenon" (id)
);

CREATE TABLE "Phenomenon_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Phenomenon" (id)
);

CREATE TABLE "PlanetaryEntity_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "PlanetaryEntity" (id)
);

CREATE TABLE "PlanetaryEntity_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "PlanetaryEntity" (id)
);

CREATE TABLE "PlanetaryEntity_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "PlanetaryEntity" (id)
);

CREATE TABLE "Project_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Project" (id)
);

CREATE TABLE "Project_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Project" (id)
);

CREATE TABLE "Project_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Project" (id)
);

CREATE TABLE "Project_affiliation" (
	backref_id TEXT, 
	affiliation TEXT, 
	PRIMARY KEY (backref_id, affiliation), 
	FOREIGN KEY(backref_id) REFERENCES "Project" (id)
);

CREATE TABLE "Regulation_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Regulation" (id)
);

CREATE TABLE "Regulation_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Regulation" (id)
);

CREATE TABLE "Regulation_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Regulation" (id)
);

CREATE TABLE "Rule_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Rule" (id)
);

CREATE TABLE "Rule_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Rule" (id)
);

CREATE TABLE "Rule_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Rule" (id)
);

CREATE TABLE "Serial_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Serial" (id)
);

CREATE TABLE "Serial_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Serial" (id)
);

CREATE TABLE "Serial_authors" (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES "Serial" (id)
);

CREATE TABLE "Serial_pages" (
	backref_id TEXT, 
	pages TEXT, 
	PRIMARY KEY (backref_id, pages), 
	FOREIGN KEY(backref_id) REFERENCES "Serial" (id)
);

CREATE TABLE "Serial_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "Serial" (id)
);

CREATE TABLE "Serial_lcsh_terms" (
	backref_id TEXT, 
	lcsh_terms TEXT, 
	PRIMARY KEY (backref_id, lcsh_terms), 
	FOREIGN KEY(backref_id) REFERENCES "Serial" (id)
);

CREATE TABLE "Serial_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Serial" (id)
);

CREATE TABLE "Software_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Software" (id)
);

CREATE TABLE "Software_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Software" (id)
);

CREATE TABLE "Software_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Software" (id)
);

CREATE TABLE "System_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "System" (id)
);

CREATE TABLE "System_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "System" (id)
);

CREATE TABLE "System_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "System" (id)
);

CREATE TABLE "EvidenceType" (
	id TEXT NOT NULL, 
	iri TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	license TEXT, 
	rights TEXT, 
	format TEXT, 
	creation_date DATE, 
	"Association_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Association_id") REFERENCES "Association" (id)
);

CREATE TABLE "Publication" (
	iri TEXT, 
	description TEXT, 
	has_attribute TEXT, 
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

CREATE TABLE "Attribute_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Attribute" (id)
);

CREATE TABLE "Attribute_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "Attribute" (id)
);

CREATE TABLE "Attribute_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Attribute" (id)
);

CREATE TABLE "BiologicalSex_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "BiologicalSex" (id)
);

CREATE TABLE "BiologicalSex_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "BiologicalSex" (id)
);

CREATE TABLE "BiologicalSex_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "BiologicalSex" (id)
);

CREATE TABLE "ControlRole_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "ControlRole" (id)
);

CREATE TABLE "ControlRole_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "ControlRole" (id)
);

CREATE TABLE "ControlRole_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "ControlRole" (id)
);

CREATE TABLE "DatasetVersion_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "DatasetVersion" (id)
);

CREATE TABLE "DatasetVersion_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "DatasetVersion" (id)
);

CREATE TABLE "DatasetVersion_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "DatasetVersion" (id)
);

CREATE TABLE "SeverityValue_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "SeverityValue" (id)
);

CREATE TABLE "SeverityValue_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "SeverityValue" (id)
);

CREATE TABLE "SeverityValue_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "SeverityValue" (id)
);

CREATE TABLE "SystemAttribute_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "SystemAttribute" (id)
);

CREATE TABLE "SystemAttribute_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "SystemAttribute" (id)
);

CREATE TABLE "SystemAttribute_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "SystemAttribute" (id)
);

CREATE TABLE "EvidenceType_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "EvidenceType" (id)
);

CREATE TABLE "EvidenceType_xref" (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "EvidenceType" (id)
);

CREATE TABLE "EvidenceType_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "EvidenceType" (id)
);

CREATE TABLE "Publication_provided_by" (
	backref_id TEXT, 
	provided_by TEXT, 
	PRIMARY KEY (backref_id, provided_by), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
);

CREATE TABLE "Publication_category" (
	backref_id TEXT, 
	category TEXT NOT NULL, 
	PRIMARY KEY (backref_id, category), 
	FOREIGN KEY(backref_id) REFERENCES "Publication" (id)
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

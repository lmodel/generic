export type OntologyClassId = string;
export type AttributeId = string;
export type ControlRoleId = string;
export type BiologicalSexId = string;
export type SeverityValueId = string;
export type EntityId = string;
export type NamedThingId = string;
export type DesignationId = string;
export type NameId = string;
export type IdentifierId = string;
export type EventId = string;
export type AdministrativeEntityId = string;
export type AgentId = string;
export type ProjectId = string;
export type InformationContentEntityId = string;
export type SpecificationId = string;
export type DatasetId = string;
export type DatasetDistributionId = string;
export type DatasetVersionId = string;
export type DatasetSummaryId = string;
export type EvidenceTypeId = string;
export type InformationResourceId = string;
export type OpenAccessId = string;
export type PublicationId = string;
export type BookId = string;
export type BookChapterId = string;
export type SerialId = string;
export type ArticleId = string;
export type PhenomenonId = string;
export type DeviceId = string;
export type SoftwareOrDeviceId = string;
export type SoftwareId = string;
export type HardwareId = string;
export type PlanetaryEntityId = string;
export type GeographicLocationId = string;
export type SystemId = string;
export type OperationalEntityId = string;
export type IndividualSystemId = string;
export type SystemAttributeId = string;
export type EnvironmentId = string;
export type ComponentId = string;
export type MessageId = string;
export type RuleId = string;
export type InstructionId = string;
export type LawId = string;
export type RegulationId = string;
export type GovernanceId = string;
export type BoundaryId = string;
export type KnowledgeId = string;
export type AssociationId = string;


/**
 * linkml:Any type is an experimental feature for allowing arbitrary objects
 */
export interface MetaObject {
};
/**
 * a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a base compatible KG can be considered both instances of base classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate base class.
 */
export interface OntologyClass {
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
};
/**
 * Generic Model root class for entity annotations.
 */
export interface Annotation {
};
/**
 * A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
 */
export interface QuantityValue extends Annotation {
    /** connects a quantity value to a unit */
    has_unit?: string,
    /** connects a quantity value to a number */
    has_numeric_value?: number,
};
/**
 * A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
 */
export interface Attribute extends NamedThing, OntologyClass {
    /** The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term. */
    name?: string,
    /** connects an attribute to a class that describes it */
    has_attribute_type: OntologyClassId,
    /** connects an attribute to a value */
    has_quantitative_value?: QuantityValue[],
    /** connects an attribute to a value */
    has_qualitative_value?: NamedThingId,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * A role played by the entity or part thereof within a control context.
 */
export interface ControlRole extends Attribute {
    /** The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term. */
    name?: string,
    /** connects an attribute to a class that describes it */
    has_attribute_type: OntologyClassId,
    /** connects an attribute to a value */
    has_quantitative_value?: QuantityValue[],
    /** connects an attribute to a value */
    has_qualitative_value?: NamedThingId,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * Status as female, male, or intersex depending on their chromosomes, reproductive organs, and other characteristics
 */
export interface BiologicalSex extends Attribute {
    /** The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term. */
    name?: string,
    /** connects an attribute to a class that describes it */
    has_attribute_type: OntologyClassId,
    /** connects an attribute to a value */
    has_quantitative_value?: QuantityValue[],
    /** connects an attribute to a value */
    has_qualitative_value?: NamedThingId,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * describes the severity of a observable feature or fault
 */
export interface SeverityValue extends Attribute {
    /** The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term. */
    name?: string,
    /** connects an attribute to a class that describes it */
    has_attribute_type: OntologyClassId,
    /** connects an attribute to a value */
    has_quantitative_value?: QuantityValue[],
    /** connects an attribute to a value */
    has_qualitative_value?: NamedThingId,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * Root Generic Model class for all things and informational relationships, real or imagined.
 */
export interface Entity {
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category?: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * a databased entity or concept/class
 */
export interface NamedThing extends Entity {
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * representation for someone or something by a sign that denotes it
 */
export interface Designation extends NamedThing {
    /** connects some information to a string */
    has_text_value?: string,
    /** a relationship that identifies, or serves as a sign, for something */
    identifies?: InformationContentEntityId[],
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * distinctive designation for an individual (person, organization or thing)
 */
export interface Name extends Designation {
    /** connects some information to a string */
    has_text_value?: string,
    /** a relationship that identifies, or serves as a sign, for something */
    identifies?: InformationContentEntityId[],
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * Sequence of characters uniquely identifying that with which it is associated
 */
export interface Identifier extends Designation {
    /** connects some information to a string */
    has_text_value?: string,
    /** a relationship that identifies, or serves as a sign, for something */
    identifies?: InformationContentEntityId[],
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * Something that happens at a given place and time.
 */
export interface Event extends NamedThing {
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * Entity responsible for managing the affairs of an organization
 */
export interface AdministrativeEntity extends NamedThing {
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * person, group, organization or project that provides a piece of information (i.e. a knowledge association)
 */
export interface Agent extends AdministrativeEntity {
    /** a professional relationship between one provider (x) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations. */
    affiliation?: string[],
    /** the particulars of the place where someone or an organization is situated. For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?). */
    address?: string,
    /** Different classes of agents have distinct preferred identifiers.  For publishers, use the ISBN publisher code.  See https://grp.isbn-international.org/ for publisher code lookups.  For editors, authors and  individual providers, use the individual's ORCID if available; Otherwise, a ScopusID, publons.researcher or Google Scholar ID ('GSID') may be used if the author ORCID is unknown. Institutional agents could be identified by an International Standard Name Identifier ('ISNI') code. */
    id: string,
    /** it is recommended that an author's 'name' property be formatted as "surname, firstname initial." */
    name?: string,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * collaborative enterprise, frequently involving research or design, that is carefully planned to achieve a particular aim
 */
export interface Project extends Agent {
    /** a professional relationship between one provider (x) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations. */
    affiliation?: string[],
    /** the particulars of the place where someone or an organization is situated. For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?). */
    address?: string,
    /** Different classes of agents have distinct preferred identifiers.  For publishers, use the ISBN publisher code.  See https://grp.isbn-international.org/ for publisher code lookups.  For editors, authors and  individual providers, use the individual's ORCID if available; Otherwise, a ScopusID, publons.researcher or Google Scholar ID ('GSID') may be used if the author ORCID is unknown. Institutional agents could be identified by an International Standard Name Identifier ('ISNI') code. */
    id: string,
    /** it is recommended that an author's 'name' property be formatted as "surname, firstname initial." */
    name?: string,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * a piece of information that typically describes some topic of discourse or is used as support.
 */
export interface InformationContentEntity extends NamedThing {
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * A detailed description of criteria for a piece of work.
 */
export interface Specification extends InformationContentEntity {
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * an item that refers to a collection of data from a data source.
 */
export interface Dataset extends InformationContentEntity {
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * an item that holds distribution level information about a dataset
 */
export interface DatasetDistribution extends InformationContentEntity {
    /** Identifier pointing to Internet location used to distribute of digital assets */
    distribution_download_url?: string,
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * an item that holds version level information about a dataset.
 */
export interface DatasetVersion extends InformationContentEntity {
    /** Entity has a dataset */
    has_dataset?: DatasetId,
    /** Date when dataset version was ingested */
    ingest_date?: string,
    /** Dataset version has distribution */
    has_distribution?: DatasetDistributionId,
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * an item that holds summary level information about a dataset.
 */
export interface DatasetSummary extends InformationContentEntity {
    /** A web page with specific collection of information provided by a website and displayed to a user in a web browser, with Dataset summary. */
    source_web_page?: string,
    /** A graphic mark or emblem associated with Web page for Dataset distribution */
    source_logo?: string,
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * Class of evidence that supports an association
 */
export interface EvidenceType extends InformationContentEntity {
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * A database or knowledgebase and its supporting ecosystem of interfaces and services that deliver content to consumers (e.g. web portals, APIs, query endpoints, streaming services, data downloads, etc.).  A single Information Resource by this definition may span many different datasets or databases, and include many access endpoints and user interfaces. Information Resources include project-specific resources such as a Translator Knowledge Provider, and community knowledgebases.
 */
export interface InformationResource extends InformationContentEntity {
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * Free distribution of knowledge
 */
export interface OpenAccess extends NamedThing {
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Generic category subclasses.
 */
export interface Publication extends InformationContentEntity {
    /** connects an publication to the list of authors who contributed to the publication.  This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".  Note that this property is a node annotation voicing the citation list of authorship which might typically otherwise be more completely documented in generic:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication. */
    authors?: string[],
    /** Different kinds of publication subtypes will have different preferred identifiers (curies when feasible). Precedence of identifiers for scientific articles is as follows PMID if available; DOI if not; actual alternate CURIE otherwise. Enclosing publications (i.e. referenced by 'published in' node property) such as books and journals, should have industry-standard identifier such as from ISBN and ISSN. */
    id: string,
    /** the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing). The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case). */
    name?: string,
    /** Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.WIKIDATA.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of generic:category generic:OntologyClass. */
    type: string,
    /** When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book. */
    pages?: string[],
    /** executive summary of a resource or publication */
    summary?: string,
    /** keywords tagging a publication */
    keywords?: string[],
    /** Library of Congress Subject Headings (lcsh) terms tagging a publication */
    lcsh_terms?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
 */
export interface Book extends Publication {
    /** connects an publication to the list of authors who contributed to the publication.  This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".  Note that this property is a node annotation voicing the citation list of authorship which might typically otherwise be more completely documented in generic:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication. */
    authors?: string[],
    /** Books should have industry-standard identifier such as from ISBN. */
    id: string,
    /** the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing). The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case). */
    name?: string,
    /** Should generally be set to an OntologyClass defined term for 'book'. */
    type: string,
    /** When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book. */
    pages?: string[],
    /** executive summary of a resource or publication */
    summary?: string,
    /** keywords tagging a publication */
    keywords?: string[],
    /** Library of Congress Subject Headings (lcsh) terms tagging a publication */
    lcsh_terms?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};

export interface BookChapter extends Publication {
    /** The enclosing parent book containing the chapter should have industry-standard identifier from ISBN. */
    published_in: string,
    /** volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication */
    volume?: string,
    /** chapter of a book */
    chapter?: string,
    /** connects an publication to the list of authors who contributed to the publication.  This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".  Note that this property is a node annotation voicing the citation list of authorship which might typically otherwise be more completely documented in generic:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication. */
    authors?: string[],
    /** Different kinds of publication subtypes will have different preferred identifiers (curies when feasible). Precedence of identifiers for scientific articles is as follows PMID if available; DOI if not; actual alternate CURIE otherwise. Enclosing publications (i.e. referenced by 'published in' node property) such as books and journals, should have industry-standard identifier such as from ISBN and ISSN. */
    id: string,
    /** the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing). The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case). */
    name?: string,
    /** Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.WIKIDATA.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of generic:category generic:OntologyClass. */
    type: string,
    /** When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book. */
    pages?: string[],
    /** executive summary of a resource or publication */
    summary?: string,
    /** keywords tagging a publication */
    keywords?: string[],
    /** Library of Congress Subject Headings (lcsh) terms tagging a publication */
    lcsh_terms?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
 */
export interface Serial extends Publication {
    /** Standard abbreviation for periodicals in the International Organization for Standardization (ISO) 4 system See https://www.issn.org/services/online-services/access-to-the-ltwa/. If the 'published in' property is set, then the iso abbreviation pertains to the broader publication context (the journal) within which the given publication node is embedded, not the publication itself. */
    iso_abbreviation?: string,
    /** Should generally be set to an OntologyClass defined term for 'serial' or 'journal'. */
    type: string,
    /** volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication */
    volume?: string,
    /** issue of a newspaper, a scientific journal or magazine for reference purpose */
    issue?: string,
    /** connects an publication to the list of authors who contributed to the publication.  This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".  Note that this property is a node annotation voicing the citation list of authorship which might typically otherwise be more completely documented in generic:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication. */
    authors?: string[],
    /** Serials (journals) should have industry-standard identifier such as from ISSN. */
    id: string,
    /** the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing). The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case). */
    name?: string,
    /** When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book. */
    pages?: string[],
    /** executive summary of a resource or publication */
    summary?: string,
    /** keywords tagging a publication */
    keywords?: string[],
    /** Library of Congress Subject Headings (lcsh) terms tagging a publication */
    lcsh_terms?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * A written composition in prose, usually nonfiction, on a specific topic, forming an independent part of a book or other publication
 */
export interface Article extends Publication {
    /** The enclosing parent serial containing the article should have industry-standard identifier from ISSN. */
    published_in: string,
    /** Optional value, if used locally as a convenience, is set to the iso abbreviation of the 'published in' parent. */
    iso_abbreviation?: string,
    /** volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication */
    volume?: string,
    /** issue of a newspaper, a scientific journal or magazine for reference purpose */
    issue?: string,
    /** connects an publication to the list of authors who contributed to the publication.  This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".  Note that this property is a node annotation voicing the citation list of authorship which might typically otherwise be more completely documented in generic:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication. */
    authors?: string[],
    /** Different kinds of publication subtypes will have different preferred identifiers (curies when feasible). Precedence of identifiers for scientific articles is as follows PMID if available; DOI if not; actual alternate CURIE otherwise. Enclosing publications (i.e. referenced by 'published in' node property) such as books and journals, should have industry-standard identifier such as from ISBN and ISSN. */
    id: string,
    /** the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing). The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case). */
    name?: string,
    /** Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.WIKIDATA.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of generic:category generic:OntologyClass. */
    type: string,
    /** When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book. */
    pages?: string[],
    /** executive summary of a resource or publication */
    summary?: string,
    /** keywords tagging a publication */
    keywords?: string[],
    /** Library of Congress Subject Headings (lcsh) terms tagging a publication */
    lcsh_terms?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * Either a physical or processual entity.
 */
export interface TangibleEssenceOrOccurrent {
};
/**
 * Semantic mixin concept. Pertains to entities that have tangible properties such as mass, volume, or charge.
 */
export interface TangibleEssence extends TangibleEssenceOrOccurrent {
};
/**
 * A processual entity that has temporal parts and happens, unfolds or develops through time. Occurrents have phases. generic:Occurrent is most consistently used as a mixin thus it should be declared as such and cannot inherit from the non-mixin generic:NamedThing
 */
export interface Occurrent extends TangibleEssenceOrOccurrent {
};
/**
 * a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
 */
export interface Phenomenon extends NamedThing, Occurrent {
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment.
 */
export interface Device extends System {
    /** connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon' */
    in_taxon?: NamedThingId[],
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * Either software or hardware
 */
export interface SoftwareOrDevice extends System {
    /** connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon' */
    in_taxon?: NamedThingId[],
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * A set of instructions in a computer programming language that can be executed by a computer, possibly after compilation into another programming language. The term Software includes ComputerPrograms (free-standing software), object methods, subroutines and software packages.
 */
export interface Software extends SoftwareOrDevice {
    /** connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon' */
    in_taxon?: NamedThingId[],
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * physical components of a computer
 */
export interface Hardware extends SoftwareOrDevice {
    /** connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon' */
    in_taxon?: NamedThingId[],
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * An entity that has the role of being studied in an investigation, study, or experiment
 */
export interface SubjectOfInvestigation {
};
/**
 * Any entity or process that exists at the level of the whole planet
 */
export interface PlanetaryEntity extends NamedThing {
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * a location that can be described in lat/long coordinates
 */
export interface GeographicLocation extends PlanetaryEntity {
    /** latitude */
    latitude?: number,
    /** longitude */
    longitude?: number,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * An entity that intends to perform some functions, interacting with other systems. Relative to a given system, the entities with which it interacts, are considered its environment. A system is structurally composed of a set of components bound together.
 */
export interface System extends NamedThing, ThingWithTaxon {
    /** connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon' */
    in_taxon?: NamedThingId[],
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * A mixin that can be used on any entity that can be taxonomically classified. This includes individual entities, their products, and other operational entities and processes.
 */
export interface ThingWithTaxon {
    /** connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon' */
    in_taxon?: NamedThingId[],
};
/**
 * A operational entity is a control entity
 */
export interface OperationalEntity extends System {
    /** indicates whether a desired state is a controller */
    is_controller?: boolean,
    /** connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon' */
    in_taxon?: NamedThingId[],
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * An instance of an system. For example, human. Computer, my pet cat.
 */
export interface IndividualSystem extends System {
    /** connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon' */
    in_taxon?: NamedThingId[],
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * describes a characteristic of an SystemEntity.
 */
export interface SystemAttribute extends Attribute {
    /** The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term. */
    name?: string,
    /** connects an attribute to a class that describes it */
    has_attribute_type: OntologyClassId,
    /** connects an attribute to a value */
    has_quantitative_value?: QuantityValue[],
    /** connects an attribute to a value */
    has_qualitative_value?: NamedThingId,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * Part of the universe outside the boundaries of a given system, interacting with that given system.
 */
export interface Environment extends System {
    /** connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon' */
    in_taxon?: NamedThingId[],
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * The component is the smallest system entity that can be deployed, isolated, and restored independently. A self-contained assembly of parts within a complete operating unit or module, which cannot be further subdivided without loss of identity or function. The compoent is part of a system structurally composed of a set of components bound together. Each component is another system and this recursive definition stops when a component is regarded as atomic."
 */
export interface Component extends System {
    /** connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'ThingWithTaxon' */
    in_taxon?: NamedThingId[],
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * discrete unit of communication intended by the source for consumption by some recipient or group of recipients
 */
export interface Message extends InformationContentEntity {
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * prescription, including laws, regulations, instructions, guidelines, and social conventions; determinate method for performing any operation
 */
export interface Rule extends Message {
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * message intended to convey a course of action for the audience to follow
 */
export interface Instruction extends Message {
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * system of rules and guidelines, generally backed by governmental authority
 */
export interface Law extends Rule {
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * general term for rules or controls, including delegated legislation and self-regulation within an organisation
 */
export interface Regulation extends Rule {
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * all of the processes of governing, whether undertaken by a government, market or network, whether over a family, tribe, formal or informal organization or territory and whether through the laws, norms, power or language of an organized society
 */
export interface Governance extends Regulation {
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * dividing line between two areas or sets of points in a topological space; difference between the closure and the interior
 */
export interface Boundary extends NamedThing {
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * A set of knowledge or reproducible skills acquired through study or experience.
 */
export interface Knowledge extends InformationResource {
    /** legal document giving official permission to do something with the resource */
    license?: string,
    /** provides information about rights held in and over the resource */
    rights?: string,
    /** arrangement of data for presentation */
    format?: string,
    /** date on which an entity was created. This can be applied to nodes or edges */
    creation_date?: date,
    /** The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph. */
    provided_by?: string[],
    /** Alternate CURIEs for a thing */
    xref?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category: string[],
    /** Clasification of an entity, or anchoring point (of a name) in taxonomy */
    type?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};
/**
 * An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of various categories of possible biological or non-biological (e.g. clinical) outcomes
 */
export interface Outcome {
};
/**
 * A typed association between two entities, supported by evidence
 */
export interface Association extends Entity {
    /** connects an association to the subject of the association. For example, in a class-to-observable feature association, the class is subject and observable feature is object. */
    subject: NamedThingId,
    /** A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes. */
    predicate: string,
    /** connects an association to the object of the association. For example, in a class-to-observable feature association, the class is subject and observable feature is object. */
    object: NamedThingId,
    /** if set to true, then the association is negated i.e. is not true */
    negated?: boolean,
    /** connects an association to qualifiers that modify or qualify the meaning of that association */
    qualifiers?: OntologyClassId[],
    /** One or more publications that report the statement expressed in an Association, or provide information used as evidence supporting this statement. */
    publications?: PublicationId[],
    /** connects an association to an instance of supporting evidence */
    has_evidence?: EvidenceTypeId[],
    /** The most upstream source of the knowledge expressed in an Association that can be identified. Performing a rigorous analysis of upstream data providers is expected; every effort is made to catalog the most upstream source of data in this property.  Only one data source should be declared primary in any association.  "aggregator knowledge source" can be used to capture non-primary sources. */
    primary_knowledge_source?: InformationResourceId,
    /** An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form. */
    aggregator_knowledge_source?: InformationResourceId[],
    /** a point in time */
    timepoint?: string,
    /** rdf:type of generic:Association should be fixed at rdf:Statement */
    type?: string,
    /** Name of the high level OntologyClass in which this entity is categorized. Corresponds to the label for the base entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a generic-model class URI.
This field is multi-valued. It should include values for ancestors of the generic-model class
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific base class, or potentially to a class more specific than something in base. */
    category?: string[],
    /** A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI */
    id: string,
    /** An IRI for an entity. This is determined by the id using expansion rules. */
    iri?: string,
    /** A human-readable name for an attribute or entity. */
    name?: string,
    /** a human-readable description of an entity */
    description?: string,
    /** connects any entity to an attribute */
    has_attribute?: AttributeId[],
};


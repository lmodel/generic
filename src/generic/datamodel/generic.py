# Auto generated from generic.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-07-09T19:08:59
# Schema: generic
#
# id: https://w3id.org/lmodel/generic
# description: Entity and association taxonomy and datamodel for generic data
# license: Apache Software License 2.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Double, String, Time, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
BTO = CurieNamespace('BTO', 'http://purl.obolibrary.org/obo/BTO_')
CDAO = CurieNamespace('CDAO', 'http://purl.obolibrary.org/obo/CDAO_')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
ERO = CurieNamespace('ERO', 'http://purl.obolibrary.org/obo/ERO_')
GR = CurieNamespace('GR', 'http://purl.org/goodrelations/v1#')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
INO = CurieNamespace('INO', 'http://purl.obolibrary.org/obo/INO_')
LOINC = CurieNamespace('LOINC', 'http://loinc.org/rdf/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBAN = CurieNamespace('OBAN', 'http://purl.org/oban/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
SAN = CurieNamespace('SAN', 'https://www.irit.fr/recherches/MELODI/ontologies/SAN.html#')
SIO = CurieNamespace('SIO', 'http://identifiers.org/sio/')
SWO = CurieNamespace('SWO', 'http://purl.obolibrary.org/obo/SWO_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.WIKIDATA.org/wiki/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.WIKIDATA.org/wiki/Property:')
XAPI = CurieNamespace('XAPI', 'http://ns.inria.fr/ludo/v1/docs/xapi.html#')
AML = CurieNamespace('aml', 'https://w3id.org/i40/aml#')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term/')
CTRL = CurieNamespace('ctrl', 'https://w3id.org/ibp/CTRLont#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
DWC = CurieNamespace('dwc', 'http://rs.tdwg.org/dwc/terms/')
EDAM = CurieNamespace('edam', 'http://identifiers.org/edam/')
EDAM_DATA = CurieNamespace('edam_data', 'http://edamontology.org/data_')
EDAM_FORMAT = CurieNamespace('edam_format', 'http://edamontology.org/format_')
EDAM_OPERATION = CurieNamespace('edam_operation', 'http://edamontology.org/operation_')
EDAM_TOPIC = CurieNamespace('edam_topic', 'http://edamontology.org/topic_')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
GEOLINK = CurieNamespace('geolink', 'http://schema.geolink.org/1.0/base/main.html#')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
GVP = CurieNamespace('gvp', 'http://vocab.getty.edu/ontology#')
LCSH = CurieNamespace('lcsh', 'http://id.loc.gov/authorities/subjects/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RR = CurieNamespace('rr', 'http://www.w3.org/ns/r2rml#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'http://www.w3.org/ns/ssn/')
SSN_SYSTEM = CurieNamespace('ssn-system', 'http://www.w3.org/ns/ssn/systems/')
SUMO = CurieNamespace('sumo', 'https://w3id.org/sumo/kb/')
UBERON = CurieNamespace('uberon', 'http://purl.obolibrary.org/obo/UBERON_')
UCO = CurieNamespace('uco', 'https://w3id.org/lmodel/uco-master')
UCS_LANDSCAPE = CurieNamespace('ucs_landscape', 'https://w3id.org/lmodel/generic/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = UCS_LANDSCAPE


# Types
class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the generic model.  The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the generic class, for example generic:Service. For an RDF representation, the value should be a URI such as https://w3id.org/lmodel/base/vocab/Service """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "category type"
    type_model_uri = UCS_LANDSCAPE.CategoryType


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = UCS_LANDSCAPE.IriType


class LabelType(String):
    """ A string that provides a human-readable name for an entity """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = UCS_LANDSCAPE.LabelType


class PredicateType(Uriorcurie):
    """ A CURIE from the generic related_to hierarchy. For example, generic:related_to """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "predicate type"
    type_model_uri = UCS_LANDSCAPE.PredicateType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = UCS_LANDSCAPE.NarrativeText


class Unit(String):
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit"
    type_model_uri = UCS_LANDSCAPE.Unit


class TimeType(Time):
    type_class_uri = XSD.time
    type_class_curie = "xsd:time"
    type_name = "time type"
    type_model_uri = UCS_LANDSCAPE.TimeType


# Class references
class OntologyClassId(extended_str):
    pass


class EntityId(extended_str):
    pass


class NamedThingId(extended_str):
    pass


class AttributeId(NamedThingId):
    pass


class DesignationId(NamedThingId):
    pass


class NameId(DesignationId):
    pass


class IdentifierId(DesignationId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class InformationResourceId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class AssociationId(EntityId):
    pass


@dataclass
class OntologyClass(YAMLRoot):
    """
    a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a base compatible KG can be
    considered both instances of base classes, and OWL classes in their own right. In general you should not need to
    use this class directly. Instead, use the appropriate base class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.OntologyClass
    class_class_curie: ClassVar[str] = "ucs_landscape:OntologyClass"
    class_name: ClassVar[str] = "OntologyClass"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.OntologyClass

    id: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)


class Annotation(YAMLRoot):
    """
    Generic Model root class for entity annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Annotation
    class_class_curie: ClassVar[str] = "ucs_landscape:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Annotation


@dataclass
class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.QuantityValue
    class_class_curie: ClassVar[str] = "ucs_landscape:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.QuantityValue

    has_unit: Optional[Union[str, Unit]] = None
    has_numeric_value: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_unit is not None and not isinstance(self.has_unit, Unit):
            self.has_unit = Unit(self.has_unit)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        super().__post_init__(**kwargs)


@dataclass
class Entity(YAMLRoot):
    """
    Root Generic Model class for all things and informational relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Entity
    class_class_curie: ClassVar[str] = "ucs_landscape:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Entity

    id: Union[str, EntityId] = None
    iri: Optional[Union[str, IriType]] = None
    category: Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]] = empty_list()
    type: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None
    has_attribute: Optional[Union[Union[str, AttributeId], List[Union[str, AttributeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, AttributeId) else AttributeId(v) for v in self.has_attribute]

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[Union[str, LabelType]] = None
    description: Optional[Union[str, NarrativeText]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if self.description is not None and not isinstance(self.description, NarrativeText):
            self.description = NarrativeText(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Attribute(NamedThing):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Attribute
    class_class_curie: ClassVar[str] = "ucs_landscape:Attribute"
    class_name: ClassVar[str] = "Attribute"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Attribute

    id: Union[str, AttributeId] = None
    has_attribute_type: Union[str, OntologyClassId] = None
    name: Optional[Union[str, LabelType]] = None
    has_quantitative_value: Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]] = empty_list()
    has_qualitative_value: Optional[Union[str, NamedThingId]] = None
    iri: Optional[Union[str, IriType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)

        if self._is_empty(self.has_attribute_type):
            self.MissingRequiredField("has_attribute_type")
        if not isinstance(self.has_attribute_type, OntologyClassId):
            self.has_attribute_type = OntologyClassId(self.has_attribute_type)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.has_quantitative_value, list):
            self.has_quantitative_value = [self.has_quantitative_value] if self.has_quantitative_value is not None else []
        self.has_quantitative_value = [v if isinstance(v, QuantityValue) else QuantityValue(**as_dict(v)) for v in self.has_quantitative_value]

        if self.has_qualitative_value is not None and not isinstance(self.has_qualitative_value, NamedThingId):
            self.has_qualitative_value = NamedThingId(self.has_qualitative_value)

        if self.iri is not None and not isinstance(self.iri, IriType):
            self.iri = IriType(self.iri)

        super().__post_init__(**kwargs)


@dataclass
class Designation(NamedThing):
    """
    representation for someone or something by a sign that denotes it
    """
    _inherited_slots: ClassVar[List[str]] = ["identifies"]

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Designation
    class_class_curie: ClassVar[str] = "ucs_landscape:Designation"
    class_name: ClassVar[str] = "Designation"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Designation

    id: Union[str, DesignationId] = None
    has_text_value: Optional[str] = None
    identifies: Optional[Union[Union[str, InformationContentEntityId], List[Union[str, InformationContentEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DesignationId):
            self.id = DesignationId(self.id)

        if self.has_text_value is not None and not isinstance(self.has_text_value, str):
            self.has_text_value = str(self.has_text_value)

        if not isinstance(self.identifies, list):
            self.identifies = [self.identifies] if self.identifies is not None else []
        self.identifies = [v if isinstance(v, InformationContentEntityId) else InformationContentEntityId(v) for v in self.identifies]

        super().__post_init__(**kwargs)


@dataclass
class Name(Designation):
    """
    distinctive designation for an individual (person, organization or thing)
    """
    _inherited_slots: ClassVar[List[str]] = ["identifies"]

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Name
    class_class_curie: ClassVar[str] = "ucs_landscape:Name"
    class_name: ClassVar[str] = "Name"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Name

    id: Union[str, NameId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NameId):
            self.id = NameId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Identifier(Designation):
    """
    Sequence of characters uniquely identifying that with which it is associated
    """
    _inherited_slots: ClassVar[List[str]] = ["identifies"]

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Identifier
    class_class_curie: ClassVar[str] = "ucs_landscape:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Identifier

    id: Union[str, IdentifierId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentifierId):
            self.id = IdentifierId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeEntity(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.AdministrativeEntity
    class_class_curie: ClassVar[str] = "ucs_landscape:AdministrativeEntity"
    class_name: ClassVar[str] = "AdministrativeEntity"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.AdministrativeEntity

    id: Union[str, AdministrativeEntityId] = None

@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.InformationContentEntity
    class_class_curie: ClassVar[str] = "ucs_landscape:InformationContentEntity"
    class_name: ClassVar[str] = "InformationContentEntity"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    license: Optional[str] = None
    rights: Optional[str] = None
    format: Optional[str] = None
    creation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        super().__post_init__(**kwargs)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.EvidenceType
    class_class_curie: ClassVar[str] = "ucs_landscape:EvidenceType"
    class_name: ClassVar[str] = "EvidenceType"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.EvidenceType

    id: Union[str, EvidenceTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceTypeId):
            self.id = EvidenceTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class InformationResource(InformationContentEntity):
    """
    A database or knowledgebase and its supporting ecosystem of interfaces and services that deliver content to
    consumers (e.g. web portals, APIs, query endpoints, streaming services, data downloads, etc.). A single
    Information Resource by this definition may span many different datasets or databases, and include many access
    endpoints and user interfaces. Information Resources include project-specific resources such as a Translator
    Knowledge Provider, and community knowledgebases.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.InformationResource
    class_class_curie: ClassVar[str] = "ucs_landscape:InformationResource"
    class_name: ClassVar[str] = "InformationResource"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.InformationResource

    id: Union[str, InformationResourceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationResourceId):
            self.id = InformationResourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal
    or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or
    section highlighted by NLP). The scope is intended to be general and include information published on the web, as
    well as printed materials, either directly or in one of the Publication Generic category subclasses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Publication
    class_class_curie: ClassVar[str] = "ucs_landscape:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Publication

    id: Union[str, PublicationId] = None
    type: str = None
    authors: Optional[Union[str, List[str]]] = empty_list()
    name: Optional[Union[str, LabelType]] = None
    pages: Optional[Union[str, List[str]]] = empty_list()
    summary: Optional[str] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()
    lcsh_terms: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        if not isinstance(self.pages, list):
            self.pages = [self.pages] if self.pages is not None else []
        self.pages = [v if isinstance(v, str) else str(v) for v in self.pages]

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if not isinstance(self.lcsh_terms, list):
            self.lcsh_terms = [self.lcsh_terms] if self.lcsh_terms is not None else []
        self.lcsh_terms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.lcsh_terms]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Association
    class_class_curie: ClassVar[str] = "ucs_landscape:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = UCS_LANDSCAPE.Association

    id: Union[str, AssociationId] = None
    subject: Union[str, NamedThingId] = None
    predicate: Union[str, PredicateType] = None
    object: Union[str, NamedThingId] = None
    negated: Optional[Union[bool, Bool]] = None
    qualifiers: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()
    publications: Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]] = empty_list()
    has_evidence: Optional[Union[Union[str, EvidenceTypeId], List[Union[str, EvidenceTypeId]]]] = empty_list()
    primary_knowledge_source: Optional[Union[str, InformationResourceId]] = None
    aggregator_knowledge_source: Optional[Union[Union[str, InformationResourceId], List[Union[str, InformationResourceId]]]] = empty_list()
    timepoint: Optional[Union[str, TimeType]] = None
    type: Optional[str] = None
    category: Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssociationId):
            self.id = AssociationId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, NamedThingId):
            self.subject = NamedThingId(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, NamedThingId):
            self.object = NamedThingId(self.object)

        if self.negated is not None and not isinstance(self.negated, Bool):
            self.negated = Bool(self.negated)

        if not isinstance(self.qualifiers, list):
            self.qualifiers = [self.qualifiers] if self.qualifiers is not None else []
        self.qualifiers = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.qualifiers]

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.publications]

        if not isinstance(self.has_evidence, list):
            self.has_evidence = [self.has_evidence] if self.has_evidence is not None else []
        self.has_evidence = [v if isinstance(v, EvidenceTypeId) else EvidenceTypeId(v) for v in self.has_evidence]

        if self.primary_knowledge_source is not None and not isinstance(self.primary_knowledge_source, InformationResourceId):
            self.primary_knowledge_source = InformationResourceId(self.primary_knowledge_source)

        if not isinstance(self.aggregator_knowledge_source, list):
            self.aggregator_knowledge_source = [self.aggregator_knowledge_source] if self.aggregator_knowledge_source is not None else []
        self.aggregator_knowledge_source = [v if isinstance(v, InformationResourceId) else InformationResourceId(v) for v in self.aggregator_knowledge_source]

        if self.timepoint is not None and not isinstance(self.timepoint, TimeType):
            self.timepoint = TimeType(self.timepoint)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.has_attribute = Slot(uri=UCS_LANDSCAPE.has_attribute, name="has attribute", curie=UCS_LANDSCAPE.curie('has_attribute'),
                   model_uri=UCS_LANDSCAPE.has_attribute, domain=Entity, range=Optional[Union[Union[str, AttributeId], List[Union[str, AttributeId]]]])

slots.has_attribute_type = Slot(uri=UCS_LANDSCAPE.has_attribute_type, name="has attribute type", curie=UCS_LANDSCAPE.curie('has_attribute_type'),
                   model_uri=UCS_LANDSCAPE.has_attribute_type, domain=Attribute, range=Union[str, OntologyClassId])

slots.has_qualitative_value = Slot(uri=UCS_LANDSCAPE.has_qualitative_value, name="has qualitative value", curie=UCS_LANDSCAPE.curie('has_qualitative_value'),
                   model_uri=UCS_LANDSCAPE.has_qualitative_value, domain=Attribute, range=Optional[Union[str, NamedThingId]])

slots.has_quantitative_value = Slot(uri=UCS_LANDSCAPE.has_quantitative_value, name="has quantitative value", curie=UCS_LANDSCAPE.curie('has_quantitative_value'),
                   model_uri=UCS_LANDSCAPE.has_quantitative_value, domain=Attribute, range=Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]])

slots.has_numeric_value = Slot(uri=UCS_LANDSCAPE.has_numeric_value, name="has numeric value", curie=UCS_LANDSCAPE.curie('has_numeric_value'),
                   model_uri=UCS_LANDSCAPE.has_numeric_value, domain=QuantityValue, range=Optional[float])

slots.has_text_value = Slot(uri=XSD.string, name="has text value", curie=XSD.curie('string'),
                   model_uri=UCS_LANDSCAPE.has_text_value, domain=InformationContentEntity, range=Optional[str])

slots.has_unit = Slot(uri=UCS_LANDSCAPE.has_unit, name="has unit", curie=UCS_LANDSCAPE.curie('has_unit'),
                   model_uri=UCS_LANDSCAPE.has_unit, domain=QuantityValue, range=Optional[Union[str, Unit]])

slots.node_property = Slot(uri=UCS_LANDSCAPE.node_property, name="node property", curie=UCS_LANDSCAPE.curie('node_property'),
                   model_uri=UCS_LANDSCAPE.node_property, domain=NamedThing, range=Optional[str])

slots.id = Slot(uri=UCS_LANDSCAPE.id, name="id", curie=UCS_LANDSCAPE.curie('id'),
                   model_uri=UCS_LANDSCAPE.id, domain=Identifier, range=Union[str, IdentifierId])

slots.iri = Slot(uri=UCS_LANDSCAPE.iri, name="iri", curie=UCS_LANDSCAPE.curie('iri'),
                   model_uri=UCS_LANDSCAPE.iri, domain=None, range=Optional[Union[str, IriType]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=UCS_LANDSCAPE.type, domain=None, range=Optional[str])

slots.category = Slot(uri=UCS_LANDSCAPE.category, name="category", curie=UCS_LANDSCAPE.curie('category'),
                   model_uri=UCS_LANDSCAPE.category, domain=Entity, range=Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]])

slots.xref = Slot(uri=UCS_LANDSCAPE.xref, name="xref", curie=UCS_LANDSCAPE.curie('xref'),
                   model_uri=UCS_LANDSCAPE.xref, domain=NamedThing, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=UCS_LANDSCAPE.name, domain=Entity, range=Optional[Union[str, LabelType]])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=UCS_LANDSCAPE.description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.timepoint = Slot(uri=UCS_LANDSCAPE.timepoint, name="timepoint", curie=UCS_LANDSCAPE.curie('timepoint'),
                   model_uri=UCS_LANDSCAPE.timepoint, domain=None, range=Optional[Union[str, TimeType]])

slots.creation_date = Slot(uri=UCS_LANDSCAPE.creation_date, name="creation date", curie=UCS_LANDSCAPE.curie('creation_date'),
                   model_uri=UCS_LANDSCAPE.creation_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.license = Slot(uri=UCS_LANDSCAPE.license, name="license", curie=UCS_LANDSCAPE.curie('license'),
                   model_uri=UCS_LANDSCAPE.license, domain=InformationContentEntity, range=Optional[str])

slots.rights = Slot(uri=UCS_LANDSCAPE.rights, name="rights", curie=UCS_LANDSCAPE.curie('rights'),
                   model_uri=UCS_LANDSCAPE.rights, domain=InformationContentEntity, range=Optional[str])

slots.copyright = Slot(uri=UCS_LANDSCAPE.copyright, name="copyright", curie=UCS_LANDSCAPE.curie('copyright'),
                   model_uri=UCS_LANDSCAPE.copyright, domain=InformationContentEntity, range=Optional[str])

slots.format = Slot(uri=UCS_LANDSCAPE.format, name="format", curie=UCS_LANDSCAPE.curie('format'),
                   model_uri=UCS_LANDSCAPE.format, domain=InformationContentEntity, range=Optional[str])

slots.authors = Slot(uri=UCS_LANDSCAPE.authors, name="authors", curie=UCS_LANDSCAPE.curie('authors'),
                   model_uri=UCS_LANDSCAPE.authors, domain=Publication, range=Optional[Union[str, List[str]]])

slots.pages = Slot(uri=UCS_LANDSCAPE.pages, name="pages", curie=UCS_LANDSCAPE.curie('pages'),
                   model_uri=UCS_LANDSCAPE.pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.summary = Slot(uri=UCS_LANDSCAPE.summary, name="summary", curie=UCS_LANDSCAPE.curie('summary'),
                   model_uri=UCS_LANDSCAPE.summary, domain=Publication, range=Optional[str])

slots.keywords = Slot(uri=UCS_LANDSCAPE.keywords, name="keywords", curie=UCS_LANDSCAPE.curie('keywords'),
                   model_uri=UCS_LANDSCAPE.keywords, domain=Publication, range=Optional[Union[str, List[str]]])

slots.lcsh_terms = Slot(uri=UCS_LANDSCAPE.lcsh_terms, name="lcsh terms", curie=UCS_LANDSCAPE.curie('lcsh_terms'),
                   model_uri=UCS_LANDSCAPE.lcsh_terms, domain=Publication, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.identifies = Slot(uri=UCS_LANDSCAPE.identifies, name="identifies", curie=UCS_LANDSCAPE.curie('identifies'),
                   model_uri=UCS_LANDSCAPE.identifies, domain=Association, range=Optional[Union[Union[str, InformationContentEntityId], List[Union[str, InformationContentEntityId]]]])

slots.association_slot = Slot(uri=UCS_LANDSCAPE.association_slot, name="association slot", curie=UCS_LANDSCAPE.curie('association_slot'),
                   model_uri=UCS_LANDSCAPE.association_slot, domain=Association, range=Optional[str])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=UCS_LANDSCAPE.subject, domain=Association, range=Union[str, NamedThingId])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=UCS_LANDSCAPE.object, domain=Association, range=Union[str, NamedThingId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=UCS_LANDSCAPE.predicate, domain=Association, range=Union[str, PredicateType])

slots.negated = Slot(uri=UCS_LANDSCAPE.negated, name="negated", curie=UCS_LANDSCAPE.curie('negated'),
                   model_uri=UCS_LANDSCAPE.negated, domain=Association, range=Optional[Union[bool, Bool]])

slots.has_evidence = Slot(uri=UCS_LANDSCAPE.has_evidence, name="has evidence", curie=UCS_LANDSCAPE.curie('has_evidence'),
                   model_uri=UCS_LANDSCAPE.has_evidence, domain=Association, range=Optional[Union[Union[str, EvidenceTypeId], List[Union[str, EvidenceTypeId]]]])

slots.provided_by = Slot(uri=UCS_LANDSCAPE.provided_by, name="provided by", curie=UCS_LANDSCAPE.curie('provided_by'),
                   model_uri=UCS_LANDSCAPE.provided_by, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.knowledge_source = Slot(uri=UCS_LANDSCAPE.knowledge_source, name="knowledge source", curie=UCS_LANDSCAPE.curie('knowledge_source'),
                   model_uri=UCS_LANDSCAPE.knowledge_source, domain=Association, range=Optional[Union[str, InformationResourceId]])

slots.primary_knowledge_source = Slot(uri=UCS_LANDSCAPE.primary_knowledge_source, name="primary knowledge source", curie=UCS_LANDSCAPE.curie('primary_knowledge_source'),
                   model_uri=UCS_LANDSCAPE.primary_knowledge_source, domain=Association, range=Optional[Union[str, InformationResourceId]])

slots.aggregator_knowledge_source = Slot(uri=UCS_LANDSCAPE.aggregator_knowledge_source, name="aggregator knowledge source", curie=UCS_LANDSCAPE.curie('aggregator_knowledge_source'),
                   model_uri=UCS_LANDSCAPE.aggregator_knowledge_source, domain=Association, range=Optional[Union[Union[str, InformationResourceId], List[Union[str, InformationResourceId]]]])

slots.supporting_documents = Slot(uri=UCS_LANDSCAPE.supporting_documents, name="supporting documents", curie=UCS_LANDSCAPE.curie('supporting_documents'),
                   model_uri=UCS_LANDSCAPE.supporting_documents, domain=Association, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.publications = Slot(uri=UCS_LANDSCAPE.publications, name="publications", curie=UCS_LANDSCAPE.curie('publications'),
                   model_uri=UCS_LANDSCAPE.publications, domain=Association, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.qualifiers = Slot(uri=UCS_LANDSCAPE.qualifiers, name="qualifiers", curie=UCS_LANDSCAPE.curie('qualifiers'),
                   model_uri=UCS_LANDSCAPE.qualifiers, domain=Association, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.related_to = Slot(uri=UCS_LANDSCAPE.related_to, name="related to", curie=UCS_LANDSCAPE.curie('related_to'),
                   model_uri=UCS_LANDSCAPE.related_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.related_to_at_instance_level = Slot(uri=UCS_LANDSCAPE.related_to_at_instance_level, name="related to at instance level", curie=UCS_LANDSCAPE.curie('related_to_at_instance_level'),
                   model_uri=UCS_LANDSCAPE.related_to_at_instance_level, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.Attribute_name = Slot(uri=RDFS.label, name="Attribute_name", curie=RDFS.curie('label'),
                   model_uri=UCS_LANDSCAPE.Attribute_name, domain=Attribute, range=Optional[Union[str, LabelType]])

slots.Designation_has_text_value = Slot(uri=XSD.string, name="Designation_has text value", curie=XSD.curie('string'),
                   model_uri=UCS_LANDSCAPE.Designation_has_text_value, domain=Designation, range=Optional[str])

slots.Publication_id = Slot(uri=UCS_LANDSCAPE.id, name="Publication_id", curie=UCS_LANDSCAPE.curie('id'),
                   model_uri=UCS_LANDSCAPE.Publication_id, domain=Publication, range=Union[str, PublicationId])

slots.Publication_name = Slot(uri=RDFS.label, name="Publication_name", curie=RDFS.curie('label'),
                   model_uri=UCS_LANDSCAPE.Publication_name, domain=Publication, range=Optional[Union[str, LabelType]])

slots.Publication_type = Slot(uri=DCTERMS.type, name="Publication_type", curie=DCTERMS.curie('type'),
                   model_uri=UCS_LANDSCAPE.Publication_type, domain=Publication, range=str)

slots.Publication_pages = Slot(uri=UCS_LANDSCAPE.pages, name="Publication_pages", curie=UCS_LANDSCAPE.curie('pages'),
                   model_uri=UCS_LANDSCAPE.Publication_pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.Association_type = Slot(uri=RDF.type, name="Association_type", curie=RDF.curie('type'),
                   model_uri=UCS_LANDSCAPE.Association_type, domain=Association, range=Optional[str])

slots.Association_category = Slot(uri=UCS_LANDSCAPE.category, name="Association_category", curie=UCS_LANDSCAPE.curie('category'),
                   model_uri=UCS_LANDSCAPE.Association_category, domain=Association, range=Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]])
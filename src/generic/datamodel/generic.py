# Auto generated from generic.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-07-09T22:47:57
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
from linkml_runtime.linkml_model.types import Boolean, Date, Double, Float, Integer, String, Time, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate, XSDTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
BTO = CurieNamespace('BTO', 'http://purl.obolibrary.org/obo/BTO_')
CDAO = CurieNamespace('CDAO', 'http://purl.obolibrary.org/obo/CDAO_')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
CTRL = CurieNamespace('CTRL', 'https://w3id.org/ibp/CTRLont#')
CVE = CurieNamespace('CVE', 'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=')
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
EDAM_TOPIC = CurieNamespace('EDAM_TOPIC', 'http://edamontology.org/topic_')
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
ERO = CurieNamespace('ERO', 'http://purl.obolibrary.org/obo/ERO_')
EXO = CurieNamespace('ExO', 'http://purl.obolibrary.org/obo/EXO_')
GR = CurieNamespace('GR', 'http://purl.org/goodrelations/v1#')
GSID = CurieNamespace('GSID', 'https://scholar.google.com/citations?user=')
GSSO = CurieNamespace('GSSO', 'http://purl.obolibrary.org/obo/GSSO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
INO = CurieNamespace('INO', 'http://purl.obolibrary.org/obo/INO_')
LOINC = CurieNamespace('LOINC', 'http://loinc.org/rdf/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBAN = CurieNamespace('OBAN', 'http://purl.org/oban/')
ORCID = CurieNamespace('ORCID', 'http://identifiers.org/orcid/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
SAN = CurieNamespace('SAN', 'https://www.irit.fr/recherches/MELODI/ontologies/SAN.html#')
SIO = CurieNamespace('SIO', 'http://identifiers.org/sio/')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
SWO = CurieNamespace('SWO', 'http://purl.obolibrary.org/obo/SWO_')
SCOPUSID = CurieNamespace('ScopusID', 'https://www.scopus.com/authid/detail.uri?authorId=')
T4FS = CurieNamespace('T4FS', 'http://purl.obolibrary.org/obo/T4FS_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.WIKIDATA.org/wiki/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.WIKIDATA.org/wiki/Property:')
XAPI = CurieNamespace('XAPI', 'http://ns.inria.fr/ludo/v1/docs/xapi.html#')
AML = CurieNamespace('aml', 'https://w3id.org/i40/aml#')
ASTROVOCAB = CurieNamespace('astrovocab', 'https://www.asc-csa.gc.ca/eng/resources/vocabulary/view.asp?id=')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCID = CurieNamespace('dcid', 'https://datacommons.org/browser/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
DWC = CurieNamespace('dwc', 'http://rs.tdwg.org/dwc/terms/')
EDAM = CurieNamespace('edam', 'http://identifiers.org/edam/')
EDAM_DATA = CurieNamespace('edam_data', 'http://edamontology.org/data_')
EDAM_FORMAT = CurieNamespace('edam_format', 'http://edamontology.org/format_')
EDAM_OPERATION = CurieNamespace('edam_operation', 'http://edamontology.org/operation_')
EDAM_TOPIC = CurieNamespace('edam_topic', 'http://edamontology.org/topic_')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
FREEDICT = CurieNamespace('freedict', 'https://www.thefreedictionary.com/')
GENERIC = CurieNamespace('generic', 'https://w3id.org/lmodel/generic/')
GEOLINK = CurieNamespace('geolink', 'http://schema.geolink.org/1.0/base/main.html#')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
GVP = CurieNamespace('gvp', 'http://vocab.getty.edu/ontology#')
ISBN = CurieNamespace('isbn', 'https://www.isbn-international.org/identifier/')
ISNI = CurieNamespace('isni', 'https://isni.org/isni/')
ISSN = CurieNamespace('issn', 'https://portal.issn.org/resource/ISSN/')
LCSH = CurieNamespace('lcsh', 'http://id.loc.gov/authorities/subjects/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
METASAT = CurieNamespace('metasat', 'https://schema.space/metasat/')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
PUBLONS_RESEARCHER = CurieNamespace('publons_researcher', 'https://publons.com/researcher/')
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
SUMO_WN = CurieNamespace('sumo-wn', 'https://w3id.org/sumo/wn/')
UBERON = CurieNamespace('uberon', 'http://purl.obolibrary.org/obo/UBERON_')
UCO = CurieNamespace('uco', 'https://w3id.org/lmodel/uco-master')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GENERIC


# Types
class FormulaValue(str):
    """ A formula """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "formula value"
    type_model_uri = GENERIC.FormulaValue


class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the universal model.  The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the universal class, for example universal:Service. For an RDF representation, the value should be a URI such as https://w3id.org/lmodel/base/vocab/Service """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "category type"
    type_model_uri = GENERIC.CategoryType


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = GENERIC.IriType


class LabelType(String):
    """ A string that provides a human-readable name for an entity """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = GENERIC.LabelType


class PredicateType(Uriorcurie):
    """ A CURIE from the universal related_to hierarchy. For example, universal:related_to """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "predicate type"
    type_model_uri = GENERIC.PredicateType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = GENERIC.NarrativeText


class SymbolType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "symbol type"
    type_model_uri = GENERIC.SymbolType


class FrequencyValue(String):
    type_class_uri = UO["0000105"]
    type_class_curie = "UO:0000105"
    type_name = "frequency value"
    type_model_uri = GENERIC.FrequencyValue


class PercentageFrequencyValue(Double):
    type_class_uri = UO["0000187"]
    type_class_curie = "UO:0000187"
    type_name = "percentage frequency value"
    type_model_uri = GENERIC.PercentageFrequencyValue


class Quotient(Double):
    type_class_uri = UO["0010006"]
    type_class_curie = "UO:0010006"
    type_name = "quotient"
    type_model_uri = GENERIC.Quotient


class Unit(String):
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit"
    type_model_uri = GENERIC.Unit


class TimeType(Time):
    type_class_uri = XSD.time
    type_class_curie = "xsd:time"
    type_name = "time type"
    type_model_uri = GENERIC.TimeType


class ComputationalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "computational sequence"
    type_model_uri = GENERIC.ComputationalSequence


# Class references
class OntologyClassId(extended_str):
    pass


class EntityId(extended_str):
    pass


class NamedThingId(EntityId):
    pass


class AttributeId(NamedThingId):
    pass


class ControlRoleId(AttributeId):
    pass


class BiologicalSexId(AttributeId):
    pass


class SeverityValueId(AttributeId):
    pass


class DesignationId(NamedThingId):
    pass


class NameId(DesignationId):
    pass


class IdentifierId(DesignationId):
    pass


class EventId(NamedThingId):
    pass


class AdministrativeEntityId(NamedThingId):
    pass


class AgentId(AdministrativeEntityId):
    pass


class ProjectId(AgentId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class SpecificationId(InformationContentEntityId):
    pass


class DatasetId(InformationContentEntityId):
    pass


class DatasetDistributionId(InformationContentEntityId):
    pass


class DatasetVersionId(InformationContentEntityId):
    pass


class DatasetSummaryId(InformationContentEntityId):
    pass


class EvidenceTypeId(InformationContentEntityId):
    pass


class InformationResourceId(InformationContentEntityId):
    pass


class OpenAccessId(NamedThingId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class BookId(PublicationId):
    pass


class BookChapterId(PublicationId):
    pass


class SerialId(PublicationId):
    pass


class ArticleId(PublicationId):
    pass


class PhenomenonId(NamedThingId):
    pass


class PlanetaryEntityId(NamedThingId):
    pass


class GeographicLocationId(PlanetaryEntityId):
    pass


class SystemId(NamedThingId):
    pass


class DeviceId(SystemId):
    pass


class SoftwareOrDeviceId(SystemId):
    pass


class SoftwareId(SoftwareOrDeviceId):
    pass


class HardwareId(SoftwareOrDeviceId):
    pass


class IndividualSystemId(SystemId):
    pass


class SystemAttributeId(AttributeId):
    pass


class EnvironmentId(SystemId):
    pass


class ComponentId(SystemId):
    pass


class MessageId(InformationContentEntityId):
    pass


class RuleId(MessageId):
    pass


class InstructionId(MessageId):
    pass


class LawId(RuleId):
    pass


class RegulationId(RuleId):
    pass


class GovernanceId(RegulationId):
    pass


class BoundaryId(NamedThingId):
    pass


class KnowledgeId(InformationResourceId):
    pass


class AssociationId(EntityId):
    pass


MetaObject = Any

@dataclass
class OntologyClass(YAMLRoot):
    """
    a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a base compatible KG can be
    considered both instances of base classes, and OWL classes in their own right. In general you should not need to
    use this class directly. Instead, use the appropriate base class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.OntologyClass
    class_class_curie: ClassVar[str] = "generic:OntologyClass"
    class_name: ClassVar[str] = "OntologyClass"
    class_model_uri: ClassVar[URIRef] = GENERIC.OntologyClass

    id: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        super().__post_init__(**kwargs)


class Annotation(YAMLRoot):
    """
    Universal Model root class for entity annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Annotation
    class_class_curie: ClassVar[str] = "generic:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = GENERIC.Annotation


@dataclass
class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric
    value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.QuantityValue
    class_class_curie: ClassVar[str] = "generic:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = GENERIC.QuantityValue

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
    Root Universal Model class for all things and informational relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Entity
    class_class_curie: ClassVar[str] = "generic:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = GENERIC.Entity

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
class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = GENERIC.NamedThing

    id: Union[str, NamedThingId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    provided_by: Optional[Union[str, List[str]]] = empty_list()
    xref: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, CategoryType) else CategoryType(v) for v in self.category]

        if not isinstance(self.provided_by, list):
            self.provided_by = [self.provided_by] if self.provided_by is not None else []
        self.provided_by = [v if isinstance(v, str) else str(v) for v in self.provided_by]

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class Attribute(NamedThing):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age,
    crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Attribute
    class_class_curie: ClassVar[str] = "generic:Attribute"
    class_name: ClassVar[str] = "Attribute"
    class_model_uri: ClassVar[URIRef] = GENERIC.Attribute

    id: Union[str, AttributeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
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
class ControlRole(Attribute):
    """
    A role played by the entity or part thereof within a control context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.ControlRole
    class_class_curie: ClassVar[str] = "generic:ControlRole"
    class_name: ClassVar[str] = "ControlRole"
    class_model_uri: ClassVar[URIRef] = GENERIC.ControlRole

    id: Union[str, ControlRoleId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControlRoleId):
            self.id = ControlRoleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BiologicalSex(Attribute):
    """
    Status as female, male, or intersex depending on their chromosomes, reproductive organs, and other characteristics
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.BiologicalSex
    class_class_curie: ClassVar[str] = "generic:BiologicalSex"
    class_name: ClassVar[str] = "BiologicalSex"
    class_model_uri: ClassVar[URIRef] = GENERIC.BiologicalSex

    id: Union[str, BiologicalSexId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalSexId):
            self.id = BiologicalSexId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SeverityValue(Attribute):
    """
    describes the severity of a observable feature or fault
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.SeverityValue
    class_class_curie: ClassVar[str] = "generic:SeverityValue"
    class_name: ClassVar[str] = "SeverityValue"
    class_model_uri: ClassVar[URIRef] = GENERIC.SeverityValue

    id: Union[str, SeverityValueId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SeverityValueId):
            self.id = SeverityValueId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Designation(NamedThing):
    """
    representation for someone or something by a sign that denotes it
    """
    _inherited_slots: ClassVar[List[str]] = ["identifies"]

    class_class_uri: ClassVar[URIRef] = GENERIC.Designation
    class_class_curie: ClassVar[str] = "generic:Designation"
    class_name: ClassVar[str] = "Designation"
    class_model_uri: ClassVar[URIRef] = GENERIC.Designation

    id: Union[str, DesignationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
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

    class_class_uri: ClassVar[URIRef] = GENERIC.Name
    class_class_curie: ClassVar[str] = "generic:Name"
    class_name: ClassVar[str] = "Name"
    class_model_uri: ClassVar[URIRef] = GENERIC.Name

    id: Union[str, NameId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

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

    class_class_uri: ClassVar[URIRef] = GENERIC.Identifier
    class_class_curie: ClassVar[str] = "generic:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = GENERIC.Identifier

    id: Union[str, IdentifierId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentifierId):
            self.id = IdentifierId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Event(NamedThing):
    """
    Something that happens at a given place and time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Event
    class_class_curie: ClassVar[str] = "generic:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = GENERIC.Event

    id: Union[str, EventId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventId):
            self.id = EventId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class AdministrativeEntity(NamedThing):
    """
    Entity responsible for managing the affairs of an organization
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.AdministrativeEntity
    class_class_curie: ClassVar[str] = "generic:AdministrativeEntity"
    class_name: ClassVar[str] = "AdministrativeEntity"
    class_model_uri: ClassVar[URIRef] = GENERIC.AdministrativeEntity

    id: Union[str, AdministrativeEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class Agent(AdministrativeEntity):
    """
    person, group, organization or project that provides a piece of information (i.e. a knowledge association)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Agent
    class_class_curie: ClassVar[str] = "generic:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = GENERIC.Agent

    id: Union[str, AgentId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    affiliation: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    address: Optional[str] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation] if self.affiliation is not None else []
        self.affiliation = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.affiliation]

        if self.address is not None and not isinstance(self.address, str):
            self.address = str(self.address)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Project(Agent):
    """
    collaborative enterprise, frequently involving research or design, that is carefully planned to achieve a
    particular aim
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Project
    class_class_curie: ClassVar[str] = "generic:Project"
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = GENERIC.Project

    id: Union[str, ProjectId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.InformationContentEntity
    class_class_curie: ClassVar[str] = "generic:InformationContentEntity"
    class_name: ClassVar[str] = "InformationContentEntity"
    class_model_uri: ClassVar[URIRef] = GENERIC.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
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
class Specification(InformationContentEntity):
    """
    A detailed description of criteria for a piece of work.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Specification
    class_class_curie: ClassVar[str] = "generic:Specification"
    class_name: ClassVar[str] = "Specification"
    class_model_uri: ClassVar[URIRef] = GENERIC.Specification

    id: Union[str, SpecificationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Dataset
    class_class_curie: ClassVar[str] = "generic:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = GENERIC.Dataset

    id: Union[str, DatasetId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DatasetDistribution(InformationContentEntity):
    """
    an item that holds distribution level information about a dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.DatasetDistribution
    class_class_curie: ClassVar[str] = "generic:DatasetDistribution"
    class_name: ClassVar[str] = "DatasetDistribution"
    class_model_uri: ClassVar[URIRef] = GENERIC.DatasetDistribution

    id: Union[str, DatasetDistributionId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    distribution_download_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetDistributionId):
            self.id = DatasetDistributionId(self.id)

        if self.distribution_download_url is not None and not isinstance(self.distribution_download_url, str):
            self.distribution_download_url = str(self.distribution_download_url)

        super().__post_init__(**kwargs)


@dataclass
class DatasetVersion(InformationContentEntity):
    """
    an item that holds version level information about a dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.DatasetVersion
    class_class_curie: ClassVar[str] = "generic:DatasetVersion"
    class_name: ClassVar[str] = "DatasetVersion"
    class_model_uri: ClassVar[URIRef] = GENERIC.DatasetVersion

    id: Union[str, DatasetVersionId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_dataset: Optional[Union[str, DatasetId]] = None
    ingest_date: Optional[str] = None
    has_distribution: Optional[Union[str, DatasetDistributionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetVersionId):
            self.id = DatasetVersionId(self.id)

        if self.has_dataset is not None and not isinstance(self.has_dataset, DatasetId):
            self.has_dataset = DatasetId(self.has_dataset)

        if self.ingest_date is not None and not isinstance(self.ingest_date, str):
            self.ingest_date = str(self.ingest_date)

        if self.has_distribution is not None and not isinstance(self.has_distribution, DatasetDistributionId):
            self.has_distribution = DatasetDistributionId(self.has_distribution)

        super().__post_init__(**kwargs)


@dataclass
class DatasetSummary(InformationContentEntity):
    """
    an item that holds summary level information about a dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.DatasetSummary
    class_class_curie: ClassVar[str] = "generic:DatasetSummary"
    class_name: ClassVar[str] = "DatasetSummary"
    class_model_uri: ClassVar[URIRef] = GENERIC.DatasetSummary

    id: Union[str, DatasetSummaryId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    source_web_page: Optional[str] = None
    source_logo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetSummaryId):
            self.id = DatasetSummaryId(self.id)

        if self.source_web_page is not None and not isinstance(self.source_web_page, str):
            self.source_web_page = str(self.source_web_page)

        if self.source_logo is not None and not isinstance(self.source_logo, str):
            self.source_logo = str(self.source_logo)

        super().__post_init__(**kwargs)


@dataclass
class EvidenceType(InformationContentEntity):
    """
    Class of evidence that supports an association
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.EvidenceType
    class_class_curie: ClassVar[str] = "generic:EvidenceType"
    class_name: ClassVar[str] = "EvidenceType"
    class_model_uri: ClassVar[URIRef] = GENERIC.EvidenceType

    id: Union[str, EvidenceTypeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

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

    class_class_uri: ClassVar[URIRef] = GENERIC.InformationResource
    class_class_curie: ClassVar[str] = "generic:InformationResource"
    class_name: ClassVar[str] = "InformationResource"
    class_model_uri: ClassVar[URIRef] = GENERIC.InformationResource

    id: Union[str, InformationResourceId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationResourceId):
            self.id = InformationResourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class OpenAccess(NamedThing):
    """
    Free distribution of knowledge
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.OpenAccess
    class_class_curie: ClassVar[str] = "generic:OpenAccess"
    class_name: ClassVar[str] = "OpenAccess"
    class_model_uri: ClassVar[URIRef] = GENERIC.OpenAccess

    id: Union[str, OpenAccessId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class Publication(InformationContentEntity):
    """
    Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal
    or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or
    section highlighted by NLP). The scope is intended to be general and include information published on the web, as
    well as printed materials, either directly or in one of the Publication Universal category subclasses.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Publication
    class_class_curie: ClassVar[str] = "generic:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = GENERIC.Publication

    id: Union[str, PublicationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
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
class Book(Publication):
    """
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Book
    class_class_curie: ClassVar[str] = "generic:Book"
    class_name: ClassVar[str] = "book"
    class_model_uri: ClassVar[URIRef] = GENERIC.Book

    id: Union[str, BookId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BookId):
            self.id = BookId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class BookChapter(Publication):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.BookChapter
    class_class_curie: ClassVar[str] = "generic:BookChapter"
    class_name: ClassVar[str] = "book chapter"
    class_model_uri: ClassVar[URIRef] = GENERIC.BookChapter

    id: Union[str, BookChapterId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    type: str = None
    published_in: Union[str, URIorCURIE] = None
    volume: Optional[str] = None
    chapter: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BookChapterId):
            self.id = BookChapterId(self.id)

        if self._is_empty(self.published_in):
            self.MissingRequiredField("published_in")
        if not isinstance(self.published_in, URIorCURIE):
            self.published_in = URIorCURIE(self.published_in)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.chapter is not None and not isinstance(self.chapter, str):
            self.chapter = str(self.chapter)

        super().__post_init__(**kwargs)


@dataclass
class Serial(Publication):
    """
    This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Serial
    class_class_curie: ClassVar[str] = "generic:Serial"
    class_name: ClassVar[str] = "Serial"
    class_model_uri: ClassVar[URIRef] = GENERIC.Serial

    id: Union[str, SerialId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    iso_abbreviation: Optional[str] = None
    type: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SerialId):
            self.id = SerialId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        super().__post_init__(**kwargs)


@dataclass
class Article(Publication):
    """
    A written composition in prose, usually nonfiction, on a specific topic, forming an independent part of a book or
    other publication
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Article
    class_class_curie: ClassVar[str] = "generic:Article"
    class_name: ClassVar[str] = "Article"
    class_model_uri: ClassVar[URIRef] = GENERIC.Article

    id: Union[str, ArticleId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    type: str = None
    published_in: Union[str, URIorCURIE] = None
    iso_abbreviation: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ArticleId):
            self.id = ArticleId(self.id)

        if self._is_empty(self.published_in):
            self.MissingRequiredField("published_in")
        if not isinstance(self.published_in, URIorCURIE):
            self.published_in = URIorCURIE(self.published_in)

        if self.iso_abbreviation is not None and not isinstance(self.iso_abbreviation, str):
            self.iso_abbreviation = str(self.iso_abbreviation)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        super().__post_init__(**kwargs)


class TangibleEssenceOrOccurrent(YAMLRoot):
    """
    Either a physical or processual entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.TangibleEssenceOrOccurrent
    class_class_curie: ClassVar[str] = "generic:TangibleEssenceOrOccurrent"
    class_name: ClassVar[str] = "TangibleEssenceOrOccurrent"
    class_model_uri: ClassVar[URIRef] = GENERIC.TangibleEssenceOrOccurrent


class TangibleEssence(TangibleEssenceOrOccurrent):
    """
    Semantic mixin concept. Pertains to entities that have tangible properties such as mass, volume, or charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.TangibleEssence
    class_class_curie: ClassVar[str] = "generic:TangibleEssence"
    class_name: ClassVar[str] = "TangibleEssence"
    class_model_uri: ClassVar[URIRef] = GENERIC.TangibleEssence


class Occurrent(TangibleEssenceOrOccurrent):
    """
    A processual entity that has temporal parts and happens, unfolds or develops through time. Occurrents have phases.
    universal:Occurrent is most consistently used as a mixin thus it should be declared as such and cannot inherit
    from the non-mixin universal:NamedThing
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Occurrent
    class_class_curie: ClassVar[str] = "generic:Occurrent"
    class_name: ClassVar[str] = "Occurrent"
    class_model_uri: ClassVar[URIRef] = GENERIC.Occurrent


@dataclass
class Phenomenon(NamedThing):
    """
    a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Phenomenon
    class_class_curie: ClassVar[str] = "generic:Phenomenon"
    class_name: ClassVar[str] = "Phenomenon"
    class_model_uri: ClassVar[URIRef] = GENERIC.Phenomenon

    id: Union[str, PhenomenonId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenomenonId):
            self.id = PhenomenonId(self.id)

        super().__post_init__(**kwargs)


class SubjectOfInvestigation(YAMLRoot):
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.SubjectOfInvestigation
    class_class_curie: ClassVar[str] = "generic:SubjectOfInvestigation"
    class_name: ClassVar[str] = "SubjectOfInvestigation"
    class_model_uri: ClassVar[URIRef] = GENERIC.SubjectOfInvestigation


@dataclass
class PlanetaryEntity(NamedThing):
    """
    Any entity or process that exists at the level of the whole planet
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.PlanetaryEntity
    class_class_curie: ClassVar[str] = "generic:PlanetaryEntity"
    class_name: ClassVar[str] = "PlanetaryEntity"
    class_model_uri: ClassVar[URIRef] = GENERIC.PlanetaryEntity

    id: Union[str, PlanetaryEntityId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlanetaryEntityId):
            self.id = PlanetaryEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GeographicLocation(PlanetaryEntity):
    """
    a location that can be described in lat/long coordinates
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.GeographicLocation
    class_class_curie: ClassVar[str] = "generic:GeographicLocation"
    class_name: ClassVar[str] = "GeographicLocation"
    class_model_uri: ClassVar[URIRef] = GENERIC.GeographicLocation

    id: Union[str, GeographicLocationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeographicLocationId):
            self.id = GeographicLocationId(self.id)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        super().__post_init__(**kwargs)


@dataclass
class ThingWithTaxon(YAMLRoot):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual entities,
    their products, and other operational entities and processes.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = GENERIC.ThingWithTaxon
    class_class_curie: ClassVar[str] = "generic:ThingWithTaxon"
    class_name: ClassVar[str] = "ThingWithTaxon"
    class_model_uri: ClassVar[URIRef] = GENERIC.ThingWithTaxon

    in_taxon: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class System(NamedThing):
    """
    An entity that intends to perform some functions, interacting with other systems. Relative to a given system, the
    entities with which it interacts, are considered its environment. A system is structurally composed of a set of
    components bound together.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = GENERIC.System
    class_class_curie: ClassVar[str] = "generic:System"
    class_name: ClassVar[str] = "System"
    class_model_uri: ClassVar[URIRef] = GENERIC.System

    id: Union[str, SystemId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    in_taxon: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemId):
            self.id = SystemId(self.id)

        if not isinstance(self.in_taxon, list):
            self.in_taxon = [self.in_taxon] if self.in_taxon is not None else []
        self.in_taxon = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.in_taxon]

        super().__post_init__(**kwargs)


@dataclass
class Device(System):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = GENERIC.Device
    class_class_curie: ClassVar[str] = "generic:Device"
    class_name: ClassVar[str] = "Device"
    class_model_uri: ClassVar[URIRef] = GENERIC.Device

    id: Union[str, DeviceId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SoftwareOrDevice(System):
    """
    Either software or hardware
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = GENERIC.SoftwareOrDevice
    class_class_curie: ClassVar[str] = "generic:SoftwareOrDevice"
    class_name: ClassVar[str] = "SoftwareOrDevice"
    class_model_uri: ClassVar[URIRef] = GENERIC.SoftwareOrDevice

    id: Union[str, SoftwareOrDeviceId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

@dataclass
class Software(SoftwareOrDevice):
    """
    A set of instructions in a computer programming language that can be executed by a computer, possibly after
    compilation into another programming language. The term Software includes ComputerPrograms (free-standing
    software), object methods, subroutines and software packages.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = GENERIC.Software
    class_class_curie: ClassVar[str] = "generic:Software"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = GENERIC.Software

    id: Union[str, SoftwareId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftwareId):
            self.id = SoftwareId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Hardware(SoftwareOrDevice):
    """
    physical components of a computer
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = GENERIC.Hardware
    class_class_curie: ClassVar[str] = "generic:Hardware"
    class_name: ClassVar[str] = "Hardware"
    class_model_uri: ClassVar[URIRef] = GENERIC.Hardware

    id: Union[str, HardwareId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HardwareId):
            self.id = HardwareId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class IndividualSystem(System):
    """
    An instance of an system. For example, human. Computer, my pet cat.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = GENERIC.IndividualSystem
    class_class_curie: ClassVar[str] = "generic:IndividualSystem"
    class_name: ClassVar[str] = "IndividualSystem"
    class_model_uri: ClassVar[URIRef] = GENERIC.IndividualSystem

    id: Union[str, IndividualSystemId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IndividualSystemId):
            self.id = IndividualSystemId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SystemAttribute(Attribute):
    """
    describes a characteristic of an SystemEntity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.SystemAttribute
    class_class_curie: ClassVar[str] = "generic:SystemAttribute"
    class_name: ClassVar[str] = "SystemAttribute"
    class_model_uri: ClassVar[URIRef] = GENERIC.SystemAttribute

    id: Union[str, SystemAttributeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None
    has_attribute_type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemAttributeId):
            self.id = SystemAttributeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Environment(System):
    """
    Part of the universe outside the boundaries of a given system, interacting with that given system.
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = GENERIC.Environment
    class_class_curie: ClassVar[str] = "generic:Environment"
    class_name: ClassVar[str] = "Environment"
    class_model_uri: ClassVar[URIRef] = GENERIC.Environment

    id: Union[str, EnvironmentId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentId):
            self.id = EnvironmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Component(System):
    """
    The component is the smallest system entity that can be deployed, isolated, and restored independently. A
    self-contained assembly of parts within a complete operating unit or module, which cannot be further subdivided
    without loss of identity or function. The compoent is part of a system structurally composed of a set of
    components bound together. Each component is another system and this recursive definition stops when a component
    is regarded as atomic."
    """
    _inherited_slots: ClassVar[List[str]] = ["in_taxon"]

    class_class_uri: ClassVar[URIRef] = GENERIC.Component
    class_class_curie: ClassVar[str] = "generic:Component"
    class_name: ClassVar[str] = "Component"
    class_model_uri: ClassVar[URIRef] = GENERIC.Component

    id: Union[str, ComponentId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComponentId):
            self.id = ComponentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Message(InformationContentEntity):
    """
    discrete unit of communication intended by the source for consumption by some recipient or group of recipients
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Message
    class_class_curie: ClassVar[str] = "schema:Message"
    class_name: ClassVar[str] = "Message"
    class_model_uri: ClassVar[URIRef] = GENERIC.Message

    id: Union[str, MessageId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MessageId):
            self.id = MessageId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Rule(Message):
    """
    prescription, including laws, regulations, instructions, guidelines, and social conventions; determinate method
    for performing any operation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Rule
    class_class_curie: ClassVar[str] = "generic:Rule"
    class_name: ClassVar[str] = "Rule"
    class_model_uri: ClassVar[URIRef] = GENERIC.Rule

    id: Union[str, RuleId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RuleId):
            self.id = RuleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Instruction(Message):
    """
    message intended to convey a course of action for the audience to follow
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Instruction
    class_class_curie: ClassVar[str] = "generic:Instruction"
    class_name: ClassVar[str] = "Instruction"
    class_model_uri: ClassVar[URIRef] = GENERIC.Instruction

    id: Union[str, InstructionId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstructionId):
            self.id = InstructionId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Law(Rule):
    """
    system of rules and guidelines, generally backed by governmental authority
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Law
    class_class_curie: ClassVar[str] = "generic:Law"
    class_name: ClassVar[str] = "Law"
    class_model_uri: ClassVar[URIRef] = GENERIC.Law

    id: Union[str, LawId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LawId):
            self.id = LawId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Regulation(Rule):
    """
    general term for rules or controls, including delegated legislation and self-regulation within an organisation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Regulation
    class_class_curie: ClassVar[str] = "generic:Regulation"
    class_name: ClassVar[str] = "Regulation"
    class_model_uri: ClassVar[URIRef] = GENERIC.Regulation

    id: Union[str, RegulationId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegulationId):
            self.id = RegulationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Governance(Regulation):
    """
    all of the processes of governing, whether undertaken by a government, market or network, whether over a family,
    tribe, formal or informal organization or territory and whether through the laws, norms, power or language of an
    organized society
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Governance
    class_class_curie: ClassVar[str] = "generic:Governance"
    class_name: ClassVar[str] = "Governance"
    class_model_uri: ClassVar[URIRef] = GENERIC.Governance

    id: Union[str, GovernanceId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GovernanceId):
            self.id = GovernanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Boundary(NamedThing):
    """
    dividing line between two areas or sets of points in a topological space; difference between the closure and the
    interior
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Boundary
    class_class_curie: ClassVar[str] = "generic:Boundary"
    class_name: ClassVar[str] = "Boundary"
    class_model_uri: ClassVar[URIRef] = GENERIC.Boundary

    id: Union[str, BoundaryId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BoundaryId):
            self.id = BoundaryId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Knowledge(InformationResource):
    """
    A set of knowledge or reproducible skills acquired through study or experience.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Knowledge
    class_class_curie: ClassVar[str] = "generic:Knowledge"
    class_name: ClassVar[str] = "Knowledge"
    class_model_uri: ClassVar[URIRef] = GENERIC.Knowledge

    id: Union[str, KnowledgeId] = None
    category: Union[Union[str, CategoryType], List[Union[str, CategoryType]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KnowledgeId):
            self.id = KnowledgeId(self.id)

        super().__post_init__(**kwargs)


class Outcome(YAMLRoot):
    """
    An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of
    various categories of possible biological or non-biological (e.g. clinical) outcomes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Outcome
    class_class_curie: ClassVar[str] = "generic:Outcome"
    class_name: ClassVar[str] = "outcome"
    class_model_uri: ClassVar[URIRef] = GENERIC.Outcome


@dataclass
class Association(Entity):
    """
    A typed association between two entities, supported by evidence
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERIC.Association
    class_class_curie: ClassVar[str] = "generic:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = GENERIC.Association

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

slots.has_attribute = Slot(uri=GENERIC.has_attribute, name="has attribute", curie=GENERIC.curie('has_attribute'),
                   model_uri=GENERIC.has_attribute, domain=Entity, range=Optional[Union[Union[str, AttributeId], List[Union[str, AttributeId]]]])

slots.has_attribute_type = Slot(uri=GENERIC.has_attribute_type, name="has attribute type", curie=GENERIC.curie('has_attribute_type'),
                   model_uri=GENERIC.has_attribute_type, domain=Attribute, range=Union[str, OntologyClassId])

slots.has_qualitative_value = Slot(uri=GENERIC.has_qualitative_value, name="has qualitative value", curie=GENERIC.curie('has_qualitative_value'),
                   model_uri=GENERIC.has_qualitative_value, domain=Attribute, range=Optional[Union[str, NamedThingId]])

slots.has_quantitative_value = Slot(uri=GENERIC.has_quantitative_value, name="has quantitative value", curie=GENERIC.curie('has_quantitative_value'),
                   model_uri=GENERIC.has_quantitative_value, domain=Attribute, range=Optional[Union[Union[dict, QuantityValue], List[Union[dict, QuantityValue]]]])

slots.has_numeric_value = Slot(uri=GENERIC.has_numeric_value, name="has numeric value", curie=GENERIC.curie('has_numeric_value'),
                   model_uri=GENERIC.has_numeric_value, domain=QuantityValue, range=Optional[float])

slots.has_text_value = Slot(uri=XSD.string, name="has text value", curie=XSD.curie('string'),
                   model_uri=GENERIC.has_text_value, domain=InformationContentEntity, range=Optional[str])

slots.has_unit = Slot(uri=GENERIC.has_unit, name="has unit", curie=GENERIC.curie('has_unit'),
                   model_uri=GENERIC.has_unit, domain=QuantityValue, range=Optional[Union[str, Unit]])

slots.base_coordinate = Slot(uri=GENERIC.base_coordinate, name="base coordinate", curie=GENERIC.curie('base_coordinate'),
                   model_uri=GENERIC.base_coordinate, domain=None, range=Optional[int])

slots.node_property = Slot(uri=GENERIC.node_property, name="node property", curie=GENERIC.curie('node_property'),
                   model_uri=GENERIC.node_property, domain=NamedThing, range=Optional[str])

slots.id = Slot(uri=GENERIC.id, name="id", curie=GENERIC.curie('id'),
                   model_uri=GENERIC.id, domain=Identifier, range=Union[str, IdentifierId])

slots.iri = Slot(uri=GENERIC.iri, name="iri", curie=GENERIC.curie('iri'),
                   model_uri=GENERIC.iri, domain=None, range=Optional[Union[str, IriType]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=GENERIC.type, domain=None, range=Optional[str])

slots.category = Slot(uri=GENERIC.category, name="category", curie=GENERIC.curie('category'),
                   model_uri=GENERIC.category, domain=Entity, range=Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=GENERIC.name, domain=Entity, range=Optional[Union[str, LabelType]])

slots.command = Slot(uri=GENERIC.command, name="command", curie=GENERIC.curie('command'),
                   model_uri=GENERIC.command, domain=None, range=Optional[Union[str, InstructionId]])

slots.file = Slot(uri=GENERIC.file, name="file", curie=GENERIC.curie('file'),
                   model_uri=GENERIC.file, domain=InformationContentEntity, range=Optional[str])

slots.image = Slot(uri=GENERIC.image, name="image", curie=GENERIC.curie('image'),
                   model_uri=GENERIC.image, domain=NamedThing, range=Optional[str])

slots.state = Slot(uri=GENERIC.state, name="state", curie=GENERIC.curie('state'),
                   model_uri=GENERIC.state, domain=IndividualSystem, range=Optional[Union[str, SystemId]])

slots.ratios = Slot(uri=GENERIC.ratios, name="ratios", curie=GENERIC.curie('ratios'),
                   model_uri=GENERIC.ratios, domain=Association, range=Optional[int])

slots.synonym = Slot(uri=GENERIC.synonym, name="synonym", curie=GENERIC.curie('synonym'),
                   model_uri=GENERIC.synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.symbol = Slot(uri=GENERIC.symbol, name="symbol", curie=GENERIC.curie('symbol'),
                   model_uri=GENERIC.symbol, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.abbreviation = Slot(uri=GENERIC.abbreviation, name="abbreviation", curie=GENERIC.curie('abbreviation'),
                   model_uri=GENERIC.abbreviation, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.acronym = Slot(uri=GENERIC.acronym, name="acronym", curie=GENERIC.curie('acronym'),
                   model_uri=GENERIC.acronym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.exact_synonym = Slot(uri=GENERIC.exact_synonym, name="exact synonym", curie=GENERIC.curie('exact_synonym'),
                   model_uri=GENERIC.exact_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.broad_synonym = Slot(uri=GENERIC.broad_synonym, name="broad synonym", curie=GENERIC.curie('broad_synonym'),
                   model_uri=GENERIC.broad_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.narrow_synonym = Slot(uri=GENERIC.narrow_synonym, name="narrow synonym", curie=GENERIC.curie('narrow_synonym'),
                   model_uri=GENERIC.narrow_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.related_synonym = Slot(uri=GENERIC.related_synonym, name="related synonym", curie=GENERIC.curie('related_synonym'),
                   model_uri=GENERIC.related_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.has_topic = Slot(uri=GENERIC.has_topic, name="has topic", curie=GENERIC.curie('has_topic'),
                   model_uri=GENERIC.has_topic, domain=NamedThing, range=Optional[Union[str, OntologyClassId]])

slots.xref = Slot(uri=GENERIC.xref, name="xref", curie=GENERIC.curie('xref'),
                   model_uri=GENERIC.xref, domain=NamedThing, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.full_name = Slot(uri=GENERIC.full_name, name="full name", curie=GENERIC.curie('full_name'),
                   model_uri=GENERIC.full_name, domain=NamedThing, range=Optional[Union[str, LabelType]])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=GENERIC.description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.logical_description = Slot(uri=GENERIC.logical_description, name="logical description", curie=GENERIC.curie('logical_description'),
                   model_uri=GENERIC.logical_description, domain=None, range=Optional[Union[str, NarrativeText]])

slots.note = Slot(uri=GENERIC.note, name="note", curie=GENERIC.curie('note'),
                   model_uri=GENERIC.note, domain=None, range=Optional[Union[str, NarrativeText]])

slots.systematic_synonym = Slot(uri=GENERIC.systematic_synonym, name="systematic synonym", curie=GENERIC.curie('systematic_synonym'),
                   model_uri=GENERIC.systematic_synonym, domain=NamedThing, range=Optional[Union[Union[str, LabelType], List[Union[str, LabelType]]]])

slots.affiliation = Slot(uri=GENERIC.affiliation, name="affiliation", curie=GENERIC.curie('affiliation'),
                   model_uri=GENERIC.affiliation, domain=Agent, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.address = Slot(uri=GENERIC.address, name="address", curie=GENERIC.curie('address'),
                   model_uri=GENERIC.address, domain=NamedThing, range=Optional[str])

slots.latitude = Slot(uri=GENERIC.latitude, name="latitude", curie=GENERIC.curie('latitude'),
                   model_uri=GENERIC.latitude, domain=NamedThing, range=Optional[float])

slots.longitude = Slot(uri=GENERIC.longitude, name="longitude", curie=GENERIC.curie('longitude'),
                   model_uri=GENERIC.longitude, domain=NamedThing, range=Optional[float])

slots.timepoint = Slot(uri=GENERIC.timepoint, name="timepoint", curie=GENERIC.curie('timepoint'),
                   model_uri=GENERIC.timepoint, domain=None, range=Optional[Union[str, TimeType]])

slots.creation_date = Slot(uri=GENERIC.creation_date, name="creation date", curie=GENERIC.curie('creation_date'),
                   model_uri=GENERIC.creation_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.update_date = Slot(uri=GENERIC.update_date, name="update date", curie=GENERIC.curie('update_date'),
                   model_uri=GENERIC.update_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.issued_date = Slot(uri=GENERIC.issued_date, name="issued date", curie=GENERIC.curie('issued_date'),
                   model_uri=GENERIC.issued_date, domain=NamedThing, range=Optional[Union[str, XSDDate]])

slots.aggregate_statistic = Slot(uri=GENERIC.aggregate_statistic, name="aggregate statistic", curie=GENERIC.curie('aggregate_statistic'),
                   model_uri=GENERIC.aggregate_statistic, domain=NamedThing, range=Optional[str])

slots.has_count = Slot(uri=GENERIC.has_count, name="has count", curie=GENERIC.curie('has_count'),
                   model_uri=GENERIC.has_count, domain=NamedThing, range=Optional[int])

slots.has_total = Slot(uri=GENERIC.has_total, name="has total", curie=GENERIC.curie('has_total'),
                   model_uri=GENERIC.has_total, domain=NamedThing, range=Optional[int])

slots.has_quotient = Slot(uri=GENERIC.has_quotient, name="has quotient", curie=GENERIC.curie('has_quotient'),
                   model_uri=GENERIC.has_quotient, domain=NamedThing, range=Optional[float])

slots.has_percentage = Slot(uri=GENERIC.has_percentage, name="has percentage", curie=GENERIC.curie('has_percentage'),
                   model_uri=GENERIC.has_percentage, domain=NamedThing, range=Optional[float])

slots.has_dataset = Slot(uri=DCTERMS.source, name="has dataset", curie=DCTERMS.curie('source'),
                   model_uri=GENERIC.has_dataset, domain=DatasetVersion, range=Optional[Union[str, DatasetId]])

slots.source_web_page = Slot(uri=GENERIC.source_web_page, name="source web page", curie=GENERIC.curie('source_web_page'),
                   model_uri=GENERIC.source_web_page, domain=DatasetSummary, range=Optional[str])

slots.source_logo = Slot(uri=SCHEMA.logo, name="source logo", curie=SCHEMA.curie('logo'),
                   model_uri=GENERIC.source_logo, domain=DatasetSummary, range=Optional[str])

slots.retrieved_on = Slot(uri=GENERIC.retrieved_on, name="retrieved on", curie=GENERIC.curie('retrieved_on'),
                   model_uri=GENERIC.retrieved_on, domain=Dataset, range=Optional[Union[str, XSDDate]])

slots.version_of = Slot(uri=GENERIC.version_of, name="version of", curie=GENERIC.curie('version_of'),
                   model_uri=GENERIC.version_of, domain=DatasetVersion, range=Optional[Union[str, DatasetSummaryId]])

slots.version = Slot(uri=GENERIC.version, name="version", curie=GENERIC.curie('version'),
                   model_uri=GENERIC.version, domain=Dataset, range=Optional[str])

slots.license = Slot(uri=GENERIC.license, name="license", curie=GENERIC.curie('license'),
                   model_uri=GENERIC.license, domain=InformationContentEntity, range=Optional[str])

slots.rights = Slot(uri=GENERIC.rights, name="rights", curie=GENERIC.curie('rights'),
                   model_uri=GENERIC.rights, domain=InformationContentEntity, range=Optional[str])

slots.copyright = Slot(uri=GENERIC.copyright, name="copyright", curie=GENERIC.curie('copyright'),
                   model_uri=GENERIC.copyright, domain=InformationContentEntity, range=Optional[str])

slots.format = Slot(uri=GENERIC.format, name="format", curie=GENERIC.curie('format'),
                   model_uri=GENERIC.format, domain=InformationContentEntity, range=Optional[str])

slots.created_with = Slot(uri=GENERIC.created_with, name="created with", curie=GENERIC.curie('created_with'),
                   model_uri=GENERIC.created_with, domain=Dataset, range=Optional[str])

slots.download_url = Slot(uri=DCAT.downloadURL, name="download url", curie=DCAT.curie('downloadURL'),
                   model_uri=GENERIC.download_url, domain=InformationContentEntity, range=Optional[str])

slots.dataset_download_url = Slot(uri=WIKIDATA.PROPERTY.P4945, name="dataset download url", curie=WIKIDATA.PROPERTY.curie('P4945'),
                   model_uri=GENERIC.dataset_download_url, domain=Dataset, range=Optional[str])

slots.distribution_download_url = Slot(uri=GENERIC.distribution_download_url, name="distribution download url", curie=GENERIC.curie('distribution_download_url'),
                   model_uri=GENERIC.distribution_download_url, domain=DatasetDistribution, range=Optional[str])

slots.ingest_date = Slot(uri=PAV.version, name="ingest date", curie=PAV.curie('version'),
                   model_uri=GENERIC.ingest_date, domain=DatasetVersion, range=Optional[str])

slots.has_distribution = Slot(uri=DCTERMS.distribution, name="has distribution", curie=DCTERMS.curie('distribution'),
                   model_uri=GENERIC.has_distribution, domain=DatasetVersion, range=Optional[Union[str, DatasetDistributionId]])

slots.published_in = Slot(uri=GENERIC.published_in, name="published in", curie=GENERIC.curie('published_in'),
                   model_uri=GENERIC.published_in, domain=Publication, range=Optional[Union[str, URIorCURIE]])

slots.iso_abbreviation = Slot(uri=GENERIC.iso_abbreviation, name="iso abbreviation", curie=GENERIC.curie('iso_abbreviation'),
                   model_uri=GENERIC.iso_abbreviation, domain=Publication, range=Optional[str])

slots.authors = Slot(uri=GENERIC.authors, name="authors", curie=GENERIC.curie('authors'),
                   model_uri=GENERIC.authors, domain=Publication, range=Optional[Union[str, List[str]]])

slots.volume = Slot(uri=GENERIC.volume, name="volume", curie=GENERIC.curie('volume'),
                   model_uri=GENERIC.volume, domain=Publication, range=Optional[str])

slots.chapter = Slot(uri=GENERIC.chapter, name="chapter", curie=GENERIC.curie('chapter'),
                   model_uri=GENERIC.chapter, domain=BookChapter, range=Optional[str])

slots.issue = Slot(uri=GENERIC.issue, name="issue", curie=GENERIC.curie('issue'),
                   model_uri=GENERIC.issue, domain=Publication, range=Optional[str])

slots.pages = Slot(uri=GENERIC.pages, name="pages", curie=GENERIC.curie('pages'),
                   model_uri=GENERIC.pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.summary = Slot(uri=GENERIC.summary, name="summary", curie=GENERIC.curie('summary'),
                   model_uri=GENERIC.summary, domain=Publication, range=Optional[str])

slots.keywords = Slot(uri=GENERIC.keywords, name="keywords", curie=GENERIC.curie('keywords'),
                   model_uri=GENERIC.keywords, domain=Publication, range=Optional[Union[str, List[str]]])

slots.lcsh_terms = Slot(uri=GENERIC.lcsh_terms, name="lcsh terms", curie=GENERIC.curie('lcsh_terms'),
                   model_uri=GENERIC.lcsh_terms, domain=Publication, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.has_computational_sequence = Slot(uri=GENERIC.has_computational_sequence, name="has computational sequence", curie=GENERIC.curie('has_computational_sequence'),
                   model_uri=GENERIC.has_computational_sequence, domain=NamedThing, range=Optional[Union[str, ComputationalSequence]])

slots.has_formula = Slot(uri=GENERIC.has_formula, name="has formula", curie=GENERIC.curie('has_formula'),
                   model_uri=GENERIC.has_formula, domain=NamedThing, range=Optional[str])

slots.has_device = Slot(uri=GENERIC.has_device, name="has device", curie=GENERIC.curie('has_device'),
                   model_uri=GENERIC.has_device, domain=NamedThing, range=Optional[Union[Union[str, DeviceId], List[Union[str, DeviceId]]]])

slots.temporal_context_qualifier = Slot(uri=GENERIC.temporal_context_qualifier, name="temporal context qualifier", curie=GENERIC.curie('temporal_context_qualifier'),
                   model_uri=GENERIC.temporal_context_qualifier, domain=Association, range=Optional[Union[str, TimeType]])

slots.temporal_interval_qualifier = Slot(uri=GENERIC.temporal_interval_qualifier, name="temporal interval qualifier", curie=GENERIC.curie('temporal_interval_qualifier'),
                   model_uri=GENERIC.temporal_interval_qualifier, domain=Association, range=Optional[Union[str, TimeType]])

slots.trade_name = Slot(uri=GENERIC.trade_name, name="trade name", curie=GENERIC.curie('trade_name'),
                   model_uri=GENERIC.trade_name, domain=NamedThing, range=Optional[Union[str, NamedThingId]])

slots.available_from = Slot(uri=GENERIC.available_from, name="available from", curie=GENERIC.curie('available_from'),
                   model_uri=GENERIC.available_from, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_control_role = Slot(uri=GENERIC.has_control_role, name="has control role", curie=GENERIC.curie('has_control_role'),
                   model_uri=GENERIC.has_control_role, domain=NamedThing, range=Optional[Union[Union[str, ControlRoleId], List[Union[str, ControlRoleId]]]])

slots.aspect_qualifier = Slot(uri=GENERIC.aspect_qualifier, name="aspect qualifier", curie=GENERIC.curie('aspect_qualifier'),
                   model_uri=GENERIC.aspect_qualifier, domain=Association, range=Optional[str])

slots.derivative_qualifier = Slot(uri=GENERIC.derivative_qualifier, name="derivative qualifier", curie=GENERIC.curie('derivative_qualifier'),
                   model_uri=GENERIC.derivative_qualifier, domain=Association, range=Optional[str])

slots.part_qualifier = Slot(uri=GENERIC.part_qualifier, name="part qualifier", curie=GENERIC.curie('part_qualifier'),
                   model_uri=GENERIC.part_qualifier, domain=Association, range=Optional[str])

slots.context_qualifier = Slot(uri=GENERIC.context_qualifier, name="context qualifier", curie=GENERIC.curie('context_qualifier'),
                   model_uri=GENERIC.context_qualifier, domain=Association, range=Optional[str])

slots.direction_qualifier = Slot(uri=GENERIC.direction_qualifier, name="direction qualifier", curie=GENERIC.curie('direction_qualifier'),
                   model_uri=GENERIC.direction_qualifier, domain=Association, range=Optional[str])

slots.exact_matches = Slot(uri=GENERIC.exact_matches, name="exact matches", curie=GENERIC.curie('exact_matches'),
                   model_uri=GENERIC.exact_matches, domain=None, range=Optional[Union[str, List[str]]])

slots.narrow_matches = Slot(uri=GENERIC.narrow_matches, name="narrow matches", curie=GENERIC.curie('narrow_matches'),
                   model_uri=GENERIC.narrow_matches, domain=None, range=Optional[Union[str, List[str]]])

slots.broad_matches = Slot(uri=GENERIC.broad_matches, name="broad matches", curie=GENERIC.curie('broad_matches'),
                   model_uri=GENERIC.broad_matches, domain=None, range=Optional[Union[str, List[str]]])

slots.qualified_predicate = Slot(uri=GENERIC.qualified_predicate, name="qualified predicate", curie=GENERIC.curie('qualified_predicate'),
                   model_uri=GENERIC.qualified_predicate, domain=Association, range=Optional[str])

slots.statement_qualifier = Slot(uri=GENERIC.statement_qualifier, name="statement qualifier", curie=GENERIC.curie('statement_qualifier'),
                   model_uri=GENERIC.statement_qualifier, domain=Association, range=Optional[str])

slots.qualifiers = Slot(uri=GENERIC.qualifiers, name="qualifiers", curie=GENERIC.curie('qualifiers'),
                   model_uri=GENERIC.qualifiers, domain=Association, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.frequency_qualifier = Slot(uri=GENERIC.frequency_qualifier, name="frequency qualifier", curie=GENERIC.curie('frequency_qualifier'),
                   model_uri=GENERIC.frequency_qualifier, domain=Association, range=Optional[Union[str, FrequencyValue]])

slots.severity_qualifier = Slot(uri=GENERIC.severity_qualifier, name="severity qualifier", curie=GENERIC.curie('severity_qualifier'),
                   model_uri=GENERIC.severity_qualifier, domain=Association, range=Optional[Union[str, SeverityValueId]])

slots.sex_qualifier = Slot(uri=GENERIC.sex_qualifier, name="sex qualifier", curie=GENERIC.curie('sex_qualifier'),
                   model_uri=GENERIC.sex_qualifier, domain=Association, range=Optional[Union[str, BiologicalSexId]])

slots.quantifier_qualifier = Slot(uri=GENERIC.quantifier_qualifier, name="quantifier qualifier", curie=GENERIC.curie('quantifier_qualifier'),
                   model_uri=GENERIC.quantifier_qualifier, domain=Association, range=Optional[Union[str, OntologyClassId]])

slots.related_to = Slot(uri=GENERIC.related_to, name="related to", curie=GENERIC.curie('related_to'),
                   model_uri=GENERIC.related_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.related_to_at_instance_level = Slot(uri=GENERIC.related_to_at_instance_level, name="related to at instance level", curie=GENERIC.curie('related_to_at_instance_level'),
                   model_uri=GENERIC.related_to_at_instance_level, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.associated_with = Slot(uri=GENERIC.associated_with, name="associated with", curie=GENERIC.curie('associated_with'),
                   model_uri=GENERIC.associated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.opposite_of = Slot(uri=GENERIC.opposite_of, name="opposite of", curie=GENERIC.curie('opposite_of'),
                   model_uri=GENERIC.opposite_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.mentions = Slot(uri=GENERIC.mentions, name="mentions", curie=GENERIC.curie('mentions'),
                   model_uri=GENERIC.mentions, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.mentioned_by = Slot(uri=GENERIC.mentioned_by, name="mentioned by", curie=GENERIC.curie('mentioned_by'),
                   model_uri=GENERIC.mentioned_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contributor = Slot(uri=GENERIC.contributor, name="contributor", curie=GENERIC.curie('contributor'),
                   model_uri=GENERIC.contributor, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.has_contributor = Slot(uri=GENERIC.has_contributor, name="has contributor", curie=GENERIC.curie('has_contributor'),
                   model_uri=GENERIC.has_contributor, domain=Agent, range=Optional[Union[Union[str, InformationContentEntityId], List[Union[str, InformationContentEntityId]]]])

slots.provider = Slot(uri=GENERIC.provider, name="provider", curie=GENERIC.curie('provider'),
                   model_uri=GENERIC.provider, domain=InformationContentEntity, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.has_provider = Slot(uri=GENERIC.has_provider, name="has provider", curie=GENERIC.curie('has_provider'),
                   model_uri=GENERIC.has_provider, domain=Agent, range=Optional[Union[Union[str, InformationContentEntityId], List[Union[str, InformationContentEntityId]]]])

slots.publisher = Slot(uri=GENERIC.publisher, name="publisher", curie=GENERIC.curie('publisher'),
                   model_uri=GENERIC.publisher, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.has_publisher = Slot(uri=GENERIC.has_publisher, name="has publisher", curie=GENERIC.curie('has_publisher'),
                   model_uri=GENERIC.has_publisher, domain=Agent, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.editor = Slot(uri=GENERIC.editor, name="editor", curie=GENERIC.curie('editor'),
                   model_uri=GENERIC.editor, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.has_editor = Slot(uri=GENERIC.has_editor, name="has editor", curie=GENERIC.curie('has_editor'),
                   model_uri=GENERIC.has_editor, domain=Agent, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.author = Slot(uri=GENERIC.author, name="author", curie=GENERIC.curie('author'),
                   model_uri=GENERIC.author, domain=Publication, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.has_author = Slot(uri=GENERIC.has_author, name="has author", curie=GENERIC.curie('has_author'),
                   model_uri=GENERIC.has_author, domain=Agent, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.assesses = Slot(uri=GENERIC.assesses, name="assesses", curie=GENERIC.curie('assesses'),
                   model_uri=GENERIC.assesses, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_assessed_by = Slot(uri=GENERIC.is_assessed_by, name="is assessed by", curie=GENERIC.curie('is_assessed_by'),
                   model_uri=GENERIC.is_assessed_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.interacts_with = Slot(uri=GENERIC.interacts_with, name="interacts with", curie=GENERIC.curie('interacts_with'),
                   model_uri=GENERIC.interacts_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.affects = Slot(uri=GENERIC.affects, name="affects", curie=GENERIC.curie('affects'),
                   model_uri=GENERIC.affects, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.affected_by = Slot(uri=GENERIC.affected_by, name="affected by", curie=GENERIC.curie('affected_by'),
                   model_uri=GENERIC.affected_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.identifies = Slot(uri=GENERIC.identifies, name="identifies", curie=GENERIC.curie('identifies'),
                   model_uri=GENERIC.identifies, domain=Association, range=Optional[Union[Union[str, InformationContentEntityId], List[Union[str, InformationContentEntityId]]]])

slots.is_name_of = Slot(uri=GENERIC.is_name_of, name="is name of", curie=GENERIC.curie('is_name_of'),
                   model_uri=GENERIC.is_name_of, domain=Name, range=Optional[Union[Union[str, InformationContentEntityId], List[Union[str, InformationContentEntityId]]]])

slots.defines = Slot(uri=GENERIC.defines, name="defines", curie=GENERIC.curie('defines'),
                   model_uri=GENERIC.defines, domain=InformationContentEntity, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.is_defined_by = Slot(uri=GENERIC.is_defined_by, name="is defined by", curie=GENERIC.curie('is_defined_by'),
                   model_uri=GENERIC.is_defined_by, domain=NamedThing, range=Optional[Union[Union[str, InformationContentEntityId], List[Union[str, InformationContentEntityId]]]])

slots.homologous_to = Slot(uri=GENERIC.homologous_to, name="homologous to", curie=GENERIC.curie('homologous_to'),
                   model_uri=GENERIC.homologous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.paralogous_to = Slot(uri=GENERIC.paralogous_to, name="paralogous to", curie=GENERIC.curie('paralogous_to'),
                   model_uri=GENERIC.paralogous_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.coexists_with = Slot(uri=GENERIC.coexists_with, name="coexists with", curie=GENERIC.curie('coexists_with'),
                   model_uri=GENERIC.coexists_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.correlated_with = Slot(uri=GENERIC.correlated_with, name="correlated with", curie=GENERIC.curie('correlated_with'),
                   model_uri=GENERIC.correlated_with, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.occurs_in = Slot(uri=GENERIC.occurs_in, name="occurs in", curie=GENERIC.curie('occurs_in'),
                   model_uri=GENERIC.occurs_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.contains_process = Slot(uri=GENERIC.contains_process, name="contains process", curie=GENERIC.curie('contains_process'),
                   model_uri=GENERIC.contains_process, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.located_in = Slot(uri=GENERIC.located_in, name="located in", curie=GENERIC.curie('located_in'),
                   model_uri=GENERIC.located_in, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.location_of = Slot(uri=GENERIC.location_of, name="location of", curie=GENERIC.curie('location_of'),
                   model_uri=GENERIC.location_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.similar_to = Slot(uri=GENERIC.similar_to, name="similar to", curie=GENERIC.curie('similar_to'),
                   model_uri=GENERIC.similar_to, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.model_of = Slot(uri=GENERIC.model_of, name="model of", curie=GENERIC.curie('model_of'),
                   model_uri=GENERIC.model_of, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.models = Slot(uri=GENERIC.models, name="models", curie=GENERIC.curie('models'),
                   model_uri=GENERIC.models, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.overlaps = Slot(uri=GENERIC.overlaps, name="overlaps", curie=GENERIC.curie('overlaps'),
                   model_uri=GENERIC.overlaps, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_part = Slot(uri=GENERIC.has_part, name="has part", curie=GENERIC.curie('has_part'),
                   model_uri=GENERIC.has_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_participant = Slot(uri=GENERIC.has_participant, name="has participant", curie=GENERIC.curie('has_participant'),
                   model_uri=GENERIC.has_participant, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.catalyzes = Slot(uri=GENERIC.catalyzes, name="catalyzes", curie=GENERIC.curie('catalyzes'),
                   model_uri=GENERIC.catalyzes, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.has_catalyst = Slot(uri=GENERIC.has_catalyst, name="has catalyst", curie=GENERIC.curie('has_catalyst'),
                   model_uri=GENERIC.has_catalyst, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.participates_in = Slot(uri=GENERIC.participates_in, name="participates in", curie=GENERIC.curie('participates_in'),
                   model_uri=GENERIC.participates_in, domain=NamedThing, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.produces = Slot(uri=GENERIC.produces, name="produces", curie=GENERIC.curie('produces'),
                   model_uri=GENERIC.produces, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.produced_by = Slot(uri=GENERIC.produced_by, name="produced by", curie=GENERIC.curie('produced_by'),
                   model_uri=GENERIC.produced_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.temporally_related_to = Slot(uri=GENERIC.temporally_related_to, name="temporally related to", curie=GENERIC.curie('temporally_related_to'),
                   model_uri=GENERIC.temporally_related_to, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.precedes = Slot(uri=GENERIC.precedes, name="precedes", curie=GENERIC.curie('precedes'),
                   model_uri=GENERIC.precedes, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.preceded_by = Slot(uri=GENERIC.preceded_by, name="preceded by", curie=GENERIC.curie('preceded_by'),
                   model_uri=GENERIC.preceded_by, domain=None, range=Optional[Union[Union[dict, "Occurrent"], List[Union[dict, "Occurrent"]]]])

slots.has_variant_part = Slot(uri=GENERIC.has_variant_part, name="has variant part", curie=GENERIC.curie('has_variant_part'),
                   model_uri=GENERIC.has_variant_part, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.related_condition = Slot(uri=GENERIC.related_condition, name="related condition", curie=GENERIC.curie('related_condition'),
                   model_uri=GENERIC.related_condition, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_not_completed = Slot(uri=GENERIC.has_not_completed, name="has not completed", curie=GENERIC.curie('has_not_completed'),
                   model_uri=GENERIC.has_not_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.not_completed_by = Slot(uri=GENERIC.not_completed_by, name="not completed by", curie=GENERIC.curie('not_completed_by'),
                   model_uri=GENERIC.not_completed_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_completed = Slot(uri=GENERIC.has_completed, name="has completed", curie=GENERIC.curie('has_completed'),
                   model_uri=GENERIC.has_completed, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.completed_by = Slot(uri=GENERIC.completed_by, name="completed by", curie=GENERIC.curie('completed_by'),
                   model_uri=GENERIC.completed_by, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.in_taxon = Slot(uri=GENERIC.in_taxon, name="in taxon", curie=GENERIC.curie('in_taxon'),
                   model_uri=GENERIC.in_taxon, domain=None, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.taxon_of = Slot(uri=GENERIC.taxon_of, name="taxon of", curie=GENERIC.curie('taxon_of'),
                   model_uri=GENERIC.taxon_of, domain=NamedThing, range=Optional[Union[Union[dict, "ThingWithTaxon"], List[Union[dict, "ThingWithTaxon"]]]])

slots.association_slot = Slot(uri=GENERIC.association_slot, name="association slot", curie=GENERIC.curie('association_slot'),
                   model_uri=GENERIC.association_slot, domain=Association, range=Optional[str])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=GENERIC.subject, domain=Association, range=Union[str, NamedThingId])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=GENERIC.object, domain=Association, range=Union[str, NamedThingId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=GENERIC.predicate, domain=Association, range=Union[str, PredicateType])

slots.negated = Slot(uri=GENERIC.negated, name="negated", curie=GENERIC.curie('negated'),
                   model_uri=GENERIC.negated, domain=Association, range=Optional[Union[bool, Bool]])

slots.has_evidence = Slot(uri=GENERIC.has_evidence, name="has evidence", curie=GENERIC.curie('has_evidence'),
                   model_uri=GENERIC.has_evidence, domain=Association, range=Optional[Union[Union[str, EvidenceTypeId], List[Union[str, EvidenceTypeId]]]])

slots.provided_by = Slot(uri=GENERIC.provided_by, name="provided by", curie=GENERIC.curie('provided_by'),
                   model_uri=GENERIC.provided_by, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.knowledge_source = Slot(uri=GENERIC.knowledge_source, name="knowledge source", curie=GENERIC.curie('knowledge_source'),
                   model_uri=GENERIC.knowledge_source, domain=Association, range=Optional[Union[str, InformationResourceId]])

slots.primary_knowledge_source = Slot(uri=GENERIC.primary_knowledge_source, name="primary knowledge source", curie=GENERIC.curie('primary_knowledge_source'),
                   model_uri=GENERIC.primary_knowledge_source, domain=Association, range=Optional[Union[str, InformationResourceId]])

slots.aggregator_knowledge_source = Slot(uri=GENERIC.aggregator_knowledge_source, name="aggregator knowledge source", curie=GENERIC.curie('aggregator_knowledge_source'),
                   model_uri=GENERIC.aggregator_knowledge_source, domain=Association, range=Optional[Union[Union[str, InformationResourceId], List[Union[str, InformationResourceId]]]])

slots.supporting_documents = Slot(uri=GENERIC.supporting_documents, name="supporting documents", curie=GENERIC.curie('supporting_documents'),
                   model_uri=GENERIC.supporting_documents, domain=Association, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.supporting_data_source = Slot(uri=GENERIC.supporting_data_source, name="supporting data source", curie=GENERIC.curie('supporting_data_source'),
                   model_uri=GENERIC.supporting_data_source, domain=Association, range=Optional[Union[Union[str, InformationResourceId], List[Union[str, InformationResourceId]]]])

slots.supporting_data_set = Slot(uri=GENERIC.supporting_data_set, name="supporting data set", curie=GENERIC.curie('supporting_data_set'),
                   model_uri=GENERIC.supporting_data_set, domain=Association, range=Optional[Union[Union[str, InformationResourceId], List[Union[str, InformationResourceId]]]])

slots.evidence_count = Slot(uri=GENERIC.evidence_count, name="evidence count", curie=GENERIC.curie('evidence_count'),
                   model_uri=GENERIC.evidence_count, domain=Association, range=Optional[int])

slots.expected_count = Slot(uri=GENERIC.expected_count, name="expected count", curie=GENERIC.curie('expected_count'),
                   model_uri=GENERIC.expected_count, domain=Association, range=Optional[str])

slots.publications = Slot(uri=GENERIC.publications, name="publications", curie=GENERIC.curie('publications'),
                   model_uri=GENERIC.publications, domain=Association, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.start_coordinate = Slot(uri=GENERIC.start_coordinate, name="start coordinate", curie=GENERIC.curie('start_coordinate'),
                   model_uri=GENERIC.start_coordinate, domain=None, range=Optional[int])

slots.end_coordinate = Slot(uri=GENERIC.end_coordinate, name="end coordinate", curie=GENERIC.curie('end_coordinate'),
                   model_uri=GENERIC.end_coordinate, domain=None, range=Optional[int])

slots.device = Slot(uri=GENERIC.device, name="device", curie=GENERIC.curie('device'),
                   model_uri=GENERIC.device, domain=Association, range=Optional[str])

slots.Attribute_name = Slot(uri=RDFS.label, name="Attribute_name", curie=RDFS.curie('label'),
                   model_uri=GENERIC.Attribute_name, domain=Attribute, range=Optional[Union[str, LabelType]])

slots.NamedThing_category = Slot(uri=GENERIC.category, name="NamedThing_category", curie=GENERIC.curie('category'),
                   model_uri=GENERIC.NamedThing_category, domain=NamedThing, range=Union[Union[str, CategoryType], List[Union[str, CategoryType]]],
                   pattern=re.compile(r'^universal:[A-Z][A-Za-z]+$'))

slots.Designation_has_text_value = Slot(uri=XSD.string, name="Designation_has text value", curie=XSD.curie('string'),
                   model_uri=GENERIC.Designation_has_text_value, domain=Designation, range=Optional[str])

slots.Agent_id = Slot(uri=GENERIC.id, name="Agent_id", curie=GENERIC.curie('id'),
                   model_uri=GENERIC.Agent_id, domain=Agent, range=Union[str, AgentId])

slots.Agent_name = Slot(uri=RDFS.label, name="Agent_name", curie=RDFS.curie('label'),
                   model_uri=GENERIC.Agent_name, domain=Agent, range=Optional[Union[str, LabelType]])

slots.Publication_id = Slot(uri=GENERIC.id, name="Publication_id", curie=GENERIC.curie('id'),
                   model_uri=GENERIC.Publication_id, domain=Publication, range=Union[str, PublicationId])

slots.Publication_name = Slot(uri=RDFS.label, name="Publication_name", curie=RDFS.curie('label'),
                   model_uri=GENERIC.Publication_name, domain=Publication, range=Optional[Union[str, LabelType]])

slots.Publication_type = Slot(uri=DCTERMS.type, name="Publication_type", curie=DCTERMS.curie('type'),
                   model_uri=GENERIC.Publication_type, domain=Publication, range=str)

slots.Publication_pages = Slot(uri=GENERIC.pages, name="Publication_pages", curie=GENERIC.curie('pages'),
                   model_uri=GENERIC.Publication_pages, domain=Publication, range=Optional[Union[str, List[str]]])

slots.book_id = Slot(uri=GENERIC.id, name="book_id", curie=GENERIC.curie('id'),
                   model_uri=GENERIC.book_id, domain=Book, range=Union[str, BookId])

slots.book_type = Slot(uri=RDF.type, name="book_type", curie=RDF.curie('type'),
                   model_uri=GENERIC.book_type, domain=Book, range=str)

slots.book_chapter_published_in = Slot(uri=GENERIC.published_in, name="book chapter_published in", curie=GENERIC.curie('published_in'),
                   model_uri=GENERIC.book_chapter_published_in, domain=BookChapter, range=Union[str, URIorCURIE])

slots.Serial_id = Slot(uri=GENERIC.id, name="Serial_id", curie=GENERIC.curie('id'),
                   model_uri=GENERIC.Serial_id, domain=Serial, range=Union[str, SerialId])

slots.Serial_type = Slot(uri=RDF.type, name="Serial_type", curie=RDF.curie('type'),
                   model_uri=GENERIC.Serial_type, domain=Serial, range=str)

slots.Article_published_in = Slot(uri=GENERIC.published_in, name="Article_published in", curie=GENERIC.curie('published_in'),
                   model_uri=GENERIC.Article_published_in, domain=Article, range=Union[str, URIorCURIE])

slots.Article_iso_abbreviation = Slot(uri=GENERIC.iso_abbreviation, name="Article_iso abbreviation", curie=GENERIC.curie('iso_abbreviation'),
                   model_uri=GENERIC.Article_iso_abbreviation, domain=Article, range=Optional[str])

slots.Association_type = Slot(uri=RDF.type, name="Association_type", curie=RDF.curie('type'),
                   model_uri=GENERIC.Association_type, domain=Association, range=Optional[str])

slots.Association_category = Slot(uri=GENERIC.category, name="Association_category", curie=GENERIC.curie('category'),
                   model_uri=GENERIC.Association_category, domain=Association, range=Optional[Union[Union[str, CategoryType], List[Union[str, CategoryType]]]])
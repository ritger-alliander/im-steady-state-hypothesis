# Auto generated from im_steady_state_hypothesis.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-04-23T15:07:42
# Schema: SteadyStateHypothesisProfile
#
# id: http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EU#Package_SteadyStateHypothesisProfile
# description: This vocabulary is describing the steady state hypothesis profile from IEC 61970-600-2.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Float, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
STEADYSTATEHYPOTHESISPROFILE = CurieNamespace('SteadyStateHypothesisProfile', 'http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EU#Package_SteadyStateHypothesisProfile/')
TC57CIM = CurieNamespace('TC57CIM', 'https://cim.ucaiug.io/ns#TC57CIM/')
CIM = CurieNamespace('cim', 'http://iec.ch/TC57/CIM100#')
CIMS = CurieNamespace('cims', 'http://iec.ch/TC57/1999/rdf-schema-extensions-19990926#')
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EU = CurieNamespace('eu', 'http://iec.ch/TC57/CIM100-European#')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
GITHUB = CurieNamespace('github', 'https://github.com/')
IDOT = CurieNamespace('idot', 'http://identifiers.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OA = CurieNamespace('oa', 'http://www.w3.org/ns/oa#')
OBOINOWL = CurieNamespace('oboInOwl', 'http://www.geneontology.org/formats/oboInOwl#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROFCIM = CurieNamespace('profcim', 'http://iec.ch/TC57/ns/CIM/prof-cim#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SH = CurieNamespace('sh', 'http://www.w3.org/ns/shacl#')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SSH = CurieNamespace('ssh', 'http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EU#')
THIS = CurieNamespace('this', 'http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EU#Package_SteadyStateHypothesisProfile')
VOID = CurieNamespace('void', 'http://rdfs.org/ns/void#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = THIS


# Types

# Class references



@dataclass
class IdentifiedObject(YAMLRoot):
    """
    This is a root class to provide common identification for all classes needing identification and naming attributes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["IdentifiedObject"]
    class_class_curie: ClassVar[str] = "cim:IdentifiedObject"
    class_name: ClassVar[str] = "IdentifiedObject"
    class_model_uri: ClassVar[URIRef] = THIS.IdentifiedObject

    m_rid: str = None
    names: Optional[Union[Union[dict, "Name"], List[Union[dict, "Name"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.m_rid):
            self.MissingRequiredField("m_rid")
        if not isinstance(self.m_rid, str):
            self.m_rid = str(self.m_rid)

        self._normalize_inlined_as_dict(slot_name="names", slot_type=Name, key_name="name_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class PowerSystemResource(IdentifiedObject):
    """
    A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many
    individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power
    system resources can have measurements associated.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["PowerSystemResource"]
    class_class_curie: ClassVar[str] = "cim:PowerSystemResource"
    class_name: ClassVar[str] = "PowerSystemResource"
    class_model_uri: ClassVar[URIRef] = THIS.PowerSystemResource

    m_rid: str = None

@dataclass
class Equipment(PowerSystemResource):
    """
    The parts of a power system that are physical devices, electronic or mechanical.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["Equipment"]
    class_class_curie: ClassVar[str] = "cim:Equipment"
    class_name: ClassVar[str] = "Equipment"
    class_model_uri: ClassVar[URIRef] = THIS.Equipment

    m_rid: str = None
    in_service: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.in_service):
            self.MissingRequiredField("in_service")
        if not isinstance(self.in_service, Bool):
            self.in_service = Bool(self.in_service)

        super().__post_init__(**kwargs)


@dataclass
class ConductingEquipment(Equipment):
    """
    The parts of the AC power system that are designed to carry current or that are conductively connected through
    terminals.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["ConductingEquipment"]
    class_class_curie: ClassVar[str] = "cim:ConductingEquipment"
    class_name: ClassVar[str] = "ConductingEquipment"
    class_model_uri: ClassVar[URIRef] = THIS.ConductingEquipment

    m_rid: str = None
    in_service: Union[bool, Bool] = None

@dataclass
class Switch(ConductingEquipment):
    """
    A generic device designed to close, or open, or both, one or more electric circuits. All switches are two terminal
    devices including grounding switches. The ACDCTerminal.connected at the two sides of the switch shall not be
    considered for assessing switch connectivity, i.e. only Switch.open, .normalOpen and .locked are relevant.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["Switch"]
    class_class_curie: ClassVar[str] = "cim:Switch"
    class_name: ClassVar[str] = "Switch"
    class_model_uri: ClassVar[URIRef] = THIS.Switch

    m_rid: str = None
    in_service: Union[bool, Bool] = None
    open: Union[bool, Bool] = None
    locked: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.open):
            self.MissingRequiredField("open")
        if not isinstance(self.open, Bool):
            self.open = Bool(self.open)

        if self._is_empty(self.locked):
            self.MissingRequiredField("locked")
        if not isinstance(self.locked, Bool):
            self.locked = Bool(self.locked)

        super().__post_init__(**kwargs)


@dataclass
class ProtectedSwitch(Switch):
    """
    A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["ProtectedSwitch"]
    class_class_curie: ClassVar[str] = "cim:ProtectedSwitch"
    class_name: ClassVar[str] = "ProtectedSwitch"
    class_model_uri: ClassVar[URIRef] = THIS.ProtectedSwitch

    m_rid: str = None
    in_service: Union[bool, Bool] = None
    open: Union[bool, Bool] = None
    locked: Union[bool, Bool] = None

@dataclass
class Breaker(ProtectedSwitch):
    """
    A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions
    and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions
    e.g. those of short circuit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["Breaker"]
    class_class_curie: ClassVar[str] = "cim:Breaker"
    class_name: ClassVar[str] = "Breaker"
    class_model_uri: ClassVar[URIRef] = THIS.Breaker

    m_rid: str = None
    in_service: Union[bool, Bool] = None
    open: Union[bool, Bool] = None
    locked: Union[bool, Bool] = None

@dataclass
class Disconnector(Switch):
    """
    A manually operated or motor operated mechanical switching device used for changing the connections in a circuit,
    or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when
    negligible current is broken or made.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["Disconnector"]
    class_class_curie: ClassVar[str] = "cim:Disconnector"
    class_name: ClassVar[str] = "Disconnector"
    class_model_uri: ClassVar[URIRef] = THIS.Disconnector

    m_rid: str = None
    in_service: Union[bool, Bool] = None
    open: Union[bool, Bool] = None
    locked: Union[bool, Bool] = None

@dataclass
class ActivePower(YAMLRoot):
    """
    Product of RMS value of the voltage and the RMS value of the in-phase component of the current.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["ActivePower"]
    class_class_curie: ClassVar[str] = "cim:ActivePower"
    class_name: ClassVar[str] = "ActivePower"
    class_model_uri: ClassVar[URIRef] = THIS.ActivePower

    value: Optional[float] = None
    multiplier: Optional[Union[str, "UnitMultiplier"]] = None
    unit: Optional[Union[str, "UnitSymbol"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.multiplier is not None and not isinstance(self.multiplier, UnitMultiplier):
            self.multiplier = UnitMultiplier(self.multiplier)

        if self.unit is not None and not isinstance(self.unit, UnitSymbol):
            self.unit = UnitSymbol(self.unit)

        super().__post_init__(**kwargs)


@dataclass
class ReactivePower(YAMLRoot):
    """
    Product of RMS value of the voltage and the RMS value of the quadrature component of the current.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["ReactivePower"]
    class_class_curie: ClassVar[str] = "cim:ReactivePower"
    class_name: ClassVar[str] = "ReactivePower"
    class_model_uri: ClassVar[URIRef] = THIS.ReactivePower

    value: Optional[float] = None
    unit: Optional[Union[str, "UnitSymbol"]] = None
    multiplier: Optional[Union[str, "UnitMultiplier"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.unit is not None and not isinstance(self.unit, UnitSymbol):
            self.unit = UnitSymbol(self.unit)

        if self.multiplier is not None and not isinstance(self.multiplier, UnitMultiplier):
            self.multiplier = UnitMultiplier(self.multiplier)

        super().__post_init__(**kwargs)


@dataclass
class EnergyConnection(ConductingEquipment):
    """
    A connection of energy generation or consumption on the power system model.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["EnergyConnection"]
    class_class_curie: ClassVar[str] = "cim:EnergyConnection"
    class_name: ClassVar[str] = "EnergyConnection"
    class_model_uri: ClassVar[URIRef] = THIS.EnergyConnection

    m_rid: str = None
    in_service: Union[bool, Bool] = None

@dataclass
class EnergyConsumer(EnergyConnection):
    """
    Generic user of energy - a  point of consumption on the power system model.
    EnergyConsumer.pfixed, .qfixed, .pfixedPct and .qfixedPct have meaning only if there is no
    LoadResponseCharacteristic associated with EnergyConsumer or if LoadResponseCharacteristic.exponentModel is set to
    False.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["EnergyConsumer"]
    class_class_curie: ClassVar[str] = "cim:EnergyConsumer"
    class_name: ClassVar[str] = "EnergyConsumer"
    class_model_uri: ClassVar[URIRef] = THIS.EnergyConsumer

    m_rid: str = None
    in_service: Union[bool, Bool] = None
    p: Union[dict, ActivePower] = None
    q: Union[dict, ReactivePower] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.p):
            self.MissingRequiredField("p")
        if not isinstance(self.p, ActivePower):
            self.p = ActivePower(**as_dict(self.p))

        if self._is_empty(self.q):
            self.MissingRequiredField("q")
        if not isinstance(self.q, ReactivePower):
            self.q = ReactivePower(**as_dict(self.q))

        super().__post_init__(**kwargs)


@dataclass
class LoadBreakSwitch(ProtectedSwitch):
    """
    A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["LoadBreakSwitch"]
    class_class_curie: ClassVar[str] = "cim:LoadBreakSwitch"
    class_name: ClassVar[str] = "LoadBreakSwitch"
    class_model_uri: ClassVar[URIRef] = THIS.LoadBreakSwitch

    m_rid: str = None
    in_service: Union[bool, Bool] = None
    open: Union[bool, Bool] = None
    locked: Union[bool, Bool] = None

@dataclass
class ACDCTerminal(IdentifiedObject):
    """
    An electrical connection point (AC or DC) to a piece of conducting equipment. Terminals are connected at physical
    connection points called connectivity nodes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["ACDCTerminal"]
    class_class_curie: ClassVar[str] = "cim:ACDCTerminal"
    class_name: ClassVar[str] = "ACDCTerminal"
    class_model_uri: ClassVar[URIRef] = THIS.ACDCTerminal

    m_rid: str = None
    connected: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.connected):
            self.MissingRequiredField("connected")
        if not isinstance(self.connected, Bool):
            self.connected = Bool(self.connected)

        super().__post_init__(**kwargs)


@dataclass
class Terminal(ACDCTerminal):
    """
    An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical
    connection points called connectivity nodes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["Terminal"]
    class_class_curie: ClassVar[str] = "cim:Terminal"
    class_name: ClassVar[str] = "Terminal"
    class_model_uri: ClassVar[URIRef] = THIS.Terminal

    m_rid: str = None
    connected: Union[bool, Bool] = None

@dataclass
class Name(YAMLRoot):
    """
    The Name class provides the means to define any number of human readable names for an object. A name is <b>not</b>
    to be used for defining inter-object relationships. For inter-object relationships instead use the object
    identification 'mRID'.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["Name"]
    class_class_curie: ClassVar[str] = "cim:Name"
    class_name: ClassVar[str] = "Name"
    class_model_uri: ClassVar[URIRef] = THIS.Name

    name_type: Union[dict, "NameType"] = None
    identified_object: Union[dict, IdentifiedObject] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name_type):
            self.MissingRequiredField("name_type")
        if not isinstance(self.name_type, NameType):
            self.name_type = NameType(**as_dict(self.name_type))

        if self._is_empty(self.identified_object):
            self.MissingRequiredField("identified_object")
        if not isinstance(self.identified_object, IdentifiedObject):
            self.identified_object = IdentifiedObject(**as_dict(self.identified_object))

        super().__post_init__(**kwargs)


@dataclass
class NameType(YAMLRoot):
    """
    Type of name. Possible values for attribute 'name' are implementation dependent but standard profiles may specify
    types. An enterprise may have multiple IT systems each having its own local name for the same object, e.g. a
    planning system may have different names from an EMS. An object may also have different names within the same IT
    system, e.g. localName as defined in CIM version 14. The definition from CIM14 is:
    The localName is a human readable name of the object. It is a free text name local to a node in a naming hierarchy
    similar to a file directory structure. A power system related naming hierarchy may be: Substation, VoltageLevel,
    Equipment etc. Children of the same parent in such a hierarchy have names that typically are unique among them.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["NameType"]
    class_class_curie: ClassVar[str] = "cim:NameType"
    class_name: ClassVar[str] = "NameType"
    class_model_uri: ClassVar[URIRef] = THIS.NameType

    description: Optional[str] = None
    name_type_authority: Optional[Union[dict, "NameTypeAuthority"]] = None
    names: Optional[Union[Union[dict, Name], List[Union[dict, Name]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.name_type_authority is not None and not isinstance(self.name_type_authority, NameTypeAuthority):
            self.name_type_authority = NameTypeAuthority(**as_dict(self.name_type_authority))

        self._normalize_inlined_as_dict(slot_name="names", slot_type=Name, key_name="name_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class NameTypeAuthority(YAMLRoot):
    """
    Authority responsible for creation and management of names of a given type; typically an organization or an
    enterprise system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CIM["NameTypeAuthority"]
    class_class_curie: ClassVar[str] = "cim:NameTypeAuthority"
    class_name: ClassVar[str] = "NameTypeAuthority"
    class_model_uri: ClassVar[URIRef] = THIS.NameTypeAuthority

    description: Optional[str] = None
    name_types: Optional[Union[Union[dict, NameType], List[Union[dict, NameType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.name_types, list):
            self.name_types = [self.name_types] if self.name_types is not None else []
        self.name_types = [v if isinstance(v, NameType) else NameType(**as_dict(v)) for v in self.name_types]

        super().__post_init__(**kwargs)


# Enumerations
class UnitMultiplier(EnumDefinitionImpl):

    y = PermissibleValue(
        text="y",
        meaning=CIM["UnitMultiplier.y"])
    z = PermissibleValue(
        text="z",
        meaning=CIM["UnitMultiplier.z"])
    a = PermissibleValue(
        text="a",
        meaning=CIM["UnitMultiplier.a"])
    f = PermissibleValue(
        text="f",
        meaning=CIM["UnitMultiplier.f"])
    p = PermissibleValue(
        text="p",
        meaning=CIM["UnitMultiplier.p"])
    n = PermissibleValue(
        text="n",
        meaning=CIM["UnitMultiplier.n"])
    micro = PermissibleValue(
        text="micro",
        meaning=CIM["UnitMultiplier.micro"])
    m = PermissibleValue(
        text="m",
        meaning=CIM["UnitMultiplier.m"])
    c = PermissibleValue(
        text="c",
        meaning=CIM["UnitMultiplier.c"])
    d = PermissibleValue(
        text="d",
        meaning=CIM["UnitMultiplier.d"])
    none = PermissibleValue(
        text="none",
        meaning=CIM["UnitMultiplier.none"])
    da = PermissibleValue(
        text="da",
        meaning=CIM["UnitMultiplier.da"])
    h = PermissibleValue(
        text="h",
        meaning=CIM["UnitMultiplier.h"])
    k = PermissibleValue(
        text="k",
        meaning=CIM["UnitMultiplier.k"])
    M = PermissibleValue(
        text="M",
        meaning=CIM["UnitMultiplier.M"])
    G = PermissibleValue(
        text="G",
        meaning=CIM["UnitMultiplier.G"])
    T = PermissibleValue(
        text="T",
        meaning=CIM["UnitMultiplier.T"])
    P = PermissibleValue(
        text="P",
        meaning=CIM["UnitMultiplier.P"])
    E = PermissibleValue(
        text="E",
        meaning=CIM["UnitMultiplier.E"])
    Z = PermissibleValue(
        text="Z",
        meaning=CIM["UnitMultiplier.Z"])
    Y = PermissibleValue(
        text="Y",
        meaning=CIM["UnitMultiplier.Y"])

    _defn = EnumDefinition(
        name="UnitMultiplier",
    )

class UnitSymbol(EnumDefinitionImpl):

    none = PermissibleValue(
        text="none",
        meaning=CIM["UnitSymbol.none"])
    m = PermissibleValue(
        text="m",
        meaning=CIM["UnitSymbol.m"])
    kg = PermissibleValue(
        text="kg",
        meaning=CIM["UnitSymbol.kg"])
    s = PermissibleValue(
        text="s",
        meaning=CIM["UnitSymbol.s"])
    A = PermissibleValue(
        text="A",
        meaning=CIM["UnitSymbol.A"])
    K = PermissibleValue(
        text="K",
        meaning=CIM["UnitSymbol.K"])
    mol = PermissibleValue(
        text="mol",
        meaning=CIM["UnitSymbol.mol"])
    cd = PermissibleValue(
        text="cd",
        meaning=CIM["UnitSymbol.cd"])
    deg = PermissibleValue(
        text="deg",
        meaning=CIM["UnitSymbol.deg"])
    rad = PermissibleValue(
        text="rad",
        meaning=CIM["UnitSymbol.rad"])
    sr = PermissibleValue(
        text="sr",
        meaning=CIM["UnitSymbol.sr"])
    Gy = PermissibleValue(
        text="Gy",
        meaning=CIM["UnitSymbol.Gy"])
    Bq = PermissibleValue(
        text="Bq",
        meaning=CIM["UnitSymbol.Bq"])
    degC = PermissibleValue(
        text="degC",
        meaning=CIM["UnitSymbol.degC"])
    Sv = PermissibleValue(
        text="Sv",
        meaning=CIM["UnitSymbol.Sv"])
    F = PermissibleValue(
        text="F",
        meaning=CIM["UnitSymbol.F"])
    C = PermissibleValue(
        text="C",
        meaning=CIM["UnitSymbol.C"])
    S = PermissibleValue(
        text="S",
        meaning=CIM["UnitSymbol.S"])
    H = PermissibleValue(
        text="H",
        meaning=CIM["UnitSymbol.H"])
    V = PermissibleValue(
        text="V",
        meaning=CIM["UnitSymbol.V"])
    ohm = PermissibleValue(
        text="ohm",
        meaning=CIM["UnitSymbol.ohm"])
    J = PermissibleValue(
        text="J",
        meaning=CIM["UnitSymbol.J"])
    N = PermissibleValue(
        text="N",
        meaning=CIM["UnitSymbol.N"])
    Hz = PermissibleValue(
        text="Hz",
        meaning=CIM["UnitSymbol.Hz"])
    lx = PermissibleValue(
        text="lx",
        meaning=CIM["UnitSymbol.lx"])
    lm = PermissibleValue(
        text="lm",
        meaning=CIM["UnitSymbol.lm"])
    Wb = PermissibleValue(
        text="Wb",
        meaning=CIM["UnitSymbol.Wb"])
    T = PermissibleValue(
        text="T",
        meaning=CIM["UnitSymbol.T"])
    W = PermissibleValue(
        text="W",
        meaning=CIM["UnitSymbol.W"])
    Pa = PermissibleValue(
        text="Pa",
        meaning=CIM["UnitSymbol.Pa"])
    m2 = PermissibleValue(
        text="m2",
        meaning=CIM["UnitSymbol.m2"])
    m3 = PermissibleValue(
        text="m3",
        meaning=CIM["UnitSymbol.m3"])
    mPers = PermissibleValue(
        text="mPers",
        meaning=CIM["UnitSymbol.mPers"])
    mPers2 = PermissibleValue(
        text="mPers2",
        meaning=CIM["UnitSymbol.mPers2"])
    m3Pers = PermissibleValue(
        text="m3Pers",
        meaning=CIM["UnitSymbol.m3Pers"])
    mPerm3 = PermissibleValue(
        text="mPerm3",
        meaning=CIM["UnitSymbol.mPerm3"])
    kgm = PermissibleValue(
        text="kgm",
        meaning=CIM["UnitSymbol.kgm"])
    kgPerm3 = PermissibleValue(
        text="kgPerm3",
        meaning=CIM["UnitSymbol.kgPerm3"])
    m2Pers = PermissibleValue(
        text="m2Pers",
        meaning=CIM["UnitSymbol.m2Pers"])
    WPermK = PermissibleValue(
        text="WPermK",
        meaning=CIM["UnitSymbol.WPermK"])
    JPerK = PermissibleValue(
        text="JPerK",
        meaning=CIM["UnitSymbol.JPerK"])
    ppm = PermissibleValue(
        text="ppm",
        meaning=CIM["UnitSymbol.ppm"])
    rotPers = PermissibleValue(
        text="rotPers",
        meaning=CIM["UnitSymbol.rotPers"])
    radPers = PermissibleValue(
        text="radPers",
        meaning=CIM["UnitSymbol.radPers"])
    WPerm2 = PermissibleValue(
        text="WPerm2",
        meaning=CIM["UnitSymbol.WPerm2"])
    JPerm2 = PermissibleValue(
        text="JPerm2",
        meaning=CIM["UnitSymbol.JPerm2"])
    SPerm = PermissibleValue(
        text="SPerm",
        meaning=CIM["UnitSymbol.SPerm"])
    KPers = PermissibleValue(
        text="KPers",
        meaning=CIM["UnitSymbol.KPers"])
    PaPers = PermissibleValue(
        text="PaPers",
        meaning=CIM["UnitSymbol.PaPers"])
    JPerkgK = PermissibleValue(
        text="JPerkgK",
        meaning=CIM["UnitSymbol.JPerkgK"])
    VA = PermissibleValue(
        text="VA",
        meaning=CIM["UnitSymbol.VA"])
    VAr = PermissibleValue(
        text="VAr",
        meaning=CIM["UnitSymbol.VAr"])
    cosPhi = PermissibleValue(
        text="cosPhi",
        meaning=CIM["UnitSymbol.cosPhi"])
    Vs = PermissibleValue(
        text="Vs",
        meaning=CIM["UnitSymbol.Vs"])
    V2 = PermissibleValue(
        text="V2",
        meaning=CIM["UnitSymbol.V2"])
    As = PermissibleValue(
        text="As",
        meaning=CIM["UnitSymbol.As"])
    A2 = PermissibleValue(
        text="A2",
        meaning=CIM["UnitSymbol.A2"])
    A2s = PermissibleValue(
        text="A2s",
        meaning=CIM["UnitSymbol.A2s"])
    VAh = PermissibleValue(
        text="VAh",
        meaning=CIM["UnitSymbol.VAh"])
    Wh = PermissibleValue(
        text="Wh",
        meaning=CIM["UnitSymbol.Wh"])
    VArh = PermissibleValue(
        text="VArh",
        meaning=CIM["UnitSymbol.VArh"])
    VPerHz = PermissibleValue(
        text="VPerHz",
        meaning=CIM["UnitSymbol.VPerHz"])
    HzPers = PermissibleValue(
        text="HzPers",
        meaning=CIM["UnitSymbol.HzPers"])
    character = PermissibleValue(
        text="character",
        meaning=CIM["UnitSymbol.character"])
    charPers = PermissibleValue(
        text="charPers",
        meaning=CIM["UnitSymbol.charPers"])
    kgm2 = PermissibleValue(
        text="kgm2",
        meaning=CIM["UnitSymbol.kgm2"])
    dB = PermissibleValue(
        text="dB",
        meaning=CIM["UnitSymbol.dB"])
    WPers = PermissibleValue(
        text="WPers",
        meaning=CIM["UnitSymbol.WPers"])
    lPers = PermissibleValue(
        text="lPers",
        meaning=CIM["UnitSymbol.lPers"])
    dBm = PermissibleValue(
        text="dBm",
        meaning=CIM["UnitSymbol.dBm"])
    h = PermissibleValue(
        text="h",
        meaning=CIM["UnitSymbol.h"])
    min = PermissibleValue(
        text="min",
        meaning=CIM["UnitSymbol.min"])
    Q = PermissibleValue(
        text="Q",
        meaning=CIM["UnitSymbol.Q"])
    Qh = PermissibleValue(
        text="Qh",
        meaning=CIM["UnitSymbol.Qh"])
    ohmm = PermissibleValue(
        text="ohmm",
        meaning=CIM["UnitSymbol.ohmm"])
    APerm = PermissibleValue(
        text="APerm",
        meaning=CIM["UnitSymbol.APerm"])
    V2h = PermissibleValue(
        text="V2h",
        meaning=CIM["UnitSymbol.V2h"])
    A2h = PermissibleValue(
        text="A2h",
        meaning=CIM["UnitSymbol.A2h"])
    Ah = PermissibleValue(
        text="Ah",
        meaning=CIM["UnitSymbol.Ah"])
    count = PermissibleValue(
        text="count",
        meaning=CIM["UnitSymbol.count"])
    ft3 = PermissibleValue(
        text="ft3",
        meaning=CIM["UnitSymbol.ft3"])
    m3Perh = PermissibleValue(
        text="m3Perh",
        meaning=CIM["UnitSymbol.m3Perh"])
    gal = PermissibleValue(
        text="gal",
        meaning=CIM["UnitSymbol.gal"])
    Btu = PermissibleValue(
        text="Btu",
        meaning=CIM["UnitSymbol.Btu"])
    l = PermissibleValue(
        text="l",
        meaning=CIM["UnitSymbol.l"])
    lPerh = PermissibleValue(
        text="lPerh",
        meaning=CIM["UnitSymbol.lPerh"])
    lPerl = PermissibleValue(
        text="lPerl",
        meaning=CIM["UnitSymbol.lPerl"])
    gPerg = PermissibleValue(
        text="gPerg",
        meaning=CIM["UnitSymbol.gPerg"])
    molPerm3 = PermissibleValue(
        text="molPerm3",
        meaning=CIM["UnitSymbol.molPerm3"])
    molPermol = PermissibleValue(
        text="molPermol",
        meaning=CIM["UnitSymbol.molPermol"])
    molPerkg = PermissibleValue(
        text="molPerkg",
        meaning=CIM["UnitSymbol.molPerkg"])
    sPers = PermissibleValue(
        text="sPers",
        meaning=CIM["UnitSymbol.sPers"])
    HzPerHz = PermissibleValue(
        text="HzPerHz",
        meaning=CIM["UnitSymbol.HzPerHz"])
    VPerV = PermissibleValue(
        text="VPerV",
        meaning=CIM["UnitSymbol.VPerV"])
    APerA = PermissibleValue(
        text="APerA",
        meaning=CIM["UnitSymbol.APerA"])
    VPerVA = PermissibleValue(
        text="VPerVA",
        meaning=CIM["UnitSymbol.VPerVA"])
    rev = PermissibleValue(
        text="rev",
        meaning=CIM["UnitSymbol.rev"])
    kat = PermissibleValue(
        text="kat",
        meaning=CIM["UnitSymbol.kat"])
    JPerkg = PermissibleValue(
        text="JPerkg",
        meaning=CIM["UnitSymbol.JPerkg"])
    m3Uncompensated = PermissibleValue(
        text="m3Uncompensated",
        meaning=CIM["UnitSymbol.m3Uncompensated"])
    m3Compensated = PermissibleValue(
        text="m3Compensated",
        meaning=CIM["UnitSymbol.m3Compensated"])
    WPerW = PermissibleValue(
        text="WPerW",
        meaning=CIM["UnitSymbol.WPerW"])
    therm = PermissibleValue(
        text="therm",
        meaning=CIM["UnitSymbol.therm"])
    onePerm = PermissibleValue(
        text="onePerm",
        meaning=CIM["UnitSymbol.onePerm"])
    m3Perkg = PermissibleValue(
        text="m3Perkg",
        meaning=CIM["UnitSymbol.m3Perkg"])
    Pas = PermissibleValue(
        text="Pas",
        meaning=CIM["UnitSymbol.Pas"])
    Nm = PermissibleValue(
        text="Nm",
        meaning=CIM["UnitSymbol.Nm"])
    NPerm = PermissibleValue(
        text="NPerm",
        meaning=CIM["UnitSymbol.NPerm"])
    radPers2 = PermissibleValue(
        text="radPers2",
        meaning=CIM["UnitSymbol.radPers2"])
    JPerm3 = PermissibleValue(
        text="JPerm3",
        meaning=CIM["UnitSymbol.JPerm3"])
    VPerm = PermissibleValue(
        text="VPerm",
        meaning=CIM["UnitSymbol.VPerm"])
    CPerm3 = PermissibleValue(
        text="CPerm3",
        meaning=CIM["UnitSymbol.CPerm3"])
    CPerm2 = PermissibleValue(
        text="CPerm2",
        meaning=CIM["UnitSymbol.CPerm2"])
    FPerm = PermissibleValue(
        text="FPerm",
        meaning=CIM["UnitSymbol.FPerm"])
    HPerm = PermissibleValue(
        text="HPerm",
        meaning=CIM["UnitSymbol.HPerm"])
    JPermol = PermissibleValue(
        text="JPermol",
        meaning=CIM["UnitSymbol.JPermol"])
    JPermolK = PermissibleValue(
        text="JPermolK",
        meaning=CIM["UnitSymbol.JPermolK"])
    CPerkg = PermissibleValue(
        text="CPerkg",
        meaning=CIM["UnitSymbol.CPerkg"])
    GyPers = PermissibleValue(
        text="GyPers",
        meaning=CIM["UnitSymbol.GyPers"])
    WPersr = PermissibleValue(
        text="WPersr",
        meaning=CIM["UnitSymbol.WPersr"])
    WPerm2sr = PermissibleValue(
        text="WPerm2sr",
        meaning=CIM["UnitSymbol.WPerm2sr"])
    katPerm3 = PermissibleValue(
        text="katPerm3",
        meaning=CIM["UnitSymbol.katPerm3"])
    d = PermissibleValue(
        text="d",
        meaning=CIM["UnitSymbol.d"])
    anglemin = PermissibleValue(
        text="anglemin",
        meaning=CIM["UnitSymbol.anglemin"])
    anglesec = PermissibleValue(
        text="anglesec",
        meaning=CIM["UnitSymbol.anglesec"])
    ha = PermissibleValue(
        text="ha",
        meaning=CIM["UnitSymbol.ha"])
    tonne = PermissibleValue(
        text="tonne",
        meaning=CIM["UnitSymbol.tonne"])
    bar = PermissibleValue(
        text="bar",
        meaning=CIM["UnitSymbol.bar"])
    mmHg = PermissibleValue(
        text="mmHg",
        meaning=CIM["UnitSymbol.mmHg"])
    M = PermissibleValue(
        text="M",
        meaning=CIM["UnitSymbol.M"])
    kn = PermissibleValue(
        text="kn",
        meaning=CIM["UnitSymbol.kn"])
    Mx = PermissibleValue(
        text="Mx",
        meaning=CIM["UnitSymbol.Mx"])
    G = PermissibleValue(
        text="G",
        meaning=CIM["UnitSymbol.G"])
    Oe = PermissibleValue(
        text="Oe",
        meaning=CIM["UnitSymbol.Oe"])
    Vh = PermissibleValue(
        text="Vh",
        meaning=CIM["UnitSymbol.Vh"])
    WPerA = PermissibleValue(
        text="WPerA",
        meaning=CIM["UnitSymbol.WPerA"])
    onePerHz = PermissibleValue(
        text="onePerHz",
        meaning=CIM["UnitSymbol.onePerHz"])
    VPerVAr = PermissibleValue(
        text="VPerVAr",
        meaning=CIM["UnitSymbol.VPerVAr"])
    ohmPerm = PermissibleValue(
        text="ohmPerm",
        meaning=CIM["UnitSymbol.ohmPerm"])
    kgPerJ = PermissibleValue(
        text="kgPerJ",
        meaning=CIM["UnitSymbol.kgPerJ"])
    JPers = PermissibleValue(
        text="JPers",
        meaning=CIM["UnitSymbol.JPers"])

    _defn = EnumDefinition(
        name="UnitSymbol",
    )

# Slots
class slots:
    pass

slots.switch__open = Slot(uri=CIM['Switch.open'], name="switch__open", curie=CIM.curie('Switch.open'),
                   model_uri=THIS.switch__open, domain=None, range=Union[bool, Bool])

slots.switch__locked = Slot(uri=CIM['Switch.locked'], name="switch__locked", curie=CIM.curie('Switch.locked'),
                   model_uri=THIS.switch__locked, domain=None, range=Union[bool, Bool])

slots.equipment__in_service = Slot(uri=CIM['Equipment.inService'], name="equipment__in_service", curie=CIM.curie('Equipment.inService'),
                   model_uri=THIS.equipment__in_service, domain=None, range=Union[bool, Bool])

slots.identifiedObject__m_rid = Slot(uri=CIM['IdentifiedObject.mRID'], name="identifiedObject__m_rid", curie=CIM.curie('IdentifiedObject.mRID'),
                   model_uri=THIS.identifiedObject__m_rid, domain=None, range=str)

slots.identifiedObject__names = Slot(uri=CIM['NameType.Names'], name="identifiedObject__names", curie=CIM.curie('NameType.Names'),
                   model_uri=THIS.identifiedObject__names, domain=None, range=Optional[Union[Union[dict, Name], List[Union[dict, Name]]]])

slots.energyConsumer__p = Slot(uri=CIM['EnergyConsumer.p'], name="energyConsumer__p", curie=CIM.curie('EnergyConsumer.p'),
                   model_uri=THIS.energyConsumer__p, domain=None, range=Union[dict, ActivePower])

slots.energyConsumer__q = Slot(uri=CIM['EnergyConsumer.q'], name="energyConsumer__q", curie=CIM.curie('EnergyConsumer.q'),
                   model_uri=THIS.energyConsumer__q, domain=None, range=Union[dict, ReactivePower])

slots.activePower__value = Slot(uri=CIM['ActivePower.value'], name="activePower__value", curie=CIM.curie('ActivePower.value'),
                   model_uri=THIS.activePower__value, domain=None, range=Optional[float])

slots.activePower__multiplier = Slot(uri=CIM['ActivePower.multiplier'], name="activePower__multiplier", curie=CIM.curie('ActivePower.multiplier'),
                   model_uri=THIS.activePower__multiplier, domain=None, range=Optional[Union[str, "UnitMultiplier"]])

slots.activePower__unit = Slot(uri=CIM['ActivePower.unit'], name="activePower__unit", curie=CIM.curie('ActivePower.unit'),
                   model_uri=THIS.activePower__unit, domain=None, range=Optional[Union[str, "UnitSymbol"]])

slots.reactivePower__value = Slot(uri=CIM['ReactivePower.value'], name="reactivePower__value", curie=CIM.curie('ReactivePower.value'),
                   model_uri=THIS.reactivePower__value, domain=None, range=Optional[float])

slots.reactivePower__unit = Slot(uri=CIM['ReactivePower.unit'], name="reactivePower__unit", curie=CIM.curie('ReactivePower.unit'),
                   model_uri=THIS.reactivePower__unit, domain=None, range=Optional[Union[str, "UnitSymbol"]])

slots.reactivePower__multiplier = Slot(uri=CIM['ReactivePower.multiplier'], name="reactivePower__multiplier", curie=CIM.curie('ReactivePower.multiplier'),
                   model_uri=THIS.reactivePower__multiplier, domain=None, range=Optional[Union[str, "UnitMultiplier"]])

slots.aCDCTerminal__connected = Slot(uri=CIM['ACDCTerminal.connected'], name="aCDCTerminal__connected", curie=CIM.curie('ACDCTerminal.connected'),
                   model_uri=THIS.aCDCTerminal__connected, domain=None, range=Union[bool, Bool])

slots.name__name_type = Slot(uri=CIM['Name.NameType'], name="name__name_type", curie=CIM.curie('Name.NameType'),
                   model_uri=THIS.name__name_type, domain=None, range=Union[dict, NameType])

slots.name__identified_object = Slot(uri=CIM['Name.IdentifiedObject'], name="name__identified_object", curie=CIM.curie('Name.IdentifiedObject'),
                   model_uri=THIS.name__identified_object, domain=None, range=Union[dict, IdentifiedObject])

slots.nameType__description = Slot(uri=CIM['NameType.description'], name="nameType__description", curie=CIM.curie('NameType.description'),
                   model_uri=THIS.nameType__description, domain=None, range=Optional[str])

slots.nameType__name_type_authority = Slot(uri=CIM['NameType.NameTypeAuthority'], name="nameType__name_type_authority", curie=CIM.curie('NameType.NameTypeAuthority'),
                   model_uri=THIS.nameType__name_type_authority, domain=None, range=Optional[Union[dict, NameTypeAuthority]])

slots.nameType__names = Slot(uri=CIM['NameType.Names'], name="nameType__names", curie=CIM.curie('NameType.Names'),
                   model_uri=THIS.nameType__names, domain=None, range=Optional[Union[Union[dict, Name], List[Union[dict, Name]]]])

slots.nameTypeAuthority__description = Slot(uri=CIM['NameTypeAuthority.description'], name="nameTypeAuthority__description", curie=CIM.curie('NameTypeAuthority.description'),
                   model_uri=THIS.nameTypeAuthority__description, domain=None, range=Optional[str])

slots.nameTypeAuthority__name_types = Slot(uri=CIM['NameTypeAuthority.NameTypes'], name="nameTypeAuthority__name_types", curie=CIM.curie('NameTypeAuthority.NameTypes'),
                   model_uri=THIS.nameTypeAuthority__name_types, domain=None, range=Optional[Union[Union[dict, NameType], List[Union[dict, NameType]]]])
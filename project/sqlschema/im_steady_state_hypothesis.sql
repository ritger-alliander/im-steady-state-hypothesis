-- # Class: "Breaker" Description: "A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit."
--     * Slot: id Description: 
--     * Slot: open Description: The attribute tells if the switch is considered open when used as input to topology processing.
--     * Slot: locked Description: If true, the switch is locked. The resulting switch state is a combination of locked and Switch.open attributes as follows:<ul>	<li>locked=true and Switch.open=true. The resulting state is open and locked;</li>	<li>locked=false and Switch.open=true. The resulting state is open;</li>	<li>locked=false and Switch.open=false. The resulting state is closed.</li></ul>
--     * Slot: in_service Description: Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
-- # Class: "ProtectedSwitch" Description: "A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment."
--     * Slot: id Description: 
--     * Slot: open Description: The attribute tells if the switch is considered open when used as input to topology processing.
--     * Slot: locked Description: If true, the switch is locked. The resulting switch state is a combination of locked and Switch.open attributes as follows:<ul>	<li>locked=true and Switch.open=true. The resulting state is open and locked;</li>	<li>locked=false and Switch.open=true. The resulting state is open;</li>	<li>locked=false and Switch.open=false. The resulting state is closed.</li></ul>
--     * Slot: in_service Description: Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
-- # Class: "Switch" Description: "A generic device designed to close, or open, or both, one or more electric circuits.  All switches are two terminal devices including grounding switches. The ACDCTerminal.connected at the two sides of the switch shall not be considered for assessing switch connectivity, i.e. only Switch.open, .normalOpen and .locked are relevant."
--     * Slot: id Description: 
--     * Slot: open Description: The attribute tells if the switch is considered open when used as input to topology processing.
--     * Slot: locked Description: If true, the switch is locked. The resulting switch state is a combination of locked and Switch.open attributes as follows:<ul>	<li>locked=true and Switch.open=true. The resulting state is open and locked;</li>	<li>locked=false and Switch.open=true. The resulting state is open;</li>	<li>locked=false and Switch.open=false. The resulting state is closed.</li></ul>
--     * Slot: in_service Description: Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
-- # Class: "ConductingEquipment" Description: "The parts of the AC power system that are designed to carry current or that are conductively connected through terminals."
--     * Slot: id Description: 
--     * Slot: in_service Description: Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
-- # Class: "Equipment" Description: "The parts of a power system that are physical devices, electronic or mechanical."
--     * Slot: id Description: 
--     * Slot: in_service Description: Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
-- # Class: "PowerSystemResource" Description: "A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated."
--     * Slot: id Description: 
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
-- # Class: "IdentifiedObject" Description: "This is a root class to provide common identification for all classes needing identification and naming attributes."
--     * Slot: id Description: 
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
-- # Class: "Disconnector" Description: "A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made."
--     * Slot: id Description: 
--     * Slot: open Description: The attribute tells if the switch is considered open when used as input to topology processing.
--     * Slot: locked Description: If true, the switch is locked. The resulting switch state is a combination of locked and Switch.open attributes as follows:<ul>	<li>locked=true and Switch.open=true. The resulting state is open and locked;</li>	<li>locked=false and Switch.open=true. The resulting state is open;</li>	<li>locked=false and Switch.open=false. The resulting state is closed.</li></ul>
--     * Slot: in_service Description: Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
-- # Class: "EnergyConsumer" Description: "Generic user of energy - a  point of consumption on the power system model.EnergyConsumer.pfixed, .qfixed, .pfixedPct and .qfixedPct have meaning only if there is no LoadResponseCharacteristic associated with EnergyConsumer or if LoadResponseCharacteristic.exponentModel is set to False."
--     * Slot: id Description: 
--     * Slot: in_service Description: Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
--     * Slot: p_id Description: Active power of the load. Load sign convention is used, i.e. positive sign means flow out from a node.For voltage dependent loads the value is at rated voltage.Starting value for a steady state solution.
--     * Slot: q_id Description: Reactive power of the load. Load sign convention is used, i.e. positive sign means flow out from a node.For voltage dependent loads the value is at rated voltage.Starting value for a steady state solution.
-- # Class: "ActivePower" Description: "Product of RMS value of the voltage and the RMS value of the in-phase component of the current."
--     * Slot: id Description: 
--     * Slot: value Description: 
--     * Slot: multiplier Description: 
--     * Slot: unit Description: 
-- # Class: "ReactivePower" Description: "Product of RMS value of the voltage and the RMS value of the quadrature component of the current."
--     * Slot: id Description: 
--     * Slot: value Description: 
--     * Slot: unit Description: 
--     * Slot: multiplier Description: 
-- # Class: "EnergyConnection" Description: "A connection of energy generation or consumption on the power system model."
--     * Slot: id Description: 
--     * Slot: in_service Description: Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
-- # Class: "LoadBreakSwitch" Description: "A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions."
--     * Slot: id Description: 
--     * Slot: open Description: The attribute tells if the switch is considered open when used as input to topology processing.
--     * Slot: locked Description: If true, the switch is locked. The resulting switch state is a combination of locked and Switch.open attributes as follows:<ul>	<li>locked=true and Switch.open=true. The resulting state is open and locked;</li>	<li>locked=false and Switch.open=true. The resulting state is open;</li>	<li>locked=false and Switch.open=false. The resulting state is closed.</li></ul>
--     * Slot: in_service Description: Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
-- # Class: "Terminal" Description: "An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes."
--     * Slot: id Description: 
--     * Slot: connected Description: The connected status is related to a bus-branch model and the topological node to terminal relation.  True implies the terminal is connected to the related topological node and false implies it is not. In a bus-branch model, the connected status is used to tell if equipment is disconnected without having to change the connectivity described by the topological node to terminal relation. A valid case is that conducting equipment can be connected in one end and open in the other. In particular for an AC line segment, where the reactive line charging can be significant, this is a relevant case.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
-- # Class: "ACDCTerminal" Description: "An electrical connection point (AC or DC) to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes."
--     * Slot: id Description: 
--     * Slot: connected Description: The connected status is related to a bus-branch model and the topological node to terminal relation.  True implies the terminal is connected to the related topological node and false implies it is not. In a bus-branch model, the connected status is used to tell if equipment is disconnected without having to change the connectivity described by the topological node to terminal relation. A valid case is that conducting equipment can be connected in one end and open in the other. In particular for an AC line segment, where the reactive line charging can be significant, this is a relevant case.
--     * Slot: m_rid Description: Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
-- # Class: "Name" Description: "The Name class provides the means to define any number of human readable  names for an object. A name is <b>not</b> to be used for defining inter-object relationships. For inter-object relationships instead use the object identification 'mRID'."
--     * Slot: id Description: 
--     * Slot: name_type_id Description: Type of this name.
--     * Slot: identified_object_id Description: Identified object that this name designates.
-- # Class: "NameType" Description: "Type of name. Possible values for attribute 'name' are implementation dependent but standard profiles may specify types. An enterprise may have multiple IT systems each having its own local name for the same object, e.g. a planning system may have different names from an EMS. An object may also have different names within the same IT system, e.g. localName as defined in CIM version 14. The definition from CIM14 is:The localName is a human readable name of the object. It is a free text name local to a node in a naming hierarchy similar to a file directory structure. A power system related naming hierarchy may be: Substation, VoltageLevel, Equipment etc. Children of the same parent in such a hierarchy have names that typically are unique among them."
--     * Slot: id Description: 
--     * Slot: description Description: Description of the name type.
--     * Slot: name_type_authority_id Description: Authority responsible for managing names of this type.
-- # Class: "NameTypeAuthority" Description: "Authority responsible for creation and management of names of a given type; typically an organization or an enterprise system."
--     * Slot: id Description: 
--     * Slot: description Description: Description of the name type authority.
-- # Class: "Breaker_names" Description: ""
--     * Slot: Breaker_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "ProtectedSwitch_names" Description: ""
--     * Slot: ProtectedSwitch_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "Switch_names" Description: ""
--     * Slot: Switch_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "ConductingEquipment_names" Description: ""
--     * Slot: ConductingEquipment_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "Equipment_names" Description: ""
--     * Slot: Equipment_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "PowerSystemResource_names" Description: ""
--     * Slot: PowerSystemResource_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "IdentifiedObject_names" Description: ""
--     * Slot: IdentifiedObject_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "Disconnector_names" Description: ""
--     * Slot: Disconnector_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "EnergyConsumer_names" Description: ""
--     * Slot: EnergyConsumer_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "EnergyConnection_names" Description: ""
--     * Slot: EnergyConnection_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "LoadBreakSwitch_names" Description: ""
--     * Slot: LoadBreakSwitch_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "Terminal_names" Description: ""
--     * Slot: Terminal_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "ACDCTerminal_names" Description: ""
--     * Slot: ACDCTerminal_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "NameType_names" Description: ""
--     * Slot: NameType_id Description: Autocreated FK slot
--     * Slot: names_id Description: All names of this type.
-- # Class: "NameTypeAuthority_name_types" Description: ""
--     * Slot: NameTypeAuthority_id Description: Autocreated FK slot
--     * Slot: name_types_id Description: All name types managed by this authority.

CREATE TABLE "Breaker" (
	id INTEGER NOT NULL, 
	open BOOLEAN NOT NULL, 
	locked BOOLEAN NOT NULL, 
	in_service BOOLEAN NOT NULL, 
	m_rid TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ProtectedSwitch" (
	id INTEGER NOT NULL, 
	open BOOLEAN NOT NULL, 
	locked BOOLEAN NOT NULL, 
	in_service BOOLEAN NOT NULL, 
	m_rid TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Switch" (
	id INTEGER NOT NULL, 
	open BOOLEAN NOT NULL, 
	locked BOOLEAN NOT NULL, 
	in_service BOOLEAN NOT NULL, 
	m_rid TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ConductingEquipment" (
	id INTEGER NOT NULL, 
	in_service BOOLEAN NOT NULL, 
	m_rid TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Equipment" (
	id INTEGER NOT NULL, 
	in_service BOOLEAN NOT NULL, 
	m_rid TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PowerSystemResource" (
	id INTEGER NOT NULL, 
	m_rid TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "IdentifiedObject" (
	id INTEGER NOT NULL, 
	m_rid TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Disconnector" (
	id INTEGER NOT NULL, 
	open BOOLEAN NOT NULL, 
	locked BOOLEAN NOT NULL, 
	in_service BOOLEAN NOT NULL, 
	m_rid TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ActivePower" (
	id INTEGER NOT NULL, 
	value FLOAT, 
	multiplier VARCHAR(5), 
	unit VARCHAR(15), 
	PRIMARY KEY (id)
);
CREATE TABLE "ReactivePower" (
	id INTEGER NOT NULL, 
	value FLOAT, 
	unit VARCHAR(15), 
	multiplier VARCHAR(5), 
	PRIMARY KEY (id)
);
CREATE TABLE "EnergyConnection" (
	id INTEGER NOT NULL, 
	in_service BOOLEAN NOT NULL, 
	m_rid TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "LoadBreakSwitch" (
	id INTEGER NOT NULL, 
	open BOOLEAN NOT NULL, 
	locked BOOLEAN NOT NULL, 
	in_service BOOLEAN NOT NULL, 
	m_rid TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Terminal" (
	id INTEGER NOT NULL, 
	connected BOOLEAN NOT NULL, 
	m_rid TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ACDCTerminal" (
	id INTEGER NOT NULL, 
	connected BOOLEAN NOT NULL, 
	m_rid TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "NameTypeAuthority" (
	id INTEGER NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "EnergyConsumer" (
	id INTEGER NOT NULL, 
	in_service BOOLEAN NOT NULL, 
	m_rid TEXT NOT NULL, 
	p_id INTEGER NOT NULL, 
	q_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(p_id) REFERENCES "ActivePower" (id), 
	FOREIGN KEY(q_id) REFERENCES "ReactivePower" (id)
);
CREATE TABLE "NameType" (
	id INTEGER NOT NULL, 
	description TEXT, 
	name_type_authority_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(name_type_authority_id) REFERENCES "NameTypeAuthority" (id)
);
CREATE TABLE "Name" (
	id INTEGER NOT NULL, 
	name_type_id INTEGER NOT NULL, 
	identified_object_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(name_type_id) REFERENCES "NameType" (id), 
	FOREIGN KEY(identified_object_id) REFERENCES "IdentifiedObject" (id)
);
CREATE TABLE "NameTypeAuthority_name_types" (
	"NameTypeAuthority_id" INTEGER, 
	name_types_id INTEGER, 
	PRIMARY KEY ("NameTypeAuthority_id", name_types_id), 
	FOREIGN KEY("NameTypeAuthority_id") REFERENCES "NameTypeAuthority" (id), 
	FOREIGN KEY(name_types_id) REFERENCES "NameType" (id)
);
CREATE TABLE "Breaker_names" (
	"Breaker_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("Breaker_id", names_id), 
	FOREIGN KEY("Breaker_id") REFERENCES "Breaker" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "ProtectedSwitch_names" (
	"ProtectedSwitch_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("ProtectedSwitch_id", names_id), 
	FOREIGN KEY("ProtectedSwitch_id") REFERENCES "ProtectedSwitch" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "Switch_names" (
	"Switch_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("Switch_id", names_id), 
	FOREIGN KEY("Switch_id") REFERENCES "Switch" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "ConductingEquipment_names" (
	"ConductingEquipment_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("ConductingEquipment_id", names_id), 
	FOREIGN KEY("ConductingEquipment_id") REFERENCES "ConductingEquipment" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "Equipment_names" (
	"Equipment_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("Equipment_id", names_id), 
	FOREIGN KEY("Equipment_id") REFERENCES "Equipment" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "PowerSystemResource_names" (
	"PowerSystemResource_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("PowerSystemResource_id", names_id), 
	FOREIGN KEY("PowerSystemResource_id") REFERENCES "PowerSystemResource" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "IdentifiedObject_names" (
	"IdentifiedObject_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("IdentifiedObject_id", names_id), 
	FOREIGN KEY("IdentifiedObject_id") REFERENCES "IdentifiedObject" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "Disconnector_names" (
	"Disconnector_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("Disconnector_id", names_id), 
	FOREIGN KEY("Disconnector_id") REFERENCES "Disconnector" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "EnergyConsumer_names" (
	"EnergyConsumer_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("EnergyConsumer_id", names_id), 
	FOREIGN KEY("EnergyConsumer_id") REFERENCES "EnergyConsumer" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "EnergyConnection_names" (
	"EnergyConnection_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("EnergyConnection_id", names_id), 
	FOREIGN KEY("EnergyConnection_id") REFERENCES "EnergyConnection" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "LoadBreakSwitch_names" (
	"LoadBreakSwitch_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("LoadBreakSwitch_id", names_id), 
	FOREIGN KEY("LoadBreakSwitch_id") REFERENCES "LoadBreakSwitch" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "Terminal_names" (
	"Terminal_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("Terminal_id", names_id), 
	FOREIGN KEY("Terminal_id") REFERENCES "Terminal" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "ACDCTerminal_names" (
	"ACDCTerminal_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("ACDCTerminal_id", names_id), 
	FOREIGN KEY("ACDCTerminal_id") REFERENCES "ACDCTerminal" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
CREATE TABLE "NameType_names" (
	"NameType_id" INTEGER, 
	names_id INTEGER, 
	PRIMARY KEY ("NameType_id", names_id), 
	FOREIGN KEY("NameType_id") REFERENCES "NameType" (id), 
	FOREIGN KEY(names_id) REFERENCES "Name" (id)
);
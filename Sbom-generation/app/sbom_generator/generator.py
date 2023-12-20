# from io import StringIO
import json
from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component, ComponentType
from cyclonedx.output import  get_instance as get_output_instance
from cyclonedx.output import OutputFormat

# from spdx.writers.tagvalue import write_document
# from spdx.document import Document, License, ExternalDocumentRef
# from spdx.creationinfo import Person, Organization, Tool
# from spdx.package import Package
# from spdx.version import Version
# from swid_generator import SWIDGenerator

class SBOMAnalyzer:
    def generateCycloneDX(self, json_data,type_framework):
        data = json.loads(json_data)
        # data=json_data
        print(type(data))
        components = []
        for dep in data['dependencies']:
            if (type_framework=="maven"):
             component = Component(name=dep['artifactId'], version=dep['version'], component_type=ComponentType.APPLICATION)
            elif(type_framework=="npm"):
                component = Component(name=dep['name'], version=dep['version'], component_type=ComponentType.APPLICATION)
            components.append(component)

        bom = Bom(components=components)
        output = get_output_instance(bom=bom,output_format=OutputFormat.JSON)
        return output.output_as_string(),output.output_to_file("sbom.json")

    # def generateSPDX(self, json_data):
    #     data = json.loads(json_data)
    #     doc = Document()
    #     doc.version = Version(2, 1)
    #     doc.data_license = License.from_identifier('CC0-1.0')
    #     doc.creation_info.add_creator(Person('CreatorName'))
    #     doc.creation_info.set_created_now()

    #     for dep in data['dependencies']:
    #         pkg = Package(name=dep['name'], version=dep['version'])
    #         doc.packages.append(pkg)

    #     output = StringIO()
    #     write_document(doc, output)
    #     return output.getvalue()

    # def generateSWID(self, json_data):
    #     data = json.loads(json_data)
    #     generator = SWIDGenerator()
    #     for dep in data['dependencies']:
    #         generator.add_component(name=dep['name'], version=dep['version'])
    #     return generator.generate()

    def generate(self, json_data, format,type):
        if format == 'CycloneDX':
            return self.generateCycloneDX(json_data,type)
        # elif format == 'SPDX':
        #     return self.generateSPDX(json_data)
        # elif format == 'SWID':
        #     return self.generateSWID(json_data)
        else:
            raise ValueError('Unsupported format')
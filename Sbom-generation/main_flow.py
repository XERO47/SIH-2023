from ast import parse

from matplotlib.style import available
from app.vex_generator.latest_packages import get_latest_npm_version,get_latest_maven_version,get_latest_pypi_version
# from app.vex_generator.vulnebrality_detection import npm_vlun
from app.github_utils import get_github_file_content,get_all_files_in_repo
from app.detection import detect_framework,detect_languages
import requests
from app.parser.parsers.maven_parser import MavenParser
from app.parser.parsers.npm_parser import npm_parser
from app.parser.parsers.pip_parser import PipParser
from app.sbom_generator.generator import SBOMAnalyzer
import json
from database.db_connect import add_sbom_data_from_json

# from SBOM import encrypt_data

def github_link_analysis(link):
    owner = link.split('/')[3]
    repo_name = link.split('/')[4]
    
    return owner,repo_name







def main_workflow(link):
    owner,repo_name=github_link_analysis(link)
    all_files=get_all_files_in_repo(owner,repo_name)
    framework,manifestfile=detect_framework(all_files)
    parser_data={}
    if(framework=="Maven"):
        parser_data= MavenParser.parse(get_github_file_content(owner,repo_name,manifestfile))
    elif(framework=="Node"):
        parser_data= npm_parser(get_github_file_content(owner,repo_name,manifestfile))
        print(parser_data)
    elif(framework=="Python"):
        parser_data= PipParser.parse(get_github_file_content(owner,repo_name,manifestfile))
    
    analysizer = SBOMAnalyzer()
    sbom=analysizer.generate(parser_data,"CycloneDX","npm")
    
    parser_data=json.loads(parser_data)
    updates_available=[]
    vuln_status={}
    for dep in parser_data['dependencies']:
        # print(f"Latest Version for {dep['name']}",get_latest_npm_version(dep['name']))
        updates_available.append(get_latest_npm_version(dep['name']))
        print("Update available at ",get_latest_npm_version(dep['name'],f"for{dep['name']} "))
        # if 'ok' in test and test['ok'] == "False":
        #     vuln_status[dep['name']] = test["severity"]
        # else:
        #     vuln_status[dep['name']] = ['ALL GOOD']
    add_sbom_data_from_json(sbom,updates_available)
    return sbom,updates_available


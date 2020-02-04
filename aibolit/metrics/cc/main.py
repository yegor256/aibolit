import subprocess
import os
import shutil
from bs4 import BeautifulSoup
import tempfile


class CCMetric(object):
    """Main Cyclical Complexity class."""

    input = ''

    def __init__(self, input):
        """Initialize class."""
        super(CCMetric, self).__init__()
        if len(input) == 0:
            raise ValueError('Empty file for analysis')
        else:
            self.input = input

    def value(self, showoutput=False):
        """Run Cyclical Complexity analaysis"""
        try:
            root = str(tempfile.TemporaryFile())
            dirName = root + '/src/main/java'
            os.makedirs(dirName)
            if os.path.isdir(self.input):
                shutil.copytree(self.input, os.path.join(dirName, self.input))
            elif os.path.isfile(self.input):
                pos1 = self.input.rfind('/')
                os.makedirs(dirName + '/' + self.input[0:pos1])
                shutil.copyfile(self.input, os.path.join(dirName, self.input))
            else:
                raise Exception('File ' + self.input + ' does not exist')

            shutil.copyfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pom.xml'), root + '/pom.xml')
            shutil.copyfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cyclical.xml'),
                            root + '/cyclical.xml')
            if showoutput:
                subprocess.run(['mvn', 'pmd:pmd'], cwd=root)
            else:
                subprocess.run(['mvn', 'pmd:pmd'], cwd=root,
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)

            if os.path.exists(root + '/target/pmd.xml'):
                res = self.parseFile(root)
                return res
            else:
                raise Exception('File ' + self.input + ' analyze failed')
        finally:
            self.finishAnalysis(root)

    def parseFile(self, root):
        result = {'data': [], 'errors': []}
        content = []
        # Read the XML file
        with open(root + '/target/pmd.xml', 'r') as file:
            # Read each line in the file, readlines() returns a list of lines
            content = file.readlines()
            # Combine the lines in the list into a string
            content = "".join(content)
            soup = BeautifulSoup(content, 'lxml')
            files = soup.find_all("file")
            for file in files:
                out = file.violation.string
                name = file['name']
                pos1 = name.find(root + '/src/main/java/')
                pos1 = pos1 + len(root + '/src/main/java/')
                name = name[pos1:]
                pos1 = out.find('has a total cyclomatic complexity')
                pos1 = out.find('of ', pos1)
                pos1 = pos1 + 3
                pos2 = out.find('(', pos1)
                complexity = int(out[pos1:pos2 - 1])
                result['data'].append({'file': name, 'complexity': complexity})
            errors = soup.find_all("error")
            for error in errors:
                name = error['filename']
                pos1 = name.find(root + '/src/main/java/')
                pos1 = pos1 + len(root + '/src/main/java/')
                name = name[pos1:]
                result['errors'].append({'file': name, 'message': error['msg']})
        return result

    def finishAnalysis(self, root):
        """Finish anayze."""
        shutil.rmtree(root)

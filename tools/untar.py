from janis import Array
from janis.unix.data_types.tar_file import TarFile

from janis.types.common_data_types import File
from janis.tool.commandtool import CommandTool, ToolInput, ToolOutput


class Untar(CommandTool):

    @staticmethod
    def base_command():
        return ["tar", "xf"]

    def friendly_name(self):
        return "Untar archive"

    @staticmethod
    def tool():
        return "Untar"

    def inputs(self):
        return [
            ToolInput("tarFile", TarFile(), position=0)
        ]

    def outputs(self):
        return [
            ToolOutput("files", Array(File()), glob="*.java")
        ]

"""

EXAMPLE XML

<Step>
    <title>Untar</title>
    <author>Michael Franklin</author>
    <cores>1</cores>
    <ram>1024</ram>
    <label>{{label}}</label>
    <supportedTypes>
        <type>cwl</type>
        <type>wdl</type>
    </supportedTypes>
    
    <inputs>
        <input>
            <tag>input</tag>
            <type>File</type>
        </input>
    </inputs>
    <outputs>
        <output>
            <tag>output</tag>
            <type>File</type>
        </output>
    </outputs>
</Step>

+ provide CWL template

#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: [tar, xf]
inputs:
  input:
    type: File
    inputBinding:
      position: 1
  output:
    type: string
    inputBinding:
      position: 2

outputs:
  example_out:
    type: File
    outputBinding:
      glob: $(inputs.outputfile)

+ wdl template

task {
    File input
    File output
    command {
        tar -xf ${input}
    }
}

"""
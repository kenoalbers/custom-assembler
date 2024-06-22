from app.models import AnalysisModel


class SynthesisModel(AnalysisModel):
    def __init__(self,
                 analysis_model: AnalysisModel,
                 symbol_table: dict[str, int],
                 opcode_table=None,
                 pseudo_instruction=None):
        super().__init__(assembly_file_path=analysis_model.path,
                         pattern=analysis_model.pattern,
                         label_definition_group=analysis_model.label_definition_group,
                         label_call_group=analysis_model.label_call_group,
                         byte_definition_group=analysis_model.byte_definition_group)
        self.symbol_table = symbol_table
        self._pseudo_instruction = pseudo_instruction
        self._opcode_table = opcode_table

    @property
    def pseudo_instruction(self):
        return self._pseudo_instruction

    @pseudo_instruction.setter
    def pseudo_instruction(self, pseudo_instruction):
        self._pseudo_instruction = pseudo_instruction

    @property
    def opcode_table(self):
        return self._opcode_table

    @opcode_table.setter
    def opcode_table(self, opcode_table):
        self._opcode_table = opcode_table

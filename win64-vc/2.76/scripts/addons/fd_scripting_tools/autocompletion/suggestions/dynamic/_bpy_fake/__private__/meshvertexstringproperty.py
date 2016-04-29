from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshVertexStringProperty(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def value(self):
        '''(String)'''
        return str()
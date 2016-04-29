from . nodetree import NodeTree
from . library import Library
from . id import ID
from . colorramp import ColorRamp
from . animdata import AnimData
from . imagepreview import ImagePreview
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Texture(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique datablock ID name'''
        return str()
    @property
    def users(self):
        '''(Integer) Number of times this datablock is referenced'''
        return int()
    @property
    def use_fake_user(self):
        '''(Boolean) Save this datablock even if it has no users'''
        return bool()
    @property
    def tag(self):
        '''(Boolean) Tools can use this to tag data for their own purposes
        (initial state is undefined)'''
        return bool()
    @property
    def is_updated(self):
        '''(Boolean) Datablock is tagged for recalculation'''
        return bool()
    @property
    def is_updated_data(self):
        '''(Boolean) Datablock data is tagged for recalculation'''
        return bool()
    @property
    def is_library_indirect(self):
        '''(Boolean) Is this ID block linked indirectly'''
        return bool()
    @property
    def library(self):
        '''(Library) Library file the datablock is linked from'''
        return Library()
    @property
    def preview(self):
        '''(ImagePreview) Preview image and icon of this datablock (None if not
        supported for this type of data)'''
        return ImagePreview()
    @property
    def type(self):
        '''(Enum)
        
        [NONE, BLEND, CLOUDS, DISTORTED_NOISE, ENVIRONMENT_MAP, IMAGE, MAGIC,
        MARBLE, MUSGRAVE, NOISE, OCEAN, POINT_DENSITY, STUCCI, VORONOI,
        VOXEL_DATA, WOOD]'''
        return str()
    @property
    def use_clamp(self):
        '''(Boolean) Set negative texture RGB and intensity values to zero, for
        some uses like displacement this option can be disabled to get the
        full range'''
        return bool()
    @property
    def use_color_ramp(self):
        '''(Boolean) Toggle color ramp operations'''
        return bool()
    @property
    def color_ramp(self):
        '''(ColorRamp)'''
        return ColorRamp()
    @property
    def intensity(self):
        '''(Float) Adjust the brightness of the texture'''
        return float()
    @property
    def contrast(self):
        '''(Float) Adjust the contrast of the texture'''
        return float()
    @property
    def saturation(self):
        '''(Float) Adjust the saturation of colors in the texture'''
        return float()
    @property
    def factor_red(self):
        '''(Float)'''
        return float()
    @property
    def factor_green(self):
        '''(Float)'''
        return float()
    @property
    def factor_blue(self):
        '''(Float)'''
        return float()
    @property
    def use_preview_alpha(self):
        '''(Boolean) Show Alpha in Preview Render'''
        return bool()
    @property
    def use_nodes(self):
        '''(Boolean) Make this a node-based texture'''
        return bool()
    @property
    def node_tree(self):
        '''(NodeTree) Node tree for node-based textures'''
        return NodeTree()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
    def copy(self):
        '''Create a copy of this datablock (not supported for all datablocks)
        
        Returns:
          id: (ID) New copy of the ID'''
        return ID()
    def user_clear(self):
        '''Clear the user count of a datablock so its not saved, on reload the
        data will be removed'''
        return 
    def animation_data_create(self):
        '''Create animation data to this ID, note that not all ID types support
        this
        
        Returns:
          anim_data: (AnimData) New animation data or NULL'''
        return AnimData()
    def animation_data_clear(self):
        '''Clear animation on this this ID'''
        return 
    def update_tag(self, refresh):
        '''Tag the ID to update its display data, e.g. when calling
        :class:`bpy.types.Scene.update`
        
        Parameter:
          refresh: (Enum) Type of updates to perform'''
        return 
    def evaluate(self, value):
        '''Evaluate the texture at the coordinates given
        
        Parameter:
          value: (Vector 3D)
        
        Returns:
          result: (Float[4])'''
        return ''
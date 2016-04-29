from . bone import Bone
from . scene import Scene
from . curve import Curve
from . materialtextureslot import MaterialTextureSlot
from . movieclip import MovieClip
from . greasepencil import GreasePencil
from . objectbase import ObjectBase
from . screen import Screen
from . userpreferences import UserPreferences
from . smokemodifier import SmokeModifier
from . property import Property
from . particlesettings import ParticleSettings
from . struct import Struct
from . text import Text
from . speaker import Speaker
from . metaball import MetaBall
from . mesh import Mesh
from . space import Space
from . editbone import EditBone
from . id import ID
from . area import Area
from . sequence import Sequence
from . softbodymodifier import SoftBodyModifier
from . fluidsimulationmodifier import FluidSimulationModifier
from . clothmodifier import ClothModifier
from . blenddata import BlendData
from . world import World
from . posebone import PoseBone
from . materialslot import MaterialSlot
from . texture import Texture
from . freestylelinestyle import FreestyleLineStyle
from . lamp import Lamp
from . armature import Armature
from . gpencillayer import GPencilLayer
from . brush import Brush
from . camera import Camera
from . image import Image
from . dynamicpaintmodifier import DynamicPaintModifier
from . operator import Operator
from . regionview3d import RegionView3D
from . mask import Mask
from . region import Region
from . gpencilstroke import GPencilStroke
from . object import Object
from . lattice import Lattice
from . windowmanager import WindowManager
from . collisionmodifier import CollisionModifier
from . window import Window
from . node import Node
from . particlesystem import ParticleSystem
from . material import Material
from . toolsettings import ToolSettings
from . bpy_struct import bpy_struct
import mathutils

class Context():
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def window_manager(self):
        '''(WindowManager)'''
        return WindowManager()
    @property
    def window(self):
        '''(Window)'''
        return Window()
    @property
    def screen(self):
        '''(Screen)'''
        return Screen()
    @property
    def area(self):
        '''(Area)'''
        return Area()
    @property
    def space_data(self):
        '''(Space)'''
        return Space()
    @property
    def region(self):
        '''(Region)'''
        return Region()
    @property
    def region_data(self):
        '''(RegionView3D)'''
        return RegionView3D()
    @property
    def blend_data(self):
        '''(BlendData)'''
        return BlendData()
    @property
    def scene(self):
        '''(Scene)'''
        return Scene()
    @property
    def tool_settings(self):
        '''(ToolSettings)'''
        return ToolSettings()
    @property
    def user_preferences(self):
        '''(UserPreferences)'''
        return UserPreferences()
    @property
    def mode(self):
        '''(Enum)
        
        [EDIT_MESH, EDIT_CURVE, EDIT_SURFACE, EDIT_TEXT, EDIT_ARMATURE,
        EDIT_METABALL, EDIT_LATTICE, POSE, SCULPT, PAINT_WEIGHT, PAINT_VERTEX,
        PAINT_TEXTURE, PARTICLE, OBJECT]'''
        return str()
    @property
    def active_bone(self):
        '''(EditBone)'''
        return EditBone()
    @property
    def active_pose_bone(self):
        '''(PoseBone)'''
        return PoseBone()
    @property
    def active_base(self):
        '''(ObjectBase)'''
        return ObjectBase()
    @property
    def active_object(self):
        '''(Object)'''
        return Object()
    @property
    def object(self):
        '''(Object)'''
        return Object()
    @property
    def edit_object(self):
        '''(Object)'''
        return Object()
    @property
    def sculpt_object(self):
        '''(Object)'''
        return Object()
    @property
    def vertex_paint_object(self):
        '''(Object)'''
        return Object()
    @property
    def weight_paint_object(self):
        '''(Object)'''
        return Object()
    @property
    def image_paint_object(self):
        '''(Object)'''
        return Object()
    @property
    def particle_edit_object(self):
        '''(Object)'''
        return Object()
    @property
    def gpencil_data(self):
        '''(GreasePencil)'''
        return GreasePencil()
    @property
    def gpencil_data_owner(self):
        '''(ID)'''
        return ID()
    @property
    def active_operator(self):
        '''(Operator)'''
        return Operator()
    @property
    def texture_slot(self):
        '''(MaterialTextureSlot)'''
        return MaterialTextureSlot()
    @property
    def world(self):
        '''(World)'''
        return World()
    @property
    def mesh(self):
        '''(Mesh)'''
        return Mesh()
    @property
    def armature(self):
        '''(Armature)'''
        return Armature()
    @property
    def lattice(self):
        '''(Lattice)'''
        return Lattice()
    @property
    def curve(self):
        '''(Curve)'''
        return Curve()
    @property
    def meta_ball(self):
        '''(MetaBall)'''
        return MetaBall()
    @property
    def lamp(self):
        '''(Lamp)'''
        return Lamp()
    @property
    def speaker(self):
        '''(Speaker)'''
        return Speaker()
    @property
    def camera(self):
        '''(Camera)'''
        return Camera()
    @property
    def material(self):
        '''(Material)'''
        return Material()
    @property
    def material_slot(self):
        '''(MaterialSlot)'''
        return MaterialSlot()
    @property
    def texture(self):
        '''(Texture)'''
        return Texture()
    @property
    def texture_user(self):
        '''(ID)'''
        return ID()
    @property
    def texture_user_property(self):
        '''(Property)'''
        return Property()
    @property
    def bone(self):
        '''(Bone)'''
        return Bone()
    @property
    def particle_system(self):
        '''(ParticleSystem)'''
        return ParticleSystem()
    @property
    def particle_system_editable(self):
        '''(ParticleSystem)'''
        return ParticleSystem()
    @property
    def particle_settings(self):
        '''(ParticleSettings)'''
        return ParticleSettings()
    @property
    def cloth(self):
        '''(ClothModifier)'''
        return ClothModifier()
    @property
    def soft_body(self):
        '''(SoftBodyModifier)'''
        return SoftBodyModifier()
    @property
    def fluid(self):
        '''(FluidSimulationModifier)'''
        return FluidSimulationModifier()
    @property
    def smoke(self):
        '''(SmokeModifier)'''
        return SmokeModifier()
    @property
    def collision(self):
        '''(CollisionModifier)'''
        return CollisionModifier()
    @property
    def brush(self):
        '''(Brush)'''
        return Brush()
    @property
    def dynamic_paint(self):
        '''(DynamicPaintModifier)'''
        return DynamicPaintModifier()
    @property
    def line_style(self):
        '''(FreestyleLineStyle)'''
        return FreestyleLineStyle()
    @property
    def edit_image(self):
        '''(Image)'''
        return Image()
    @property
    def edit_mask(self):
        '''(Mask)'''
        return Mask()
    @property
    def active_node(self):
        '''(Node)'''
        return Node()
    @property
    def edit_text(self):
        '''(Text)'''
        return Text()
    @property
    def edit_movieclip(self):
        '''(MovieClip)'''
        return MovieClip()
    @property
    def visible_objects(self):
        '''(Sequence of Object)'''
        return (Object(),)
    @property
    def visible_bases(self):
        '''(Sequence of ObjectBase)'''
        return (ObjectBase(),)
    @property
    def selectable_objects(self):
        '''(Sequence of Object)'''
        return (Object(),)
    @property
    def selectable_bases(self):
        '''(Sequence of ObjectBase)'''
        return (ObjectBase(),)
    @property
    def selected_objects(self):
        '''(Sequence of Object)'''
        return (Object(),)
    @property
    def selected_bases(self):
        '''(Sequence of ObjectBase)'''
        return (ObjectBase(),)
    @property
    def selected_editable_objects(self):
        '''(Sequence of Object)'''
        return (Object(),)
    @property
    def selected_editable_bases(self):
        '''(Sequence of ObjectBase)'''
        return (ObjectBase(),)
    @property
    def visible_bones(self):
        '''(Sequence of EditBone)'''
        return (EditBone(),)
    @property
    def editable_bones(self):
        '''(Sequence of EditBone)'''
        return (EditBone(),)
    @property
    def selected_bones(self):
        '''(Sequence of EditBone)'''
        return (EditBone(),)
    @property
    def selected_editable_bones(self):
        '''(Sequence of EditBone)'''
        return (EditBone(),)
    @property
    def visible_pose_bones(self):
        '''(Sequence of PoseBone)'''
        return (PoseBone(),)
    @property
    def selected_pose_bones(self):
        '''(Sequence of PoseBone)'''
        return (PoseBone(),)
    @property
    def sequences(self):
        '''(Sequence of Sequence)'''
        return (Sequence(),)
    @property
    def selected_sequences(self):
        '''(Sequence of Sequence)'''
        return (Sequence(),)
    @property
    def selected_editable_sequences(self):
        '''(Sequence of Sequence)'''
        return (Sequence(),)
    @property
    def visible_gpencil_layers(self):
        '''(Sequence of GPencilLayer)'''
        return (GPencilLayer(),)
    @property
    def editable_gpencil_layers(self):
        '''(Sequence of GPencilLayer)'''
        return (GPencilLayer(),)
    @property
    def editable_gpencil_strokes(self):
        '''(Sequence of GPencilStroke)'''
        return (GPencilStroke(),)
    @property
    def active_gpencil_layer(self):
        '''(Sequence of GPencilLayer)'''
        return (GPencilLayer(),)
    @property
    def active_gpencil_frame(self):
        '''(Sequence of GPencilLayer)'''
        return (GPencilLayer(),)
    @property
    def selected_nodes(self):
        '''(Sequence of Node)'''
        return (Node(),)
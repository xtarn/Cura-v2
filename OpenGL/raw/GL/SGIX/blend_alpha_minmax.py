'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_SGIX_blend_alpha_minmax'
_p.unpack_constants( """GL_ALPHA_MIN_SGIX 0x8320
GL_ALPHA_MAX_SGIX 0x8321""", globals())


def glInitBlendAlphaMinmaxSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
